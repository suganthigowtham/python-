import requests

class users:

    def __init__(self,url):
        self.url = url
        self.response = requests.get(url)

    def isConnected(self):
        if self.response.status_code == 200:
            return True
        return False
    
    def fetchData(self):
        try:
            if self.isConnected():
                return self.response.json()
            raise Exception()
        except:
            print(" It is not connected")
            return None
        
    def getNames(self):
        namesList= []
        if not self.fetchData() is None:
            for userDict in self.fetchData():
                namesList.append(userDict["name"]["common"])
            return namesList
        else:
            print("It is not connected")

    def getCurriencies(self):
        CurrenciesList=[]
        if not self.fetchData() is None:
            for userDict in self.fetchData():
                 if (userDict.get("currencies",None)) is not None:
                     for user in userDict.get("currencies").values():
                         print(user.get("name"))
            return CurrenciesList
        else:
            print(" It is not connected")

               


url = "https://restcountries.com/v3.1/all"
userobj = users(url)
print(userobj.getNames())
print(userobj.getCurriencies())