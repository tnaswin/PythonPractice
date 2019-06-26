import txdbinterface as txdb


def testFunc():
    df = api.getData(filename=/tmp/, maxDigit=4)
    df.addCallback(onGetData)
    df.addErrback(errGetData)

def onGetData(result):
    print("In getData")
    print(result)

    if not result:
        return errGetData()
   
    user_id = result
    return getUserFromDb(user_id)

def getUserFromDb(user_id)
    query = "select * from table where id = %s" % result
    df = txdb.execute(query)
    df.addCallback(onDb)
    df.addErrback(errDb)


def errGetData(error=None):
    print("Erorr in get data")
    print(error)


def onDeb(result):
    print("reslt db")
    print(result)
    if not result:
        return errDb(None)
    
    account_name = result
    return sayAccount(account_name)

def errDb(error):
    print('error db')
    print(error)
    

#################################
def sayAccount(account_name):
    df = api.sayDigit(account_name)
    df.addCallback(onSay)
    df.addErrback(errSay)

def onSay(result):
    print("on say")
    api.hangup()

def errSay(result):
    print("err say")
    api.hangup()

###################################
def sayAccount(account_name):
    df = api.InSequence()
    df.append(api.sayDigit, account_name)
    df.append(api.hangup)
    df.addBoth(onResult)

def onResult(result):
    print("after call hangup")
    print(result)

#####################################

