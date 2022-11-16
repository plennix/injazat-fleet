import datetime
import json
from lxml import etree

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    fleet= fields.Many2one('fleet.vehicle', string='Fleet')
    from_department = fields.Many2one('hr.department', string='From Department')
    to_department = fields.Many2one('hr.department', string='To Department')
    has_fleet = fields.Selection(related="category_id.has_fleet")
    has_department_from = fields.Selection(related="category_id.has_department_from")
    has_department_to = fields.Selection(related="category_id.has_department_to")
