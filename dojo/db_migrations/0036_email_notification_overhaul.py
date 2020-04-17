# Generated by Django 2.2.12 on 2020-04-05 16:35

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0035_push_all_issues_help_text_rename_gh_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='results_added',
            new_name='scan_added',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.Dojo_User'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='product',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.Product'),
        ),
        migrations.AddConstraint(
            model_name='notifications',
            constraint=models.UniqueConstraint(fields=('user', 'product'), name='notifications_user_product'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='scan_added',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('hipchat', 'hipchat'), ('mail', 'mail'), ('alert', 'alert')], default='alert', help_text='Triggered whenever an (re-)import has been done that created/updated/closed findings.', max_length=24),
        ),
    ]
