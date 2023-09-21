


from odoo import models, fields, api,http

class Accounting(models.Model):
    _inherit = 'account.move'
    _description = 'Custom Accounting'



    link = fields.Char(compute='_compute_invoice_link')


    def _compute_invoice_link(self):
        for invoice in self:
            request = http.request
            # path = request.httprequest.path
            full_path = request.httprequest.url
            # Store the full URL path in the invoice_link field
            invoice.link = full_path
            print(full_path)




