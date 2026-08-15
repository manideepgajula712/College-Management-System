from rest_framework.routers import DefaultRouter

from .views import ExaminationViewSet, ResultViewSet


router = DefaultRouter()

router.register(
    "examinations",
    ExaminationViewSet,
    basename="examination"
)

router.register(
    "results",
    ResultViewSet,
    basename="result"
)


urlpatterns = router.urls