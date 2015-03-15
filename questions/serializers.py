__author__ = 'Taylor'

from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'positive_count', 'negative_count', 'time_asked')