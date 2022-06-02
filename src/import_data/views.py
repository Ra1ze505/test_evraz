from rest_framework import generics

from .serializers import ImportDataSerializer
from .service import ImportService


class ImportView(generics.CreateAPIView):
    """
    Import data from a file.
    """
    serializer_class = ImportDataSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        ImportService(serializer.validated_data.get('file')).import_data()