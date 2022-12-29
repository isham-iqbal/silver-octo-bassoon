
from rest_framework.serializers import Serializer, ModelSerializer

from polls.models import Bar

class BarSerializer(ModelSerializer):
    class Meta:

        model = Bar

        fields = (
            "value",
        )