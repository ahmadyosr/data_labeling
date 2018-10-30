from django.db import models
from django.contrib.auth.models import User

NEWSPAPER_CHOICES = (
    ('ADDUSTOUR', 'addustour'),
    ('ALRAI', 'alrai'),
)

class Category(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Publisher(models.Model):
	title = models.CharField(max_length=50)
	
	def __str__(self):
		return self.title

class Newspaper(models.Model):
	is_extracted = models.BooleanField(default=False)
	is_splitted = models.BooleanField(default=False)
	is_ocr = models.BooleanField(default=False)
	is_find_tenders = models.BooleanField(default=False)
	

	title = models.CharField(blank=True, max_length=50,choices=NEWSPAPER_CHOICES)
	publish_date = models.DateField(null=True, blank=True, auto_now_add=False)
	file = models.FileField(blank=False, null=False, upload_to='newspapers_pdfs/', unique=True)
	
	def __str__(self):
		return self.file.name


class NewspaperPage(models.Model):
	newspaper = models.ForeignKey(Newspaper, null=True, on_delete=models.CASCADE)
	page_no = models.IntegerField(default=0)
	image = models.FileField(upload_to='newspapers_pages/')
	has_tenders = models.BooleanField(default=False)
	has_snippets = models.BooleanField(default=False)
	is_extracted = models.BooleanField(default=False)

class Snippet(models.Model):
	newspaper = models.ForeignKey(Newspaper, null=True, on_delete=models.SET_NULL)
	page = models.ForeignKey(NewspaperPage, null=True, on_delete=models.SET_NULL)

	title = models.CharField(blank=True, max_length=50)
	extract_date = models.DateField(auto_now_add=True)
	start_date = models.DateField(blank=True, null=True)
	finish_date = models.DateField(blank=True, null=True)


	publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)
	admin = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)


	is_tender = models.BooleanField(default=False)
	is_auction = models.BooleanField(default=False)
	is_republished = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	image = models.FileField(upload_to='tenders_images/')
	text = models.CharField(blank=True, max_length=200)
	suggested_category = models.ForeignKey(Category,blank=True, null=True, on_delete=models.SET_NULL, related_name='suggested_category')
	# category = models.ForeignKey(Category,blank=True, null=True, on_delete=models.SET_NULL)
	category = models.CharField(null=True, blank=True, max_length=50)

	bw_rate = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title


