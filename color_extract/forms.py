from django import forms
from django.core.exceptions import ValidationError

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']

class UploadStripForm(forms.Form):
    file = forms.FileField()


# checks if uploaded files are relevant
    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension not in ALLOWED_EXTENSIONS:
            raise ValidationError("Only JPG and PNG files are allowed.")

        return uploaded_file