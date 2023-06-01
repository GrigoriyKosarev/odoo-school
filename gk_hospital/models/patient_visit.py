from odoo import models, fields


class PatientVisit(models.Model):
    _name = 'gk.patient.visit'
    _description = 'Patient visit'

    name = fields.Char()
