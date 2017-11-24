from django import forms
from django.forms import widgets, SelectDateWidget, Select


class DateTypeInput(forms.DateInput):
    input_type = 'date'


class PCForm(forms.Form):
    PC_Num = forms.IntegerField()
    Floor_Num = forms.IntegerField()


class ReservationForm(forms.Form):
    date = forms.DateField(widget=DateTypeInput())
    time = forms.TimeField()

    def __init__(self, *args, **kwargs):
        self.choice = kwargs.pop('choice')
        self.choice2 = kwargs.pop('choice2')
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['floor'] = forms.ChoiceField(choices=self.choice)
        self.fields['pc'] = forms.ChoiceField(choices=self.choice2)
