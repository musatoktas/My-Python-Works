<h1>Installation</h1>

I will write all of the codes that needed for install Python Django Web App Development Framework. There will be no long story descriptions because this is CheatSheet.

Before all of these you need to get pip and open your command prompt or terminal

Start with installing Virtual Environment<br/>

`pip install virtualenv`
<br/>

Creating Venv

`
virtualenv sample_venv`<br/>
`cd sample_venv`<br/>

Install Django into the venv<br/>
`pip install django==1.8`

```
python .\Scripts\django-admin.py startproject test_project

cd test_project

python manage.py migrate #you can use syncdb version1.8< instead of this.

python manage.py createsuperuser #note your username&password youll login from your local server / admin

python manage.py runserver #now all of boileplate is ready

```
Now you are ready to go!

<h1>Start App</h1>

for start new app in django project

`python migrate.py startapp merhaba`

urls.py staff
```
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [ 
  url(r'^admin/', admin.site.urls),
  url(r'^', include('merhaba.urls'))
]
```
In the second app make a new urls.py file. Django just make it once project just built.

```
from django.conf.urls import include, url 
from merhaba import views

urlpatterns = [
  url('r^$', views.merhaba)
  url('r^$merhaba', views.merhaba_html)
]
```
<h2>views.py</h2> 
First

```
from django.http import HttpResponse
from django.shortcuts import render

def merhaba(request)
  print ("merhaba")
  return HttpResponse("Merhaba")
```
Second
```
def merhaba(request):
  print("body: %s" % request.body)
  print("path: %s" % request.path)
  print("content_type %s" % request.content_try)
  print("META %s" %request.META)
  return HttpResponse("merhaba")
```
Third
```
def toplama(request):
  sayi1 = 10
  sayi2 = 20
  return HttpResponse(sayi1+sayi2)
```
Forth

```
def toplama(request):
  sayi1 = 10
  sayi2 = 20
  return HttpResponse(sayi1+sayi2)
```
Fifth
```
def merhaba_html(request)
  response = HttpResponse()
  response.write("<h1>Django Kursu</h1>")
  response.write("<p>alademik bilisim</p>")
  return response
```

<h2>Test Methodu</h2>
<strong>Unit Test</strong>

```
from django import TestCase
class MerhabaViewTest(TestCase):
def test_toplama(self):
  response = self.client.get("/toplama")
  self.assertEqual(response.content, b'30')
```

<li>Delete ab part inthe url part. There are several string types exists like byte string. In total b'30' is expecting.</li>
  
  
### Template directory settings in settings.py;

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'),
                 os.path.join(os.path.dirname(__file__), 'static'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
