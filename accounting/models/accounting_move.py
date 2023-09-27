from odoo import models, fields, api,http


class Accounting(models.Model):
    _inherit = 'account.move'
    _description = 'Custom Accounting'

    link = fields.Char(compute='_compute_invoice_link')


    def _compute_invoice_link(self):
        for invoice in self:
            full_url = invoice.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
            invoice.link = f"{full_url}/web#id={invoice.id}&view_type=form&model={invoice._name}"





class Sales(models.Model):
    _inherit = 'sale.order'


    link = fields.Char(compute='_compute_invoice_link')


    def _compute_invoice_link(self):
        for invoice in self:
            full_url = invoice.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
            invoice.link = f"{full_url}/web#id={invoice.id}&view_type=form&model={invoice._name}"



class Sales(models.Model):
    _inherit = 'account.payment'


    link = fields.Char(compute='_compute_invoice_link')


    def _compute_invoice_link(self):
        for invoice in self:
            full_url = invoice.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
            invoice.link = f"{full_url}/web#id={invoice.id}&view_type=form&model={invoice._name}"





class Purchase(models.Model):
    _inherit = 'purchase.order'


    link = fields.Char(compute='_compute_invoice_link')


    def _compute_invoice_link(self):
        for invoice in self:
            full_url = invoice.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
            invoice.link = f"{full_url}/web#id={invoice.id}&view_type=form&model={invoice._name}"

            # invoice.link = '%s/web#id=%s&view_type=form&model=%s' % (full_url, invoice.id, invoice._name)

    # def action_share_whatsapp(self):
    #     base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
    #     message = f"Check out this product: {base_url}/web#id={self.id}&view_type=form&model=purchase.order"
    #     whatsapp_url = f"https://api.whatsapp.com/send?text={message}"
    #     print(whatsapp_url)
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': whatsapp_url + "&text=" + message,
    #         'target': 'new',
    #         'res_id': self.id,
    #     }