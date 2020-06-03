from splitwise import Splitwise
from splitwise.expense import Expense
from splitwise.user import ExpenseUser, Friend

Consumer_Key = 'Your Consumer Key'
Consumer_Secret = 'Your Secret Key'
access_token = 'Your Access Token'

sObj = Splitwise(Consumer_Key,Consumer_Secret)
sObj.setAccessToken(access_token)

user = sObj.getCurrentUser()
friends = dict()
for friend in sObj.getFriends():
    friends[friend.first_name] = friend

expense = Expense()
expense.setCost('10')
expense.setDescription("Testing")

user1 = ExpenseUser()
user1.setId(user.id)
user1.setPaidShare('10.00')
user1.setOwedShare('5.00')

user2 = ExpenseUser()
user2.setId(friends['name'].id)
user2.setPaidShare('0')
user2.setOwedShare('5.0')

users = []
users.append(user1)
users.append(user2)

expense.setUsers(users)
sObj.createExpense(expense)