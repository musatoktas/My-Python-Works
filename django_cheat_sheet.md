I will write all of the codes that needed for install Python Django Web App Development Framework. There will be no long story descriptions because this is CheatSheet.


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