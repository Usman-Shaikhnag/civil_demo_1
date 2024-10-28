from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
import math



class ConcreteDesign(models.Model):
    _name = "mechanical.concrete.design"
    _inherit = "lerm.eln"
    _rec_name = "name"

    name = fields.Char("Name",default="CONCRETE MIX DESIGN FOR GRADE OF M-40")
    parameter_id = fields.Many2one('eln.parameters.result',string="Parameter")
    sample_parameters = fields.Many2many('lerm.parameter.master',string="Parameters",compute="_compute_sample_parameters",store=True)
    eln_ref = fields.Many2one('lerm.eln',string="Eln")

    
    # Parameter Name = 1) CONCRETE MIX DESIGN FOR GRADE OF M-40
   
    kgm3_1 = fields.Float(string="Abstract") 
    spgr_1 = fields.Float(string="Cement")
    mixgrade_1 = fields.Float(string="Slag")
    std_dev_1 = fields.Float(string="Mirosilica")
    # wcf_1 = fields.Float(string="W/(C+F)")
    # cf_1 = fields.Float(string="(C+F)")
    # rsand_1 = fields.Float(string="R/SAND")
    # csand_1 = fields.Float(string="C/SAND")
    # 10_1 = fields.Float(string="10 MM")
    # _1 = fields.Float(string="20 MM")
    # csand_1 = fields.Float(string="C/SAND")

    kgm3_2 = fields.Float(string="Abstract") 
    kgm3_3 = fields.Float(string="Abstract") 
    kgm3_4 = fields.Float(string="Abstract") 
    kgm3_5 = fields.Float(string="Abstract") 
    kgm3_6 = fields.Float(string="Abstract") 
    kgm3_7 = fields.Float(string="Abstract") 
    kgm3_8 = fields.Float(string="Abstract") 
    kgm3_9 = fields.Float(string="Abstract") 
