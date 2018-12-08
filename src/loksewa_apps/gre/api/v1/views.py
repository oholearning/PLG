from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import (
    # SimpleQuestionWithOneBlankSerializer,
    # SimpleQuestionWithTwoBlankSerializer,
    # SimpleQuestionWithThreeBlankSerializer,
    # SimpleQuestionWithNumericInputSerializer,
    # SimpleQuestionWithTextInputSerializer,
    # SimpleQuestionWithMultipleSelectionThreeInputSerializer,
    # SimpleQuestionWithMultipleSelectionFiveInputSerializer,
    # VerbalOneParagraphManyQuestionSerializer,
    # QuantativeDataAnalysisQuestionSerializer,
    QuantativeSetSerializer,
    VerbalSetSerializer,
    EssaySetSerializer

)
from loksewa_apps.gre.models import (
    # SimpleQuestionWithOneBlank,
    # SimpleQuestionWithTwoBlank,
    # SimpleQuestionWithThreeBlank,
    # SimpleQuestionWithNumericInput,
    # SimpleQuestionWithTextInput,
    # SimpleQuestionWithMultipleSelectionThreeInput,
    # SimpleQuestionWithMultipleSelectionFiveInput,
    # VerbalOneParagraphManyQuestion,
    # QuantativeDataAnalysisQuestion,
    QuantativeSet,
    VerbalSet,
    EssaySet   
)

# Need to work on this one