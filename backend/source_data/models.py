import uuid
from django.db import models

class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)

    class Meta:
        abstract = True


class SourceFormTemplate(BaseModel):

    class SourceType(models.TextChoices):
        SALESFORCE = 'SALESFORCE'
        GOOGLE_SHEETS = 'GOOGLE_SHEETS'
        FRESHDESK = 'FRESHDESK'
        SHOPIFY = 'SHOPIFY'

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # it is assumed that, there'll only be one template for a source type
    type = models.CharField(max_length=100, choices=SourceType.choices, unique=True)

    fields = models.JSONField()

class Source(BaseModel):

    source_form_template = models.ForeignKey(SourceFormTemplate, on_delete=models.PROTECT)
    source_form_data = models.JSONField()

    # to store different creds for a data source, by different companies/users
    # ideally, this should be a foreign key to company or user model
    company_id = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company_id', 'source_form_template'], name='unique_source_form_for_company'),
        ]
