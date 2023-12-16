from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
import logging

_logger = logging.getLogger(__name__)



class LermSampleForm(models.Model):
    _name = "lerm.srf.sample"
    _inherit = ['mail.thread','mail.activity.mixin']

    _description = "Sample"
    _rec_name = 'kes_no'

    # ref = fields.Char(string="ULR No.",required=True,readonly=True, default=lambda self: 'New',store=True)
 
    # @api.model
    # def create(self, vals):
    #     discipline = self.env['lerm_civil.discipline'].browse(vals.get('discipline_id'))
    #     if discipline:
    #         lab_cert_no = discipline.lab_c_seq_no
    #         lab_loc = discipline.lab_seq_no
    #         # lab_date = discipline.start_date

    #         # lab_date_str = str(lab_date)
    #         # last_two_digits_year = str(lab_date.year)[-2:]
    #         # lab_date = discipline.start_date
    #         ref = self.env['ir.sequence'].next_by_code('lerm_civil.discipline') or 'New'
    #         ref = ref.replace('(lab_c_seq_no)', lab_cert_no)
    #         # ref = ref.replace('(start_date)', str(lab_date))  # Convert lab_date to string               
    #         ref = ref.replace('(lab_seq_no)', lab_loc)
    #         # ref = ref.replace('(start_date)', last_two_digits_year)

    #         # Update the 'ref' value in the 'vals' dictionary
    #         vals['ref'] = ref

    #     return super(LermSampleForm, self).create(vals)


    # @api.model
    # def create(self, vals):
    #     discipline = self.env['lerm_civil.discipline'].browse(vals.get('discipline_id'))
    #     lab_location = discipline.lab_l_ids and discipline.lab_l_ids[0]  # Assuming there is at least one lab location
    #     if lab_location:
    #         lab_cert_no = str(lab_location.lab_c_no)  # Convert to string
    #         lab_loc = str(lab_location.lab_no)  # Convert to string

    #         ref = self.env['ir.sequence'].next_by_code('lerm_civil.discipline') or 'New'
    #         ref = ref.replace('(lab_c_no)', lab_cert_no)
    #         ref = ref.replace('(lab_no)', lab_loc)

    #         vals['ulr_no'] = ref  # Assign the value to the correct field

    #     return super(LermSampleForm, self).create(vals)
                
    
        
    srf_id = fields.Many2one('lerm.civil.srf' , string="SRF ID" ,tracking=True)
    sample_range_id = fields.Many2one('sample.range.line',string="Sample Range")
    sample_no = fields.Char(string="Sample ID." ,required=True,readonly=True, default=lambda self: 'New')
    casting = fields.Boolean(string="Casting")
    discipline_id = fields.Many2one('lerm_civil.discipline',string="Discipline")
    lab_l_id = fields.Many2one('lab.location', string="Lab Locations",required=True,domain="[('parent_id', '=', discipline_id)]")
    group_id = fields.Many2one('lerm_civil.group',string="Group")
    material_id = fields.Many2one('product.template',string="Material")
    material_id_lab_name = fields.Char(string="Material",compute="compute_material_id_lab_name",store=True)
    ulr_no = fields.Char(string="ULR No." ,required=True,readonly=True, default=lambda self: 'New')
    brand = fields.Char(string="Brand")
    size_id = fields.Many2one('lerm.size.line',string="Size")
    grade_id = fields.Many2one('lerm.grade.line',string="Grade")
    # qty_id = fields.Many2one('lerm.qty.line',string="Quantity")
    sample_qty = fields.Integer(string="Sample Quantity")
    received_by_id = fields.Many2one('res.partner',string="Received By")
    sample_received_date = fields.Date(string="Sample Received Date")
    sample_condition = fields.Selection([
        ('satisfactory', 'Satisfactory'),
        ('non_satisfactory', 'Non-Satisfactory'),
    ], string='Sample Condition', default='satisfactory')
    technicians = fields.Many2one("res.users",string="Technicians",tracking=5)
    location = fields.Char(string="Location")
    sample_reject_reason = fields.Char(string="Sample Reject Reason")
    has_witness = fields.Boolean(string="Witness")
    witness = fields.Char(string="Witness Name")
    scope = fields.Selection([
        ('nabl', 'NABL'),
        ('non_nabl', 'Non-NABL'),
    ], string='Scope', default='nabl')
    sample_description = fields.Text(string="Sample Description")
    group_ids = fields.Many2many('lerm_civil.group',string="Group Ids",compute="compute_group_ids")
    material_ids = fields.Many2many('product.template',string="Material Ids",compute="compute_material_ids")
    size_ids = fields.Many2many('lerm.size.line',string="Size Ids",compute="compute_size_ids")
    grade_ids = fields.Many2many('lerm.grade.line',string="Grade Ids",compute="compute_grade_ids")
    qty_ids = fields.Many2many('lerm.qty.line',string="Qty Ids",compute="compute_qty_ids")
    days_casting = fields.Selection([
        ('3', '3 Days'),
        ('7', '7 Days'),
        ('14', '14 Days'),
        ('28', '28 Days'),
    ], string='Days of casting', default='3')
    date_casting = fields.Date("Date of Casting")
    customer_id = fields.Many2one('res.partner' , string="Customer")
    alias = fields.Char(string="Alias")
    parameters = fields.Many2many('lerm.parameter.master',string="Parameter")
    # parameters_ids = fields.Many2many('lerm.datasheet.line',string="Parameter" , compute="compute_param_ids")
    kes_no = fields.Char("KES No",required=True,readonly=True, default=lambda self: 'New' ,tracking=True)
    casting_date = fields.Date(string="Casting Date")
    client_sample_id = fields.Char(string='Client Sample ID')
    filled_by = fields.Many2one('res.users',string="Filled By")
    check_by = fields.Many2one('res.users',string="Check By")
    approved_by = fields.Many2one('res.users',string="Approved By")
    file_upload = fields.Binary(string="Datasheet Upload")
    report_upload = fields.Binary(string="Report Upload")


    # @api.model
    # def create(self, vals):
    #     # Generate lab_c sequence number during creation
    #     vals['ref'] = self.env['ir.sequence'].next_by_code('ulr.line') or '/'
    #     return super(LermSampleForm, self).create(vals)



    status = fields.Selection([
        ('1-pending', 'Pending'),
        ('2-confirmed', 'Confirmed'),
    ], string='Status', default='1-pending')

    state = fields.Selection([
        ('1-allotment_pending', 'Assignment Pending'),
        ('2-alloted', 'Alloted'),
        ('3-pending_verification','Pending Verification'),
        ('5-pending_approval','Pending Approval'),
        ('4-in_report', 'In-Report'),
    ], string='State',default='1-allotment_pending')
    conformity = fields.Boolean(string="Conformity")
    parameters_result = fields.One2many('sample.parameters.result','sample_id',string="Parameters Result")
    volume = fields.Char(string="Volume")
    product_name = fields.Many2one('product.template',string="Product Name")
    main_name = fields.Char(string="Product Name")
    price = fields.Float(string="Price")
    product_or_form_based = fields.Boolean("Product or Form Based",compute="compute_form_product_based")

    # @api.model
    # def create(self, vals):
    #     sample = super(LermSampleForm, self).create(vals)

    #     # Assuming lab_l_id is a Many2one field in LermSampleForm
    #     lab_location = vals.get('lab_l_id')
    #     if lab_location:
    #         lab_cert_no = str(lab_location.lab_c_no)
    #         lab_loc = str(lab_location.lab_no)

    #         ref = self.env['ir.sequence'].next_by_code('lerm_civil.discipline') or 'New'
    #         ref = ref.replace('(lab_c_no)', lab_cert_no)
    #         ref = ref.replace('(lab_no)', lab_loc)

    #         sample.write({'ulr_no': ref})

    #     return sample
    # @api.model
    # def create(self, vals):
    #     sample = super(LermSampleForm, self).create(vals)

    #     # Assuming lab_l_id is a Many2one field in LermSampleForm
    #     lab_location = vals.get('lab_l_id')
    #     if lab_location:
    #         lab_location = self.env['lab.location'].browse(lab_location[0])  # Assuming you are interested in the first selected location
    #         lab_cert_no = str(lab_location.lab_c_no)
    #         lab_loc = str(lab_location.lab_no)

    #         ref = self.env['ir.sequence'].next_by_code('lerm_civil.discipline') or 'New'
    #         ref = ref.replace('(lab_c_no)', lab_cert_no)
    #         ref = ref.replace('(lab_no)', lab_loc)

    #         sample.write({'ulr_no': ref})

    #     return sample
    
    # @api.model
    # def create(self, vals):
    #     sample = super(LermSampleForm, self).create(vals)

    #     # Assuming lab_l_id is a Many2one field in LermSampleForm
    #     lab_location = self.lab_l_id
    #     if lab_location:
    #         lab_cert_no = str(lab_location.lab_c_no)
    #         lab_loc = str(lab_location.lab_no)

    #         ref = self.env['ir.sequence'].next_by_code('lerm_civil.discipline') or 'New'
    #         ref = ref.replace('(lab_c_no)', lab_cert_no)
    #         ref = ref.replace('(lab_no)', lab_loc)

    #         sample.write({'ulr_no': ref})

    #     return sample


    @api.depends('state')
    def compute_form_product_based(self):
        for record in self:
            record.product_or_form_based = False
            if record.state != '1-allotment_pending':
                eln_id = self.env['lerm.eln'].search([('sample_id','=',self.id)])
                is_product_based = eln_id.is_product_based_calculation
                print("DATA",eln_id.parameters_result)
                is_form_based = eln_id.parameters_result[0].calculation_type == "form_based"

                if is_product_based or is_form_based:
                    record.product_or_form_based = True
                    record.parameters_result.write({'verified':True})
                else:
                    record.product_or_form_based = False
            else:
                record.product_or_form_based = False

    @api.depends('material_id')
    def compute_material_id_lab_name(self):
        for record in self:
            record.material_id_lab_name = record.material_id.lab_name


    def open_form(self):

        eln = self.env['lerm.eln'].search([('sample_id','=',self.id)])
        if self.product_or_form_based:
            if eln.is_product_based_calculation:
                model_record = self.env['lerm.product.based.calculation'].search([('product_id','=',eln.material.id),('grade','=',eln.grade_id.id)])
                model = model_record.ir_model.model
                return {
                        'view_mode': 'form',
                        'res_model': model,
                        'type': 'ir.actions.act_window',
                        'target': 'current',
                        'res_id': eln.model_id,
                        }
            else:
                if eln.parameters_result[0].calculation_type == 'form_based':
                    model = eln.parameters_result[0].parameter.ir_model.model
                    print(model)
                    return {
                        'view_mode': 'form',
                        'res_model': model,
                        'type': 'ir.actions.act_window',
                        'target': 'current',
                        'res_id': eln.parameters_result[0].model_id,
                        }
                    


    def open_related_eln(self):

        #  self.env['lerm.eln'].search()
        # import wdb ; wdb.set_trace()
        # Assuming you want to open a record in the 'res.partner' model
        eln_id = self.env['lerm.eln'].search([('sample_id','=',self.id)]).id  # Replace with the actual ID of the record you want to open

        eln = self.env['lerm.eln'].browse(eln_id)

        if eln:
            # Open the record in a form view
            return {
                'name': eln.eln_id,
                'view_mode': 'form',
                'res_model': 'lerm.eln',
                'res_id': eln.id,
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
        else:
            raise UserError('ELN record not found!')




    @api.onchange('material_id')
    def compute_parameters(self):
        for record in self:
            if record.material_id:
                parameters_ids = []
                product_records = self.env['product.template'].search([('id','=', record.material_id.id)]).parameter_table1
                for rec in product_records:
                    parameters_ids.append(rec.id)
                domain = {'parameters': [('id', 'in', parameters_ids)]}
                return {'domain': domain}
            else:
                domain = {'parameters': [('id', 'in', [])]}
                return {'domain': domain}

    # def open_bulk_allotment_wizard(self):
    #     print("Workign")


    def approve_sample(self):
        for result in self.parameters_result:
            self.check_by = self.env.user
            if not result.verified:
                raise ValidationError("Not all parameters are verified. Please ensure all parameters are verified before proceeding.")
        self.write({'state': '5-pending_approval'})
        # eln = self.env['lerm.eln'].search([('sample_id','=',self.id)])
        # eln.write({'state':'3-approved'})


    def approve_pending_sample(self):
        for result in self.parameters_result:
            self.approved_by = self.env.user
            if not result.verified:
                raise ValidationError("Not all parameters are verified. Please ensure all parameters are verified before proceeding.")
        self.write({'state': '4-in_report'})
        eln = self.env['lerm.eln'].search([('sample_id','=',self.id)])
        approved_by = self.env.user
        eln.write({'state':'3-approved'})


    # def reject_pending_sample(self):
    #     self.write({'state': '2-alloted'})
    #     eln = self.env['lerm.eln'].search([('sample_id','=',self.id)])
    #     eln.write({'state':'1-draft'})



    def reject_sample(self):
        # self.write({'state': '2-alloted'})
        # eln = self.env['lerm.eln'].search([('sample_id','=',self.id)])
        # eln.write({'state':'4-rejected'})

        action = self.env.ref('lerm_civil.sample_reject_wizard')
        return {
            'name': "Reject Sample",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sample.reject.wizard',
            'view_id': action.id,
            'target': 'new'
            }


    def print_datasheet(self):
        eln = self.env["lerm.eln"].search([('sample_id','=', self.id)])
        is_product_based = eln.is_product_based_calculation
        if is_product_based == True:
            template_name = eln.material.product_based_calculation[0].datasheet_report_template.report_name
        else:
            template_name = eln.parameters_result.parameter[0].datasheet_report_template.report_name
        return {
            'type': 'ir.actions.report',
            'report_type': 'qweb-pdf',
            'report_name': template_name,
            'report_file': template_name,
            'data' : {'fromsample' : True}
        }
        
    def print_nabl_report(self):
        inreport = self.state
        eln = self.env["lerm.eln"].search([('sample_id','=', self.id)])
        is_product_based = eln.is_product_based_calculation
        if is_product_based == True:
            template_name = eln.material.product_based_calculation[0].main_report_template.report_name
        else:
            template_name = eln.parameters_result.parameter[0].main_report_template.report_name
        return {
            # 'name':str(self.kes_no),
            'type': 'ir.actions.report',
            'report_type': 'qweb-html',
            'report_name': template_name,
            'report_file': template_name,
            'data' : {'fromsample' : True , 'inreport' : inreport , 'nabl' : True}
        }
    def print_non_nabl_report(self):
        inreport = self.state
        eln = self.env["lerm.eln"].search([('sample_id','=', self.id)])
        is_product_based = eln.is_product_based_calculation
        if is_product_based == True:
            template_name = eln.material.product_based_calculation[0].main_report_template.report_name
        else:
            template_name = eln.parameters_result.parameter[0].main_report_template.report_name
        return {
            'type': 'ir.actions.report',
            'report_type': 'qweb-pdf',
            'report_name': template_name,
            'report_file': template_name,
            'data' : {'fromsample' : True , 'inreport' : inreport , 'nabl' : False}
        }
    # def print_sample_report(self):
    #     eln = self.env["lerm.eln"].search([('sample_id','=', self.id)])
    #     is_product_based = eln.is_product_based_calculation
    #     model_record = eln.material.product_based_calculation.filtered(lambda r: r.grade.id == eln.grade_id.id)
        
    #     if is_product_based:
    #         template_name = model_record.main_report_template.report_name
    #         return {
    #         'type': 'ir.actions.report',
    #         'report_type': 'qweb-pdf',
    #         'report_name': template_name,
    #         'report_file': template_name
    #         }
    #     else:
    #         template_name = eln.parameters_result.parameter[0].main_report_template.report_name
    #         return {
    #         'type': 'ir.actions.report',
    #         'report_type': 'qweb-pdf',
    #         'report_name': template_name,
    #         'report_file': template_name
    #         }



        # sample = self
        # # print(self.kes_no , 'kes no of self')

        # template_name = sample.parameters_result.parameter[0].datasheet_report_template.report_name

        # report = self.env.ref('lerm_civil.sample_report_action')
        # report_action = report.report_action(self)
        # import wdb;wdb.set_trace()
        # Generate the report and retrieve the file content
        # report_data = report.render_qweb_pdf(self.ids)[0]
        # report_name = report.filename

        # Return the report as a file to be downloaded or printed
        # dynamic_part = "sample_report_template"
        # dynamic_part = "10per_fine_coarse_agg_mechanical"

        # report_name = f"lerm_civil.{dynamic_part}"
        
        # return {
        #     'type': 'ir.actions.report',
        #     'report_type': 'qweb-pdf',
        #     'report_name': template_name,
        #     'report_file': template_name
        # }
        # return self.env.ref('lerm_civil.sample_report_action').report_action(self)

    def open_sample_allotment_wizard(self):
        self.filled_by = self.env.user
        action = self.env.ref('lerm_civil.srf_sample_allotment_wizard')
        return {
            'name': "Allot Sample",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sample.allotment.wizard',
            'view_id': action.id,
            'target': 'new'
            }


    # @api.model
    # def create(self, vals):
    #     if vals.get('sample_no', 'New') == 'New' and vals.get('kes_no', 'New') == 'New':
    #         vals['sample_no'] = self.env['ir.sequence'].next_by_code('lerm.srf.sample') or 'New'
    #         vals['kes_no'] = self.env['ir.sequence'].next_by_code('lerm.srf.sample.kes') or 'New'
    #         res = super(LermSampleForm, self).create(vals)
    #         return res


    # @api.depends('material_id')
    # def compute_param_ids(self):
    #     for record in self:
    #         parameters_ids = self.env['lerm.datasheet.line'].search([('datasheet_id','=', record.material_id.data_sheet_format_no.id)])
    #         print("sas",parameters_ids)
    #         record.parameters_ids = parameters_ids
                

    @api.onchange('material_id.casting_required','material_id')
    def onchange_material_id(self):
        for record in self:
            if record.material_id.casting_required:
                record.casting = True
            else:
                record.casting = False

    @api.onchange('material_id.alias' ,'customer_id', 'material_id')
    def onchange_material_id(self):
        for record in self:
            result = self.env['lerm.alias.line'].search([('customer', '=', record.customer_id.id),('product_id', '=', record.material_id.id)])
            record.alias = result.alias



    @api.depends('discipline_id')
    def compute_group_ids(self):
        for record in self:
            group_ids = self.env['lerm_civil.group'].search([('discipline','=', record.discipline_id.id)])
            record.group_ids = group_ids

    @api.depends('discipline_id' , 'group_id')
    def compute_material_ids(self):
        for record in self:
            if record.discipline_id and record.group_id:
                material_ids = self.env['product.template'].search([('discipline','=', record.discipline_id.id) , ('group','=', record.group_id.id)])
                record.material_ids = material_ids
            else:
                record.material_ids = None

    @api.depends('material_id')
    def compute_size_ids(self):
        for record in self:
            if record.material_id:
                size_ids = self.env['lerm.size.line'].search([('product_id','=', record.material_id.id)])
                record.size_ids = size_ids
            else:
                record.size_ids = None

    @api.depends('material_id')
    def compute_grade_ids(self):
        for record in self:
            if record.material_id:
                grade_ids = self.env['lerm.grade.line'].search([('product_id','=', record.material_id.id)])
                record.grade_ids = grade_ids
            else:
                record.grade_ids = None

    @api.depends('material_id')
    def compute_qty_ids(self):
        for record in self:
            if record.material_id:
                qty_ids = self.env['lerm.qty.line'].search([('product_id','=', record.material_id.id)])
                record.qty_ids = qty_ids
            else:
                record.qty_ids = None


class SampleParameter(models.Model):
    _name = "lerm.srf.sample.parameter"
    _description = "Sample Parameter"
    sample_id = fields.Many2one('',string="Sample Id")
    product_id = fields.Many2one('product.template' , string="Product Id")
    paramter = fields.Many2one('lerm.parameter.master' , string="Parameter")


class RejectSampleWizard(models.Model):
    _name = 'sample.reject.wizard'

    sample_id = fields.Many2one('lerm.srf.sample',string="Sample")
    reject_reason = fields.Char('Reject Reason')


    def reject_sample_button(self):
        # return {'type': 'ir.actions.act_window_close'}
        if self.reject_reason:
            sample_id = self.env.context.get('active_id')
            sample = self.env['lerm.srf.sample'].search([('id','=',sample_id)]).write({'state': '2-alloted'})
            eln = self.env['lerm.eln'].search([('sample_id','=',sample_id)])
            eln.write({'state':'4-rejected'})
            eln.message_post(body="<b>Sample Rejected :<b> " + self.reject_reason)

            

            return {'type': 'ir.actions.act_window_close'}
        else:
            raise UserError("Please Specify Reject Reason")

    def close_reject_wizard(self):
        return {'type': 'ir.actions.act_window_close'}


class SampleParametersResult(models.Model):
    _name = 'sample.parameters.result'
    _rec_name = 'parameter'
    sample_id = fields.Many2one('lerm.srf.sample',string="Sample ID")
    parameter = fields.Many2one('lerm.parameter.master',string="Parameter")
    unit = fields.Many2one('uom.uom',string="Unit")
    test_method = fields.Many2one('lerm_civil.test_method',string="Test Method")
    specification = fields.Text(string="Specification")
    verified = fields.Boolean("Verified")
    result = fields.Float(string="Result",digits=(12, 5))