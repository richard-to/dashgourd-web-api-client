from dashgourd.web_api_client import ActionsApi

actions_api = ActionsApi('http://localhost:5000', ('user', 'secret'))
r = actions_api.create_user({'user_id':99999, 'gender':'Male'})
print r.headers
print r.status_code