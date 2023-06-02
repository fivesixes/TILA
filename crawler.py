'''
    This is the crawler module (interacts with html only). As seen in the 'Authentication' class the default url maps to the LinkedIn login page as LinkedIn is what this module is primarily for.
    It will be modified for other websites in the future. All dependencies must be installed.
'''

import errors

url = 'https://www.linkedin.com/login'

def signIn(account, **kwargs):
    if account.email == None or account.password == None:
        print(errors.SIGNIN_DETAILS_NOT_PROVIDED)
    else:
        print(url)
        # actual sign-in code goes here