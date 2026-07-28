# -*- coding: utf-8 -*-
import re
import base64
from odoo.tools import file_open


def _fix_header(env):
    view = env['ir.ui.view'].search([('key', '=', 'website.header_text_element')], limit=1)
    if not view:
        return
    new_arch = (
        view.arch_db
        .replace('+1 555-555-5556', '')
        .replace('tel:+1 555-555-5556', 'tel:')
        .replace('info@yourcompany.example.com', 'info@guldboda.se')
    )
    if new_arch != view.arch_db:
        view.write({'arch_db': new_arch})


def post_init_hook(env):
    our_page = env.ref('gsf_web_jubileum.page_gsf_jubileum_home', raise_if_not_found=False)
    if our_page:
        competing = env['website.page'].search([
            ('url', '=', '/'),
            ('id', '!=', our_page.id),
            ('website_id', '=', our_page.website_id.id),
        ])
        if competing:
            competing.write({'url': '/home-default', 'is_published': False})

    with file_open('gsf_web_jubileum/static/img/company_logo.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode()
    env['website'].browse(1).logo = logo_b64

    env['res.company'].browse(1).write({'phone': False})

    _fix_header(env)
