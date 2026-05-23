from odoo import models, fields


class Doctors(models.Model):
    _name = 'hms.doctors'
    _description = 'HMS Doctors'

    # Basic info
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    image = fields.Image(string="Image")
