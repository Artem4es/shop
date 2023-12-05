# Generated by Django 3.2.16 on 2023-02-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0002_remove_order_order_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(
                auto_now_add=True, default=None, verbose_name="Дата заявки"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="comment",
            field=models.TextField(verbose_name="Комментарий"),
        ),
    ]
