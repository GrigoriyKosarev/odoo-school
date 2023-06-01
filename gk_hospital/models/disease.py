from odoo import models, fields


class Disease(models.Model):
    _name = 'gk.disease'
    _description = 'Disease'

    name = fields.Char()
