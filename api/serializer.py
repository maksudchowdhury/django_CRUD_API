from rest_framework.serializers import ModelSerializer
from inPage.models import notes

class noteSeralizer(ModelSerializer):
    class Meta:
        model=notes
        fields=['serial','title','desc']