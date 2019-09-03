
class A:
    def __init__(self):
        self.name = 'xiaoming'
    def test(self):
        print('----testA----')

class B:
    def __init__(self):
        self.age = 8
    def test(self):
        print('--testB--')

class Person(A,B):
    pass

'''
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def testP(self):
        print('-testP-')
'''

person = Person()
#print(person.name)
#print(person.age)

person.test()
#person.testB()
#person.testP()

print(Person.mro())
