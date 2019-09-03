class Animal():
    owner = 'jack'
    def __init__(self,name):
        self._name = name

    @classmethod
    def get_owner(cls):
        return cls.owner

    @classmethod
    def set_owner(cls,name):
        cls.owner = name

if __name__ == '__main__':

    print(Animal.get_owner())

    print(Animal.set_owner('rosy'))

    print(Animal.owner)

