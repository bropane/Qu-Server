from random import sample
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from api_keys.permissions import AuthorizedClientPermission

from .models import Question
from .serializers import QuestionSerializer


@permission_classes((AuthorizedClientPermission,))
@api_view()
def get_random_question(request, format=None):
    count = Question.objects.all().count()
    question = Question.objects.all()[sample(xrange(0, count), 1)[0]]
    serializer = QuestionSerializer(question)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((AuthorizedClientPermission,))
def create_question(request, format=None):
    try:
        question_text = request.data['question']
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    question = Question(question=question_text)
    question.save()
    serializer = QuestionSerializer(question)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((AuthorizedClientPermission,))
def answer_positive(request, pk, format=None):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        return Http404
    question.positive_count += 1
    question.save()
    serializer = QuestionSerializer(question)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((AuthorizedClientPermission,))
def answer_negative(request, pk, format=None):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        return Http404
    question.negative_count += 1
    question.save()
    serializer = QuestionSerializer(question)
    return Response(serializer.data)


@permission_classes((AuthorizedClientPermission,))
class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer