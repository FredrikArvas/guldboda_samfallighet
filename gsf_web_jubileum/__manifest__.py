# -*- coding: utf-8 -*-
{
    'name': 'GSF — Jubileumssida',
    'version': '19.0.1.0.0',
    'summary': 'Jubileumslandningssida för Guldboda Samfällighetsförening',
    'author': 'Arvas International AB',
    'license': 'LGPL-3',
    'depends': [
        'website',
    ],
    'data': [
        'data/res_company_data.xml',
        'data/website_pages.xml',
        'data/website_footer.xml',
        'data/website_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
}
