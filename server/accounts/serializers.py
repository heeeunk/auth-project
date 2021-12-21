from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            phone = validated_data['phone'],
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['phone', 'email', 'username', 'password']

class UserListSerializer(serializers.ModelSerializer):
    # write_only는 시리얼라이징은 하지만 응답에는 포함시키지 않는다는 의미
    # 비밀번호를 응답에 표현한다면 보안상의 유출이 되는 것이기 떄문
    # password = serializers.CharField(write_only=True)

    class Meta : 
        model = User
        fields = '__all__'