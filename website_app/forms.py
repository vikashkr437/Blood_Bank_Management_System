from django import forms
from bloodbank.models import donor, order, hospital



class newdonorform(forms.ModelForm) :
    class Meta:
        model = donor
        fields = '__all__'



class neworderform(forms.ModelForm) :

    class Meta:
        model = order
        fields = '__all__'




class newhospitalform(forms.ModelForm) :

    class Meta:
        model = hospital
        fields = '__all__'
