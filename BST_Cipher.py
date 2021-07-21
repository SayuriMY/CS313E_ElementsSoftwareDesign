'''Description: Encryption/ Decryption with Binary Search Trees
Create a simple encryption scheme using a BST. the encryption key is transformed
into a BST using each character's ASCII value as a comparative measure. This allows
the encoding of plain text by referring to the BST key.
A reference to the root node of the BST is represented by an "*". A reference to
another character in the BST is represented by a chain on "<" or ">" signs signifying
the tree traversal towards the left or right child of each subsequent node starting
from the root. The exclamation mark "!" is used as a delimeter.
Student's Name: Sayuri Monarrez Yesaki
Student's UT EID: sdm3465
Course Name: CS 313E Elements of Software design
Unique Number: 51335
Date Created: 04/15/2018
Date Last Modified: 04/18/2018
'''

class Node(object):
   def __init__(self, data=None):
      self.data = data
      self.lchild = None
      self.rchild = None

class Tree (object):
   # the init() function creates the binary search tree with the
   # encryption string. If the encryption string contains any
   # character other than the characters 'a' through 'z' or the
   # space character drop that character.
   def __init__(self, encrypt_str):
      self.root = None

      list_ch = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

      encrypt_str = list(encrypt_str)

      for ch in encrypt_str:
         result = self.in_Tree(ch)
         if ch in list_ch and not(result is True):
            self.insert(ch)

   def in_Tree(self, ch):
      current = self.root
      while not(current is None) and not(current.data == ch):
         if (ch < current.data):
            current = current.lchild
         else:
            current = current.rchild

      if current is None:
         return False
      return True

   # the insert() function adds a node containing a character in
   # the binary search tree. If the character already exists, it
   # does not add that character. There are no duplicate characters
   # in the binary search tree.
   def insert (self, ch):
      # create new node
      new_node = Node(ch)

      #special case when root is is_empty
      if self.root is None:
         self.root = new_node
      else:
         current = self.root
         parent = self.root

         while not(current is None):
            parent = current
            if ch < current.data:
               current = current.lchild
            else:
               current = current.rchild

         # insert new node
         if ch < parent.data:
            parent.lchild = new_node
         else:
            parent.rchild = new_node

   # the search() function will search for a character in the binary
   # search tree and return a string containing a series of lefts
   # (<) and rights (>) needed to reach that character. It will
   # return a blank string if the character does not exist in the tree.
   # It will return * if the character is the root of the tree.
   def search (self, ch):
      s = ""

      current = self.root

      #special case when tree is empty
      if current is None:
         return s
      elif current.data == ch:
         return "*"
      else:
         while not(current is None) and not(current.data == ch):
            if ch < current.data:
               current = current.lchild
               s += "<"
            else:
               current = current.rchild
               s += ">"

         if current is None:
            return " "
         else:
            return s

   # the traverse() function will take string composed of a series of
   # lefts (<) and rights (>) and return the corresponding
   # character in the binary search tree. It will return an empty string
   # if the input parameter does not lead to a valid character in the tree.
   def traverse (self, st):
      current = self.root

      st = list(st)

      if current is None:
         return " "
      else:
         for ch in st:
            if current is None:
               return " "
            elif ch == "<":
               current = current.lchild
            elif ch == ">":
               current = current.rchild

         return current.data

   # the encrypt() function will take a string as input parameter, convert
   # it to lower case, and return the encrypted string. It will ignore
   # all digits, punctuation marks, and special characters.
   def encrypt (self, st):
      encrypted_str = ""

      st = st.lower()
      st = list(st)

      list_ch = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

      for ch in st:
         if ch in list_ch:
            encrypted_str += self.search(ch) + "!"

      encrypted_str = encrypted_str[:-1]

      return encrypted_str

   # the decrypt() function will take a string as input parameter, and
   # return the decrypted string.
   def decrypt (self, st):
      decrypted_str = ""

      st = st.split("!")

      for element in st:
         decrypted_str += self.traverse(element)

      return decrypted_str

def main():
   # prompt the user to enter the encryption key
   key = input("Enter encryption key: ")
   key = key.lower()

   #create tree based on the key
   Encryption_tree = Tree(key)

   #prompt the user to enter string to be encrypted
   string_enc = input("Enter string to be encrypted: ")
   encrypted_str = Encryption_tree.encrypt(string_enc)
   print("Encrypted string: ", encrypted_str)

   #prompt the user to enter string to be decrypted
   string_dec = input("Enter string to be decrypted: ")
   decrypted_str = Encryption_tree.decrypt(string_dec)
   print("Decrypted string: ", decrypted_str)

main()
