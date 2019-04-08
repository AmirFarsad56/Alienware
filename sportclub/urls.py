from django.urls import include, path
from sportclub.views import SportClubSignupView

app_name ='sportclub'
urlpatterns = [
    path('sportclub/signup/', SportClubSignupView, name='signup'),
]