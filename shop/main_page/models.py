from django.db import models

class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30, help_text='Имя')
    bike = models.CharField(verbose_name='Мотик', max_length=30, help_text='Мотоцикл')
    phone = models.CharField(verbose_name='Телефон', max_length=30, help_text='Телефон')
    comment = models.TextField(verbose_name='Комментарий', help_text='Расскажите что Вы ожидаете от прошивки', blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-order_date',)
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'  
        constraints = [
            models.UniqueConstraint(fields=['name', 'bike', 'phone'], name='unique_order'),    
        ]