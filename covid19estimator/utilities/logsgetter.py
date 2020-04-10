def get_logs():
    from covid19estimator.settings import BASE_DIR
    logs = ''
    with open('{}/estimator.logs'.format(BASE_DIR), 'r') as log_file:
        logs = log_file.read()
    return logs
    