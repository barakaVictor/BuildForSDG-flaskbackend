import json
from flask import request, jsonify, Response, render_template, abort
from flask.views import MethodView
from covid19estimator.api import api_bp
from covid19estimator.utilities.jsonxml import json_to_xml
from covid19estimator.utilities.estimator import estimator
from covid19estimator.utilities.logsgetter import get_logs

class CovidImpactEstimator(MethodView):

    accepted_formats = ['json', 'xml']

    def get(self, resource):
        if resource and resource == 'logs':
            return get_logs()
        else:
            abort(404, description="Resource not found")

    def post(self, data_format):
        output = estimator(request.get_json(force=True))
        if data_format and data_format == "xml" :
            return Response(json_to_xml(output), mimetype='application/xml')
        return jsonify(output)

view = CovidImpactEstimator.as_view('estimator')
api_bp.add_url_rule("/v1/on-covid-19/<string:resource>", view_func=view, methods=['GET'])
api_bp.add_url_rule("/v1/on-covid-19", defaults={'data_format': None }, view_func=view, methods=['POST'])
api_bp.add_url_rule("/v1/on-covid-19/<string:data_format>", view_func=view, methods=['POST'])
