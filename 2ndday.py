from abc import ABC , abstractmethod
import urllib.request as req
import json

#abtract class
class AbstractPerson(ABC):
    def name(self, name):
        pass
    def age(self,age):
        pass

# level 1 inhirited 
class Person(AbstractPerson):
    def __init__(self , name , age):
        self._name = name
        self._age = age
# getter 
    @property
    def name(self):
        return self._name
# getter 
    @name.setter
    def name( self , name):
        self._name = name
# getter 

    @property
    def age(self):
        return self._age
    
# getter 
    @name.setter
    def age( self , age):
        self._age = age

    @classmethod
    def persontype(cls , type):
        cls.type = type
        
# level 2 inhirited    
class Devloper(Person):
    def __init__(self , name , age , languge):
        super().__init__( name , age)
        self._languge  = languge
    @property
    def languge(self):
        return self._languge
    
# method with defalt value 
    def fullname(self , firstname , lastname = ""):
        return "{} {}".format(firstname, lastname)

'''
Person.persontype("Human")
person1     = Person("person 1" , 24)
person2     = Person("person 2" , 19)
Devloper    = Devloper("Devloper 1" , 42 , 'python')

print(person1.name)
print(person2.name)
print(Devloper.languge)
print(Devloper.fullname("test" , "dev"))
Devloper.type = "God"
print(Devloper.type)
print(person1.type)
'''


content = req.urlopen("https://samples.openweathermap.org/data/2.5/weather?q=pune&appid=b6907d289e10d714a6e88b30761fae22").read();
weather = json.loads(content)
print("Weather App: ")
print("Todays weather ")
print(weather['weather'][0]['main'])
print(weather['weather'][0]['description'])

print("\nNews App: \n ")
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f7016653a5bb49f0ae27eb496c1272ad"

content = req.urlopen(url).read();
news = json.loads(content)

articles  = (news['articles'])
count = 0
for article in articles :
    count = count + 1
    if(count > 5):
        break
    print("Author : \n "+article['author'])
    print("Title : \n "+article['title'])




    
