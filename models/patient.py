from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'HMS Patient'

    # Basic info
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    history = fields.Html(string="History")
    cr_ratio = fields.Float(string="CR Ratio")

    blood_type = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string="Blood Type")

    pcr = fields.Boolean(string="PCR")

    # Patient email
    email = fields.Char(string="Email", required=True)

    image = fields.Image(string="Image")

    address = fields.Text(string="Address")

    age = fields.Integer(string="Age")

    # Logs relation
    patient_log_ids = fields.One2many('hms.patient.log', 'patient_id', string='Logs', readonly=True)

    # Department relation
    department_id = fields.Many2one('hms.department', string="Department")
    department_capacity = fields.Integer(
        string="Department Capacity",
        related='department_id.capacity',
        readonly=True
    )

    # Doctors field
    doctor_ids = fields.Many2many('hms.doctors', string="Doctors")

    # Patient state
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string="State", default='undetermined')

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Patient email must be unique.'),
    ]

    @api.constrains('email')
    def _check_email_format(self):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        for rec in self:
            if not re.match(pattern, (rec.email or '')):
                raise ValidationError('Please provide a valid email address for the patient.')

    @api.onchange('age')
    def _onchange_age_set_pcr(self):
        for rec in self:
            if rec.age and rec.age < 30:
                rec.pcr = True
                return {
                    'warning': {
                        'title': 'PCR checked',
                        'message': 'PCR has been automatically checked because age is below 30.'
                    }
                }

    def write(self, vals):
        # Detect state changes and create logs when state changes
        logs = self.env['hms.patient.log']
        for rec in self:
            old_state = rec.state
            # If state will be updated and changes
            if 'state' in vals and vals.get('state') and vals.get('state') != old_state:
                # create log for this patient
                logs.create({
                    'patient_id': rec.id,
                    'description': f"State changed to {vals.get('state')}"
                })
        return super().write(vals)