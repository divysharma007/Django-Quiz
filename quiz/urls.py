from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('quiz/<int:quiz_id>/test', showquiz,name="test"),
    path('quiz/<int:quiz_id>/enroll',enrollment_key_checker,name="check")



]
