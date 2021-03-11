from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    def index(self):
        return "Hello"

    @http.route('/academy/test1/', auth='public', website=True)
    def index2(self):
        return '<h1>test</h1>'

    @http.route('/academy/<int:id>/', auth='public', website=True)
    def teacher(self, id):
        return '<h1> ({})</h1>'.format(id, type(id).__name__)

    @http.route('/academy/academy2/', auth='public')
    def index3(self, **kw):
        return http.request.render('openacademy.index', {
            'teachers': ["Ned Stark"],
        })

    @http.route('/academy/<model("openacademy.session"):partner>/', auth='public', website=True)
    def teacher2(self, partner):
        return http.request.render('openacademy.biography', {
            'person': partner
        })

    @http.route('/academy/academy3/', auth='public')
    def index(self, **kw):
        Teachers = http.request.env['openacademy.session']
        return http.request.render('openacademy.index2', {
            'teachers': Teachers.search([])
        })
