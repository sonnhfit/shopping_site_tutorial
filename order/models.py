from django.db import models
from user.models import CustomerUser
from cart.models import Cart
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name='Khách hàng')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Giỏ hàng')
    shipping_address = models.CharField(max_length=255, default='', verbose_name='Địa chỉ giao hàng')
    order_description = models.TextField(default='', verbose_name='Mô tả đơn hàng')
    is_completed = models.BooleanField(default=False, verbose_name='Trạng thái đơn hàng')
    def __str__(self):
        return 'Đơn hàng số %s'%self.id

    class Meta:
        verbose_name_plural = "Quản lý đặt hàng"
