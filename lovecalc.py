print("Love Calculator")
# To write a test that checks compatibility between two people
# INPUT:Take in two names
# FUNCTION:To check number of times the letters in the word "TRUE LOVE" occurs
# OUTPUT: Return a two digit number based on that
name1=input()
name2=input()
fname=list(name1.lower())
t=fname.count("t")
r=fname.count("r")
u=fname.count("u")
e=fname.count("e")
true=t+r+u+e
lname=list(name2.lower())
l=lname.count("l")
o=lname.count("o")
v=lname.count("v")
i=lname.count("e")
love=l+o+v+i
print(f"Your love score is {str(true)+str(love)}.")
