from django.urls import path, include
from . import views
from rest_framework import routers
from .views import QuestionViewSet, ChoiceViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/', include(router.urls)),
]
