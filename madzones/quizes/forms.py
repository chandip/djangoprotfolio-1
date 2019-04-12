from django import forms

class QuizForm(forms.Form):

    def __init__(self, CHOICES, INITIAL, IS_MULTIPLE_CHOICE,  *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        if IS_MULTIPLE_CHOICE:
            self.fields['choices'] = forms.ChoiceField(widget=forms.CheckboxSelectMultiple,
                                                         choices=CHOICES,
                                                         initial=INITIAL,
                                                         required=True)
        else:
            self.fields['choices'] = forms.ChoiceField(widget=forms.RadioSelect,
                                                         choices=CHOICES,
                                                         initial=INITIAL,
                                                         required = True)