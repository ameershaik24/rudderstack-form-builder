from source_data.models import SourceFormTemplate, Source
from rest_framework import serializers, exceptions


class SourceFormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceFormTemplate
        fields = "__all__"


class SourceSerializer(serializers.ModelSerializer):
    source_form_fields = serializers.SerializerMethodField()

    class Meta:
        model = Source
        fields = "__all__"

    def get_source_form_fields(self, obj):
        return obj.source_form_template.fields

    def create(self, validated_data):
        source_form_template_fields = validated_data["source_form_template"].fields

        for field_name, field_details in source_form_template_fields.items():
            if (not field_details["required"]) and (validated_data.get(field_name) is None):
                # nothing to validate, if a non required field is not provided
                continue

            if (field_details["required"]) and (validated_data.get(field_name) is None):
                raise exceptions.ValidationError({
                    "error_msg": f"The required field '{field_name}' is not provided."
                })

            # at this point, the field is present in the data
            # it could be a required field, or a not required field
            field_value = validated_data.get(field_name)

            # checks for input type
            if field_details["type"] == "input":
                if not isinstance(field_value, str):
                    raise exceptions.ValidationError({
                        "error_msg": f"The value for field '{field_name}' should be a string."
                    })

                # TODO - add regex validation

            # check for checkbox type
            if field_details["type"] == "checkbox":
                pass

            # check for singleSelect
            if field_details["type"] == "singleSelect":
                pass

        return super().create(validated_data)

