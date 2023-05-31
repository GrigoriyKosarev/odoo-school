# -*- coding: utf-8 -*-
# from odoo import http


# class GkHospital(http.Controller):
#     @http.route('/gk_hospital/gk_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gk_hospital/gk_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gk_hospital.listing', {
#             'root': '/gk_hospital/gk_hospital',
#             'objects': http.request.env['gk_hospital.gk_hospital'].search([]),
#         })

#     @http.route('/gk_hospital/gk_hospital/objects/<model("gk_hospital.gk_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gk_hospital.object', {
#             'object': obj
#         })
