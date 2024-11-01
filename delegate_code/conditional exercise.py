#1. Create a script named exercise1_console_io.py.
#2. Prompt the user to input his/her name and capture it in variable named name.
#3. Prompt the user to input his/her age and capture it in a variable named age.
#4. Print the user's name and age to the console. You might try doing this with one
#invocation of the built-in print function.
#5. Execute the script in VSC.
birth_year=input("enter birth year:")
birth_year_int=int(birth_year)
if birth_year_int>=1946 and birth_year_int<= 1965:
    print("you are baby boomer")
elif birth_year_int>=1966 and birth_year_int<= 1976:
    print(f"you are Generation X born in {birth_year_int}")
elif birth_year_int>=1977 and birth_year_int<= 1994:
    print(f"you are millenial born in {birth_year_int}")
elif birth_year_int>=1995:
    print("you are Generation z")
else:
    print("can't find match")
