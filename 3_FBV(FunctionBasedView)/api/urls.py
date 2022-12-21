from django.urls import path
from .views import totalQuiz
from .views import randomQuiz
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', totalQuiz),
    path('<int:id>/', randomQuiz)
    # path('',  totalQuiz.as_view()),
    # path('<int:pk>/', randomQuiz.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
