from django import forms

class PCForm(forms.Form):
	PC_Num = forms.IntegerField()
	Floor_Num = forms.IntegerField()