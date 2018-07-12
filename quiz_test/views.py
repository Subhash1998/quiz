from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm,AboutForm,TestForm
from .models import Profile,City,Country,Test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json as simplejson
from django.core.serializers.json import DjangoJSONEncoder
from random import randint
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@login_required
def dashboard(request):
	test=Test.objects.filter()
	easy=test.filter(level=0)
	medium=test.filter(level=1)
	hard=test.filter(level=2)
	e=[]
	m=[]
	h=[]
	for p in easy:
		e.append(p.points)
	for q in medium:	
		m.append(q.points)
	for r in hard:
		h.append(r.points)

	all_tests=Test.objects.filter(user=request.user)
	context={
			'h':h,
			'm':m,
			'e':e,
			'all_tests':all_tests
	}
	return render(request,'quiz_test/dashboard.html',context)


@login_required
def profile(request):
	user=User.objects.get(username=request.user.username)
	args={'user':request.user}
	try:
		ob=Profile.objects.get(user=request.user)
		form=ProfileForm(instance=ob)
		var='edit'
	except Profile.DoesNotExist:
		form=ProfileForm()
		var='create'
		ob=None
	if request.method=='POST':
		if var=='create':
			form=ProfileForm(request.POST)
		elif var=='edit':
			form=ProfileForm(request.POST,instance=ob)
		if form.is_valid():
			p=form.save(commit=False)
			p.user=request.user
			p.save()
			messages.success(request,'Profile Created Successfully')
			return redirect('quiz_test:dashboard')
		else:
			messages.error(request,'Error Creating Profile')
			print(form.errors)
			return HttpResponseRedirect(reverse('quiz_test:profile'))
	return render(request,'quiz_test/profile.html',{'form':form,'ob':ob},args)



@login_required
def about_profile(request):
	user=User.objects.get(username=request.user.username)
	args={'user':request.user}
	try:
		ob=Profile.objects.get(user=request.user)
		about_form=AboutForm(instance=ob)
		var='edit'
	except Profile.DoesNotExist:
		about_form=AboutForm()
		var='create'
		ob=None
	if request.method=='POST':
		if var=='create':
			about_form=AboutForm(request.POST,request.FILES)
		elif var=='edit':
			about_form=AboutForm(request.POST,request.FILES,instance=ob)
		if about_form.is_valid():
			p=about_form.save(commit=False)
			p.user=request.user
			p.save()
			messages.success(request,'Profile Created Successfully')
			return redirect('quiz_test:dashboard')
		else:
			messages.error(request,'Error Creating Profile')
			print(about_form.errors)
			return HttpResponseRedirect(reverse('quiz_test:profile'))
	return render(request,'quiz_test/profile.html',{'about_form':about_form,'ob':ob},args)




import requests
def country(request):

	url='https://restcountries.eu/rest/v2/all'
	response = requests.get(url)
	responsej = response.json()
	for i in range(0,len(responsej)):	
		c=Country()
		c.name=responsej[i]["name"]
		c.save()



@login_required
def easy(request,test_id):
	context={}
	test_obj=Test.objects.get(user=request.user,id=test_id)
	if test_obj.session == 0:

		if test_obj.q_type == 0:
			ques_type="multiple"
		elif test_obj.q_type == 1:
			ques_type="boolean"
		else:
			ques_type=""


		if test_obj.category.code != 8:
			category=test_obj.category.code
		else:
			category=""

		amount=test_obj.get_amount_display()

		difficulty=test_obj.get_level_display()		

		url='https://opentdb.com/api.php?amount='+str(amount)+'&category='+str(category)+'&difficulty='+difficulty+'&type='+ques_type
		print(url)
		response = requests.get(url)
		responsej = response.json()
		
		question=[]
		for i in range(0,len(responsej['results'])):
			list1={}
			ans2=[0,0,0,0]
			r=randint(0, 3)
			ans2[r]=responsej['results'][i]['correct_answer']
			print(r+1)
			k=0
			for j in range(4):
				if j != r:
					ans2[j]=responsej['results'][i]['incorrect_answers'][k]
					k=k+1	
					
			list1["question"]=responsej['results'][i]['question']
			list1["choices"]=ans2
			list1["correctAnswer"]=responsej['results'][i]['correct_answer']
			list1["position"]=r+1
			question.append(list1)
		
		context={
			'question':simplejson.dumps(question,cls=DjangoJSONEncoder),
			'test':test_obj,
			'difficulty':difficulty
		}
		test_obj.session=1
		test_obj.save()
	elif test_obj.status == 0: 
		if test_obj.session == 1:
			test_obj.session=0
			test_obj.save()
		return HttpResponseRedirect(reverse('quiz_test:cancel',kwargs={'test_id':test_id}))
	elif test_obj.status == 1:
		return redirect('quiz_test:test_form')
	return render(request,'quiz_test/easy.html',context)



def test_form(request):
	form=TestForm()
	if request.method== 'POST':
		form = TestForm(request.POST)
		if form.is_valid():
		    try:
		        test = form.save(commit=False)
		        test.user=request.user
		        test_id=test.id
		        test.session=0
		        test.save()	
		        time=0
		        if test.level==0:
		        	time=20
		        elif test.level==1:
		        	time=40
		        elif test.level==2:
		        	time=60
		        type_q=test.q_type
		        return render(request,'quiz_test/rules.html',{'test':test,'time':time,'type_q':type_q})
		    except Exception as e:
		        messages.error(request, 'Error creating test form.')
		        print(e)
		        return HttpResponseRedirect(reverse('quiz_test:test_form'))
	return render(request, 'quiz_test/test_form.html',{'form':form})



def cancel(request,test_id):
	test=Test.objects.get(user=request.user,id=test_id)
	return render(request,'quiz_test/test_cancelled.html',{'test':test})



def calculate_points(request):

	if request.is_ajax():
		t=request.GET.get('test')
		a=request.GET.get('answered')
		question=request.GET.get('questions')
		t=simplejson.loads(t)
		answered=simplejson.loads(a)
		question=simplejson.loads(question)
		correctly=0
		point=0
		i=0
		for a in answered:
			pos=int(question[i]["position"])
			ans=int(a)
			if pos==ans:
				correctly=correctly+1
				point=point+5
			else:
				if ans!=0:
					point=point-1
			i=i+1
		print(correctly)
		print(point)
		test_obj=Test.objects.get(user=request.user,id=t)
		test_obj.status=1
		test_obj.points=point
		test_obj.correct=correctly
		test_obj.save()
		data={'correctly':correctly,'point':point}
		return JsonResponse(data,safe=False)


@login_required
def my_password_change(request):
	form = PasswordChangeForm(request.user)
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			try:
				user = form.save()
				update_session_auth_hash(request, user)
				messages.success(request, 'Your password is successfully updated.')
				return HttpResponseRedirect(reverse('quiz_test:dashboard'))
			except Exception as e:
				print(e)	
				messages.error(request, 'Error updating password.')
		else:
			messages.error(request, 'Error updating password.')
	return render(request, 'quiz_test/my_password_change.html', {'form':form})