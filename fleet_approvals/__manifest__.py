# -*- coding: utf-8 -*-
{
    'name': "Fleet Approvals",


    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Approvals',
    'version': '16.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','approvals', 'fleet'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/fleet_vehicle.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}