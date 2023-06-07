from odoo import models, fields, api
from datetime import datetime, time
from dateutil.relativedelta import relativedelta


class Patient(models.Model):
    _name = 'gk.patient'
    _description = 'Patient'
    _inherit = 'gk.person'

    active = fields.Boolean(
        default=True)
    observing_doctor = fields.Many2one(
        comodel_name='gk.doctor')
    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Years', compute='_compute_age')
    passport = fields.Char(string='Passport')
    contact_person = fields.Many2one(comodel_name='gk.contact.person', string='Contact person')
    personal_doctor = fields.Many2one(comodel_name='gk.doctor', string='Personal doctor')

    @api.depends('birthday')
    def _compute_age(self):
        self.ensure_one()
        if self.birthday:
            current_date = datetime.now()
            self.age = current_date.year - self.birthday.year

            if current_date.month < self.birthday.month or (
                    current_date.month == self.birthday.month and current_date.day < self.birthday.day):
                self.age -= 1
        else:
            self.age = 0