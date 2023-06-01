from odoo import models, fields


class Doctor(models.Model):
    _name = 'gk.doctor'
    _description = 'Doctor'

    name = fields.Char()
    active = fields.Boolean(
        default=True)
