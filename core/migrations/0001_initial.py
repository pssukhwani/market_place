# Generated by Django 3.2.4 on 2021-06-26 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Category Name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Custom Users',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('custom_id', models.IntegerField(unique=True, verbose_name='Custom Product Id')),
                ('image_url', models.TextField(default='https://picsum.photos/400?image=780', verbose_name='Image URL')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is In Stock')),
                ('product_price', models.DecimalField(decimal_places=10, default=0.0, max_digits=20, verbose_name='Product Price')),
                ('sell_price', models.DecimalField(decimal_places=10, default=0.0, max_digits=20, verbose_name='Sell Price')),
                ('added_on', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('last_modified_on', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('category', models.ManyToManyField(blank=True, to='core.Category')),
                ('product_viewed', models.ManyToManyField(blank=True, to='core.CustomUser')),
            ],
        ),
    ]
