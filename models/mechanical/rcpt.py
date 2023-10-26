from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
import math


class RcptConcreteCube(models.Model):
    _name = "mechanical.rcpt.concrete.cube"
    _inherit = "lerm.eln"
    _rec_name = "name"

    name = fields.Char("Name",default="RCPT Concrete Cube")
    parameter_id = fields.Many2one('eln.parameters.result',string="Parameter")
    sample_parameters = fields.Many2many('lerm.parameter.master',string="Parameters",compute="_compute_sample_parameters",store=True)
    eln_ref = fields.Many2one('lerm.eln',string="ELN")


    child_lines = fields.One2many('mechanical.rcpt.concrete.cube.line','parent_id',string="Parameter")
    io_sample1 = fields.Float(string="Io",compute="_compute_io_sample1", store=True)
    io_sample2 = fields.Float(string="Io",compute="_compute_io_sample2",store=True)
    io_sample3 = fields.Float(string="Io",compute="_compute_io_sample3",store=True)
    i30_sample1 = fields.Float(string="I30",compute="_compute_i30_sample1",store=True)
    i30_sample2 = fields.Float(string="I30",compute="_compute_i30_sample2",store=True)
    i30_sample3 = fields.Float(string="I30",compute="_compute_i30_sample3",store=True)
    i60_sample1 = fields.Float(string="I60",compute="_compute_i60_sample1",store=True)
    i60_sample2 = fields.Float(string="I60",compute="_compute_i60_sample2",store=True)
    i60_sample3 = fields.Float(string="I60",compute="_compute_i60_sample3",store=True)
    i90_sample1 = fields.Float(string="I90",compute="_compute_i90_sample1",store=True)
    i90_sample2 = fields.Float(string="I90",compute="_compute_i90_sample2",store=True)
    i90_sample3 = fields.Float(string="I90",compute="_compute_i90_sample3",store=True)
    i120_sample1 = fields.Float(string="I120",compute="_compute_i120_sample1",store=True)
    i120_sample2 = fields.Float(string="I120",compute="_compute_i120_sample2",store=True)
    i120_sample3 = fields.Float(string="I120",compute="_compute_i120_sample3",store=True)
    i150_sample1 = fields.Float(string="I150",compute="_compute_i150_sample1",store=True)
    i150_sample2 = fields.Float(string="I150",compute="_compute_i150_sample2",store=True)
    i150_sample3 = fields.Float(string="I150",compute="_compute_i150_sample3",store=True)
    i180_sample1 = fields.Float(string="I180",compute="_compute_i180_sample1",store=True)
    i180_sample2 = fields.Float(string="I180",compute="_compute_i180_sample2",store=True)
    i180_sample3 = fields.Float(string="I180",compute="_compute_i180_sample3",store=True)
    i210_sample1 = fields.Float(string="I210",compute="_compute_i210_sample1",store=True)
    i210_sample2 = fields.Float(string="I210",compute="_compute_i210_sample2",store=True)
    i210_sample3 = fields.Float(string="I210",compute="_compute_i210_sample3",store=True)
    i240_sample1 = fields.Float(string="I240",compute="_compute_i240_sample1",store=True)
    i240_sample2 = fields.Float(string="I240",compute="_compute_i240_sample2",store=True)
    i240_sample3 = fields.Float(string="I240",compute="_compute_i240_sample3",store=True)
    i270_sample1 = fields.Float(string="I270",compute="_compute_i270_sample1",store=True)
    i270_sample2 = fields.Float(string="I270",compute="_compute_i270_sample2",store=True)
    i270_sample3 = fields.Float(string="I270",compute="_compute_i270_sample3",store=True)
    i300_sample1 = fields.Float(string="I300",compute="_compute_i300_sample1",store=True)
    i300_sample2 = fields.Float(string="I300",compute="_compute_i300_sample2",store=True)
    i300_sample3 = fields.Float(string="I300",compute="_compute_i300_sample3",store=True)
    sample1_i330 = fields.Float(string="I330",compute="_compute_sample1_i330",store=True)
    sample2_i330 = fields.Float(string="I330",compute="_compute_sample2_i330",store=True)
    sample3_i330 = fields.Float(string="I330",compute="_compute_sample3_i330",store=True)
    
    i360_sample1 = fields.Float(string="I360",compute="_compute_i360_sample1",store=True)
    i360_sample2 = fields.Float(string="I360",compute="_compute_i360_sample2",store=True)
    i360_sample3 = fields.Float(string="I360",compute="_compute_i360_sample3",store=True)

    

    @api.depends('child_lines.io')
    def _compute_io_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    first_child_line = record.child_lines[0]
                    record.io_sample1 = first_child_line.io*1000
                else:
                    record.io_sample1 = 0.0
            else:
                record.io_sample1 = 0.0

    @api.depends('child_lines.io')
    def _compute_io_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    second_child_line = record.child_lines[1]
                    record.io_sample2 = second_child_line.io*1000
                else:
                    record.io_sample2 = 0.0
            else:
                record.io_sample2 = 0.0

    @api.depends('child_lines.io')
    def _compute_io_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    third_child_line = record.child_lines[2]
                    record.io_sample3 = third_child_line.io*1000
                else:
                    record.io_sample3 = 0.0
            else:
                record.io_sample3 = 0.0


    @api.depends('child_lines.i30')
    def _compute_i30_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i30_first_child_line = record.child_lines[0]
                    record.i30_sample1 = i30_first_child_line.i30*1000
                else:
                    record.i30_sample1 = 0.0
            else:
                record.i30_sample1 = 0.0

    @api.depends('child_lines.i30')
    def _compute_i30_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i30_second_child_line = record.child_lines[1]
                    record.i30_sample2 = i30_second_child_line.i30*1000
                else:
                    record.i30_sample2 = 0.0
            else:
                record.i30_sample2 = 0.0

    @api.depends('child_lines.i30')
    def _compute_i30_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i30_third_child_line = record.child_lines[2]
                    record.i30_sample3 = i30_third_child_line.i30*1000
                else:
                    record.i30_sample3 = 0.0
            else:
                record.i30_sample3 = 0.0

    @api.depends('child_lines.i60')
    def _compute_i60_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i60_first_child_line = record.child_lines[0]
                    record.i60_sample1 = i60_first_child_line.i60*1000
                else:
                    record.i60_sample1 = 0.0
            else:
                record.i60_sample1 = 0.0

    @api.depends('child_lines.i60')
    def _compute_i60_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i60_second_child_line = record.child_lines[1]
                    record.i60_sample2 = i60_second_child_line.i60*1000
                else:
                    record.i60_sample2 = 0.0
            else:
                record.i60_sample2 = 0.0

    @api.depends('child_lines.i60')
    def _compute_i60_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i60_third_child_line = record.child_lines[2]
                    record.i60_sample3 = i60_third_child_line.i60*1000
                else:
                    record.i60_sample3 = 0.0
            else:
                record.i60_sample3 = 0.0

    @api.depends('child_lines.i90')
    def _compute_i90_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i90_first_child_line = record.child_lines[0]
                    record.i90_sample1 = i90_first_child_line.i90*1000
                else:
                    record.i90_sample1 = 0.0
            else:
                record.i90_sample1 = 0.0

    @api.depends('child_lines.i90')
    def _compute_i90_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i90_second_child_line = record.child_lines[1]
                    record.i90_sample2 = i90_second_child_line.i90*1000
                else:
                    record.i90_sample2 = 0.0
            else:
                record.i90_sample2 = 0.0

    @api.depends('child_lines.i90')
    def _compute_i90_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i90_third_child_line = record.child_lines[2]
                    record.i90_sample3 = i90_third_child_line.i90*1000
                else:
                    record.i90_sample3 = 0.0
            else:
                record.i90_sample3 = 0.0

    @api.depends('child_lines.i120')
    def _compute_i120_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i120_first_child_line = record.child_lines[0]
                    record.i120_sample1 = i120_first_child_line.i120*1000
                else:
                    record.i120_sample1 = 0.0
            else:
                record.i120_sample1 = 0.0

    @api.depends('child_lines.i120')
    def _compute_i120_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i120_second_child_line = record.child_lines[1]
                    record.i120_sample2 = i120_second_child_line.i120*1000
                else:
                    record.i120_sample2 = 0.0
            else:
                record.i120_sample2 = 0.0

    @api.depends('child_lines.i120')
    def _compute_i120_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i120_third_child_line = record.child_lines[2]
                    record.i120_sample3 = i120_third_child_line.i120*1000
                else:
                    record.i120_sample3 = 0.0
            else:
                record.i120_sample3 = 0.0

    
    @api.depends('child_lines.i150')
    def _compute_i150_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i150_first_child_line = record.child_lines[0]
                    record.i150_sample1 = i150_first_child_line.i150*1000
                else:
                    record.i150_sample1 = 0.0
            else:
                record.i150_sample1 = 0.0

    @api.depends('child_lines.i150')
    def _compute_i150_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i150_second_child_line = record.child_lines[1]
                    record.i150_sample2 = i150_second_child_line.i150*1000
                else:
                    record.i150_sample2 = 0.0
            else:
                record.i150_sample2 = 0.0

    @api.depends('child_lines.i150')
    def _compute_i150_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i150_third_child_line = record.child_lines[2]
                    record.i150_sample3 = i150_third_child_line.i150*1000
                else:
                    record.i150_sample3 = 0.0
            else:
                record.i150_sample3 = 0.0

    @api.depends('child_lines.i180')
    def _compute_i180_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i180_first_child_line = record.child_lines[0]
                    record.i180_sample1 = i180_first_child_line.i180*1000
                else:
                    record.i180_sample1 = 0.0
            else:
                record.i180_sample1 = 0.0

    @api.depends('child_lines.i180')
    def _compute_i180_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i180_second_child_line = record.child_lines[1]
                    record.i180_sample2 = i180_second_child_line.i180*1000
                else:
                    record.i180_sample2 = 0.0
            else:
                record.i180_sample2 = 0.0

    @api.depends('child_lines.i180')
    def _compute_i180_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i180_third_child_line = record.child_lines[2]
                    record.i180_sample3 = i180_third_child_line.i180*1000
                else:
                    record.i180_sample3 = 0.0
            else:
                record.i180_sample3 = 0.0

    @api.depends('child_lines.i210')
    def _compute_i210_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i210_first_child_line = record.child_lines[0]
                    record.i210_sample1 = i210_first_child_line.i210*1000
                else:
                    record.i210_sample1 = 0.0
            else:
                record.i210_sample1 = 0.0

    @api.depends('child_lines.i210')
    def _compute_i210_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i210_second_child_line = record.child_lines[1]
                    record.i210_sample2 = i210_second_child_line.i210*1000
                else:
                    record.i210_sample2 = 0.0
            else:
                record.i210_sample2 = 0.0

    @api.depends('child_lines.i210')
    def _compute_i210_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i210_third_child_line = record.child_lines[2]
                    record.i210_sample3 = i210_third_child_line.i210*1000
                else:
                    record.i210_sample3 = 0.0
            else:
                record.i210_sample3 = 0.0


    @api.depends('child_lines.i240')
    def _compute_i240_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i240_first_child_line = record.child_lines[0]
                    record.i240_sample1 = i240_first_child_line.i240*1000
                else:
                    record.i240_sample1 = 0.0
            else:
                record.i240_sample1 = 0.0

    @api.depends('child_lines.i240')
    def _compute_i240_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i240_second_child_line = record.child_lines[1]
                    record.i240_sample2 = i240_second_child_line.i240*1000
                else:
                    record.i240_sample2 = 0.0
            else:
                record.i240_sample2 = 0.0

    @api.depends('child_lines.i240')
    def _compute_i240_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i240_third_child_line = record.child_lines[2]
                    record.i240_sample3 = i240_third_child_line.i240*1000
                else:
                    record.i240_sample3 = 0.0
            else:
                record.i240_sample3 = 0.0

    
    @api.depends('child_lines.i270')
    def _compute_i270_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i270_first_child_line = record.child_lines[0]
                    record.i270_sample1 = i270_first_child_line.i270*1000
                else:
                    record.i270_sample1 = 0.0
            else:
                record.i270_sample1 = 0.0

    @api.depends('child_lines.i270')
    def _compute_i270_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i270_second_child_line = record.child_lines[1]
                    record.i270_sample2 = i270_second_child_line.i270*1000
                else:
                    record.i270_sample2 = 0.0
            else:
                record.i270_sample2 = 0.0

    @api.depends('child_lines.i270')
    def _compute_i270_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i270_third_child_line = record.child_lines[2]
                    record.i270_sample3 = i270_third_child_line.i270*1000
                else:
                    record.i270_sample3 = 0.0
            else:
                record.i270_sample3 = 0.0

    @api.depends('child_lines.i300')
    def _compute_i300_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i300_first_child_line = record.child_lines[0]
                    record.i300_sample1 = i300_first_child_line.i300*1000
                else:
                    record.i300_sample1 = 0.0
            else:
                record.i300_sample1 = 0.0

    @api.depends('child_lines.i300')
    def _compute_i300_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i300_second_child_line = record.child_lines[1]
                    record.i300_sample2 = i300_second_child_line.i300*1000
                else:
                    record.i300_sample2 = 0.0
            else:
                record.i300_sample2 = 0.0

    @api.depends('child_lines.i300')
    def _compute_i300_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i300_third_child_line = record.child_lines[2]
                    record.i300_sample3 = i300_third_child_line.i300*1000
                else:
                    record.i300_sample3 = 0.0
            else:
                record.i300_sample3 = 0.0

   
    
    @api.depends('child_lines.i330')
    def _compute_sample1_i330(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    sample1_i330_first_child_line = record.child_lines[0]
                    record.sample1_i330 = sample1_i330_first_child_line.i330*1000
                else:
                    record.sample1_i330 = 0.0
            else:
                record.sample1_i330 = 0.0

    @api.depends('child_lines.i330')
    def _compute_sample2_i330(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    sample2_i330_sec_child_line = record.child_lines[1]
                    record.sample2_i330 = sample2_i330_sec_child_line.i330*1000
                else:
                    record.sample2_i330 = 0.0
            else:
                record.sample2_i330 = 0.0

    @api.depends('child_lines.i330')
    def _compute_sample3_i330(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    sample3_i330_third_child_line = record.child_lines[2]
                    record.sample3_i330 = sample3_i330_third_child_line.i330*1000
                else:
                    record.sample3_i330 = 0.0
            else:
                record.sample3_i330 = 0.0


    @api.depends('child_lines.i360')
    def _compute_i360_sample1(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 0:
                    i360_first_child_line = record.child_lines[0]
                    record.i360_sample1 = i360_first_child_line.i360*1000
                else:
                    record.i360_sample1 = 0.0
            else:
                record.i360_sample1 = 0.0

    @api.depends('child_lines.i360')
    def _compute_i360_sample2(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 1:
                    i360_second_child_line = record.child_lines[1]
                    record.i360_sample2 = i360_second_child_line.i360*1000
                else:
                    record.i360_sample2 = 0.0
            else:
                record.i360_sample2 = 0.0

    @api.depends('child_lines.i360')
    def _compute_i360_sample3(self):
        for record in self:
            if record.child_lines:
                if len(record.child_lines) > 2:
                    i360_third_child_line = record.child_lines[2]
                    record.i360_sample3 = i360_third_child_line.i360*1000
                else:
                    record.i360_sample3 = 0.0
            else:
                record.i360_sample3 = 0.0

    


   


    @api.model
    def create(self, vals):
        # import wdb;wdb.set_trace()
        record = super(RcptConcreteCube, self).create(vals)
        record.get_all_fields()
        record.eln_ref.write({'model_id':record.id})
        return record
    

    @api.depends('eln_ref')
    def _compute_sample_parameters(self):
        # records = self.env['lerm.eln'].search([('id','=', record.eln_id.id)]).parameters_result
        # print("records",records)
        # self.sample_parameters = records
        for record in self:
            records = record.eln_ref.parameters_result.parameter.ids
            record.sample_parameters = records
            print("Records",records)

    def get_all_fields(self):
        record = self.env['mechanical.rcpt.concrete.cube'].browse(self.ids[0])
        field_values = {}
        for field_name, field in record._fields.items():
            field_value = record[field_name]
            field_values[field_name] = field_value

        return field_values
    


   

    
class RcptConcreteCubeLine(models.Model):
    _name = "mechanical.rcpt.concrete.cube.line"
    parent_id = fields.Many2one('mechanical.rcpt.concrete.cube',string="Parent Id")
   
    sr_no = fields.Integer(string="Sample No", readonly=True, copy=False, default=1)
    undefined=fields.Float(string="Undefined")
    dia_core = fields.Integer(string="Dia Of Core")
    identification_mark = fields.Char(string="Identification Mark")
    io = fields.Float(string="Io", digits=(16,4))
    i30 = fields.Float(string="I30", digits=(16,4))
    i60 = fields.Float(string="I60", digits=(16,4))
    i90 = fields.Float(string="I90", digits=(16,4))
    i120 = fields.Float(string="I120", digits=(16,4))
    i150 = fields.Float(string="I150", digits=(16,4))
    i180 = fields.Float(string="I180", digits=(16,4))
    i210 = fields.Float(string="I210", digits=(16,4))
    i240 = fields.Float(string="I240", digits=(16,4))
    i270 = fields.Float(string="I270", digits=(16,4))
    i300 = fields.Float(string="I300", digits=(16,4))
    i330 = fields.Float(string="I330", digits=(16,4))
    i360 = fields.Float(string="I360", digits=(16,4))
    qx = fields.Float(string="Qx", compute="_compute_qx", store=True)
    # qs = fields.Float(string="Qs",)
    qs = fields.Float(string="Qs", compute="_compute_qs", store=True)
    # observe_value = fields.Float(string="Observed Sample Value")


    @api.depends(
        "io", "i30", "i60", "i90", "i120", "i150", "i180", "i210", "i240",
        "i270", "i300", "i330", "i360"
    )
    def _compute_qx(self):
        for record in self:
            qx = 900 * (
                record.io
                + 2 * record.i30
                + 2 * record.i60
                + 2 * record.i90
                + 2 * record.i120
                + 2 * record.i150
                + 2 * record.i180
                + 2 * record.i210
                + 2 * record.i240
                + 2 * record.i270
                + 2 * record.i300
                + 2 * record.i330
                + record.i360
            )
            # Round the calculated value to the nearest integer
            record.qx = round(qx)




    
    @api.depends("qx", "dia_core", "undefined")
    def _compute_qs(self):
        for record in self:
            if record.dia_core > 0:
                qs = record.qx * (95 / record.dia_core) ** 2 * record.undefined / 50
                # Round the calculated value to the nearest integer
                record.qs = round(qs)
            else:
                record.qs = 0.0

    

    @api.model
    def create(self, vals):
        # Set the serial_no based on the existing records for the same parent
        if vals.get('parent_id'):
            existing_records = self.search([('parent_id', '=', vals['parent_id'])])
            if existing_records:
                max_serial_no = max(existing_records.mapped('sr_no'))
                vals['sr_no'] = max_serial_no + 1

        return super(RcptConcreteCubeLine, self).create(vals)

    def _reorder_serial_numbers(self):
        # Reorder the serial numbers based on the positions of the records in child_lines
        records = self.sorted('id')
        for index, record in enumerate(records):
            record.sr_no = index + 1