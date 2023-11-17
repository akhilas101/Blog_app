from rest_framework import serializers
from login.models import RegisterationModel

class RegisterSerailizer(serializers.ModelSerializer):
    class Meta:
        model=RegisterationModel
        fields=(
             'name',
             'password',
             'email',
             'image',
             
    
        )