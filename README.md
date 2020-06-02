# Box-User-Management


Box user management script that works with LDAP for enterprise user management. 
 
boxLDAPJWT.py is integrated with JWT. So no need to manually provide access tokens all the time. 

Works using public/private key pair.

You need to generate a JSON file with the private key and credentials. So, whenever you run the boxLDAPJWT.py, you need to use the JSON file. Best to put the two files under the same folder. The script will automatically read it. 

Store your private key securely. If it’s lost, then you have to generate a new pair with a new JSON file. 
