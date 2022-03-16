from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CarModel(models.Model):
    make = models.CharField(_('Make'), max_length=50, null=False, help_text=_(
        'Car manufacturer'), db_index=True)
    model = models.CharField(_('Model'), max_length=50, null=False, help_text=_(
        'Car model'), db_index=True)

    class Meta:
        ordering = ['make', 'model']
        verbose_name = _('Car Model')
        verbose_name_plural = _('Car Models')

    def __str__(self) -> str:
        return f'{self.make} {self.model}'


class CarInstance(models.Model):
    registration = models.CharField(
        _('Registration'), max_length=6, null=False, db_index=True)
    vin = models.CharField(_('VIN'), max_length=17, null=False, db_index=True)
    model = models.ForeignKey(
        CarModel,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Car Model"),
        related_name='car_instances',
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Car Instance')
        verbose_name_plural = _('Car Instances')

    def __str__(self) -> str:
        return f'{self.model} {self.registration}'


class Order(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    car_instance = models.ForeignKey(
        CarInstance,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Car Instance"),
        related_name='orders',
    )
    sum = models.DecimalField(_('Sum'), null=False,
                              max_digits=10, decimal_places=2)
    
    ORDER_STATUS = (
        (0, _("New")),
        (10, _("Working")),
        (20, _("Finished repairs")),
        (30, _("Closed (paid)")),
        (50, _("Removed")),
    )

    status = models.PositiveIntegerField(
        _('Status'), default=0, choices=ORDER_STATUS)


    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self) -> str:
        return f'{self.car_instance}: {self.created_at} - {self.sum}'


class Service(models.Model):
    name = models.CharField(_('Name'), max_length=50, null=False, db_index=True)
    price = models.DecimalField(
        _('Price'), null=False, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self) -> str:
        return f'{self.name}: {self.price}'


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Order"),
        related_name='order_lines',
    )
    service = models.ForeignKey(
        Service,
        null=False,
        on_delete=models.CASCADE,
        verbose_name=_("Service"),
        related_name='order_lines',
    )
    quantity = models.PositiveIntegerField(_('Quantity'), null=False)
    price = models.DecimalField(
        _('Price'), null=False, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('Order Line')
        verbose_name_plural = _('Orders Lines')

    def __str__(self) -> str:
        return f'{self.service.name}: {self.price}'
