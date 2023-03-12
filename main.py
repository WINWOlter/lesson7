import requests
from colorama import Fore

class Person:
  def __init__ (self,nat):
    r = requests.get("https://randomuser.me/api/?nat=" + nat)
    res = r.json()
    self.name = res["results"][0]["name"]["first"]
    self.surename = res["results"][0]["name"]["last"]
    self.age = res["results"][0]["dob"]["age"]
    self.phone = res["results"][0]["phone"]
    self.email = res["results"][0]["email"]
    self.isMale = res["results"][0]["gender"] == "male"
    
  def print_person(self):
    if self.isMale:
      print(Fore.CYAN)
    else:
      print(Fore.MAGENTA)
    print(self.name)
    print(self.surename)
    print(self.age)
    print(self.phone)
    print(self.email)
    print(self.isMale)



random_person = Person('fi')
random_person.print_person()

a = input("Скільки працівників потрібно для компанії")
a = int(a)

rabotnici = []






     