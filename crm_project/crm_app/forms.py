from django import (
    forms,
)


class ClientForm(forms.Form):
    """oefiefoenfeowinfeowinfewoinfewonfoewinfoiewnfoiewnfoewnfoewnfoewnfeowinfion
    tgrggrtgrtgtrgoioeiwndoiendoiendoadoqdno
    """
    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    birth_date = forms.CharField(label='Birth Date', max_length=100)
    potential_client_level = forms.CharField(label='Potential Level', max_length=100)
    next_action = forms.CharField(label='Next Action', max_length=100)
    notes = forms.CharField(label='Notes', max_length=100)


