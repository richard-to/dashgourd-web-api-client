import json
import requests

class ActionsApi(object):
    """Client for managing users/actions through example web api
    
    Attributes:
        base_url: Base url.
        auth: Tuple with user and pass. Used for basic auth.
    """
    
    def __init__(self, base_url, auth=None):
        
        self.auth = auth
        self.headers = {'content-type': 'application/json'}
        self.base_url = base_url 
        self.endpoints = {
            'create_users': "{}{}".format(base_url, '/users'),
            'create_users_actions': "{}{}".format(base_url, '/users/{user_id}/actions'),
            'create_users_abtests': "{}{}".format(base_url, '/users/{user_id}/abtests'),
        }
       
    def create_user(self, data):
        """Creates a new user in DashGourd through web api
        
        See equivalent method in actions api for more information.
        
        Args:
            data: Dict that contains at least an `user_id` key
        """
         
        if 'user_id' in data:
            url = self.endpoints['create_users']
            payload = {'data':data}
            return requests.post(url, data=json.dumps(payload), 
                headers=self.headers, auth=self.auth)
                       
    def insert_action(self, user_id, data):
        """Logs a user action through web api
        
        See equivalent method in actions api for more information.
        
        `created_at` is the date the action ocurred.
        
        
        Args:
            user_id: Id of user
            data: Dict that contains at least `name`, and `created_at` keys
        """        
        
        if ('name' in data and 
            'created_at' in data):
            url = self.endpoints['create_users_actions'].format(user_id=user_id)
            payload = {'data':data}
            return requests.post(url, data=json.dumps(payload), 
                headers=self.headers, auth=self.auth)
    
    def tag_abtest(self, user_id, data): 
        """Tags as a user as being part of an ab test through web api
        
        See equivalent method in ab test api for more information.
        
        Args:
            user_id: User id of user
            data: Dict that contains `abtest` `variation`
        """
        
        if ('abtest' in data and 
            'variation' in data):
            url = self.endpoints['create_users_abtests'].format(user_id=user_id)
            payload = {'data':data}
            return requests.post(url, data=json.dumps(payload), 
                headers=self.headers, auth=self.auth)       