class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
        
        def __eq__(self,other):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


build_1 = Building(12, "Дом 1")
build_2 = Building(12, "Дом 2")
print(build_1 == build_2)
