from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'cpu', 'ram', 'disk', 'created']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.cpu = validated_data.get('cpu', instance.cpu)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.disk = validated_data.get('disk', instance.disk)
        instance.save()
        return instance
