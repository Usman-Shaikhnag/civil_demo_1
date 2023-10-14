from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
import math


class MechanicalBricks(models.Model):
    _name = "mechanical.bricks"
    _inherit = "lerm.eln"
    _rec_name = "name"

    grade = fields.Many2one('lerm.grade.line',string="Grade",compute="_compute_grade_id",store=True)
    name = fields.Char("Name",default="Brick")
    parameter_id = fields.Many2one('eln.parameters.result',string="Parameter")
    sample_parameters = fields.Many2many('lerm.parameter.master',string="Parameters",compute="_compute_sample_parameters",store=True)
    eln_ref = fields.Many2one('lerm.eln',string="Eln")
    # child_lines = fields.One2many('mechanical.water.absorption.bricks.line','parent_id',string="Parameter")
    test_start_date = fields.Date("Test Start Date")
    test_end_date = fields.Date("Test End Date")
   

        #1------------ Compressive Strength

    compressive_strength_visible = fields.Boolean("Compressive Strengt Visible",compute="_compute_visible")
    compressive_strength_name = fields.Char("Name",default="Compressive Strength")
    length = fields.Float(string="Length mm")
    length_2 = fields.Float(string="Length mm")
    length_3 = fields.Float(string="Length mm")
    length_4 = fields.Float(string="Length mm")
    length_5 = fields.Float(string="Length mm")
    width = fields.Float(string="Width mm")
    width_2 = fields.Float(string="Width mm")
    width_3 = fields.Float(string="Width mm")
    width_4 = fields.Float(string="Width mm")
    width_5 = fields.Float(string="Width mm")
    height = fields.Float(string="Height mm")
    height_2 = fields.Float(string="Height mm")
    height_3 = fields.Float(string="Height mm")
    height_4 = fields.Float(string="Height mm")
    height_5 = fields.Float(string="Height mm")
    area = fields.Float(string="Area (mm²)", digits=(12,4),compute="_compute_area")
    area_2 = fields.Float(string="Area (mm²)", digits=(12,4),compute="_compute_area_2")
    area_3 = fields.Float(string="Area (mm²)", digits=(12,4),compute="_compute_area_3")
    area_4 = fields.Float(string="Area (mm²)", digits=(12,4),compute="_compute_area_4")
    area_5 = fields.Float(string="Area (mm²)", digits=(12,4),compute="_compute_area_5")
    load = fields.Float(string=" Load in, KN", digits=(12,1))
    load_2 = fields.Float(string=" Load in, KN", digits=(12,1))
    load_3 = fields.Float(string=" Load in, KN", digits=(12,1))
    load_4 = fields.Float(string=" Load in, KN", digits=(12,1))
    load_5 = fields.Float(string=" Load in, KN", digits=(12,1))
    comp_strength_1 = fields.Float(string="Compressive strength MPa",compute="_compute_comp_strength_1")
    comp_strength_2 = fields.Float(string="Compressive strength MPa",compute="_compute_comp_strength_2")
    comp_strength_3 = fields.Float(string="Compressive strength MPa",compute="_compute_comp_strength_3")
    comp_strength_4 = fields.Float(string="Compressive strength MPa",compute="_compute_comp_strength_4")
    comp_strength_5 = fields.Float(string="Compressive strength MPa",compute="_compute_comp_strength_5")
    
    avrg_compressive_strength = fields.Float(string="Average Compressive Strength",compute="_compute_avrg_compressive_strength")

    

    

    @api.depends('comp_strength_1', 'comp_strength_2', 'comp_strength_3', 'comp_strength_4', 'comp_strength_5')
    def _compute_avrg_compressive_strength(self):
        for record in self:
            comp_strength_1 = [
                record.comp_strength_1,
                record.comp_strength_2,
                record.comp_strength_3,
                record.comp_strength_4,
                record.comp_strength_5,
            ]
            # Filter out None values and calculate the average
            non_empty_strengths = [strength for strength in comp_strength_1 if strength is not None]
            if non_empty_strengths:
                average_strength = sum(non_empty_strengths) / len(non_empty_strengths)
            else:
                average_strength = 0.0
            record.avrg_compressive_strength = average_strength

      
    @api.depends('length', 'width')
    def _compute_area(self):
        for record in self:
            record.area = record.length * record.width

    @api.depends('length_2', 'width_2')
    def _compute_area_2(self):
        for record in self:
            record.area_2 = record.length_2 * record.width_2

    @api.depends('length_3', 'width_3')
    def _compute_area_3(self):
        for record in self:
            record.area_3 = record.length_3 * record.width_3

    @api.depends('length_4', 'width_4')
    def _compute_area_4(self):
        for record in self:
            record.area_4 = record.length_4 * record.width_4

    @api.depends('length_5', 'width_5')
    def _compute_area_5(self):
        for record in self:
            record.area_5 = record.length_5 * record.width_5

    @api.depends('load', 'area')
    def _compute_comp_strength_1(self):
        for record in self:
            if record.area != 0:
                record.comp_strength_1 = record.load / record.area * 1000
            else:
                record.comp_strength_1 = 0.0
    
    @api.depends('load_2', 'area_2')
    def _compute_comp_strength_2(self):
        for record in self:
            if record.area_2 != 0:
                record.comp_strength_2 = record.load_2 / record.area_2 * 1000
            else:
                record.comp_strength_2 = 0.0

    @api.depends('load_3', 'area_3')
    def _compute_comp_strength_3(self):
        for record in self:
            if record.area_3 != 0:
                record.comp_strength_3 = record.load_3 / record.area_3 * 1000
            else:
                record.comp_strength_3 = 0.0

    @api.depends('load_4', 'area_4')
    def _compute_comp_strength_4(self):
        for record in self:
            if record.area_4 != 0:
                record.comp_strength_4 = record.load_4 / record.area_4 * 1000
            else:
                record.comp_strength_4 = 0.0

    @api.depends('load_5', 'area_5')
    def _compute_comp_strength_5(self):
        for record in self:
            if record.area_5 != 0:
                record.comp_strength_5 = record.load_5 / record.area_5 * 1000
            else:
                record.comp_strength_5 = 0.0

    


        #-2---------- Visual Observation

    visual_observation_name = fields.Char("Name",default="Efflorence")
    visual_observation_1 = fields.Selection([('like', 'Like'), ('nil', 'Nil'), ('slight', 'Slight'), ('moderate', 'Moderate'), ('heavy', 'Heavy'), ('serious', 'Serious')],string='Visual observation')
    visual_observation_2 = fields.Selection([('like', 'Like'), ('nil', 'Nil'), ('slight', 'Slight'), ('moderate', 'Moderate'), ('heavy', 'Heavy'), ('serious', 'Serious')],string='Visual observation')
    visual_observation_3 = fields.Selection([('like', 'Like'), ('nil', 'Nil'), ('slight', 'Slight'), ('moderate', 'Moderate'), ('heavy', 'Heavy'), ('serious', 'Serious')],string='Visual observation')
    visual_observation_4 = fields.Selection([('like', 'Like'), ('nil', 'Nil'), ('slight', 'Slight'), ('moderate', 'Moderate'), ('heavy', 'Heavy'), ('serious', 'Serious')],string='Visual observation')
    visual_observation_5 = fields.Selection([('like', 'Like'), ('nil', 'Nil'), ('slight', 'Slight'), ('moderate', 'Moderate'), ('heavy', 'Heavy'), ('serious', 'Serious')],string='Visual observation')


         #-3----------  Dimension As per IS: IS : 1077 -1992 

    dimension_name = fields.Char("Name",default="Dimension")
    avrg_length = fields.Float(string="Average length", compute="_compute_avrg_length")
    avrg_width = fields.Float(string="Average Width", compute="_compute_avrg_width")
    avrg_height = fields.Float(string="Average Height", compute="_compute_avrg_height")

    @api.depends('length', 'length_2', 'length_3', 'length_4', 'length_5')
    def _compute_avrg_length(self):
        for record in self:
            lengths = [
                record.length,
                record.length_2,
                record.length_3,
                record.length_4,
                record.length_5,
            ]
            # Filter out None values and calculate the average
            non_empty_lengths = [length for length in lengths if length is not None]
            if non_empty_lengths:
                average_length = sum(non_empty_lengths) / len(non_empty_lengths)
            else:
                average_length = 0.0
            record.avrg_length = average_length


    @api.depends('width', 'width_2', 'width_3', 'width_4', 'width_5')
    def _compute_avrg_width(self):
        for record in self:
            widths = [
                record.width,
                record.width_2,
                record.width_3,
                record.width_4,
                record.width_5,
            ]
            # Filter out None values and calculate the average
            non_empty_widths = [width for width in widths if width is not None]
            if non_empty_widths:
                average_width = sum(non_empty_widths) / len(non_empty_widths)
            else:
                average_width = 0.0
            record.avrg_width = average_width

    @api.depends('height', 'height_2', 'height_3', 'height_4', 'height_5')
    def _compute_avrg_height(self):
        for record in self:
            heights = [
                record.height,
                record.height_2,
                record.height_3,
                record.height_4,
                record.height_5,
            ]
            # Filter out None values and calculate the average
            non_empty_heights = [height for height in heights if height is not None]
            if non_empty_heights:
                average_height = sum(non_empty_heights) / len(non_empty_heights)
            else:
                average_height = 0.0
            record.avrg_height = average_height


    #-4--------------  Water Absorption

    water_absorbtion_visible = fields.Boolean("Water Absorption Visible",compute="_compute_visible")
    wt_absorption_name = fields.Char("Name",default="Water Absorption")
    initial_wt = fields.Float(string="Initial wt after 24 hr emersion water")
    initial_wt_2 = fields.Float(string="Initial wt after 24 hr emersion water")
    initial_wt_3 = fields.Float(string="Initial wt after 24 hr emersion water")
    initial_wt_4 = fields.Float(string="Initial wt after 24 hr emersion water")
    initial_wt_5 = fields.Float(string="Initial wt after 24 hr emersion water")
    final_wt = fields.Float(string="Final wt after 24 hr oven")
    final_wt_2 = fields.Float(string="Final wt after 24 hr oven")
    final_wt_3 = fields.Float(string="Final wt after 24 hr oven")
    final_wt_4 = fields.Float(string="Final wt after 24 hr oven")
    final_wt_5 = fields.Float(string="Final wt after 24 hr oven")
    water_absorption = fields.Float(string="Water Absorption %", compute="_compute_water_absorption")
    water_absorption_2 = fields.Float(string="Water Absorption %", compute="_compute_water_absorption_2")
    water_absorption_3 = fields.Float(string="Water Absorption %", compute="_compute_water_absorption_3")
    water_absorption_4 = fields.Float(string="Water Absorption %", compute="_compute_water_absorption_4")
    water_absorption_5 = fields.Float(string="Water Absorption %", compute="_compute_water_absorption_5")
    avrg_water_absorption = fields.Float(string="Average Water Absorption, %", compute="_compute_avrg_water_absorption")

    @api.depends('water_absorption', 'water_absorption_2', 'water_absorption_3', 'water_absorption_4', 'water_absorption_5')
    def _compute_avrg_water_absorption(self):
        for record in self:
            total_absorption = (
                record.water_absorption +
                record.water_absorption_2 +
                record.water_absorption_3 +
                record.water_absorption_4 +
                record.water_absorption_5
            )
            num_entries = sum(1 for field in [
                record.water_absorption,
                record.water_absorption_2,
                record.water_absorption_3,
                record.water_absorption_4,
                record.water_absorption_5
            ] if field)
            if num_entries > 0:
                record.avrg_water_absorption = total_absorption / num_entries
            else:
                record.avrg_water_absorption = 0.0

    @api.depends('initial_wt' , 'final_wt')
    def _compute_water_absorption(self):
        for record in self:
            if record.final_wt != 0:
                record.water_absorption = (record.initial_wt - record.final_wt) / record.final_wt * 100
            else:
                record.water_absorption = 0

    @api.depends('initial_wt_2' , 'final_wt_2')
    def _compute_water_absorption_2(self):
        for record in self:
            if record.final_wt_2 != 0:
                record.water_absorption_2 = (record.initial_wt_2 - record.final_wt_2) / record.final_wt_2 * 100
            else:
                record.water_absorption_2 = 0

    @api.depends('initial_wt_3' , 'final_wt_3')
    def _compute_water_absorption_3(self):
        for record in self:
            if record.final_wt_3 != 0:
                record.water_absorption_3 = (record.initial_wt_3 - record.final_wt_3) / record.final_wt_3 * 100
            else:
                record.water_absorption_3 = 0

    @api.depends('initial_wt_4' , 'final_wt_4')
    def _compute_water_absorption_4(self):
        for record in self:
            if record.final_wt_4 != 0:
                record.water_absorption_4 = (record.initial_wt_4 - record.final_wt_4) / record.final_wt_4 * 100
            else:
                record.water_absorption_4 = 0

    @api.depends('initial_wt_5' , 'final_wt_5')
    def _compute_water_absorption_5(self):
        for record in self:
            if record.final_wt_5 != 0:
                record.water_absorption_5 = (record.initial_wt_5 - record.final_wt_5) / record.final_wt_5 * 100
            else:
                record.water_absorption_5 = 0

    confirmity = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ], string='Confirmity', default='fail')


    ### Compute Visible
    @api.depends('sample_parameters')
    def _compute_visible(self):
        
        for record in self:
            record.compressive_strength_visible = False
            record.water_absorbtion_visible = False

            for sample in record.sample_parameters:
                print("Internal Ids",sample.internal_id)
                if sample.internal_id == "b0eecb4f-9287-48c7-a607-bf1b64a8115d":
                    record.compressive_strength_visible = True
                if sample.internal_id == "537e20c5-f3ab-4b19-af25-91a4671baf5f":
                    record.water_absorbtion_visible = True 
    # In Brick Form total 4 parameter But 2 parameters Visual Observation and Dimension are depend on Compressive Strength
    # so visible condition only taked on Compressive Strength. 

    

    @api.model
    def create(self, vals):
        # import wdb;wdb.set_trace()
        record = super(MechanicalBricks, self).create(vals)
        record.get_all_fields()
        record.eln_ref.write({'model_id':record.id})
        return record

    @api.depends('eln_ref')
    def _compute_grade_id(self):
        if self.eln_ref:
            self.grade = self.eln_ref.grade_id.id
    

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
        record = self.env['mechanical.bricks'].browse(self.ids[0])
        field_values = {}
        for field_name, field in record._fields.items():
            field_value = record[field_name]
            field_values[field_name] = field_value

        return field_values