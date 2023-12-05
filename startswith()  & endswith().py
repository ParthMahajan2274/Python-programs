a="Hello"
print(a.endswith("llo")) #True
print(a.endswith("lol")) #False
print(a.startswith("He"))#True
print(a.startswith("Hi"))#False
b="Welcome to the Console"
print(b.endswith("to",4,10)) #check from b[4] to b[10-1]=b[9] #True
print(b.endswith(" to ",4,10))#False
print(b.startswith("co",3,10))#True
print(b.startswith("me",3,10))#False
