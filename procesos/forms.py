from django import forms



class ProcesoForm(forms.Form):
    juzgado = forms.CharField(
        label="Juzgado",
        required=False,
        widget=forms.TextInput(
            attrs={
                "calss": "proceso-juzgado",
                "placeholder": "juzgado de origen",
                "required": "True",
                }
            ),
    )
    radicado = forms.IntegerField(
        label="Radicado",
        required=False,
        widget=forms.TextInput(
            attrs={
                
                "calss": "proceso-radicado",
                "placeholder": "numero de radicado",
                "required": "True",
            }
        ),
    )