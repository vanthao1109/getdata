# Generated by Django 3.1.14 on 2022-08-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serpage', '0002_auto_20220808_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('invoice_id', models.CharField(blank=True, db_column='Invoice_ID', max_length=255, null=True)),
                ('branch', models.CharField(blank=True, db_column='Branch', max_length=30, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=50, null=True)),
                ('customer', models.CharField(blank=True, db_column='Customer', max_length=20, null=True)),
                ('sex', models.CharField(blank=True, db_column='Sex', max_length=20, null=True)),
                ('product', models.CharField(blank=True, db_column='Product', max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, db_column='Price', decimal_places=0, max_digits=10, null=True)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
                ('tax', models.DecimalField(blank=True, db_column='Tax', decimal_places=0, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, db_column='Total_Price', decimal_places=0, max_digits=10, null=True)),
                ('date', models.CharField(blank=True, db_column='Date', max_length=50, null=True)),
                ('time', models.CharField(blank=True, db_column='Time', max_length=20, null=True)),
                ('payment', models.CharField(blank=True, db_column='Payment', max_length=30, null=True)),
                ('cogs', models.DecimalField(blank=True, db_column='Cogs', decimal_places=0, max_digits=10, null=True)),
                ('gross_margin_percentage', models.DecimalField(blank=True, db_column='Gross_Margin_Percentage', decimal_places=0, max_digits=10, null=True)),
                ('gross_income', models.DecimalField(blank=True, db_column='Gross_Income', decimal_places=0, max_digits=10, null=True)),
                ('rating', models.DecimalField(blank=True, db_column='Rating', decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'customer_data',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CustommerData',
        ),
    ]
