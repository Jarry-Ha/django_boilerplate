from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random
from rest_framework import generics


# class totalQuiz(generics.ListCreateAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer


# class randomQuiz(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer

@api_view(['GET'])
def totalQuiz(request):
    totalQuizs = Quiz.objects.all()
    serializer = QuizSerializer(totalQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomQuiz(request, id):	 # id가 url의 인자로 들어옴
    totalQuizs = Quiz.objects.get(pk=id)
    # totalQuizs = random.sample(list(totalQuizs),id)
    serializer = QuizSerializer(totalQuizs, many=False)
    return Response(serializer.data)