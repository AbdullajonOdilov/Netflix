from rest_framework.exceptions import ValidationError
from .models import *
from rest_framework.serializers import ModelSerializer, Serializer

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
    def validate_jins(self,qiymat):
        if qiymat.lower() != 'erkak' and qiymat.lower() != 'ayol':
            raise ValidationError("Jins kiritishda xatolik bor")
        return qiymat
    # def create(self, validated_data):
    #     Actor.objects.create(
    #
    #         ism = validated_data['ism'],
    #         jins = validated_data['jins'],
    #         davlat = validated_data['davlat'],
    #
    #         t_yil =validated_data['t_yil']
    #     )

class KinoSerializer(ModelSerializer):
    # actors =ActorSerializer(many=True)
    class Meta:
        model = Kino
        fields = "__all__"


    def create(self, validated_data):
        Kino.objects.create(
            nom = validated_data['nom'],
            reyting = validated_data['reyting'],
            janr = validated_data['janr'],
            yil = validated_data['yil']
        )
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"