from rest_framework import serializers


class ImportDataSerializer(serializers.Serializer):
    """
    Serializer for the import data
    """
    file = serializers.FileField()