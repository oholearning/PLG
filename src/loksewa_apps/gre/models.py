from django.db import models
from django.urls import reverse
from loksewa_apps.core.models import (
    # questions
    Simple_Question,
    Essay_Writing_Question,
    Quant_Data_Analysis_Question,
    Verbal_One_Paragraph_Many_Question,
    # answers
    Answer_One_Blank,
    Answer_Two_Blank,
    Answer_Three_Blank,
    Answer_With_Numeric_Input,
    Answer_With_Text_Input,
    Answer_Multiple_selection,
    Answer_Multiple_selection_With_Five_Option,
)
# Create your models here.

# Note answer types
# ("SOB","Simple one blank"),
# ("STB","Simple two blank"),
# ("STr","Simple three blank"),
# ("NI","Numeric input"),
# ("TI","Text input"),
# ("MC3","Multiple check answer with 3 options"),
# ("MC5","Multiple check answer with 5 options"),

class SimpleQuestionWithOneBlank(Simple_Question,Answer_One_Blank):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "SOB"
        super(SimpleQuestionWithOneBlank, self).save(*args, **kwargs)

class SimpleQuestionWithTwoBlank(Simple_Question,Answer_Two_Blank):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "STB"
        super(SimpleQuestionWithTwoBlank, self).save(*args, **kwargs)

class SimpleQuestionWithThreeBlank(Simple_Question,Answer_Three_Blank):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "STr"
        super(SimpleQuestionWithThreeBlank, self).save(*args, **kwargs)

class SimpleQuestionWithNumericInput(Simple_Question,Answer_With_Numeric_Input):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "NI"
        super(SimpleQuestionWithNumericInput, self).save(*args, **kwargs)

class SimpleQuestionWithTextInput(Simple_Question,Answer_With_Text_Input):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "TI"
        super(SimpleQuestionWithTextInput, self).save(*args, **kwargs)

class SimpleQuestionWithMultipleSelectionThreeInput(Simple_Question,Answer_Multiple_selection):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "MC3"
        super(SimpleQuestionWithMultipleSelctionThreeInput, self).save(*args, **kwargs)

class SimpleQuestionWithMultipleSelectionFiveInput(Simple_Question,Answer_Multiple_selection_With_Five_Option):
    
    def question(self):
        return self.question
    
    def published_yes_no(self):
        return self.published
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
    def question_section(self):
        return self.question_section

    # Lets overwrite the save method
    def save(self, *args, **kwargs):
        if self.id is not None:
            # then we set the values
            self.answer_id = self.id
            self.answer_type = "MC5"
        super(SimpleQuestionWithMultipleSelectionFiveInput, self).save(*args, **kwargs)

# For many to many question and paragraph selection question ,will have one para with many types of questions
class VerbalOneParagraphManyQuestion(Verbal_One_Paragraph_Many_Question):
    
    def question_paragraph(self):
        return self.question_paragraph
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))
    
class QuantativeDataAnalysisQuestion(Quant_Data_Analysis_Question):
    
    def updated_date_string(self):
        return self.updated_date
    
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %(self._meta.app_label, self._meta.model_name), args=(self.pk,))

