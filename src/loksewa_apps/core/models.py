from django.db import models
import uuid
from django.utils.translation import ugettext as _
from .abstract_models import (
    AbstractTimeStampModel,
    Gre_Question_Type,
    Gre_Answer_type,
    Gre_common_type,
)
# Note: question numbering, totoal = 20 per set
# For verbal: 1-6: Text Completion, 7-11: R.C, 12-16:Sent.Equiv,17-20: Critical Reasoning
# For math: 16,17,18 : data analysis, 1-15, and 19,20 arithmetic, algebra, geometric


# question type 1: simple
class Simple_Question(Gre_Question_Type): #Gre_Question_Type already has models.Model imported
    question = models.TextField(
        verbose_name=_("Question"),
    )

    # These are non-display field
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    question_created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    question_updated_date = models.DateTimeField(_("Updated date"), auto_now=True)

    
    difficulty_level = models.CharField(
        max_length=1,
        default="E",
        choices=Gre_common_type.DIFF_LEVEL
        )

    question_section = models.CharField(
        _("section"),
        max_length=2, 
        default="Ve",
        choices= Gre_common_type.GRE_TEST_SECTION
        )

    question_subject = models.CharField(
        _("subject"),
        max_length=6, 
        default="SC",
        choices=(
            ("Verbal",Gre_Question_Type.VERBAL_CHAPTER),
            ("Quant",Gre_Question_Type.QUANT_CHAPTER),
            ("uk","unknown"),
            )
        )
    
    
    # answer type e.g one blank , two blank , three blank, etc.
    # This is the table reference
    answer_type = models.CharField(
        _("Answer type"),
        max_length=3,
        choices=Gre_Answer_type.ANSWER_CHOICE
    )
    
    # This is the uuid of answer in answer table
    answer_id  = models.CharField(
        _("Answer Id"),
        max_length=100,
    )
    # Note required in case we need internal information 
    question_description = models.TextField(
        verbose_name=_("question description"),
        blank=True,
        default=""
    )

    published = models.CharField(
        verbose_name=_("published"),
        max_length=3,
        default="yes",
        choices=(
            ("yes", _("Yes")),
            ("no", _("No"))
        )
    )

# question type 1: paragraph based question essay writing question
class Essay_Writing_Question(AbstractTimeStampModel):
    question_description = models.TextField(
        verbose_name=_("Essay question"),
        blank=True,
        default=""
    )
    # This is required because argument essay comes first and then issue essay
    essay_type  = models.CharField(
        _("Essay type"),
        max_length=2,
        default="Ae",
        choices=(
            ("Ae","Argument Essay"),
            ("Ie","Issue Essay"),
        ) 
    )

    answer = models.TextField(
        verbose_name=_("essay answer"),
        blank=True,
        default=""
    )

# Paragraph based question , paragraph selection or one paragraph but 3-4 question. 
# since we need paragrph question lets have it seperated 
# We have: Paragraph_selection_question for one question with sentence selection in paragraph
# we have:Verbal_One_Paragraph_Many_Question for many question associated with one paragraph. 
# These two are associated with verbal section only 
# for sentence selection we can use verbal one paragraph many to many question we may not need this one
class Verbal_Paragraph_Selection_Question(AbstractTimeStampModel):
    question_paragraph = models.TextField(
        verbose_name=_("Question paragraph"),
        blank=True,
        default=""
    )
    # on_delete=models.SET_NULL, null=True
    question = models.ForeignKey(Simple_Question, on_delete= models.CASCADE)

class Verbal_One_Paragraph_Many_Question(AbstractTimeStampModel):
    question_paragraph = models.TextField(
        verbose_name=_("Question paragraph"),
        blank=True,
        default=""
    )
    # This choice is required to categorize the question in number
    # e.g if RC question should be placed in 10-15/14 number, if CR then 16/17-20
    Question_type  = models.CharField(
        _("verbal question type"),
        max_length=2,
        default="RC",
        choices=(
            ("RC","Reading Comprehension"),
            ("CR","Critical Reasoning"),
        ) 
    )
    
    # We will first make question and the we stick it here after making it
    paragraph_question_collection = models.ManyToManyField(
        Simple_Question,
        verbose_name=_("Paragraph question collection"),
        blank=True
    )
    # answer  will be in the question reference

