from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lot_id = fields.Many2one('stock.lot', string='Lot/Serial Number')

    def _prepare_procurement_values(self, group_id=False):
        values = super()._prepare_procurement_values(group_id=group_id)
        if self.lot_id:
            values['lot_id'] = self.lot_id.id
        return values


class AddProductLotWizard(models.TransientModel):
    _name = 'add.product.lot.wizard'
    _description = 'Add Products with Lots Wizard'

    line_ids = fields.One2many('add.product.lot.wizard.line', 'wizard_id', string='Lines')

    def action_add_to_sale_order(self):
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))

        # Create new sale order lines
        sale_order_lines = []
        for line in self.line_ids:
            if line.product_id:
                vals = {
                    'order_id': sale_order.id,
                    'product_id': line.product_id.id,
                    'lot_id': line.lot_id.id,
                    'product_uom_qty': line.quantity,
                }
                sale_order_lines.append((0, 0, vals))

        if sale_order_lines:
            sale_order.write({'order_line': sale_order_lines})

        return {'type': 'ir.actions.act_window_close'}


class AddProductLotWizardLine(models.TransientModel):
    _name = 'add.product.lot.wizard.line'
    _description = 'Add Product with Lot Wizard Line'

    wizard_id = fields.Many2one('add.product.lot.wizard', string='Wizard')
    lot_id = fields.Many2one('stock.lot', string='Lot/Serial Number', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0, required=True)

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        if self.lot_id:
            self.product_id = self.lot_id.product_id
