from odoo import models, fields


class Person(models.AbstractModel):
    _name = 'gk.person'
    _description = 'Person Abstract model'

    full_name = fields.Char(string="Full name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    photo = fields.Binary(string="Photo")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", default='male')



