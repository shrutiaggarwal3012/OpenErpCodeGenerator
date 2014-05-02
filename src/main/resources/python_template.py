from osv import osv, fields


class tvi_%s(osv.osv):
    _name = "tvi.%s"
    _description="%s"
    _inherit = ['mail.thread']
    _order = "%s"
    _columns = {
        "%s": fields.%s("%s"),
    }


tvi_%s()