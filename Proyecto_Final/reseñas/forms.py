from ckeditor.widgets import CKEditorWidget
from django import forms

from reseñas.models import Reseña


class ReseñaForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del juego",
        required=True,
        widget=forms.TextInput(
            attrs={
                "juego": "reseña-name",
                "placeholder": "Nombre del juego",
                "required": "True",
            }
        ),
    )

    autor_reseña = forms.CharField(
        label="Autor de la reseña:",
        required=True,
        widget=CKEditorWidget(
            attrs={
                "class": "reseña-autor",
                "placeholder": "Autor de la reseña",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=True,
        widget=CKEditorWidget(
            attrs={
                "class": "reseña-description",
                "placeholder": "Reseña del juego",
                "required": "True",
            }
        ),
    )    
