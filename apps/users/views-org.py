from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    SignUpSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    TokenObtainSerializer,
)

User = get_user_model()


class UserViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    http_method_names = ("post", "put", "patch")
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "create":
            return SignUpSerializer
        elif self.action == "change_password":
            return ChangePasswordSerializer
        return UserSerializer

    def change_password(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response()


class TokenObtainView(GenericAPIView):
    serializer_class = TokenObtainSerializer
    http_method_names = ("post",)
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_set = Token.objects.filter(user=user)
        if token_set.exists():
            token_set.delete()
        token = Token.objects.create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)
