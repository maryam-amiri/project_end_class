from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


#modele dastebandi:
#bayad ghabl az product bashad(shey garayi/ertebate yek b chand)

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

#ertebate yek b yek

class ProductInformation(models.Model):
    color=models.CharField(max_length=200,verbose_name='رنگ')
    size=models.CharField(max_length=200,verbose_name='سایز')

    def __str__(self):
        return f'{self.color}----{self.size}'

    class Meta:
        verbose_name='لیست اطلاعات'
        verbose_name_plural='لیست اطلاعات'

#rabeteye chand b chand:

class ProductTag(models.Model):
    tag=models.CharField(max_length=200,verbose_name='عنوان تگ')

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name='تگ محصول'
        verbose_name_plural='تگ های محصولات'


#bayad kilid tarif shavad-->category--relation bein product va productCategory ijad mikonim
#unique kardan slug:
class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True,verbose_name='دسته بندی')
    product_information=models.OneToOneField(ProductInformation,on_delete=models.CASCADE,null=True,blank=True,verbose_name='اطلاعات تکمیلی',related_name='product_info')
    product_tag=models.ManyToManyField(ProductTag,verbose_name='تگ محصول')
    title=models.CharField(max_length=50,verbose_name='عنوان محصول')
    price=models.IntegerField(verbose_name='قیمت')
    description=models.CharField(max_length=300,verbose_name='توضیحات')
    is_active=models.BooleanField(verbose_name='فعال/غیرفعال')
    ratings=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)],verbose_name='امتیاز')
    slug=models.SlugField(max_length=400,unique=True,default='',null=False,db_index=True,verbose_name='عنوان در url')
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}--{self.description}--{self.price}'

    def get_absolute_url(self):
        return reverse('product-details',args={self.slug})

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'


class Karbaran(models.Model):
    name=models.CharField(max_length=20)
    family=models.CharField(max_length=20)
    age=models.IntegerField()
    #emailk=models.EmailField()
    is_active=models.BooleanField()


