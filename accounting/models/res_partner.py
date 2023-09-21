
from odoo import models, fields, api, http

class Partner(models.Model):
    _inherit = 'res.partner'

    property_payable_account_id = fields.Many2one('account.account', company_dependent=True,
                                                  string="Account Payable",
                                                  help="This account will be used instead of the default one as the payable account for the current partner",
                                                  required=True)

    property_receivable_account_id = fields.Many2one('account.account', company_dependent=True,
                                                     string="Account Receivable",
                                                     help="This account will be used instead of the default one as the receivable account for the current partner",
                                                     required=True)