import sys
from splitwise import Splitwise
from splitwise.expense import Expense
from splitwise.user import ExpenseUser, Friend


def getUserInput():
    Name = sys.argv[1]
    TargetUser = sys.argv[2]
    Amount = float(sys.argv[3])
    Ratio = 0.5

    if len(sys.argv) > 4:
        Ratio = float(sys.argv[4])

    My_Amount = str(round(Amount * Ratio, 2))
    Target_Amount = str(Amount - float(My_Amount))
    return [Name, TargetUser, Amount, My_Amount, Target_Amount]

Name, TargetUser, Amount, My_Amount, Target_Amount = getUserInput()

Consumer_Key = 'Your Consumer Key'
Consumer_Secret = 'Your Secret Key'
access_token = 'Get Your Access Token From GetAccessToken.py'

sObj = Splitwise(Consumer_Key,Consumer_Secret)
sObj.setAccessToken(access_token)

user = sObj.getCurrentUser()
friends = dict()
for friend in sObj.getFriends():
    friends[friend.first_name] = friend

expense = Expense()
expense.setCost(str(Amount))
expense.setDescription(Name)

user1 = ExpenseUser()
user1.setId(user.id)
user1.setPaidShare(str(Amount))
user1.setOwedShare(My_Amount)

user2 = ExpenseUser()
user2.setId(friends[TargetUser].id)
user2.setPaidShare('0')
user2.setOwedShare(Target_Amount)

users = []
users.append(user1)
users.append(user2)

expense.setUsers(users)
sObj.createExpense(expense)