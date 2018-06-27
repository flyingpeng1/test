import ldap

#a simple test program
class User:
  'represents a user'
  userCount = 0

  def __init__(self, name, isOnGithub, githubID):
    self.name = name
    self.isOnGithub = isOnGithub
    self.githubID = githubID

  def display(self):
    if(self.isOnGithub):
      print('Name: ' + self.name + '   Github ID: ' + self.githubID)
    else:
      print('Name: ' + self.name)

  def __del__(self):
    class_name = self.__class__.__name__


user1 = User('John', True, 'john12345')
user2 = User('Ethan', False, '')

user1.display()
user2.display()

del user1
del user2


