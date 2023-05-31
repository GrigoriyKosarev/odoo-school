# -*- coding: utf-8 -*-
{
    'name': "gk_hospital",

    'summary': """
        Odoo-school. Module 'Hospital'
        """,

    'description': """
        Odoo-school. Module 'Hospital'
        """,

    'author':  "grigoriykosarev@gmail.com",
    'website': "grigoriykosarev@gmail.com",

    'category': 'Customizations',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'auto_install': False,

    'demo': [
    ],
}
