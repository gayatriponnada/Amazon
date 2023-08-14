name_1=input("enter your name")
name_2=input("enter their name")
combine_name=name_1+name_2
t=combine_name.count("t")
r=combine_name.count("r")
u=combine_name.count("u")
e=combine_name.count("e")
print(t)
print(r)
print(u)
print(e)
total_1=int(t)+int(r)+int(u)+int(e)
print(total_1)
l=combine_name.count("l")
o=combine_name.count("o")
v=combine_name.count("v")
e=combine_name.count("e")
print(l)
print(o)
print(v)
print(e)
total_2=int(l)+int(o)+int(v)+int(e)
print(total_2)
(love_score_1)=str(total_1)+str(total_2)
love_score=int(love_score_1)
print(love_score)
if(love_score<10)or(love_score>90):
    print("your not match each other")
elif(love_score>40)or(love_score<50):
    print("ur good")
else:
    print("ur wonderful")




