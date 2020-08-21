# Generated by Django 2.2.13 on 2020-08-12 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20200723_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=250)),
                ('nationality', models.CharField(max_length=64)),
                ('no_of_serving', models.PositiveSmallIntegerField()),
                ('picture', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('glutten_free', models.BooleanField(default=False)),
                ('customizable', models.BooleanField(default=False)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('avg_rating', models.FloatField(default=0)),
                ('category', models.CharField(default='Fast food', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.PositiveSmallIntegerField()),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seller.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('calorie_count', models.FloatField()),
                ('price', models.FloatField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishingredient', to='seller.Dish')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Restaurant'),
        ),
        migrations.AddField(
            model_name='dish',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cooks', to='seller.Seller'),
        ),
    ]
