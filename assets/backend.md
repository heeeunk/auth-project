###

### 2. 로그인 기능

#### [백엔드]

[내장 기능으로 구현법]

🌷 Django 에는 obtain_jwt_token 이라는 jwt를 자동 생성해서 보내주는 기능이 있다.

```python
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

path('api-token-auth/', obtain_jwt_token),

```



[직접 구현]

🌻 내장 기능 구현 대신 직접 jwt 를 생성하고 원하는 정보를 보내줄 수 있도록 만들어보았다.

> urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
]

```



> views.py

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

**[질문사항]**

- 비밀번호입력값과 비밀번호확인입력값이 같음을 확인하는 경우 프론트와 백 둘다 처리해주는 것이 맞는지, 프론트에서만 처리해주는 것이 맞는지?

  [프론트에서 처리]

  ```javascript
  // 비밀번호입력값 == 비밀번호확인값
        if (this.credentials.password == this.credentials.passwordConfirmation){
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/signup/',
            data: this.credentials,
          })
            .then(res => {
              console.log(res)
              // this.$router.push({ name: 'Login' })
            })
            .catch(err => {
              console.log(err)
            })
        }else{
          alert('입력하신 비밀번호와 비밀번호 확인값이 다릅니다.')
        }// 비밀번호입력값 == 비밀번호확인값
        if (this.credentials.password == this.credentials.passwordConfirmation){
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/signup/',
            data: this.credentials,
          })
            .then(res => {
              console.log(res)
              // this.$router.push({ name: 'Login' })
            })
            .catch(err => {
              console.log(err)
            })
        }else{
          alert('입력하신 비밀번호와 비밀번호 확인값이 다릅니다.')
        }
  ```

  [백엔드에서 처리]

  ```python
  #1-1. Client에서 온 데이터를 받아서
  password = request.data.get('password')
  password_confirmation = request.data.get('passwordConfirmation')

  #1-2. 패스워드 일치 여부 체크
  if password != password_confirmation:
      return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
  		
  ```



> models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```



> serializers.py

```python
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # write_only : 시리얼라이징은 하지만 응답에는 포함시키지 않음
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
```



https://wisdom-990629.tistory.com/44

https://wikidocs.net/10308

https://hckcksrl.medium.com/django-%EC%BB%A4%EC%8A%A4%ED%85%80-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8-custom-user-model-b8487c0d150



list error

https://spoonhasi.tistory.com/2

[참고] https://github.com/SSAFY-5th-seungwoon/Moya_backend