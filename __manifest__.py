{
    'name': 'HMS',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/patient_view.xml',
        'views/patient_log_view.xml',
        'views/department_view.xml',
        'views/doctors_view.xml',
        'views/res_partner_view.xml',
        'reports/patient_report.xml',
        'reports/patient_report_template.xml',
    ],
    'application': True,
}