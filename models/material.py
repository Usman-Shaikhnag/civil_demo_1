from odoo import api, fields, models

class Material(models.Model):
    _inherit = "product.template"

    is_sample = fields.Boolean(string="Is Sample?")
    casting_required = fields.Boolean(string="Casting Required")
    is_product_based_calculation = fields.Boolean(string="Product Based Calculation")
    test_parameter = fields.Char("Test Column Title")
    results = fields.Char("Result Column Title")
    specifications = fields.Char("Specifications Column Title")
    unit = fields.Char("Unit Column Title")
    method_reference = fields.Char("Method Reference Column Title")
    result_remark = fields.Char("Results Remark Column Title")
    discipline = fields.Many2one('lerm_civil.discipline',string="Discipline")
    group = fields.Many2one('lerm_civil.group',string="Group")
    test_format_no = fields.Char(string="Test Format No")
    data_sheet_format_no = fields.Many2one('lerm.datasheet.master',string="Data Sheet Format No")
    group_ids = fields.Many2many('lerm_civil.group',string="Group Ids",compute="compute_group_ids")
    # parameter_table = fields.One2many('lerm.parameter.line','parameter_id',string="Parameter")
    size_table = fields.One2many('lerm.size.line','product_id',string="Size")
    qty_table = fields.One2many('lerm.qty.line','product_id',string="Qty")
    grade_table = fields.One2many('lerm.grade.line','product_id',string="Grade")
    alias_table = fields.One2many('lerm.alias.line','product_id',string="Alias")
    datasheet_table = fields.One2many('lerm.material.datasheet.line','product_id',string="Datasheet Table")
    parameter_master_ids = fields.Many2many('lerm.parameter.master',string="Parameter Master IDS",compute="compute_parameter_master_ids")
    parameter_table1 = fields.Many2many('lerm.parameter.master',string="Parameters",)
    volume = fields.Char("Volume")
    lab_name = fields.Char(string="Lab Name")
    product_based_calculation = fields.One2many('lerm.product.based.calculation','product_id',string="Product Based Calculation")
    # discipline2 = fields.One2many('material.discipline.line')


    def name_get(self):
        res = []
        for product in self:
            # print("saa" + str(self.env.context.get('hide_reference')))
            if self.env.context.get('lab_name'):
                # import wdb; wdb.set_trace()
                if product.lab_name:
                    name = product.lab_name
                    print("from lab")
                    print("name" + str(name))
                    res.append((product.id, name))
                else:
                    print("from elsse")
                    name = product.name
                    print("name" + str(name))
                    res.append((product.id, name))
            elif self.env.context.get('main_name'):
                print("from main")
                name = product.name
                print("name" + str(name))
                res.append((product.id, name))
            else:
                print("from elsse")
                name = product.name
                print("name" + str(name))
                res.append((product.id, name))
        return res

    @api.depends('discipline')
    def compute_parameter_master_ids(self):
        for record in self:
            parameter_master_ids = self.env['lerm.parameter.master'].search([('discipline', '=', record.discipline.id)])
            record.parameter_master_ids = parameter_master_ids

    @api.depends('discipline')
    def compute_group_ids(self):
        for record in self:
            # record.group = None
            group_ids = self.env['lerm_civil.group'].search([('discipline', '=', record.discipline.id)])
            record.group_ids = group_ids

class DatasheetLine(models.Model):
    _name = 'lerm.material.datasheet.line'

    product_id = fields.Many2one('product.template',string="Product ID")
    datasheet = fields.Many2one('lerm.datasheet.master',string="Datasheet")

class ParameterMasterAliasLine(models.Model):
    _name = 'lerm.alias.line'

    product_id = fields.Many2one('product.template',string="Parameter Id")
    alias = fields.Char(string="Alias")
    customer = fields.Many2one('res.partner',string="Customer")

# class ParameterLine(models.Model):
#     _name = 'lerm.parameter.line'

#     parameter_id = fields.Many2one('product.template')
#     parameter = fields.Many2one('lerm.parameter.master',string="Parameter")
#     discipline = fields.Many2one('lerm_civil.discipline',readonly=True)
#     parameters_ids = fields.Many2many('lerm.parameter.master',string="Parameters")
    # minimum = fields.Float("min")
    # maximum = fields.Float("max")
    # mu_value = fields.Float("MU Value")
    # specification1 = fields.Char("Specification 1")
    # specification2 = fields.Char("Specifications 2")
    # unit = fields.Char("Unit")
    # test_method = fields.Many2one('lerm_civil.test_method',string="Test Parameter")

    # @api.onchange('parameter')
    # def compute_discipline(self):
    #     for record in self:
    #         self.discipline = self.parameter.discipline

    # @api.depends('discipline')
    # def compute_parameter_ids(self):
    #     for rec in self:
    #         parameters_ids = self.env['lerm.parameter.master'].search(['discipline','=',rec.discipline.id])
    #         rec.parameters_ids = parameters_ids

class SizeLine(models.Model):
    _name = 'lerm.size.line'
    _rec_name = 'size'

    product_id = fields.Many2one('product.template')
    size = fields.Char("Size")

class QtyLine(models.Model):
    _name = 'lerm.qty.line'
    _rec_name = 'qty'
    
    product_id = fields.Many2one('product.template')
    qty = fields.Char("Qty")

class GradeLine(models.Model):
    _name = 'lerm.grade.line'
    _rec_name = 'grade'
    
    product_id = fields.Many2one('product.template')
    grade = fields.Char("Grade")


class ProductBasedCalculation(models.Model):
    _name = 'lerm.product.based.calculation'
    _rec_name = 'grade'
    product_id = fields.Many2one('product.template')
    grade_ids = fields.Many2many("lerm.grade.line",string="Grade IDs",compute="compute_grade_table")
    grade = fields.Many2one("lerm.grade.line",string="Grade")
    main_report_template = fields.Many2one('ir.actions.report',string="Main Report Template")
    datasheet_report_template = fields.Many2one('ir.actions.report',string="DataSheet Report Template")
    ir_model = fields.Many2one('ir.model',string="Model")

    @api.depends('product_id.grade_table')
    def compute_grade_table(self):
        for rec in self:
            table_data = self.env.context.get("grade_table_datas")
            print(self.env.context)
            grade_ids = []
            if table_data:
                for data in table_data:
                    grade_ids.append(data[1])
                print(grade_ids)
                grade_ids = self.env["lerm.grade.line"].search([("id","in",grade_ids)])
                print(grade_ids)
                rec.grade_ids = grade_ids
            else:
                rec.grade_ids = []
                

