from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register),
    path('login', views.login),
    path('selectcategory', views.selectcategory),
    path('selectquiz/<int:category_id>', views.selectquiz),
    path('takequiz/<int:quiz_id>', views.takequiz),
    path('processquiz/<int:quiz_id>', views.processquiz),
    path('results', views.results),
    path('logout', views.logout)
]