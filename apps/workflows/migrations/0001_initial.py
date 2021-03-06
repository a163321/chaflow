# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-02-01 11:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alter',
            fields=[
                ('date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='创建时间')),
                ('alter_id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('alter_title', models.CharField(max_length=255, verbose_name='变更名称')),
                ('in_queue', models.BooleanField(default=True, help_text='只要任务没被人处理，就会一直在queue中')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('risk_level', models.SmallIntegerField(choices=[(0, '低'), (1, '中'), (2, '高')], verbose_name='风险等级')),
                ('alter_type', models.SmallIntegerField(choices=[(0, '一般变更'), (1, '紧急变更')], default=None, verbose_name='变更类型')),
                ('memo', models.TextField(blank=True, default=None, null=True, verbose_name='备注')),
                ('alter_effect', models.SmallIntegerField(choices=[(0, '无影响'), (1, '业务中断')], default=0, verbose_name='业务影响')),
                ('alter_stop_time', models.CharField(default=None, max_length=128, verbose_name='业务中断时间')),
                ('alter_stop_range', models.CharField(default=None, max_length=128, verbose_name='业务中断范围')),
                ('technical_director_opnion', models.TextField(default=None, max_length=500, verbose_name='团队技术负责人意见')),
                ('committee_opnion', models.TextField(default=None, max_length=500, verbose_name='方案评审会评审意见')),
                ('implement_plan', models.TextField(default=None, max_length=500, verbose_name='实施方案')),
                ('implement_plan_time', models.CharField(default=None, max_length=128, verbose_name='实施方案预期耗时')),
                ('implement_validate_plan', models.TextField(default=None, max_length=500, verbose_name='实施后验证方案')),
                ('implement_validate_plan_time', models.CharField(default=None, max_length=128, verbose_name='实施后验证方案预期耗时')),
                ('back_plan', models.TextField(default=None, max_length=500, verbose_name='回退方案')),
                ('back_plan_time', models.CharField(default=None, max_length=128, verbose_name='回退方案预期耗时')),
                ('back_validate_plan', models.TextField(default=None, max_length=500, verbose_name='应急处理后验证方案')),
                ('back_validate_plan_time', models.CharField(default=None, max_length=128, verbose_name='处理后预期耗时')),
                ('yingji_plan', models.TextField(default=None, max_length=500, verbose_name='应急预案')),
                ('yingji_plan_time', models.CharField(default=None, max_length=128, verbose_name='应急预案预期耗时')),
                ('yingji_validate_plan', models.TextField(default=None, max_length=500, verbose_name='回退后验证方案')),
                ('yingji_validate_plan_time', models.CharField(default=None, max_length=128, verbose_name='回退后验证方案预期耗时')),
                ('customer_director', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='customer_director_alters', to=settings.AUTH_USER_MODEL, verbose_name='团队技术负责人')),
                ('operator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='operator_alters', to=settings.AUTH_USER_MODEL, verbose_name='变更操作人')),
                ('proposer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='proposer_alters', to=settings.AUTH_USER_MODEL, verbose_name='变更申请人')),
                ('technical_director', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='technical_director_alters', to=settings.AUTH_USER_MODEL, verbose_name='团队技术负责人')),
            ],
        ),
        migrations.CreateModel(
            name='Alter_Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alter_momo', models.CharField(max_length=255, verbose_name='变更内容概括')),
                ('change_type', models.SmallIntegerField(choices=[(0, '功能优化'), (1, '问题修复'), (2, '数据调整'), (3, '测试环境调整'), (4, '数据导入导出')], verbose_name='修改类型')),
                ('approve_user', models.CharField(max_length=128, verbose_name='提出人')),
                ('alter_description', models.TextField(blank=True, null=True, verbose_name='详细说明')),
                ('other_env', models.CharField(max_length=256, verbose_name='涉及环境')),
                ('alter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='workflows.Alter')),
            ],
        ),
        migrations.CreateModel(
            name='FlowRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('is_dynamic_role', models.BooleanField(default=False)),
                ('role_lookup_func', models.CharField(blank=True, max_length=64, null=True, verbose_name='查找动态role的函数')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FlowTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('flow_type', models.CharField(choices=[('Alter', '变更流程')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='环节名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='环节介绍')),
                ('order', models.PositiveSmallIntegerField(verbose_name='环节步骤')),
                ('is_countersign', models.BooleanField(default=False, verbose_name='会签环节')),
                ('required_polls', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='会签最少需同意的人数')),
                ('flow_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.FlowTemplate', verbose_name='所属流程')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.FlowRole', verbose_name='审批角色')),
            ],
        ),
        migrations.AddField(
            model_name='alter',
            name='template',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workflows.FlowTemplate'),
        ),
        migrations.AlterUniqueTogether(
            name='step',
            unique_together=set([('flow_template', 'order')]),
        ),
    ]
