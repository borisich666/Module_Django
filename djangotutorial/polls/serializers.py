from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        read_only_fields = ["id"]
        fields = [
            "id",
            "question_text",
            "pub_date"
        ]