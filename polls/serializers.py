from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.fields import SerializerMethodField

from polls.models import Bar


class BarSerializer(ModelSerializer):

    bor = SerializerMethodField()

    class Meta:

        model = Bar

        fields = (
            "value",
            "bor",
        )

    def get_bor(self, bar):

        if self.context["bor_value"] is None:

            return "None"

        return "Exist"
