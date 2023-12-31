# Generated by Django 4.1.7 on 2023-10-15 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obrok', '0002_restaurant_available_funds'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obrok.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_type', models.CharField(choices=[('donation', 'Donation'), ('restaurant', 'Restaurant')], max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obrok.donation')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obrok.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
