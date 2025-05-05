class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def meow(self):
        print(f"{self.name} says: Meow!")

my_cat = Cat("Coco", "Siamese") 
my_cat.meow()