# Generated by Django 3.2.3 on 2023-04-15 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='ingredient',
            field=models.ForeignKey(blank=True, db_column='ingredient_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredient_recipe_table_ingredient', to='recipes.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='recipe',
            field=models.ForeignKey(blank=True, db_column='recipe_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredient_recipe_table_recipe', to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipes_by_this_author', to='users.user', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
