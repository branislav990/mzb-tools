from django import forms
from django.forms import ModelForm
from .models import *


class UploadFileForm(forms.Form):
    csv_file = forms.FileField(label="Select 'full- CSV' file",
                               widget=forms.ClearableFileInput(
                                   attrs={'class': 'filePicker',
                                          'value': 'Select CSV file'}))


class UploadDehliForm(forms.Form):
    dehli_file = forms.FileField(label="Select 'DEHLI' file",
                                 widget=forms.ClearableFileInput(
                                     attrs={'class': 'filePicker',
                                            'value': 'Select "DEHLI" file'}),
                                 required=False)
