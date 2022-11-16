import datetime
import json
from lxml import etree

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    fleet= fields.Many2one('fleet.vehicle', string='Fleet')
