from odoo import models, api, fields

class fleet_vehicle(models.Model):
    _inherit = 'fleet.vehicle'

    done_approval_request_count = fields.Integer(string='Approval Request', compute='_get_approval_request_count', readonly=True)

    def _get_approval_request_count(self):
        for rec in self:
            self.done_approval_request_count = self.env['approval.request'].search_count([('fleet', '=', rec.id),('request_status','=','approved')])

    def action_view_transfer_history(self):
        res = self.env.ref('fleet_approvals.approval_request_extended_action').read()[0]
        for rec in self:
            res['domain'] = str([('fleet', '=', rec.id),('request_status','=','approved')])
        return res