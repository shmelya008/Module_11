import inspect


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
    res['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))]
    res['module'] = inspect.getmodule(introspection_info).__name__
    res['hash'] = obj.__hash__()
    res['methods'] = dir(obj)
    return res


class_info = introspection_info(House.setNewNumberOfFloors)
print(class_info)
object_info = introspection_info(h_1)
print(object_info)

object_info = introspection_info('abc')
print(object_info)
object_info = introspection_info(42)
print(object_info)