# ata analysis question will have figure , image figure and question betn 15-17
class Quant_Data_Analysis_Question(AbstractTimeStampModel):
    # file will be saved to MEDIA_ROOT/uploads/2018/11/25
    # Note file should be renamed randomly everytime upload,
    # if user upload same file in same day it might get conflicted with file name,so rename it with uuid
    upload_analysis_image = models.FileField(upload_to='uploads/%Y/%m/%d/')

    # first create the questions from simple model and come back here to stick it
    simple_question_collection = models.ManyToManyField(
        Simple_Question,
        verbose_name=_("Data analysis question collection"),
        blank=True
    )

# ==================== Below: Question Sets========================== #

# set infomations : Note each set must have 20 question so we need to be able to count the question
class Quant_Set(AbstractTimeStampModel):
    set_name = models.CharField(
        _("Set name"),
        max_length=40,
    )
    set_difficulty_level =  models.CharField(
        _("set dificulty"),
        max_length=1,
        default="E",
        choices=Gre_common_type.DIFF_LEVEL 
    )

    simple_question_collection = models.ManyToManyField(
        Simple_Question,
        verbose_name=_("Simple question collection"),
        blank=True
    )
    
    data_analysis_question_collection = models.ManyToManyField(
        Quant_Data_Analysis_Question,
        verbose_name=_("Data analysis question collection"),
        blank=True
    )

class Verbal_Set(AbstractTimeStampModel):
    set_name = models.CharField(
        _("Set name"),
        max_length=40,
    )
    set_difficulty_level =  models.CharField(
        _("set dificulty"),
        max_length=1,
        default="E",
        choices=Gre_common_type.DIFF_LEVEL 
    )

    simple_question_collection = models.ManyToManyField(
        Simple_Question,
        verbose_name=_("Simple question collection"),
        blank=True
    )

    # question between 10-15 number for RC, and for reading comprehension 17-20 
    paragraph_question_collection = models.ManyToManyField(
        Verbal_One_Paragraph_Many_Question,
        verbose_name=_("Paragraph based multiple question collection"),
        blank=True
    )
    # question in 16 or 17 number
    paragraph_selection_question_collection = models.ManyToManyField(
        Verbal_Paragraph_Selection_Question,
        verbose_name=_("Paragraph selection question "),
        blank=True
    )

# Essay set has no difficulty level:  Each collection has two essays
class Essay_Set(AbstractTimeStampModel):
    set_name = models.CharField(
        _("Set name"),
        max_length=40,
    )

    essay_question_collection = models.ManyToManyField(
        Essay_Writing_Question,
        verbose_name=_("Essay collection"),
        blank=True
    )

# ============= Below: answer sections================== # 

class Answer_One_Blank(AbstractTimeStampModel):
    
    # question = models.ForeignKey(Simple_Question, on_delete= models.CASCADE)

    ANSWER_CHOICE = (
            ("a","Option A"),
            ("b","Option B"),
            ("c","Option C"),
            ("d","Option D"),
            ("e","Option E"),
            )

    option_a = models.CharField(
        _("Option A"),
        max_length=40,
    )
    option_b = models.CharField(
        _("Option B"),
        max_length=40,
    )
    option_c = models.CharField(
        _("Option C"),
        max_length=40,
    )
    option_d = models.CharField(
        _("Option D"),
        max_length=40,
    )
    option_e = models.CharField(
        _("Option E"),
        max_length=40,
    )
    correct_answer = models.CharField(
        _("Correct Option"),
        max_length=1,
        choices=ANSWER_CHOICE,
        default=ANSWER_CHOICE[0][0]
        )
    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )

