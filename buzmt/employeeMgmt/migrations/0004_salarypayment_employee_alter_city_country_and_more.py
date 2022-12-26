# Generated by Django 4.1.4 on 2022-12-26 03:33

from django.db import migrations, models
import django.db.models.deletion
import employeeMgmt.models


class Migration(migrations.Migration):

    dependencies = [
        ("employeeMgmt", "0003_alter_employee_telephone"),
    ]

    operations = [
        migrations.AddField(
            model_name="salarypayment",
            name="employee",
            field=models.ForeignKey(
                default=employeeMgmt.models.Employee.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.employee",
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                default=employeeMgmt.models.Country.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.country",
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="office",
            field=models.ForeignKey(
                default=employeeMgmt.models.Office.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.office",
            ),
        ),
        migrations.AlterField(
            model_name="departmenthistory",
            name="department",
            field=models.ForeignKey(
                default=employeeMgmt.models.Department.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.department",
            ),
        ),
        migrations.AlterField(
            model_name="departmenthistory",
            name="employee",
            field=models.ForeignKey(
                default=employeeMgmt.models.Employee.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.employee",
            ),
        ),
        migrations.AlterField(
            model_name="employmentterm",
            name="employee",
            field=models.ForeignKey(
                default=employeeMgmt.models.Employee.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.employee",
            ),
        ),
        migrations.AlterField(
            model_name="jobhistory",
            name="employee",
            field=models.ForeignKey(
                default=employeeMgmt.models.Employee.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.employee",
            ),
        ),
        migrations.AlterField(
            model_name="jobhistory",
            name="jobTitle",
            field=models.ForeignKey(
                default=employeeMgmt.models.Job.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.job",
            ),
        ),
        migrations.AlterField(
            model_name="office",
            name="city",
            field=models.ForeignKey(
                default=employeeMgmt.models.City.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.city",
            ),
        ),
        migrations.AlterField(
            model_name="schedule", name="code", field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="workhour",
            name="employee",
            field=models.ForeignKey(
                default=employeeMgmt.models.Employee.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.employee",
            ),
        ),
        migrations.AlterField(
            model_name="workhour",
            name="schedule",
            field=models.ForeignKey(
                default=employeeMgmt.models.Schedule.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="employeeMgmt.schedule",
            ),
        ),
    ]
