#You have write a function that accepts, a string which length is “len”, the string has some “#”,
# in it you have to move all the hashes to the front of the string 
# and return the whole string back and print it.


def hash(self):
    x = self.count('#')
    y = self.replace('#','')
    print('#'*x + y)
a = input("enter string : ")
hash(a)