from odoo import models, fields


class Doctor(models.Model):
    _name = 'gk.doctor'
    _description = 'Doctor'
    _inherit = ['gk.person']

    active = fields.Boolean(
        default=True)
