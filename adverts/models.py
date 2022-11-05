from extensions.dateJalali import django_jalali
from django.utils import timezone
from users.models import User
from django.db import models


class Advert(models.Model):
    INSURANCE = (
        ('a', 'دارد'),
        ('b', 'ندارد')
    )
    GEARBOX = (
        ('a', 'اتوماتیک'),
        ('b', 'دنده ای'),
    )
    USE = (
        ('a', 'همه'),
        ('b', 'کارکرده'),
        ('c', 'صقر کیلومتر')
    )
    BRAND = (
        ('a', 'آذرخش'),
        ('b', 'بنلی'),
        ('c', 'آپاچی'),
        ('d', 'پولسار'),
        ('e', 'سوزوکی'),
        ('f', 'هوندا'),
    )
    YEARS = (
        ('1370', '۱۳۷۰'),
        ('1371', '۱۳۷۱'),
        ('1372', '۱۳۷۲'),
        ('1373', '۱۳۷۳'),
        ('1374', '۱۳۷۴'),
        ('1375', '۱۳۷۵'),
        ('1376', '۱۳۷۶'),
        ('1377', '۱۳۷۷'),
        ('1378', '۱۳۷۸'),
        ('1379', '۱۳۷۹'),
        ('1380', '۱۳۸۰'),
        ('1381', '۱۳۸۱'),
        ('1382', '۱۳۸۲'),
        ('1383', '۱۳۸۳'),
        ('1384', '۱۳۸۴'),
        ('1385', '۱۳۸۵'),
        ('1386', '۱۳۸۶'),
        ('1387', '۱۳۸۷'),
        ('1388', '۱۳۸۸'),
        ('1389', '۱۳۸۹'),
        ('1390', '۱۳۹۰'),
        ('1391', '۱۳۹۱'),
        ('1392', '۱۳۹۲'),
        ('1393', '۱۳۹۳'),
        ('1394', '۱۳۹۴'),
        ('1395', '۱۳۹۵'),
        ('1396', '۱۳۹۶'),
        ('1397', '۱۳۹۷'),
        ('1398', '۱۳۹۸'),
        ('1399', '۱۳۹۹'),
        ('1400', '۱۴۰۰'),
        ('1401', '۱۴۰۱'),
    )
    COLORS = (
        ('a', 'نقره ای'),
        ('b', 'زرشکی'),
        ('c', 'مارون'),
        ('d', 'نوک مدادی'),
        ('e', 'نارنجی'),
        ('f', 'بژ'),
        ('g', 'مشکی'),
        ('h', 'سفید'),
        ('i', 'قهوه ای'),
        ('j', 'قرمز'),
        ('k', 'آبی'),
    )
    FUELS = (
        ('a', 'بنزینی'),
        ('b', 'گازی'),
        ('c', 'گازویل'),
    )
    brand = models.CharField(choices=BRAND, max_length=55, verbose_name="برند")
    description = models.TextField(verbose_name='درباره')
    image = models.ImageField(null=True, verbose_name='تصویر', upload_to='advert photo')
    use = models.CharField(choices=USE, max_length=10, verbose_name='مصرف')
    function = models.IntegerField(verbose_name='استفاده', default=0)
    volume = models.IntegerField(verbose_name='حجم')
    insurance = models.CharField(choices=INSURANCE, max_length=10, verbose_name='بیمه')
    gearbox = models.CharField(choices=GEARBOX, max_length=10, verbose_name='گیربکس')
    year = models.CharField(choices=YEARS, max_length=5, verbose_name='سال تولید')
    phoneNumber = models.CharField(max_length=11, verbose_name='شماره تلفن', default='0')
    color = models.CharField(choices=COLORS, max_length=10, verbose_name='رنگ')
    fuel = models.CharField(choices=FUELS, max_length=10, verbose_name='مصرف')
    status = models.BooleanField(verbose_name='وضعیت', default=False)
    created = models.DateTimeField(default=timezone.now, verbose_name='زمان ایجاد')

    class Meta:
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی ها'

    def __str__(self):
        return f'{self.BRAND}({self.volume})'

    def created_jdate(self):
        return django_jalali(self.created_date)