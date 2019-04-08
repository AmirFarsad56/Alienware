from django.urls import include, path
from commonuser.views import CommonUserSignupView,CommonUserListView

app_name ='commonuser'
urlpatterns = [
    path('commonuser/signup/', CommonUserSignupView, name='signup'),
    path('accounts/list/', CommonUserListView.as_view())
]