from django import forms
from emoji_picker.widgets import EmojiPickerTextareaAdmin, EmojiPickerTextInputAdmin
from main.models import QuestionAnswer, SurveyQuestion, BotText


class SurveyQuestionForm(forms.ModelForm):
    text = forms.CharField(widget=EmojiPickerTextareaAdmin)

    class Meta:
        model = SurveyQuestion
        exclude = ['my_order']


class QuestionAnswerForm(forms.ModelForm):
    text = forms.CharField(widget=EmojiPickerTextInputAdmin)

    class Meta:
        model = QuestionAnswer
        exclude = ['my_order']


class BotTextForm(forms.ModelForm):
    text = forms.CharField(widget=EmojiPickerTextInputAdmin)

    class Meta:
        model = QuestionAnswer
        exclude = ['my_order']

