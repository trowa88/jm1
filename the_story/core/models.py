from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    """
    'created'와 'modified' 필드를 자동으로 업데이트해 주는
    추상화 기반 클래스 모델
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
