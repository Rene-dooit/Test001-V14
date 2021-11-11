# -*- coding: utf-8 -*-
from odoo import http


class MyModule(http.Controller):
    @http.route('/my_module/my_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

  
    @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_module.object', {
            'object': obj
        })
