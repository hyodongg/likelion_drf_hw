from django.urls import path
from .views import * # views.py에 있는 모든 함수, 클래스를 전부 가져옴
from . import views # views라는 전체 파일을 통째로 가져오고 꺼내올 땐 views. 붙이기
from django.conf import settings
from django.conf.urls.static import static

app_name = "music"

urlpatterns = [
    path('',views.singer_list_create),
    path('singers/<int:singer_id>',views.singer_detail_update_delete),
    path('singers/<int:singer_id>/song',views.song_read_create),
    path('tags/<str:tags_name>',views.find_tag),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)