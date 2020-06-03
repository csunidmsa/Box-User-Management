from boxsdk import OAuth2, Client
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
from boxsdk import JWTAuth

serverObject = Server("LDAP_SERVER", get_info=ALL)
conObject = Connection(serverObject, user="cn=rmwd read,ou=proxies,ou=auth,o=domain", password="ENTER_PASS_HERE",
                       auto_bind=True, )
conObject.bind()



# Read the JSON file

config = JWTAuth.from_settings_file('JSON_FILE')
# Initialize SDK client

client = Client(config)


user = client.user().get()

# Authentication Check. If printed, then successfully established OAuth2
print('The current user ID is {0}'.format(user.id))

print("")
users = client.users(user_type='all')

for user in users:
    searchFilter = '(' + 'employeeNumber=' + user.id + ')'
    testFilter = '(TEST_USER_ID)'


    conObject.search('ou=people,ou=auth,o=domain', searchFilter, attributes=['ATTRIBUTE_ONE', 'ATTRIBUTE_TWO'])
    try:
        entry = conObject.entries[0]
        if entry.ATTRIBUTE_TWO != None:
            activeStatus = str(entry.ATTRIBUTE_TWO)
            temp = activeStatus.split(':')
            activeStatus = temp[1]
            if activeStatus == "inactive":
                print("User Id: ", user.id)
                print("User Name: ", user.name)
                print("User Login: ", user.login)
                print("User Creation Time: ", user.created_at)
                print("The user’s total available space amount in bytes: ", user.space_amount)
                print("TThe amount of space in use by the user: ", user.space_used)
                print("The Status of the user's account: ", user.status)
                if user.login != "USER_LOGIN":
                    client.user(user.id).delete(force=False)
                print("")


    except:
        print("The user does not exist on the LDAP server!")
