from rest_framework.permissions import *
from rest_framework.generics import *
from .permissions import *
from .serializers import *
from .models import User


class CreateUserByAdmin(CreateAPIView):
    """
        create user by admins
    """
    staticmethod = 'POST'
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CreateUserByUsers(CreateAPIView):
    """
        create user by users
    """
    staticmethod = 'POST'
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ListUser(ListAPIView):
    """
        List of users for admins
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class DetailUser(RetrieveAPIView):
    """
        View user by phone number to admins or user
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'phoneNumber'
    permission_classes = [IsAuthenticated, IsUserORALLStaff]


class DeleteUser(RetrieveDestroyAPIView):
    """
        View and Delete user by phone number to admins or user
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'phoneNumber'
    permission_classes = [IsAuthenticated, IsUserORALLStaff]


class UpdateUser(RetrieveUpdateAPIView):
    """
        View and update user by phone number to admins or user
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'phoneNumber'
    permission_classes = [IsAuthenticated, IsUserORALLStaff]
