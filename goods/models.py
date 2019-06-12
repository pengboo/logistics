from django.db import models

# Create your models here.
class TypeInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='类型名称')
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class GoodsInfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='物品名称')
    pic = models.ImageField(upload_to='goods', verbose_name='物品图片', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格', blank=True)
    isDelete = models.BooleanField(default=False)
    unit = models.CharField(max_length=20, verbose_name='单位', blank=True)
    click = models.IntegerField(verbose_name='点击量', blank=True)
    desc = models.CharField(max_length=200, verbose_name='型号', blank=True)
    invertory = models.IntegerField(verbose_name='库存', blank=True)
    content = models.CharField(max_length=500, verbose_name='物品详情', blank=True)
    supplier = models.CharField(max_length=200,verbose_name='供应商', blank=True)
    type = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name='物品类型')
    last_date_added = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    def __str__(self):
        return self.title