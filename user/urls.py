from rest_framework import routers

from user.views import AdminProfileViews


router = routers.DefaultRouter()
router.register("users", AdminProfileViews, basename="users_apis")

app_name= "user"

urlpatterns = [

]

urlpatterns += router.urls
