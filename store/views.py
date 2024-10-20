from rest_framework.response import Response
from rest_framework import viewsets, serializers

from .models import Bolg
from .serializer import BlogSerializer


class BlogCrud(viewsets.ModelViewSet):

    queryset = Bolg.objects.all()
    permission_classes = []

    class EditSerializer(serializers.Serializer):
        title = serializers.CharField(required=False)
        content = serializers.CharField(required=False)

    serializer_class = EditSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        
        print(f"partial: {partial}")
        print(f"data: {request.data}")

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        print(f"serialized_data: {serializer.validated_data}")

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
