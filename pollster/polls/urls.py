from django.urls import path

from . import views
from rest_framework import routers
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    #router.urls,
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
