'''
    This is the crawler module (interacts with html only). As seen in the 'Authentication' class the default url maps to the LinkedIn login page as LinkedIn is what this module is primarily for.
    It will be modified for other websites in the future. All dependencies must be installed.
'''

import json

# error messages
PRIMARY_ACCOUNT_KEY_NOT_FOUND = 'The file does not contain a primary account. This should have the key \"PrimaryAccount\". Manually add the key along with corresponding account details: ' 
SIGNIN_DETAILS_NOT_PROVIDED = 'You can\'t sign in without an email and a password. Use getLoginInfo() to access login info'
LOGIN_INFO_FILE_NOT_FOUND = 'The default login info file appears to be missing. Manually enter the file path: '
CHANGE_PRIMARY_ACCOUNT_INFO_DETAILS_NOT_PROVIDED = ''

class AccountAccess(object):
    def __init__(self, primaryEmail=None, primaryPassword=None, url='https://www.linkedin.com/login', **kwargs):
        self.primaryEmail = primaryEmail
        self.primaryPassword = primaryPassword
        self.url = url
        self.loginInfoFile = None
        self.loginInfo = {}
        self.errors = {}

    def getLoginInfo(self, filePath='loginInfo.json', **kwargs):
        try:
            with open(filePath) as file:
                loginInfo = json.load(file)

            try:
                loginInfo["PrimaryAccount"]
            except KeyError:
                filePath = input(PRIMARY_ACCOUNT_KEY_NOT_FOUND)
                if len(filePath) > 0:
                    self.getLoginInfo(filePath)

            self.loginInfoFile = file
            self.loginInfo = loginInfo            
        except FileNotFoundError:
            newFilePath = input(LOGIN_INFO_FILE_NOT_FOUND)
            self.getLoginInfo(filePath=newFilePath)

        return loginInfo

    def setPrimaryAccountInfo(self, loginInfo={}, primaryAccountInfo={}):
        loginInfo = self.getLoginInfo()
        primaryAccountInfo = loginInfo["PrimaryAccount"]

        self.email = primaryAccountInfo["email"]
        self.password = primaryAccountInfo["password"]

    def changePrimaryAccount(self, newPrimaryAccountName=None, newPrimaryAccountEmail=None, newPrimaryAccountPassword=None):
        if newPrimaryAccountEmail == None or newPrimaryAccountPassword == None:
            print(CHANGE_PRIMARY_ACCOUNT_INFO_DETAILS_NOT_PROVIDED)
            return
        
        self.primaryEmail = newPrimaryAccountEmail
        self.primaryPassword = newPrimaryAccountPassword

        # Write new primary account info to loginInfo.json

    def signIn(self, **kwargs):
        if self.email == None or self.password == None:
            print(SIGNIN_DETAILS_NOT_PROVIDED)
        else:
            print(self.url)
            print(self.email)
            print(self.password)
            # actual sign-in code goes here
