from boxsdk import OAuth2, Client, JWTAuth
import csv
from datetime import datetime

# read csv inpt files for inactive affilaitions
usersList = []
usersdeletedList = []

with open("C:\\tmp\\uid.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            usersList.append(row);
            line_count += 1
    print(f'Processed {line_count} lines.')

print(dir(JWTAuth))
config = JWTAuth.from_settings_file('C:\\CSUN\\Box\\224660_nad5llrh_config.json')

client = Client(config)

service_account = client.user().get()
print('Service Account user ID is {0}'.format(service_account.id))
def writeToFile(fileToWriteTo):

    with open(fileToWriteTo, "w") as output_file:
        output_file.write('%s\n'% 'Deleted Users');
        for listitem in  usersdeletedList:
            outputVal=listitem+ ','+ str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S"));
            output_file.write('%s\n' % outputVal)



user = client.user().get()
counter =0;
for ldapUser in usersList:

    # Authentication Check. If printed, then successfully established OAuth2
    users = client.users(filter_term=ldapUser[1].strip());
    for user in users:
        print(user.space_used);
        if(user.space_used ==0 and counter < 51):
            counter = counter + 1;
            #print("User Id: ", user.id);
            print("User Name: ", user.name)
            #print("User Login: ", user.login)
            #print("User Creation Time: " ,user.created_at)
            #print("The user’s total available space amount in bytes: ", user.space_amount)
            #print("TThe amount of space in use by the user: ", user.space_used)
            #print("The Status of the user's account: ", user.status+":counter:"+str(counter));
            #print("");
            ## Delete Users
            #client.user(user.id).delete(force=False)
            usersdeletedList.append(user.login);

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%m_%d_%Y-%H_%M_%S")
writeToFile("C:\\tmp\\BoxDeletedList-"+timestampStr+".txt");

