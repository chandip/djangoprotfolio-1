from django import forms

class QuizForm(forms.Form):

    def __init__(self, CHOICES, INITIAL, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.fields['choices'] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial=INITIAL, required = True)