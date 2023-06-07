from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'gk.diagnosis'
    _description = 'Diagnosis'

    diagnosis_date = fields.Date()
    doctor = fields.Many2one(comodel_name='gk.doctor', string='Doctor')
    patient = fields.Many2one(comodel_name='gk.patient', string='Patient')
    disease = fields.Many2one(comodel_name='gk.disease', string='Disease')
    appointment_for_treatment = fields.Char(string='Appointment for treatment')
