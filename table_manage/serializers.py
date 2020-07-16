from rest_framework import serializers
from  table_manage.models import Deviation

class DeviationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deviation
        fields = '__all__'