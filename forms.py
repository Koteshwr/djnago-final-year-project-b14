import os
from django import forms

from myapp.models import Audio_store


# class AudioForm(forms.ModelForm):
#     class Meta:
#         model = Audio_store
#         fields = ['record']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio_store
        fields = ['Audio_file']

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Get the file extension
        _, extension = os.path.splitext(instance.Audio_file.name)

        # Rename the file to "audio.mp3"
        instance.Audio_file.name = 'audio.mp3'

        if commit:
            instance.save()
        return instance


