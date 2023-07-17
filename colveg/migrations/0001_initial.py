# Generated by Django 4.1.3 on 2023-03-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clasific', models.CharField(choices=[('Papa', 'Papa'), ('Aguacate', 'Aguacate')], max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('descrip', models.CharField(max_length=30)),
                ('peso', models.IntegerField()),
                ('unidad_peso', models.CharField(choices=[('kg', 'Kilogramos'), ('lb', 'Libras')], max_length=2)),
                ('price', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]