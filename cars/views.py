
from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


