from rest_framework import routers 
from main.views import *

router = routers.DefaultRouter()

router.register("category", CategoryView)
router.register("product", ProductView)
router.register("productitem", ProductItemView)
router.register("deliver", DeliverView)