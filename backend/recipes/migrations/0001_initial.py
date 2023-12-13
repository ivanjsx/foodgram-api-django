# Generated by Django 3.2 on 2023-12-13 14:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import recipes.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
                ('amount', models.IntegerField(help_text='Provide the amount needed', validators=[django.core.validators.MinValueValidator(1)], verbose_name='amount')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
                ('name', models.CharField(help_text='Provide a name', max_length=200, verbose_name='name')),
                ('measurement_unit', models.CharField(help_text='Provide a measurement unit', max_length=200, verbose_name='measurement unit')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
                ('name', models.CharField(help_text='Provide a name', max_length=200, verbose_name='name')),
                ('text', models.TextField(help_text='Provide a description', verbose_name='description')),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='Provide a cooking time, in minutes', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cooking time, in minutes')),
                ('image', models.ImageField(help_text='Upload a cover image', upload_to='recipes/', verbose_name='Cover image')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='RecipeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date & time of instance creation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date & time of last instance modification')),
                ('name', models.CharField(help_text='Provide a name', max_length=200, verbose_name='name')),
                ('slug', models.SlugField(help_text='Provide a unique slug (will be used in the URL address)', max_length=200, unique=True, verbose_name='slug')),
                ('color', models.CharField(help_text='Provide a unique color', max_length=7, unique=True, validators=[recipes.validators.hex_color_validator], verbose_name='color')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('name',), name='tag name must be unique'),
        ),
        migrations.AddField(
            model_name='recipetag',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='recipes.recipe'),
        ),
        migrations.AddField(
            model_name='recipetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_on', to='recipes.tag'),
        ),
    ]
