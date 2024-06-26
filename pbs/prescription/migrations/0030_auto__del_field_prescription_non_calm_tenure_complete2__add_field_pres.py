# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Prescription.non_calm_tenure_approved'
        db.add_column(u'prescription_prescription', 'non_calm_tenure_approved',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)



    def backwards(self, orm):

        # Deleting field 'Prescription.non_calm_tenure_approved'
        db.delete_column(u'prescription_prescription', 'non_calm_tenure_approved')
    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'prescription.approval': {
            'Meta': {'ordering': "[u'-id']", 'object_name': 'Approval'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_approval_created'", 'to': u"orm['auth.User']"}),
            'extension_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_valid_to': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2020, 6, 23, 0, 0)'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_approval_modified'", 'to': u"orm['auth.User']"}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'on_delete': 'models.PROTECT'}),
            'valid_to': ('django.db.models.fields.DateField', [], {})
        },
        u'prescription.briefingchecklist': {
            'Meta': {'ordering': "[u'smeac__id', u'id']", 'object_name': 'BriefingChecklist'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['risk.Action']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_briefingchecklist_created'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_briefingchecklist_modified'", 'to': u"orm['auth.User']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'on_delete': 'models.PROTECT'}),
            'smeac': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.SMEAC']", 'on_delete': 'models.PROTECT'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'prescription.defaultbriefingchecklist': {
            'Meta': {'object_name': 'DefaultBriefingChecklist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'smeac': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.SMEAC']", 'on_delete': 'models.PROTECT'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.district': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'District'},
            'archive_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Region']", 'on_delete': 'models.PROTECT'})
        },
        u'prescription.endorsement': {
            'Meta': {'ordering': "[u'role']", 'object_name': 'Endorsement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_endorsement_created'", 'to': u"orm['auth.User']"}),
            'endorsed': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_endorsement_modified'", 'to': u"orm['auth.User']"}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'on_delete': 'models.PROTECT'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.EndorsingRole']", 'on_delete': 'models.PROTECT'})
        },
        u'prescription.endorsingrole': {
            'Meta': {'ordering': "[u'index']", 'object_name': 'EndorsingRole'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'disclaimer': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '320'})
        },
        u'prescription.forecastarea': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'ForecastArea'},
            'districts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.District']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.fueltype': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'FuelType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.fundingallocation': {
            'Meta': {'unique_together': "((u'prescription', u'allocation'),)", 'object_name': 'FundingAllocation'},
            'allocation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'on_delete': 'models.PROTECT'}),
            'proportion': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'})
        },
        u'prescription.objective': {
            'Meta': {'ordering': "[u'created']", 'object_name': 'Objective'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_objective_created'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_objective_modified'", 'to': u"orm['auth.User']"}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'on_delete': 'models.PROTECT'})
        },
        u'prescription.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'aircraft_burn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approval_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'approval_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'area': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '1'}),
            'burn_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'bushfire_act_zone': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'carried_over': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'closure_officer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'closure'", 'null': 'True', 'on_delete': 'models.PROTECT', 'to': u"orm['auth.User']"}),
            'contentious': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'contentious_rationale': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contingencies_migrated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_prescription_created'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['prescription.District']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'endorsement_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'endorsement_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'endorsing_roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.EndorsingRole']", 'symmetrical': 'False'}),
            'endorsing_roles_determined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financial_year': ('django.db.models.fields.CharField', [], {'default': "u'2018/2019'", 'max_length': '10'}),
            'forecast_areas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.ForecastArea']", 'null': 'True', 'blank': 'True'}),
            'forest_blocks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fuel_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.FuelType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignition_completed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ignition_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'ignition_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_season': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'last_season_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_year': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'last_year_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': "u'320'", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_prescription_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'non_calm_tenure': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'non_calm_tenure_approved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'non_calm_tenure_complete': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'non_calm_tenure_included': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'non_calm_tenure_risks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'non_calm_tenure_value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'perimeter': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '1'}),
            'planned_season': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '8', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'planned_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'blank': 'True'}),
            'planning_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'planning_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'prescribing_officer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'prohibited_period': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purposes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.Purpose']", 'symmetrical': 'False'}),
            'rationale': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Region']", 'on_delete': 'models.PROTECT'}),
            'regional_objectives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.RegionalObjective']", 'null': 'True', 'blank': 'True'}),
            'remote_sensing_priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '4'}),
            'shires': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.Shire']", 'null': 'True', 'blank': 'True'}),
            'short_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'tenures': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.Tenure']", 'symmetrical': 'False', 'blank': 'True'}),
            'treatment_percentage': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'prescription.priorityjustification': {
            'Meta': {'ordering': "[u'order']", 'unique_together': "((u'purpose', u'prescription'),)", 'object_name': 'PriorityJustification'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_priorityjustification_created'", 'to': u"orm['auth.User']"}),
            'criteria': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_priorityjustification_modified'", 'to': u"orm['auth.User']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Purpose']", 'on_delete': 'models.PROTECT'}),
            'rationale': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'relevant': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'prescription.purpose': {
            'Meta': {'ordering': "[u'display_order', u'name']", 'object_name': 'Purpose'},
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'prescription.regionalobjective': {
            'Meta': {'object_name': 'RegionalObjective'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_regionalobjective_created'", 'to': u"orm['auth.User']"}),
            'fma_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_regionalobjective_modified'", 'to': u"orm['auth.User']"}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Region']", 'on_delete': 'models.PROTECT'})
        },
        u'prescription.season': {
            'Meta': {'ordering': "[u'-start']", 'object_name': 'Season'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_season_created'", 'to': u"orm['auth.User']"}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_season_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '8'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        u'prescription.shire': {
            'Meta': {'ordering': "[u'name']", 'unique_together': "((u'name', u'district'),)", 'object_name': 'Shire'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.District']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.smeac': {
            'Meta': {'object_name': 'SMEAC'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'prescription.successcriteria': {
            'Meta': {'ordering': "[u'created']", 'object_name': 'SuccessCriteria'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_successcriteria_created'", 'to': u"orm['auth.User']"}),
            'criteria': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_successcriteria_modified'", 'to': u"orm['auth.User']"}),
            'objectives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.Objective']", 'symmetrical': 'False'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'on_delete': 'models.PROTECT'})
        },
        u'prescription.tenure': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Tenure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'risk.action': {
            'Meta': {'ordering': "[u'risk__category', u'-relevant', u'risk__name', u'pk']", 'object_name': 'Action'},
            'context_statement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'risk_action_created'", 'to': u"orm['auth.User']"}),
            'day_of_burn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_administration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_command': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_completed': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'day_of_burn_completer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'day_of_burn_execution': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_include': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_mission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_responsible': ('django.db.models.fields.CharField', [], {'default': "u'IC'", 'max_length': '200'}),
            'day_of_burn_safety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day_of_burn_situation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'risk_action_modified'", 'to': u"orm['auth.User']"}),
            'post_burn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post_burn_completed': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'post_burn_completer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pre_burn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pre_burn_completed': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pre_burn_completer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pre_burn_explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pre_burn_resolved': ('django.db.models.fields.CharField', [], {'default': "u'No'", 'max_length': '200', 'blank': 'True'}),
            'relevant': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'risk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['risk.Risk']", 'on_delete': 'models.PROTECT'}),
            'total': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'risk.risk': {
            'Meta': {'ordering': "[u'category', u'name']", 'object_name': 'Risk'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['risk.RiskCategory']", 'on_delete': 'models.PROTECT'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'risk_risk_created'", 'to': u"orm['auth.User']"}),
            'custom': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'risk_risk_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'risk': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'risk.riskcategory': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'RiskCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['prescription']
