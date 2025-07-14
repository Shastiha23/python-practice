location="chennai central"
reloc=location.replace("chennai central","ennore")
print(reloc)
message="your uber id:UB123 . please keep it safe"
book_id=message.split(":")[1].split(".")[0].strip()
print(book_id)
promo_msg="use UB100 to get offer"
if "UB100" in promo_msg:
    print("the  offer is applied")
print("position:",message.find("UB123"))
for word in location.split():
    print("".join(word[0].upper()))
    
