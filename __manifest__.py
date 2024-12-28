# -*- coding: utf-8 -*-
# Copyright 2024  Advicts LTD.
# Part of Advicts. See LICENSE file for full copyright and licensing details.
{
    'name': "Advicts Lot in Sale",
    'description': """
       This Module Customize for Al-Jibal Company
       This module adds the ability to select specific lots when adding products to sale orders.
        Features:
        - Add Product button in sale orders
        - Lot selection wizard
        - Automatic lot assignment in delivery orders
    """,
    'summary': """ This Module Customize for Al-Jibal Company to Add products with specific lots to sale orders""",
    'version': "1.0",
    'author': 'GhaithAhmed@Advicts',
    'company': 'Advicts LTD.',
    'website': "https://www.advicts.com",
    'category': 'Sale',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        # security
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
}
