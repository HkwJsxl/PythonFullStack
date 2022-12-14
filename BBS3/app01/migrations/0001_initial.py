# Generated by Django 2.2.28 on 2022-07-28 11:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='?????????')),
                ('avatar', models.FileField(default='/static/img/default.jpg', upload_to='avatar/', verbose_name='????????????')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='??????????????????')),
                ('gender', models.IntegerField(choices=[(1, '???'), (2, '???'), (3, '??????')], default=3, verbose_name='????????????')),
                ('desc', models.CharField(max_length=128, verbose_name='????????????')),
            ],
            options={
                'verbose_name_plural': '?????????',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='????????????')),
                ('desc', models.CharField(max_length=255, verbose_name='????????????')),
                ('content', models.TextField(verbose_name='????????????')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='??????????????????')),
                ('up_num', models.IntegerField(default=0, verbose_name='?????????')),
                ('down_num', models.IntegerField(default=0, verbose_name='?????????')),
                ('comment_num', models.IntegerField(default=0, verbose_name='?????????')),
            ],
            options={
                'verbose_name_plural': '?????????',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=64, verbose_name='????????????')),
                ('site_title', models.CharField(blank=True, max_length=64, null=True, verbose_name='????????????')),
                ('site_css', models.CharField(blank=True, max_length=64, null=True, verbose_name='????????????')),
            ],
            options={
                'verbose_name_plural': '???????????????',
            },
        ),
        migrations.CreateModel(
            name='UpAndDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_up', models.BooleanField(verbose_name='????????????')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '???????????????',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='????????????')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Blog')),
            ],
            options={
                'verbose_name_plural': '???????????????',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='????????????')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='????????????')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '?????????',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='????????????')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Blog')),
            ],
            options={
                'verbose_name_plural': '???????????????',
            },
        ),
        migrations.CreateModel(
            name='ArticleToTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Tag')),
            ],
            options={
                'verbose_name_plural': '???????????????',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Blog'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='app01.ArticleToTag', to='app01.Tag'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Blog'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
