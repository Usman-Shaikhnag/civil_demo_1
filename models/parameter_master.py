from odoo import models, fields ,api

class ParameterMaster(models.Model):
    _name = 'lerm.parameter.master'
    _rec_name = 'parameter_name'

    parameter_name = fields.Char(string="Parameter Name")
    lab_min_value = fields.Float(string="Lab min Value")
    lab_max_value = fields.Float(string="Lab max Value")
    nabl_min_value = fields.Float(string="Nabl min value")
    nabl_max_value = fields.Float(string="Nabl max value")
    client_min_value = fields.Float(string="Client min Value")
    client_max_value = fields.Float(string="Client max Value")
    mu_value = fields.Float(string="Mu Value")
    unit = fields.Many2one('uom.uom',string="Unit")
    calculated = fields.Boolean("Pseudo Parameter")
    test_method = fields.Many2one('lerm_civil.test_method',string="Test Method")
    discipline = fields.Many2one('lerm_civil.discipline',string="Discipline")
    nabl_select = fields.Selection([('nabl', 'NABL'), ('non_nabl', 'Non NABL')], string='NABL')
    spreadsheet_template = fields.Many2one("spreadsheet.template",string="Spreadsheet Template")
    sheets = fields.Char("Sheet Name")
    cell = fields.Char("Result Cell")
    group = fields.Many2one('lerm_civil.group',string="Group")
    parameter_table = fields.One2many('lerm.parameter.master.table','parameter_id',string="Material Table")
    dependent_inputs = fields.One2many("lerm.dependent.inputs","parameter_id",string="Inputs")
    formula = fields.Text("Formula")
    material = fields.Many2one('product.template',string="Material")
    

    def name_get(self):
        res = []
        for parameter in self:
            # import wdb;wdb.set_trace();
            
            if parameter.test_method.test_method and self.env.context.get('test_method') :

                name = parameter.parameter_name+":"+parameter.test_method.test_method
            else:
                name = parameter.parameter_name
            res.append((parameter.id, name))
        return res

    def fetch_dependent_parameters_recursive(self, depth=1):
        parameters = []

        def recursive_fetch(record, curr_depth):
            nonlocal parameters
            if curr_depth <= 0:
                return

            for input_record in record.dependent_inputs:
                if input_record.is_parameter_dependent:
                    parameters.append(input_record.parameter)
                    recursive_fetch(input_record.parameter, curr_depth - 1)

        recursive_fetch(self, depth)

        return parameters




class DependentInputs(models.Model):
    _name = 'lerm.dependent.inputs'
    _rec_name = 'label'
    parameter_id =  fields.Many2one('lerm.parameter.master',string="Parameters")
    is_parameter_dependent = fields.Boolean("Dependent Parameter")
    identifier = fields.Char(string="Identifier")
    label = fields.Char(string="Label")
    decimal_place = fields.Integer(string="Decimal Place")
    parameter = fields.Many2one("lerm.parameter.master",string="Parameter")
    default = fields.Float(string='Default')






class ParameterMaster(models.Model):
    _name = 'lerm.parameter.master.table'

    parameter_id = fields.Many2one('lerm.parameter.master',string="Material Table")
    material = fields.Many2one('product.template' , string="Material")
    grade = fields.Many2one('lerm.grade.line' , string="Grade")
    grade_ids = fields.Many2many('lerm.grade.line',string="Grades")
    size = fields.Many2one('lerm.size.line' , string="Size")
    size_ids = fields.Many2many('lerm.size.line',string="Size")
    specification = fields.Char(string="Specification")
    req_max = fields.Float(string="Req Max")
    req_min = fields.Float(string="Req Min")
    material_ids = fields.Many2many('product.template',string="Material Ids")

    @api.onchange('material')
    def compute_grade(self):
        for record in self:
            if record.material:
                record.grade_ids = self.env['product.template'].search([('id','=', record.material.id)]).grade_table
                
    @api.onchange('material')
    def compute_size(self):
        for record in self:
            if record.material:
                record.size_ids = self.env['product.template'].search([('id','=', record.material.id)]).size_table