import sys
full_name=sys.argv[1]
last_name=sys.argv[2]
email=full_name.lower()+last_name.lower()+"@gmail.com"
print("name:",full_name)
print("email:",email)
