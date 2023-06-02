import json
from .. import errors

loginInfoFile = None
loginInfo = {}

def getLoginInfo(filePath='loginInfo.json', **kwargs):
    try:
        with open(filePath) as file:
            loginInfo = json.load(file)

        try:
            loginInfo["PrimaryAccount"]
        except KeyError:
            filePath = input(errors.PRIMARY_ACCOUNT_KEY_NOT_FOUND)
            if len(filePath) > 0:
                getLoginInfo(filePath)

        loginInfoFile = file
        loginInfo = loginInfo            
    except FileNotFoundError:
        newFilePath = input(errors.LOGIN_INFO_FILE_NOT_FOUND)
        getLoginInfo(filePath=newFilePath)

    return loginInfo

def setPrimaryAccountInfo(loginInfo={}, primaryAccountInfo={}):
    loginInfo = getLoginInfo()
    primaryAccountInfo = loginInfo["PrimaryAccount"]

    email = primaryAccountInfo["email"]
    password = primaryAccountInfo["password"]

def changePrimaryAccount(newPrimaryAccountName=None, newPrimaryAccountEmail=None, newPrimaryAccountPassword=None):
    if newPrimaryAccountEmail == None or newPrimaryAccountPassword == None:
        print(errors.CHANGE_PRIMARY_ACCOUNT_INFO_DETAILS_NOT_PROVIDED)
        return
    
    primaryEmail = newPrimaryAccountEmail
    primaryPassword = newPrimaryAccountPassword

    # Write new primary account info to loginInfo.json
