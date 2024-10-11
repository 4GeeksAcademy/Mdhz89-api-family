from flask import jsonify

class APIException(Exception):
    status_code = 400

    def to_dict(self):
        return {'message': str(self)}

def generate_sitemap(app):
    routes = [str(rule) for rule in app.url_map.iter_rules()]
    return jsonify(routes)
