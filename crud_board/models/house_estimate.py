from django.db import models


# Create your models here.
class HouseEstimate(models.Model):
    estimate_company = models.CharField("会社", max_length=255)
    contact_person = models.CharField("担当者名", max_length=255)
    property_address = models.CharField("物件住所", max_length=255)
    estimate = models.DecimalField("見積もり", max_digits=10, decimal_places=2)
    layout_memo = models.TextField("間取りメモ", blank=True)
    sunlight_memo = models.TextField("日当たりメモ", blank=True)
    memo = models.TextField("備考", blank=True)
    created_by = models.CharField("作成者", max_length=255)
    updated_by = models.CharField("更新者", max_length=255)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.company
