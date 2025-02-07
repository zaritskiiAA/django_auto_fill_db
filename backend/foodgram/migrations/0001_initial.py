# Generated by Django 3.2.16 on 2023-12-04 13:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='FavoriteRecipe',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'FavoriteRecipes',
            },
        ),
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        help_text='Укажите название',
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                '^[а-яА-ЯёЁa-zA-Z]*$',
                                'Поле должно содержать только буквы кириллицы/латиницы',
                            )
                        ],
                        verbose_name='Название',
                    ),
                ),
                (
                    'measurement_unit',
                    models.CharField(
                        help_text='Укажите единицу измерения',
                        max_length=200,
                        verbose_name='Единица измерения',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Ingridients',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        help_text='Укажите название',
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                '^[а-яА-ЯёЁa-zA-Z]*$',
                                'Поле должно содержать только буквы кириллицы/латиницы',
                            )
                        ],
                        verbose_name='Название',
                    ),
                ),
                (
                    'image',
                    models.ImageField(
                        help_text='Добавьте фотографию рецепта',
                        upload_to='',
                        verbose_name='Фотография',
                    ),
                ),
                (
                    'text',
                    models.TextField(
                        help_text='Опишите рецепт',
                        verbose_name='Описание рецепта',
                    ),
                ),
                (
                    'cooking_time',
                    models.PositiveSmallIntegerField(
                        help_text='Укажите время приготовления',
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message='Укажите значение 1 и более',
                            )
                        ],
                        verbose_name='Время приготовления',
                    ),
                ),
                (
                    'pub_date',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата публикации'
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Recipes',
                'ordering': ('-pub_date',),
                'default_related_name': 'recipes',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngridients',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'amount',
                    models.SmallIntegerField(
                        help_text='Укажите количество ингредиента',
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message='Укажите значение 1 и более',
                            )
                        ],
                        verbose_name='количество',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        help_text='Укажите название',
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                '^[а-яА-ЯёЁa-zA-Z]*$',
                                'Поле должно содержать только буквы кириллицы/латиницы',
                            )
                        ],
                        verbose_name='Название',
                    ),
                ),
                (
                    'color',
                    models.CharField(
                        help_text='Укажите цвет',
                        max_length=7,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code='invalid_HEX_color',
                                message='Укажите корректный HEX цвет',
                                regex='^#([A-Fa-f0-9]{3,6})$',
                            )
                        ],
                        verbose_name='Цвет',
                    ),
                ),
                (
                    'slug',
                    models.SlugField(
                        help_text='Укажите слаг, поле должно быть уникальным',
                        max_length=200,
                        unique=True,
                        verbose_name='Слаг',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'recipe',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='shopping_cart',
                        to='foodgram.recipe',
                        verbose_name='Рецепт',
                    ),
                ),
            ],
        ),
    ]
