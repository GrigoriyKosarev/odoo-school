from odoo import models, fields


class Patient(models.Model):
    _name = 'gk.patient'
    _description = 'Patient'

    name = fields.Char()
    active = fields.Boolean(
        default=True)
    observing_doctor = fields.Many2one(
        comodel_name='gk.doctor')
