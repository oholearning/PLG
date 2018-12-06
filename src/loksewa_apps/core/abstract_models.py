from django.db import models 
# import abc
import uuid
from django.utils.translation import ugettext_lazy as _

class AbstractTimeStampModel(models.Model):
    """TimeStampModel that holds created_date and updated_date field"""
    # django will add id field automatically as pk , so no need for this
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated date"), auto_now=True)

    def __str__(self):
        return self.created_date

    class Meta:
        abstract = True

class Gre_Question_Type(models.Model):
    QUANT_CHAPTER = (
        ("Ar", _("Arithmetic")),
        ("Al", _("Algebra")),
        ("Ge", _("Geometry")),
        ("DA", _("Data analysis")),
    )
    
    VERBAL_CHAPTER = (
        ("SC", _("Sentence Completion")),
        ("RC", _("Reading Comprehension")),
        ("CR", _("Critical reasoning")),
        ("IE", _("Issue essay")),
        ("AE", _("Argument essay")),
    )

    def __str__(self):
        return "Gre_Question_Type"

    class Meta:
        abstract = True

class Gre_Answer_type(models.Model):
    
    ANSWER_CHOICE=(
        ("SOB","Simple one blank"),
        ("STB","Simple two blank"),
        ("STr","Simple three blank"),
        ("NI","Numeric input"),
        ("TI","Text input"),
        ("MC3","Multiple check answer with 3 options"),
        ("MC5","Multiple check answer with 5 options"),
    )

    def __str__(self):
        return "Gre_Answer_type"

    class Meta:
        abstract = True

class Gre_common_type(models.Model):
    DIFF_LEVEL =(
        ("E","Easy"),
        ("M","Medium"),
        ("H","Hard"),
    )

    GRE_TEST_SECTION = (
            ("Ve","Verbal"),
            ("Qu","Quant"),
            ("Ie","Issue Essay"),
            ("Ae","Argument Essay"),
            )