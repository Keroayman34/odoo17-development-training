from odoo import models, fields


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

    image = fields.Image(string="Image")

    address = fields.Text(string="Address")

    age = fields.Integer(string="Age")

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