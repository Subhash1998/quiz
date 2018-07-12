from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey	

occupation_choice=(
	(0,'Student'),
	(1,'Teacher'),
	(2,'Other')
	)

q_choices=(
	(0,'5'),
	(1,'10'),
	(2,'15'),
	(3,'20'),
	(4,'25'),
	(5,'30'),
	)

q_level=(
	(0,'easy'),
	(1,'medium'),
	(2,'hard'),
	)

q_type=(
	(0,'Multiple Choice'),
	(1,'True/False'),
	(2,'Any Type'),
	)

status=(
	(0,'Cancelled'),
	(1,'Completed'),
	)

class Category(models.Model):
    name = models.CharField(max_length=300)
    code=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Profile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	address=models.CharField(max_length=1000)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	city = ChainedForeignKey(City, chained_field="country",
                                      chained_model_field="country", show_all=False,
                                      auto_choose=True, sort=True)
	occupation=models.IntegerField(default=0,choices=occupation_choice)
	mobile_number=PhoneNumberField()
	image=models.ImageField(upload_to='images')
	about=models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 


class Test(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	amount=models.IntegerField(default=0,choices=q_choices)
	level=models.IntegerField(default=0,choices=q_level)
	category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
	q_type=models.IntegerField(default=0,choices=q_type)
	status=models.IntegerField(default=0,choices=status)
	points=models.IntegerField(default=0)
	correct=models.IntegerField(default=0)
	session=models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

