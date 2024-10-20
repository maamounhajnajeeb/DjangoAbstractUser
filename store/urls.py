from rest_framework import routers

from .views import BlogCrud


app_name = "store"


router = routers.DefaultRouter()
router.register("blog", BlogCrud, basename="blog_crud_router")

urlpatterns = [

]

urlpatterns += router.urls
