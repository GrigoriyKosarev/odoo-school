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
    years = fields.Integer(string='Years', compute='_compute_years')


    @api.depends('birthday')
    def _compute_years(self):
        for patient in self:
            if patient.birthday:
                birthday_date = patient.birthday
                full_age = relativedelta(datetime.today() - datetime.combine(birthday_date, time()))
                patient.years = full_age.years
            else:
                patient.years = 0