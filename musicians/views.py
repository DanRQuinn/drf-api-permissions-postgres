from rest_framework import generics
from .serializer import MusicianSerializer
from .models import Musician
from .permissions import IsOwnerOrReadOnly

class MusicianList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

class MusicianDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
