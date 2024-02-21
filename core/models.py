import uuid
from django.db import models
from django.utils import timezone


class CommonFieldsMixin(models.Model):
    """
    Mixin for common fields that are used in many models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Updates the "deleted_at field when the is_deleted field is toggled."""

        if self.is_deleted and not self.deleted_at:
            self.deleted_at = timezone.now()
        elif not self.is_deleted and self.deleted_at:
            self.deleted_at = None
        super().save(*args, **kwargs)


class UUIDBaseModel(CommonFieldsMixin):
    """
        Base model that other models inherit from.
        Each new record will have a unique UUID generated automatically as its primary key.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AutoIncrementBaseModel(CommonFieldsMixin):
    """
        Base model that other models inherit from.
    """

    class Meta:
        abstract = True


class UUIDTestModel(UUIDBaseModel):
    """A concrete model for testing the UUIDBaseModel."""
    pass


class AutoIncrementTestModel(AutoIncrementBaseModel):
    """A concrete model for testing the AutoIncrementBaseModel."""
    pass
