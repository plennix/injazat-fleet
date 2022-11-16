# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

CATEGORY_SELECTION = [
    ('required', 'Required'),
    ('optional', 'Optional'),
    ('no', 'None')]


class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    has_fleet = fields.Selection(CATEGORY_SELECTION, string="Fleet", default="no", required=True)
    has_department_from = fields.Selection(CATEGORY_SELECTION, string="Department From", default="no", required=True)
    has_department_to = fields.Selection(CATEGORY_SELECTION, string="Department To", default="no", required=True)