# -*- coding: utf-8 -*-
{
    'name': 'GSF — Webbplats',
    'version': '19.0.1.0.0',
    'summary': 'Startsida och styrelselista för Guldboda Samfällighetsförening',
    'author': 'Arvas International AB',
    'website': 'https://github.com/FredrikArvas/guldboda_samfallighet/tree/19.0/gsf_web',
    'license': 'LGPL-3',
    'depends': [
        'website',
    ],
    'data': [
        'data/res_company_data.xml',
        'data/website_pages.xml',
        'data/website_footer.xml',
        'data/website_contactus.xml',
        'data/website_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
}
