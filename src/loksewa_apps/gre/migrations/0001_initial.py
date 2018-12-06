# Generated by Django 2.1.3 on 2018-12-02 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantativeDataAnalysisQuestion',
            fields=[
                ('quant_data_analysis_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Quant_Data_Analysis_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.quant_data_analysis_question',),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithMultipleSelectionFiveInput',
            fields=[
                ('answer_multiple_selection_with_five_option_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_Multiple_selection_With_Five_Option')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_multiple_selection_with_five_option'),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithMultipleSelectionThreeInput',
            fields=[
                ('answer_multiple_selection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_Multiple_selection')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_multiple_selection'),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithNumericInput',
            fields=[
                ('answer_with_numeric_input_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_With_Numeric_Input')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_with_numeric_input'),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithOneBlank',
            fields=[
                ('answer_one_blank_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_One_Blank')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_one_blank'),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithTextInput',
            fields=[
                ('answer_with_text_input_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_With_Text_Input')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_with_text_input'),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithThreeBlank',
            fields=[
                ('answer_three_blank_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_Three_Blank')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_three_blank'),
        ),
        migrations.CreateModel(
            name='SimpleQuestionWithTwoBlank',
            fields=[
                ('answer_two_blank_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.Answer_Two_Blank')),
                ('simple_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Simple_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.simple_question', 'core.answer_two_blank'),
        ),
        migrations.CreateModel(
            name='VerbalOneParagraphManyQuestion',
            fields=[
                ('verbal_one_paragraph_many_question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Verbal_One_Paragraph_Many_Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.verbal_one_paragraph_many_question',),
        ),
    ]