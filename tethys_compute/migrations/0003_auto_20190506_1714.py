# Generated by Django 2.1.8 on 2019-05-06 17:14

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


DATA = {}


def data_export(apps, schema_editor):
    CondorPyJob = apps.get_model('tethys_compute', 'CondorPyJob')
    CondorPyWorkflow = apps.get_model('tethys_compute', 'CondorPyWorkflow')
    CondorWorkflowNode = apps.get_model('tethys_compute', 'CondorWorkflowNode')
    TethysJob = apps.get_model('tethys_compute', 'TethysJob')

    condorpyjob_dict = dict()

    for o in CondorPyJob.objects.raw('SELECT * FROM tethys_compute_condorpyjob'):
        condorpyjob_dict[o.condorpyjob_id] = {
            '_attributes': o._attributes,
            '_remote_input_files': o._remote_input_files
        }

    DATA[CondorPyJob.__name__] = condorpyjob_dict

    condorpyworkflow_dict = dict()

    for o in CondorPyWorkflow.objects.raw('SELECT * FROM tethys_compute_condorpyworkflow'):
        condorpyworkflow_dict[o.condorpyworkflow_id] = {
            '_max_jobs': o._max_jobs
        }

    DATA[CondorPyWorkflow.__name__] = condorpyworkflow_dict

    condorworkflownode_dict = dict()

    for o in CondorWorkflowNode.objects.raw('SELECT * FROM tethys_compute_condorworkflownode'):
        condorworkflownode_dict[o.id] = {
            'variables': o.variables
        }

    DATA[CondorWorkflowNode.__name__] = condorworkflownode_dict

    tethysjob_dict = dict()

    for o in TethysJob.objects.raw('SELECT * FROM tethys_compute_tethysjob'):
        tethysjob_dict[o.id] = {
            'extended_properties': o.extended_properties
        }

    DATA[TethysJob.__name__] = tethysjob_dict


def data_import(apps, schema_editor):
    CondorPyJob = apps.get_model('tethys_compute', 'CondorPyJob')
    CondorPyWorkflow = apps.get_model('tethys_compute', 'CondorPyWorkflow')
    CondorWorkflowNode = apps.get_model('tethys_compute', 'CondorWorkflowNode')
    TethysJob = apps.get_model('tethys_compute', 'TethysJob')

    MODEL_NAME_MAP = {
        CondorPyJob.__name__: (CondorPyJob, 'condorpyjob_id'),
        CondorPyWorkflow.__name__: (CondorPyWorkflow, 'condorpyworkflow_id'),
        CondorWorkflowNode.__name__: (CondorWorkflowNode, 'id'),
        TethysJob.__name__: (TethysJob, 'id')
    }

    for model_name in DATA.keys():
        records = DATA[model_name]
        ModelClass, id_name = MODEL_NAME_MAP[model_name]

        for id in records.keys():
            record = records[id]
            o = ModelClass.objects.get(**{id_name: id})

            for attr, value in record.items():
                setattr(o, attr, value)

            o.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tethys_compute', '0002_daskjob'),
    ]

    operations = [
        migrations.RunPython(data_export),
        # Remove fields to clear data
        migrations.RemoveField(
            model_name='condorpyjob',
            name='_attributes',
        ),
        migrations.RemoveField(
            model_name='condorpyjob',
            name='_remote_input_files',
        ),
        migrations.RemoveField(
            model_name='condorpyworkflow',
            name='_max_jobs',
        ),
        migrations.RemoveField(
            model_name='condorworkflownode',
            name='variables',
        ),
        migrations.RemoveField(
            model_name='tethysjob',
            name='extended_properties',
        ),
        # Add new versions of the fields
        migrations.AddField(
            model_name='condorpyjob',
            name='_attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='condorpyjob',
            name='_remote_input_files',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1024, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='condorpyworkflow',
            name='_max_jobs',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='condorworkflownode',
            name='variables',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='tethysjob',
            name='extended_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.RunPython(data_import),
    ]
