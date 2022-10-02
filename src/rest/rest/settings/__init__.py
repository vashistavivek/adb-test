import os

environment_name = os.environ.get('CURRENT_ENV', 'LOCAL').lower()

print("Current Environment :", environment_name)

if environment_name == 'staging':
    from .staging import *

elif environment_name == 'production':
    from .production import *

else:
    from .local import *
