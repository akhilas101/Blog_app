from rest_framework import serializers
from blog.models import PostModel

class PostSerailizer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields=(
             'userid',
             'title',
             'message',
             
             
    
        )