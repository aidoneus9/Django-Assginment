from django.contrib import admin
from django.urls import path
from django.http import Http404
from django.shortcuts import render
from fake_db import user_db

_db = user_db # {키(숫자):값(딕셔너리)}
# users/ 유저 리스트를 확인할 수 있는 페이지
# users/<int:user_id>/ 유저의 상세 정보를 볼 수 있는 페이지

def user_list(request): # 유저의 이름을 템플릿에 전달하고 user_list.html 렌더링
    # _db에서 이름만 추출하여 리스트에 넣기 -> context에 넘겨줌
    user_data = [(user_id, user['이름']) for user_id, user in _db.items()]

    return render(request, 'user_list.html', {'user_data': user_data})

def user_info(request, user_id): # 유저의 정보를 템플릿에 전달하고 user_info.html을 렌더링
    user_data =  _db.get(user_id) # 딕셔너리 반환
    if user_data is None:
        raise Http404("User not found")
    '''
    {
        '이름': '머용',
        '나이': 27,
        '생년월일': '1998-08-29',
        '취미': '배드민턴',
        '거주지': '서울특별시 강서구',
        '개발경력': '2년 2개월'
    }
    '''
    name = user_data['이름']
    info_data = {k: v for k, v in user_data.items() if k != '이름'}

    return render(request, 'user_info.html', {'name':name, 'info_data': info_data})

urlpatterns = [
    # url과 view 연결
    # path('url', 함수)
    path('users/', user_list),
    path('users/<int:user_id>/', user_info, name='user_info'),
    path('admin/', admin.site.urls),
]
