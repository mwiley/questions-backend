from rest_framework_json_api import serializers
from questions.models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Question
    fields = ('title_text', 'question_text')