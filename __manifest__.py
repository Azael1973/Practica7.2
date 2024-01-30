# -*- coding: utf-8 -*-
{
    'name': "Libreria",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	'views/libreria_views.xml',
    ],
    'installable': True,
    'application': True,
}

