from rest_framework import serializers
from loksewa_apps.gre.models import (
    SimpleQuestionWithOneBlank,
    SimpleQuestionWithTwoBlank,
    SimpleQuestionWithThreeBlank,
    SimpleQuestionWithNumericInput,
    SimpleQuestionWithTextInput,
    SimpleQuestionWithMultipleSelectionThreeInput,
    SimpleQuestionWithMultipleSelectionFiveInput,
    VerbalOneParagraphManyQuestion,
    QuantativeDataAnalysisQuestion,
    # sets serializer
    QuantativeSet,
    VerbalSet,
    EssaySet
)

# class DocumentLinkInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DocumentLinkInfo
#         fields = '__all__'

class SimpleQuestionWithOneBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithOneBlank
        fields = '__all__'

class SimpleQuestionWithTwoBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithTwoBlank
        fields = '__all__'

class SimpleQuestionWithThreeBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithThreeBlank
        fields = '__all__'

class SimpleQuestionWithNumericInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithNumericInput
        fields = '__all__'

class SimpleQuestionWithTextInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithTextInput
        fields = '__all__'

class SimpleQuestionWithMultipleSelectionThreeInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithMultipleSelectionThreeInput
        fields = '__all__'

class SimpleQuestionWithMultipleSelectionFiveInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleQuestionWithMultipleSelectionFiveInput
        fields = '__all__'

class VerbalOneParagraphManyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbalOneParagraphManyQuestion
        fields = '__all__'

class QuantativeDataAnalysisQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantativeDataAnalysisQuestion
        fields = '__all__'

# serialize sets
class QuantativeSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantativeSet
        fields = '__all__'


class VerbalSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbalSet
        fields = '__all__'

class EssaySetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssaySet
        fields = '__all__'
