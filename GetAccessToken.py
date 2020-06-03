from splitwise import Splitwise

Consumer_Key = 'Your Consumer Key'
Consumer_Secret = 'Your Secret Key'

sObj = Splitwise(Consumer_Key,Consumer_Secret)
token, secret = sObj.getAuthorizeURL()
oauth_verifier = 'Get from your http response'

access_token = sObj.getAccessToken(token, secret, oauth_verifier)
print(access_token)