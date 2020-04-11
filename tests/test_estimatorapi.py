import json
dummydata = json.dumps(
    {
        "region": {
            "name": "Africa",
            "avgAge": 19.7,
            "avgDailyIncomeInUSD": 5,
            "avgDailyIncomePopulation": 0.71
        },
        "periodType": "days",
        "timeToElapse": 58,
        "reportedCases": 674,
        "population": 66622705,
        "totalHospitalBeds": 1380614
    }
) 
def test_noformat_route(client, app):
    response = client.post("/api/v1/on-covid-19/json", data=dummydata)
    assert response.status_code == 200

def test_json_route(client, app):
    response = client.post("/api/v1/on-covid-19/json", data=dummydata)
    assert response.status_code == 200

def test_xml_route(client, app):
    response = client.post("/api/v1/on-covid-19/xml", data=dummydata)
    assert response.status_code == 200

def test_logs_route(client, app):
    response = client.get("/api/v1/on-covid-19/logs")
    assert response.status_code == 200