from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
import jwt
from datetime import datetime
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.core.cache import cache
from django.contrib.auth import get_user, get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http.response import JsonResponse
from json import JSONEncoder


@api_view(['POST'])
def signup(request):
	# clietn 요청에서 data를 맏아 담아준다.
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	# 비밀번호와 비밀번호 확인이 동일한지 체크 : 동일하지 않다면 400에러가 메세지와 함께 보내진다. (이미 client에서도 막음)
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
	
	# UserSerializer로 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['get'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def getUser(request, username):    
    person = get_object_or_404(get_user_model(), username=username)
    users = get_user_model().objects.all()
    context ={
        'username': person.username,
        'email': person.email,
        'is_admin': person.is_admin,
        'users': list(users.values())
        # 'email_hash':email_hash,
    }
    return JsonResponse(context)

# @api_view(['get'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def userlist(request):    
#     user = get_user_model()
#     users = User.objects.all()
#         # Set your variables here
#     # email = person.email
#     # email_hash = hashlib.md5(request.user.email.encode('utf-8').strip().lower()).hexdigest() #gravatar hash 
#     context ={
#         'users': list(users.values())
#         # 'email_hash':email_hash,
#     }
#     return JsonResponse(context)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = get_object_or_404(get_user_model(), username=username)
    # user = get_user_model().object.get(username=username)
    context = {
        'response': 'success',
        'message': 'sucess login',
        'user': user,
        'token': jwt_create(username)
    }
    return JsonResponse(EmployeeEncoder().encode(context), safe=False)

    # if check_password(password, user.password):
    #     jwt_token = jwt_create(username)
    #     cache.set('jwttoken', jwt_token)
    #     response = Response({
    #         'response': 'success',
    #         'message': 'sucess login',
    #         'user': user
    #     })
    #     response.set_cookie('jwttoken', jwt_token)
    #     return response
    # else:
    #     return Response({
    #         'response': 'error',
    #         'message': 'password is wrong'
    #     })


def jwt_create(username):
    now = datetime.now()
    key = settings.SECRET_KEY
    now_time = str(now.year)+str(now.month)+str(now.day) + \
        str(now.hour)+str(now.minute)+str(now.second)
    payload = {
        "username": username,
        "now_time": now_time
    }
    jwt_token = jwt.encode(payload, key, algorithm='HS256').decode('utf-8')
    return jwt_token

# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__