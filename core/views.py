from django.contrib.auth.models import User
from rest_framework import serializers, permissions, generics
from .models import MyMessage
from rest_framework.mixins import CreateModelMixin
from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MyMessageSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = MyMessage
        fields = ['id', 'message', 'created_at', 'updated_at', 'created_by']

    def get_created_by(self, msg: MyMessage):
        user = self.context['request'].user
        user_data = dict(UserSerializer(user).data)
        return user_data

    def create(self, validated_data):
        created_by = self.context['request'].user
        validated_data["created_by"] = created_by
        message = MyMessage.objects.create(**validated_data)
        return message


class CreateMessageView(generics.GenericAPIView, CreateModelMixin):

    queryset = MyMessage.objects.all()
    serializer_class = MyMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def throttled(self, request, wait):
    	raise Throttled(detail={
		'message': 'request limit exceeded',
		'availableIn': f"This will be available {wait} seconds",
		})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
