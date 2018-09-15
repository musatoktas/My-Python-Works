<h1> Django Fresh Breath - After 23458 Times Learning Attempts</h1>
<p> From now on Code Starts to speak </p>
<code> 
python --version 
pip --version
pip install virtualenwrapper-win
cd users/musa/projects
mkvirtualenv py1
workon py1 // selecting working env
pip install django==1.8
clear // clear screen
django-admin startproject projectname
dir
cd projectname
code . // Opening Visual Studio
Commend Line Interface Tool Admin
manage.py is CLI client wrapper of Django Admin
run migration etc using by this
Secret Key must hidden in github
Debug = True while develop
Installed Apps as the name of itself
Database
URL routing, uses regex, 
^ mean start with;  than goes to there anything admin/ goes to admin to admin file
wsgi primary development area for django
common standard for web servers and applications
runing a web server
python manage.py runserver
running on localhost
migrations are things in database tables rows etc.
unapplied migrationns mean, we havent created in our database
if dont wanna use sqlite3 we dont apply those
pip install mysqlclient
go django database section
dekete database
create following
DATABASES ={
  'default' {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'djangoproject // NOW GO DOWN and come again
    'USER': 'root',
    'PASSWORD': '123456',
    'HOST': 'localhost',
    'PORT': '' //SAVE IT
    }
}
start xampp and go localhost/phpmyadmin/
create database named djangoproject

python manage.py migrate // you can go check phpmyadmin databse do you have your tables in your database
python manage.py runserver
now we should go localhost:8000/admin
goto command line
python manage.py createsuperuser --username=name --email=yourmail@gmail.com
go run it and it will ask for password it has to at least 8 charr
run server again and reload admin page
here is the admin page,
lets start the server from command line and create a blog app
ctrl+c for stop the server
python manage.py startapp post 
post/admin.py //adding admin the models
go projectname/settings.py installed apps section add post
go projectname/urls.py add this to below admin url conf (r^post/, include('post.urls')),
go post/urls.oy
from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$0', views.index, name='index') //we dont want post/ on brrowser search bar we want post end with nathing
]; we will create index method for view 
go post/views
from django.shortcuts import render
from django.http import HttpResponse
// Creating views
def index(request):
  return HttpResponse('Post tan merhabalar') when goes to /post in browser we eill see post tan merhabalar
  after we test it out, lets change HttpResponse just comment it out
def index will be like this below:
def index(request);
  return render(request, 'post/index.html') we havent created index.html 
go to projectname folder and create templates/post/index.html
<h1> Hello From index.html</h1>
restart and test it from localhost:8000/post
we dont wanna use every time h1 and other elements so we gonna create laouy
 go to projectname/templates/layout.html
use just exclamation ! and press enter
we wanna use materiealize css so visit their website and copy the CDN css link to the head as a style sheet ling
so we are start to coding body
<header class="container center-align">
  <h1>I admire my Django Learning Desire</h1>
</header>
<div class='container'>
  {% block content %}
  {% endblock %}
</div>
go to projectname/templates/post/index.html
{% extends 'posts/layout.html'%}
{% block content %}
<h3 class="center-align red lighten-3">Latest Posts</h3>
{% endblock %}
Lets go post/models.py
from django.db import models
from datetime import datetime
class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True) //now save it stop server, makemigrations post, migrate
  def __str__(self):
    return self.title
    
we might add admin login button to our layouts so lets do it
go to projectname/templates/post/layout.html
<a style="display:block" class="center-align" href="/admin">Admin Login</a>
we need to bring our models to admin panel lets do it
go to projectname/admin.py
from post/models/py import Post

admin.site.register(Post) go to admin site and check it out
to fix plural problem go to post/models.py
add below line under the Post class as a list item
class Meta:
  verbose_name_plural = "Post"

So everything is ready we are able to add post item to our site
Now we redirect our homepage to post, to do that jump in to projectname/urls.py ad at the top of urls add a eew one
url(r'^$', include('post.urls')),
we basicly one to bring all the blogs from the model,  so open the post/view.py [age
in the def index we will create a variable and import post
def index(request):
  post = Post.objects.all()[:10]
  context = {
    'title': 'Latest Posts',
    'posts': post
  }
After editing the view, final step is editing the index.html and creating the url path for redirect each posts
<ul class="collection">
{% for post in post%}
  <li class="collection-item"><a href="/posts/details/{{post.id}}"{{post.title}}</li>
{% endfor%}
</ul>
post/urls.py
url(r'^details/(?P<id>\d+)/$', view.details, name='details')
lets go into our views again
def details(request, id):
  post =Post.objects.get(id=id)
  context = {
    'post' : post
    }
creating new file in templates/post/details.html
{% extends 'post/layout.html%}
{% block content %}
<h3 class=|center-align red lighten-3">{{post.title}}</h3>
<div class="card">
  <div class="card-content">
    {{%post.body%}}
  </div>
  <div class="card-action">
      {{post.created_at}}
  </div>
  <a href="/post" class="btn"> Go Back</a>
{% endblock %}

</code>
