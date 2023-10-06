from datetime import date

from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Karbaran
from .models import Product

# Create your views here.

all_posts = [
    {
        'slug': 'Prezi',
        'title': 'Prezi',
        'author': 'Isavandi',
        'image': 'Prezi.jfif',
        'date': date(2018, 1, 31),
        'short_description': 'Prezi is a Cloud-Based',
        'content': """What is Prezi Design?
            Meet Prezi Design, a cloud-based graphic design tool that lets anyone create and share dynamic designs and data visualizations with ease! Create eye-catching social media posts, share results with interactive infographics or dashboards, and produce engaging animated visualizations. You just have to pick a template, add your content or data, and share your creation with the world! Here's a short overview of what Prezi Design has to offer.
        """
    },

    {
        'slug': 'django',
        'title': 'Django',
        'author': 'Arbabi',
        'image': 'Django.png',
        'date': date.today(),
        'short_description': 'Django is Web Design',
        'content': """What is Django?
        The Django web framework is a free, open source framework that can speed up development of a web application being built in the Python programming language. 
        Django—pronounced “Jango,” named after the famous jazz guitarist Django Reinhardt—is a free, open source framework that was first publicly released in 2005. Django facilitates “rapid development and clean, pragmatic design.” The Django web framework, deployed on a web server, can help developers quickly produce a web frontend that’s feature-rich, secure and scalable.
        Starting with the Django web framework is more efficient way to build a web app than starting from scratch, which requires building the backend, APIs, javascript and sitemaps. With the Django web framework, web developers can focus on creating a unique application and benefit from greater flexibility than using a web development tool.
        """
    },

    {
        'slug': 'Database-SQLite',
        'title': 'Database',
        'author': 'Isavandi',
        'image': 'SQLite.jfif',
        'date': date(2019, 3, 3),
        'short_description': 'SQLite is a Database',
        'content': """What is SQLite?
        SQLite is a database engine written in the C programming language. It is not a standalone app; rather, it is a library that software developers embed in their apps. As such, it belongs to the family of embedded databases
        """
    },

    {
        'slug': 'Python-Programming',
        'title': 'Python.py',
        'author': 'Isavandi',
        'image': 'python1.png',
        'date': date.today(),
        'short_description': 'Python is a Programming Language',
        'content': """What is Python?
            Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems. This versatility, along with its beginner-friendliness, has made it one of the most-used programming languages today.

            Stack Overflow's 2022 Developer Survey revealed that Python is the fourth most popular programming language, with respondents saying that they use Python almost 50 percent of the time in their development work. Survey results also showed that Python is tied with Rust as the most-wanted technology, with 18% percent of developers who aren't using it already saying that they are interested in learning Python 

        """
    },

    {
        'slug': 'CSharp',
        'title': 'C#',
        'author': 'Khomi',
        'image': 'C#.png',
        'date': date.today(),
        'short_description': 'CSharp is a Programming Language',
        'content': """What is C# and what is it used for?
            C# (pronounced "See Sharp") is a modern, object-oriented, and type-safe programming language. C# enables developers to build many types of secure and robust applications that run in .NET. C# has its roots in the C family of languages and will be immediately familiar to C, C++, Java, and JavaScript programmers.
        """
    }
]


def get_date(post):
    return post['date']

def index(request):

    # d=list(all_posts)
    # context={
    #     'a':d
    # }
    # return render(request, 'blogs/index.html',context)

    sorted_post=sorted(all_posts,key=get_date)
    leatests=sorted_post[-2:]
    return render(request,'blogs/index.html',{'leatest_post':leatests})



def posts(request):
    return render(request,'blogs/all_post.html',{'all_posts':all_posts})


def single_post(request,slug):
    post=next(post for post in all_posts if post['slug']==slug)
    return render(request,'blogs/post_details.html',{'post':post})

def karbaran_list(request):
    all_karbaran=Karbaran.objects.all()
    return render(request,'blogs/karbaran_list.html',{'all_karbaran':all_karbaran})

def product_list(request):
    all_product=Product.objects.all().order_by('-price')
    number_of_product=all_product.count()
    info=all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('ratings'))
    return render(request,'blogs/product_list.html',{'all_products':all_product,'number_of_product':number_of_product,'info':info})

# def product_details(request,product_id):
    # try:
    #     products=Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    # products = get_object_or_404(Product,pk=product_id)
    # return render(request,'blogs/product_details.html',{'product':products})

def product_details(request,slug):
    products = get_object_or_404(Product,slug=slug)
    return render(request,'blogs/product_details.html',{'product':products})
