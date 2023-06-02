
from .. import errors
from ..dataManager import accounts

class Account(object):
    def __init__(self, id):
        self.id = id

        accountInfo = self.getLoginInfo(self.id)

        self.name = accountInfo["name"]
        self.password = accountInfo["password"]
        self.dateCreated = self.getDateCreated()
        self.number_of_connections = self.getNumberOfConnections()
        self.email = id

    def getLoginInfo(self, id):
        return accounts.getLoginInfo()[id]

    def getNumberOfConnections(self):
        # code to get number of connections
        return

    def getDateCreated(self):
        # code to get account creation date
        return

    def signIn(self):
        # code for signing in (refers to crawler)
        return
    
    def signOut(self):
    # code for signing out (refers to crawler)
        return
    
    def setPrimary(self):
        # code to set as primary account in offline database (refers to dataManager.accounts)
        return