class Answer_Two_Blank(AbstractTimeStampModel):
    option_a = models.CharField(
        _("Option A"),
        max_length=40,
    )
    option_b = models.CharField(
        _("Option B"),
        max_length=40,
    )
    option_c = models.CharField(
        _("Option C"),
        max_length=40,
    )
    option_d = models.CharField(
        _("Option D"),
        max_length=40,
    )
    option_e = models.CharField(
        _("Option E"),
        max_length=40,
    )
    option_f = models.CharField(
        _("Option E"),
        max_length=40,
    )
    correct_answer_first_blank = models.CharField(
        _("Correct Option for first blank"),
        max_length=1,
        default="a",
        choices=(
            ("a","Option A"),
            ("b","Option B"),
            ("c","Option C"),
            )
        )
    correct_answer_second_blank = models.CharField(
        _("Correct Option for second blank"),
        max_length=1,
        default="d",
        choices=(
            ("d","Option D"),
            ("e","Option E"),
            ("f","Option F"),
            )
        )

    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )

class Answer_Three_Blank(AbstractTimeStampModel):
    option_a = models.CharField(
        _("Option A"),
        max_length=40,
    )
    option_b = models.CharField(
        _("Option B"),
        max_length=40,
    )
    option_c = models.CharField(
        _("Option C"),
        max_length=40,
    )
    option_d = models.CharField(
        _("Option D"),
        max_length=40,
    )
    option_e = models.CharField(
        _("Option E"),
        max_length=40,
    )
    option_f = models.CharField(
        _("Option E"),
        max_length=40,
    )
    option_g = models.CharField(
        _("Option G"),
        max_length=40,
    )
    option_h = models.CharField(
        _("Option H"),
        max_length=40,
    )
    option_i = models.CharField(
        _("Option I"),
        max_length=40,
    )
    
    correct_answer_first_blank = models.CharField(
        _("Correct Option for first blank"),
        max_length=1,
        default="a",
        choices=(
            ("a","Option A"),
            ("b","Option B"),
            ("c","Option C"),
            )
        )

    correct_answer_second_blank = models.CharField(
        _("Correct Option for second blank"),
        max_length=1,
        default="d",
        choices=(
            ("d","Option D"),
            ("e","Option E"),
            ("f","Option F"),
            )
        )

    correct_answer_third_blank = models.CharField(
        _("Correct Option for third blank"),
        max_length=1,
        default="g",
        choices=(
            ("g","Option G"),
            ("h","Option H"),
            ("i","Option I"),
            )
        )

    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )

# seperated to do math operation
class Answer_With_Numeric_Input(AbstractTimeStampModel):

    correct_answer = models.CharField(
        _("Correct Answer"),
        max_length=10,
        default=""
        ) 

    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )

# This choice could have single paragraph as input, not used in GRE for now
class Answer_With_Text_Input(AbstractTimeStampModel):
    
    correct_answer = models.CharField(
        _("Correct Answer"),
        max_length=400,
        default=""
        )
    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )

# for multiple selection the answer is text, so could be upto 300 character
class Answer_Multiple_selection(AbstractTimeStampModel):
    option_a = models.CharField(
        _("Option A"),
        max_length=350,
    )
    option_b = models.CharField(
        _("Option B"),
        max_length=350,
    )
    option_c = models.CharField(
        _("Option C"),
        max_length=350,
    )
    
    option_a_status = models.BooleanField(default=False)
    option_b_status = models.BooleanField(default=False)
    option_c_status = models.BooleanField(default=False)

    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )

# for multiple selection for math question with 5 multiple selection option
class Answer_Multiple_selection_With_Five_Option(AbstractTimeStampModel):
    option_a = models.CharField(
        _("Option A"),
        max_length=350,
    )
    option_b = models.CharField(
        _("Option B"),
        max_length=350,
    )
    option_c = models.CharField(
        _("Option C"),
        max_length=350,
    )
    option_d = models.CharField(
        _("Option D"),
        max_length=350,
    )
    option_e = models.CharField(
        _("Option E"),
        max_length=350,
    )

    option_a_status = models.BooleanField(default=False)
    option_b_status = models.BooleanField(default=False)
    option_c_status = models.BooleanField(default=False)
    option_d_status = models.BooleanField(default=False)
    option_e_status = models.BooleanField(default=False)

    answer_description = models.TextField(
        verbose_name=_("Answer description"),
        blank=True,
        default=""
    )









