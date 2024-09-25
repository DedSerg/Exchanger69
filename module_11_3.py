from inspect import getmodule

def introspection_info(obj):
    return {
        'type' : type(obj).__name__,
        'atributes' : obj.__dict__,
        'methods' : dir(obj),
        'module' : getmodule(obj)
    }
class Dogs():
    def __init__(self, breed, gender, age, name):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.name = name


obj = Dogs('Basset Hound', 'The dog is a boy','Tyma',10)
dog_info = introspection_info(obj)
print(dog_info)
