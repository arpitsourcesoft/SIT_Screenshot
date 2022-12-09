from rest_framework import serializers


class ScreenShotSerializer(serializers.Serializer):
	file = serializers.FileField(required=False)
	# name = serializers.CharField(required=False)
