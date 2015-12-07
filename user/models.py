# coding=utf-8
from django.contrib.auth.models import Group, User

__author__ = 'mehmet'

from django.db import models


"""
Categories tablosu katagori bilgilerini içerir.
    title = Sayfa başlığı
    content = html içerik
    for_company = SAdece bayiiyler görsün
    seo = Seo için seçenekler
    cdate = Satırın oluşturulma tarihi.
"""


class Pages(models.Model):
    title = models.CharField(max_length=70, default='', null=True)
    content = models.TextField(max_length=None, blank=False)
    for_companies = models.BooleanField(null=False, blank=False, default=False)
    seo_title = models.CharField(max_length=100, default='', null=True, blank=True)
    seo_meta_keyword = models.CharField(max_length=1000, default='', null=True, blank=True)
    seo_meta_description = models.CharField(max_length=1000, default='', null=True, blank=True)
    cdate = models.DateTimeField(auto_now_add=True)


"""
Return_Product tablosu geri iade ve değişim bildirimlerini içerir.
    title = Sayfa başlığı
    content = html içerik
    type = geri iade yada ürün değişim isteği
    product_name = ürün adı
    order_code = sipariş kodu
    cargo_no = kargo numarası
    cdate = Satırın oluşturulma tarihi.
"""


class ReturnProduct(models.Model):
    TYPE = (
        (u'0', u'Geri İade'),
        (u'1', u'Ürün Değişim'),
    )
    STATUS_TYPE = (
        (u'0', u'Kargo No Bekleniyor'),
        (u'1', u'Onay Bekleniyor'),
        (u'2', u'Ek Sürede'),
        (u'3', u'Kullanıcı Teslimatında'),
        (u'4', u'Red Edildi'),
    )
    user = models.ForeignKey(User)
    title = models.CharField(max_length=70, default='', null=True)
    content = models.TextField(max_length=None, blank=False)
    type = models.CharField(max_length=1, choices=TYPE, default='0')
    status_type = models.CharField(max_length=1, choices=STATUS_TYPE, default='0')
    product_name = models.CharField(max_length=100, default='', null=True, blank=True)
    order_code = models.CharField(max_length=100, default='', null=True, blank=True)
    cargo_no = models.CharField(max_length=70, default='', null=True, blank=True)
    cargo_add_date = models.DateTimeField(auto_now_add=True)
    add_extra_time = models.DateTimeField(auto_now_add=True)
    cdate = models.DateTimeField(auto_now_add=True)
