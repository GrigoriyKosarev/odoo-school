from odoo import models, fields


class ContactPerson(models.Model):
    _name = 'gk.contact.person'
    _description = 'Contact person'
    _inherit = 'gk.person'

