# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Report',
    'summary': 'Report Module used by CLVsol Solutions.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_global_log',
    ],
    'data': [
        'security/report_security.xml',
        'security/ir.model.access.csv',
        'views/abstract_row_view.xml',
        'views/report_view.xml',
        'views/report_log_view.xml',
        'views/report_template_view.xml',
        'views/report_template_log_view.xml',
        'views/report_schedule_view.xml',
        'views/report_schedule_log_view.xml',
        'views/report_batch_view.xml',
        'views/report_batch_log_view.xml',
        'views/report_batch_member_view.xml',
        'views/referenceable_model_view.xml',
        'data/report_batch_member.xml',
        # 'wizard/report_mass_edit_view.xml',
        # 'wizard/report_template_mass_edit_view.xml',
        # 'wizard/report_schedule_mass_edit_view.xml',
        # 'wizard/report_schedule_exec_view.xml',
        # 'wizard/report_batch_exec_view.xml',
        'data/global_log_client.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
