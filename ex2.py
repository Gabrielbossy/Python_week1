#Age calculator: ask for birth year, print the age
from datetime import date

birth_year = int(input("What year were you born? "))
current_year = date.today().year
age = current_year - birth_year

print(f"You are about {age} years of age! ")