from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get("title", instance.title)
        instance.description = validate_data.get(
            "description", instance.description)
        instance.duration = validate_data.get("duration", instance.duration)

        instance.save()
        return instance
