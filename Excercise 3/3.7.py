guest_list = ['Jake','John','James']

print ("Hey " + guest_list[0] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[1] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[2] + ", I invite you to come to my dinner")

print ("\n"+"James can't make it"+"\n")

del guest_list[2]
guest_list.append('Josh')

print ("\n"+"Hey, I found a bigger dinner table"+"\n")

guest_list.insert(0, 'Ash')
guest_list.insert(2, 'Ana')
guest_list.append('Anthony')

print ("Hey " + guest_list[0] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[1] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[2] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[3] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[4] + ", I invite you to come to my dinner")
print ("Hey " + guest_list[5] + ", I invite you to come to my dinner")

print ("\n"+"Sorry, I can only invite two people for dinner"+"\n")

not_invite = guest_list.pop(0)
print ("Sorry, " + not_invite + " I can't invite you to dinner")

not_invite = guest_list.pop(0)
print ("Sorry, " + not_invite + " I can't invite you to dinner")

not_invite = guest_list.pop(0)
print ("Sorry, " + not_invite + " I can't invite you to dinner")

not_invite = guest_list.pop(0)
print ("Sorry, " + not_invite + " I can't invite you to dinner" + "\n")

print (guest_list[0] + ", you're still invited")
print (guest_list[1] + ", you're still invited")

del guest_list[0]
del guest_list[0]

print (guest_list)
