import json
from flask import request, jsonify, Response, render_template, abort
from covid19estimator.api import api_bp
from covid19estimator.utilities.jsonxml import json_to_xml
from covid19estimator.utilities.estimator import estimator
from covid19estimator.utilities.logsgetter import get_logs


@api_bp.route("/v1/on-covid-19", defaults={"output_format": None}, methods=('POST', 'GET'))
@api_bp.route("/v1/on-covid-19/<string:output_format>", methods=('POST', 'GET'))
def estimate(output_format):
    if request.method == "POST":
        output = estimator(request.get_json(force=True))
        if output_format and output_format == 'xml':
            return Response(json_to_xml(output), mimetype='application/xml')
        return jsonify(output)
    
    elif output_format and output_format == 'logs':
        return get_logs()
    else:
        abort(404, description="Resource not found")


