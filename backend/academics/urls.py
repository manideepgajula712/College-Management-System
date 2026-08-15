from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, SubjectViewSet


router = DefaultRouter()

router.register(
    "courses",
    CourseViewSet,
    basename="course"
)

router.register(
    "subjects",
    SubjectViewSet,
    basename="subject"
)

urlpatterns = router.urls