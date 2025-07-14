amount=int(input("enter the total item:"))
total_cost=amount*100
if total_cost>=3300 and amount>=5:
    print("you got a discount")
elif total_cost<=330 or amount>=5:
    print("you got a discount")
else:
    print("discount is not applied")
    
