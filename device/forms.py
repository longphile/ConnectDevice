from django import forms

TYPE_CHOICES = (
    ("Air Condition", ("Air Condition")),
    ("Pump", ("Pump"))
)
class DeviceForm(forms.Form):
    type = forms.ChoiceField(choices = TYPE_CHOICES,  required=True)
    name = forms.CharField()

STATE_CHOICES = (
    ("On", ("On")),
    ("Off", ("Off"))
)
MODE_CHOICES = (
    ("Manual", ("Manual")),
    ("Auto", ("Auto"))
)

class DevideInfoForm(forms.Form):
    mode = forms.ChoiceField(choices = MODE_CHOICES,  required=True)
    state = forms.ChoiceField(choices = STATE_CHOICES, required=True)
        