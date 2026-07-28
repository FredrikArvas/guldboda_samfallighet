# -*- coding: utf-8 -*-
import re
import base64
from odoo.tools import file_open

_GSF_CONTACT_BLOCK = (
    '<div class="col-lg-4 offset-lg-1 mt-4 mt-lg-0">'
    '<h5 style="color:#192A3D;border-bottom:2px solid #1559ED;padding-bottom:8px;margin-bottom:12px;">'
    'Guldboda Samfällighetsförening</h5>'
    '<ul class="list-unstyled mb-0 ps-2" style="color:#3A4F66;">'
    '<li class="mb-2"><i class="fa fa-map-marker fa-fw me-2" style="color:#1559ED;"/>'
    '<span>c/o Franzéns Redovisningsbyrå, 134 34 Gustavsberg</span></li>'
    '<li class="mb-2"><i class="fa fa-envelope fa-fw me-2" style="color:#1559ED;"/>'
    '<a href="mailto:info@guldboda.se" style="color:#3A4F66;">info@guldboda.se</a></li>'
    '<li class="mb-2"><i class="fa fa-envelope fa-fw me-2" style="color:#1559ED;"/>'
    '<a href="mailto:kassor@guldboda.se" style="color:#3A4F66;">kassor@guldboda.se</a></li>'
    '<li><i class="fa fa-envelope fa-fw me-2" style="color:#1559ED;"/>'
    '<a href="mailto:styrelsen@guldboda.se" style="color:#3A4F66;">styrelsen@guldboda.se</a></li>'
    '</ul></div>'
)


def _fix_contactus(env):
    view = env['ir.ui.view'].search([('key', '=', 'website.contactus')], limit=1)
    if not view:
        return
    new_arch = re.sub(
        r'<div class="col-lg-4 offset-lg-1[^"]*">.*?<h5>My Company</h5>.*?</ul>\s*</div>',
        _GSF_CONTACT_BLOCK,
        view.arch_db,
        flags=re.DOTALL,
    )
    if new_arch != view.arch_db:
        view.write({'arch_db': new_arch})


def post_init_hook(env):
    our_page = env.ref('gsf_web.page_gsf_home', raise_if_not_found=False)
    if our_page:
        competing = env['website.page'].search([
            ('url', '=', '/'),
            ('id', '!=', our_page.id),
            ('website_id', '=', our_page.website_id.id),
        ])
        if competing:
            competing.write({'url': '/home-default', 'is_published': False})

    with file_open('gsf_web/static/img/company_logo.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode()
    env['website'].browse(1).logo = logo_b64

    _fix_contactus(env)
