# -*- coding: utf-8 -*-
# from odoo import http


# class GkLibrary(http.Controller):
#     @http.route('/gk_library/gk_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gk_library/gk_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gk_library.listing', {
#             'root': '/gk_library/gk_library',
#             'objects': http.request.env['gk_library.gk_library'].search([]),
#         })

#     @http.route('/gk_library/gk_library/objects/<model("gk_library.gk_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gk_library.object', {
#             'object': obj
#         })
