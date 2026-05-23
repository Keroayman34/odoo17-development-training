from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')

    @api.constrains('related_patient_id')
    def _check_patient_email_conflict(self):
        for rec in self:
            if rec.related_patient_id and rec.related_patient_id.email:
                patient_email = rec.related_patient_id.email
                # find other partners (customers) that already use the same patient email
                other = self.search([('id', '!=', rec.id), ('email', '=', patient_email)])
                if other:
                    raise ValidationError('Another customer already uses this patient\'s email. Cannot link.')

    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError('You cannot delete a customer linked to a patient.')
        return super().unlink()

    @api.constrains('vat')
    def _check_vat_required(self):
        for rec in self:
            # Make vat required for customers
            if rec.customer_rank and not rec.vat:
                raise ValidationError('Tax ID (VAT) is required for customers.')
