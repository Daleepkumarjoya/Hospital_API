from rest_framework import serializers
from .models import HomeModel, ServicesModel, AboutModel, DoctorsModel, BookModel, ReviewModel, ContactModel, \
    commentModel


class HomeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeModel
        fields = "__all__"


class ServicesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServicesModel
        fields = '__all__'


class AboutModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutModel
        fields = '__all__'


class DoctorsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DoctorsModel
        fields = '__all__'


class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'


class ReviewModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'


class commentModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = commentModel
        fields = '__all__'


class ContactModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'
