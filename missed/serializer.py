from rest_framework import serializers
from .models import Dane


class DaneSerial(serializers.ModelSerializer):
    class Meta:
        model = Dane
        fields = ['slackUsername','backend','age','bio']