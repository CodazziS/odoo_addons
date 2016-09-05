from openerp.osv import fields, osv

class gantt_improvement(osv.Model):
    _inherit = 'res.users'

    _columns = {
        'gantt_improvement_zoom': fields.selection(
            [
            ('1','Day'),
            ('2','Week'),
            ('3','Year'),
            ('4','Week'),
            ],
            'Default zoom',
            help="Choose the default zoom for the gantt view"),
    }
