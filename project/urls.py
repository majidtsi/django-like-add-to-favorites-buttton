
from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/<int:id>",views.product_detail,name="detail"),
    path("user/favourites",views.user_favourites,name="user_favourites"),
    path("product/<int:id>/like_or_dislike",views.like_or_unlike,name="like"),
]
