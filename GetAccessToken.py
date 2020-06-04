from splitwise import Splitwise

Consumer_Key = 'Your Consumer Key'
Consumer_Secret = 'Your Secret Key'

sObj = Splitwise(Consumer_Key,Consumer_Secret)
token, secret = sObj.getAuthorizeURL()
# Go to ""'https://secure.splitwise.com/authorize?oauth_token?' + token" to get your oauth_verifier
# Then uncomment the code below to get your access token, and place the token in AddExpense.py

# access_token = sObj.getAccessToken(token, secret, oauth_verifier)
# print(access_token)