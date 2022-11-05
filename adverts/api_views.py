from rest_framework.response import Response
from .serializers import AdvertSerializer
from rest_framework.permissions import *
from rest_framework.generics import *
from users.models import User
from .models import Advert
from .permissions import *


class CreateAdvert(CreateAPIView):
    """
        Create Advert by users or admins
    """
    serializer_class = AdvertSerializer

    def create(self, request, *args, **kwargs):
        data = AdvertSerializer(data=request.data)
        if data.is_valid():
            data.save()
            data.instance.auther = request.user
            data.instance.phoneNumber = request.user.phoneNumber
            data.save()
            return Response({'message': 'آکهی در انتظار تایید قرار گرفت'})
        else:
            return Response(data.errors)

    permission_classes = [IsAuthenticated]


class AdvertList(ListAPIView):
    """
        Show adverts list to admins
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class ConfirmAdvert(RetrieveUpdateAPIView):
    """
        Confirm advert by admins
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.filter(status=False).all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser]


class ConfirmedAdvertsList(ListAPIView):
    """
        Show confirmed adverts to users
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.filter(status=True).all()
    permission_classes = [IsAuthenticated]


class WaitingAdvertsList(ListAPIView):
    """
        Show Waiting adverts list to admin for confirm
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.filter(status=False).all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class AdvertViewOrDestroy(RetrieveDestroyAPIView):
    """
        View and manage advert by auther or admins
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.filter(status=True).all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, AutherALLStaffOrReadOnly]


class AdvertUpdate(RetrieveUpdateAPIView):
    """
        Update advert by auther or admins
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.filter(status=True).all()
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, AutherALLStaffOrReadOnly]


class ConfirmedAdvertsAutherList(ListAPIView):
    """
        Show confirmed adverts list to auther
    """
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Advert.objects.filter(auther=user, status=True).all()


class WaitingAdvertsAutherList(ListAPIView):
    """
        Show waiting adverts list to auther
    """
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Advert.objects.filter(auther=user, status=False).all()
