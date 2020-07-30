from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Category, Genre, Title, Review, Comment, User


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['name', 'slug']


class TitlePostSerializer(serializers.ModelSerializer):
	genre = serializers.SlugRelatedField(
		slug_field='slug',
		many=True,
		queryset=Genre.objects.all())
	category = serializers.SlugRelatedField(
		slug_field='slug',
		queryset=Category.objects.all())

	class Meta:
		model = Title
		fields = ['id', 'name', 'year', 'description', 'genre', 'category',]


class TitleListSerializer(serializers.ModelSerializer):
	genre = GenreSerializer(many=True)
	category = CategorySerializer()
	rating = serializers.IntegerField()

	class Meta:
		model = Title
		fields = ['id', 'name', 'year', 'rating', 'description', 'genre', 'category']


class ReviewSerializer(serializers.ModelSerializer):
	#title = serializers.HiddenField(read_only=True)
	author = serializers.SlugRelatedField(
		slug_field='username',
		read_only=True
	)

	# def validate(self, attrs):
	# 	return attrs

	class Meta:
		model = Review
		fields = ('id', 'author', 'text', 'score', 'pub_date')
		# validators = [
		# 	UniqueTogetherValidator(
		# 		queryset=Review.objects.all(),
		# 		fields=['title', 'author'],
		# 		message='Такой отзыв уже создан!'
		# 	)
		# ]


class CommentSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(
		slug_field='username',
		read_only=True
	)

	class Meta:
		model = Comment
		fields = ('id', 'author', 'text', 'pub_date')
