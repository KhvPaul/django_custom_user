from django.urls import path

from . import views

app_name = "example"

urlpatterns = [
    path("", views.UserListView.as_view(), name="user_list"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("registration/", views.RegisterFormView.as_view(), name="user_register"),
    path("update_profile/", views.UserUpdateView.as_view(), name="user_update"),
]
