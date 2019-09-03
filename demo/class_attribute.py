#!/usr/bin/env python3

class UserData:
    
    def __init__(self,_id,_name):
        self._id = _id
        self._name = _name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self._id,self._name)

    def voice(self):
        print('is it work?')


class NewUser(UserData):

    group = 'shiyanlou-louplus'

'''
    def get_name(self):
        return self._name

    def set_name(self,value):
        self._name = value
'''

    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id,name):
        print('{}\' id is {}'.format(name,id))
    


if __name__ == '__main__':
    
    '''
    user1 = UserData(101,'Jack')
    user2 = UserData(201,'Louplus')
    print(user1)
    print(user2)
    '''

    user1 = NewUser(101,'Jack')
    user1.set_name('Jackie')
    user2 = NewUser(102,'Louplus')
    print(user1)
    print(user2)
    
