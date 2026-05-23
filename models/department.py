from odoo import models, fields


class Department(models.Model):
    _name = 'hms.department'
    _description = 'HMS Department'

    # Basic info
    name = fields.Char(string="Name")
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean(string="Is Opened")

    # Patients relation
    patient_ids = fields.One2many('hms.patient', 'department_id', string="Patients")
