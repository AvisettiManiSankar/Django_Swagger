from .views import *
from django.urls import path

urlpatterns = [
    path("get_questions", GetQuestionsView.as_view())
]