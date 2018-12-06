from django.contrib import admin
from  django.utils.html import format_html
# # Register your models here.

from .models import (
    SimpleQuestionWithOneBlank,
    SimpleQuestionWithTwoBlank,
    SimpleQuestionWithThreeBlank,
    SimpleQuestionWithNumericInput,
    SimpleQuestionWithTextInput,
    SimpleQuestionWithMultipleSelectionThreeInput,
    SimpleQuestionWithMultipleSelectionFiveInput,
    VerbalOneParagraphManyQuestion,
    QuantativeDataAnalysisQuestion,
)


# single blank
@admin.register(SimpleQuestionWithOneBlank)
class SingleBlankWithFiveOptionQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "option_a",       
        "option_b",       
        "option_c",       
        "option_d",       
        "option_e",
        "correct_answer",
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))

# double blank
@admin.register(SimpleQuestionWithTwoBlank)
class TwoBlankWithSixOptionQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "option_a",       
        "option_b",       
        "option_c",       
        "option_d",       
        "option_e",
        "option_f",
        "correct_answer_first_blank",
        "correct_answer_second_blank",
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))


# Three blank
@admin.register(SimpleQuestionWithThreeBlank)
class ThreeBlankWithNineOptionQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "option_a",       
        "option_b",       
        "option_c",       
        "option_d",       
        "option_e",
        "option_f",
        "option_g",
        "option_h",
        "option_i",
        "correct_answer_first_blank",
        "correct_answer_second_blank",
        "correct_answer_third_blank",
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))


# Numeric input
@admin.register(SimpleQuestionWithNumericInput)
class NumericInputOptionQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "correct_answer",
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))


# Text input
@admin.register(SimpleQuestionWithTextInput)
class TextInputOptionQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "correct_answer",
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))


# multiple selection 3 input
@admin.register(SimpleQuestionWithMultipleSelectionThreeInput)
class MultipleSelectionThreeInputQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "option_a",       
        "option_b",       
        "option_c",       
        "option_a_status",       
        "option_b_status",       
        "option_c_status",       
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))

# multiple selection 5 input
@admin.register(SimpleQuestionWithMultipleSelectionFiveInput)
class MultipleSelectionFiveInputQuestion(admin.ModelAdmin):
    fields = (
        "question",
        "difficulty_level",
        "question_section",
        "question_subject",
        "question_description",
        "option_a",       
        "option_b",       
        "option_c",       
        "option_d",       
        "option_e",
        "option_a_status",       
        "option_b_status",       
        "option_c_status", 
        "option_d_status", 
        "option_e_status", 
        "answer_description",       
    )

    list_display = ['question_section','title_link',  'published_',  'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question[0:50]))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
    def question_section(self,obj):
        return format_html('%s' % (obj.question_section()))

# one para many question
@admin.register(VerbalOneParagraphManyQuestion)
class OneParagraphManyQuestion(admin.ModelAdmin):
    fields = (
        "question_paragraph",
        "Question_type",
        "paragraph_question_collection",       
    )

    list_display = ['Question_type','title_link',   'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % (obj.question_paragraph[0:50]))
    
    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
    
# data analaysis : with image/figure
@admin.register(QuantativeDataAnalysisQuestion)
class DataAnalysisQuestion(admin.ModelAdmin):
    fields = (
        "upload_analysis_image",
        "simple_question_collection",
    )

    list_display = [ 'title_link',    'edit_link', 'updated_date_' ]

    ordering = ('-updated_date',)

    def title_link(self,obj):
        return  format_html('%s' % ("Data Analysis"))

    def updated_date_(self,obj):
        return format_html('%s' % ( obj.updated_date_string()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())
