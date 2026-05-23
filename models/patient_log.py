from odoo import models, fields, api


class PatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'HMS Patient Log'

    # Link to patient
    patient_id = fields.Many2one('hms.patient', string='Patient', required=True, ondelete='cascade')

    # User who created the log
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)

    # Datetime of the log
    date = fields.Datetime(string='Date', default=fields.Datetime.now, readonly=True)

    # Description of the log
    description = fields.Text(string='Description', required=True)
