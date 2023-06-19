{
    'name': "gk_hospital",

    'summary': """
        Odoo-school. Module 'Hospital'
        """,

    'author':  "grigoriykosarev@gmail.com",

    'category': 'Customizations',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menu.xml',
        'views/disease_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/patient_visit_views.xml',
    ],

    'installable': True,
    'auto_install': False,

    'demo': [
        'data/disease_demo.xml',
    ],
}
