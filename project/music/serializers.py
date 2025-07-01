from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self,instance):
        serializer = SongSerializer(instance.songs,many=True)
        return serializer.data

    class Meta:
        model = Singer
        fields = ['id','name','genre','content','debut','created_at','updated_at','songs']

class SongSerializer(serializers.ModelSerializer):
    singer = serializers.CharField(source='singer.name', read_only=True) # singer가 id로 뜨는 게 아닌 가수 이름으로 뜨게하기
    class Meta:
        model = Song
        fields = ['id','title','release','content','singer']
        read_only_fields = ['singer']