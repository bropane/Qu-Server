from rest_framework import viewsets

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

