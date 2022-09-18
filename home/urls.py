from django.conf import settings
#from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
#from .views import SignUpView
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('home', views.home, name='home'),
    #path('register/', views.register_user, name='register'),
    path('register/', views.register_user, name='register'),
    #path('accounts/login/', LoginView.as_view()),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)