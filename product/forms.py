from django import forms


class QtyForm(forms.Form):
    qty = forms.IntegerField(max_value=10, min_value=1)
