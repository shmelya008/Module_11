class House:
    def __init__(self, name, number_Of_Floors):
        self.name = name
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        # print(f'В ЖК {self.name} {self.numberOfFloors} этажей')


h_1 = House('Романтик', ())
h_2 = House('Montblanc', ())
House.setNewNumberOfFloors(h_1, 12)
House.setNewNumberOfFloors(h_2, 56)


def introspection_info(obj):
    res = {}
    res['type'] = type(obj)
    res['callable'] = callable(obj)
    res['attributes'] = hasattr(obj, 'setNewNumberOfFloors')
    res['module'] = obj.__module__
    res['hash'] = obj.__hash__()
    res['methods'] = dir(obj)
    return res


class_info = introspection_info(House.setNewNumberOfFloors)
print(class_info)
object_info = introspection_info(h_1)
print(object_info)


