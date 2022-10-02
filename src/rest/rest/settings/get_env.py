import os, json

def get_environment_variables(environment='local'):
    if environment.lower() in ['local']:
        with open(os.path.join(os.path.abspath(os.path.dirname(__name__)), 'rest/settings/env_vars.json')) as env_vars:
            env_vars = json.load(env_vars)
        return env_vars