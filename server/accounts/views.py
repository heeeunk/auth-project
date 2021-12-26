from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
import jwt
from datetime import datetime
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
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
def getUser(request, username):    
    person = get_user_model().objects.get(username=username)
    users = get_user_model().objects.all()
    context ={
        'username': person.username,
        'email': person.email,
        'is_admin': person.is_admin,
        'users': list(users.values())
        # 'email_hash':email_hash,
    }
    return JsonResponse(context)


@api_view(['POST'])
def changeAdmin(request, username):
    user = get_user_model().objects.get(username=username)
    if user.is_admin:
        user.is_admin = 0
        user.save()
    else:
        user.is_admin = 1
        user.save()
    context = {
        'response' : 'success',
        'status' : user.is_admin,
    }
    return JsonResponse(context)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = get_user_model().objects.get(username=username)
    # 암호화된 비밀번호와 입력된 비밀번호가 같은지 확인해주고 같다면 성공메시지와 함께 토큰발급
    if check_password(password, user.password):
        context = {
            'response': 'success',
            'message': 'sucess login',
            'user': user,
            'token': jwt_create(username)
        }
    # 정보가 틀리다면 통신은 성공했으니 에러는 띄우지 않지만 실패메시지를 보낸다.
    else:
        context = {
            'response': 'fail',
            'message': "password doesn't match",
        }
    return JsonResponse(EmployeeEncoder().encode(context), safe=False)


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