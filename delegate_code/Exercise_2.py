ID = input ("Enter the ID:")
ID=int(ID)
First_name=input("Enter first name:")
First_name=str(First_name)
Last_name=input("Enter last name:")
Last_name=str(Last_name)
Checked_bags=bool(True)
visited_countries={"Latvia","Guyana","Yemen","Uzbekistan"}
Flight= "LGW to CDG"
Flight_time = str("1 hour 15 minutes")
print(int(ID),
        str(First_name),
        str(Last_name),
        bool(Checked_bags),
        set(visited_countries),
        str(Flight))


####solution###
id=1234#underscore letter
first_name="John"
last_name="Doe"
checked_bags=False
visited_countries=["Latvia","Guyana","Yemen","Uzbekistan"]
flight={"departure":"LGW","arrival":"CDG"}
flight_time=1.25
print(f"id:{id}")
print(f"First name:{first_name}")
print(f"Last name:{last_name}")
print(f"Checked bags:{checked_bags}")
print(f"Visited countries:{visited_countries}")
print(f"flight:{flight}")
print(f"Duration:{flight_time}")





