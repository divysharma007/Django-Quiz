from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/<int:id>',user_details),
    path('logout',logout_user),
    path('login',login_user,name="login"),
    path('signup', signup),
    # path('profile/<int:id>', profile),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
