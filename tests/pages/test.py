class Deprt(object):
   def __init__(self, username, ms=None):
      if not ms:
         ms = []
      self.username = username
      self.ms = ms
   def m_addition(self, usernane):
      assert usernane not in self.ms
      self.ms.append(usernane)
class LModel(object):
   def __init__(self):
      self.loginusrs = []
      self.passwords = {}
   def usr_addition(self, username, password):
      assert username not in self.loginusrs
      if password not in self.passwords:
         self.passwords[password] = Deprt(password)
      self.passwords[password].m_addition(username)