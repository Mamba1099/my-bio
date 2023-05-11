print("grading system... ")

#compulsory subjects
math_pp1 = float(input("maths paper 1:"))
math_pp2 = float(input("maths paper 2:"))
math_total = (math_pp1 + math_pp2) / 2
print("math: ", + math_total)

english_pp1 = float(input("english paper1(out of 60):"))
english_pp2 = float(input("english paper2(out of 80):"))
english_pp3 = float(input("english paper 3(out of 60): "))
english_total = ((english_pp1 + english_pp2 + english_pp3) / 200) * 100
print("English: ", + english_total)

kiswahili_pp1 = float(input("kiswahili paper 1(out of 60):"))
kiswahili_pp2 = float(input("kiswahili paper 2(out of 80):"))
kiswahili_pp3 = float(input("kiswahili paper 3(out of 60):"))
kiswahili_total = ((kiswahili_pp1 + kiswahili_pp2 + kiswahili_pp3) / 200) * 100
print("kiswahili: ", + kiswahili_total)

chemistry_pp1 = int(input("chemistry paper 2(out of 80):"))
chemistry_pp2 = int(input("chemistry paper 2(out of 80):"))
chemistry_pp3 = int(input("chemistry paper 3(out of 40):"))
chemistry_total = (((chemistry_pp1 + chemistry_pp2) / 160) * 60) +chemistry_pp3
print("chemistry: ", + chemistry_total)

cre_pp1 = int(input("cre paper 1(out of 100):"))
cre_pp2 = int(input("cre paper 2(out of 100):"))
cre_total = (cre_pp1 + cre_pp2) / 2
print("cre: ", + cre_total)

#total for the compulsory subjects
total1 = math_total + english_total + kiswahili_total + chemistry_total + cre_total
#selected subjects
print("sciences:")
print("if your doing both sciences press ENTER to contimue")
list1 = ["biology", "physics"]
print(list1)
subject1 = input("enter subject1:") 
if subject1 == "biology":
    biology_pp1 = float(input("biology paper1(out of 80):"))
    biology_pp2 = float(input("biology paper2(out of 80):"))
    biology_pp3 = float(input("biology paper3(out of 40):"))
    biology_total = (((biology_pp1 + biology_pp2) / 160) * 60) + biology_pp3
    print("biology: ", + biology_total)

elif subject1 == "physics":
    physics_pp1 = float(input("physics paper1(out of 80):"))
    physics_pp2 = float(input("physics paper2(out of 80):"))
    physics_pp3 = float(input("physics paper3(out of 40):"))
    physics_total = (((physics_pp1 + physics_pp2) / 160) * 60) + physics_pp3
    print("physics: ", + physics_total)

else:
    biology_pp1 = float(input("biology paper1(out of 80):"))
    biology_pp2 = float(input("biology paper2(out of 80):"))
    biology_pp3 = float(input("biology paper3(out of 40):"))
    biology_total = (((biology_pp1 + biology_pp2) / 160) * 60) + biology_pp3
    print("biology: ", + biology_total)

    physics_pp1 = float(input("physics paper1(out of 80):"))
    physics_pp2 = float(input("physics paper2(out of 80):"))
    physics_pp3 = float(input("physics paper3(out of 40):"))
    physics_total = (((physics_pp1 + physics_pp2) / 160) * 60) + physics_pp3
    print("physics: ", + physics_total)    
print("humanities:")
print("if your doing both humanities press ENTER to contimue")
list2 = ["geography", "history"]
print(list2)    
subject2 = input("enter subject2:")
if subject2 == "geography":
    geography_pp1 = float(input("geography paper 1(out of 100):")) 
    geography_pp2 = float(input("geography paper 2(out of 100):")) 
    geography_total = float(geography_pp1 + geography_pp2) / 2 
    print("Geography:", + float(geography_total))

elif subject2 == "history":
  history_pp1 = float(input("history paper 1( out of 100):"))
  history_pp2 = float(input("history paper 2( out of 100):"))
  history_total = (history_pp1 + history_pp2) / 2
  print("History:", + float(history_total)) 

else:
 geography_pp1 = float(input("geography paper 1(out of 100):")) 
 geography_pp2 = float(input("geography paper 2(out of 100):")) 
 geography_total = float(geography_pp1 + geography_pp2) / 2 
 print("Geography:", + float(geography_total))

 history_pp1 = float(input("history paper 1( out of 100):"))
 history_pp2 = float(input("history paper 2( out of 100):"))
 history_total = (history_pp1 + history_pp2) / 2
 print("History:", + float(history_total)) 



print("Applied sciences:")
print("if ur doing both Applied sciences press ENTER to continue.")
list3 = ["business", "homescience", ]
print(list3)  
subject3 = input("enter subject3:")
if subject3 == "business":
    business_pp1 = float(input("business paper 1(out of 100):"))
    business_pp2 = float(input("business paper 2(out of 100):"))
    business_total = (business_pp1 + business_pp2) / 2
    print("Business:", + float(business_total))

elif subject3 == "homescience":
    home_science_pp1 = float(input("home science paper 1(out of 25):"))
    home_science_pp2 = float(input("home science paper 2(out of 45):"))
    home_science_pp3 = float(input("home science paper 3(out of 100):"))
    home_science_total = (home_science_pp1 + home_science_pp2 + home_science_pp3) / 170 * 100
    print("Home science:", + float(home_science_total))

else:
    business_pp1 = float(input("business paper 1(out of 100):"))
    business_pp2 = float(input("business paper 2(out of 100):"))
    business_total = (business_pp1 + business_pp2) / 2
    print("Business:", + float(business_total)) 

    home_science_pp1 = float(input("home science paper 1(out of 25):"))
    home_science_pp2 = float(input("home science paper 2(out of 45):"))
    home_science_pp3 = float(input("home science paper 3(out of 100):"))
    home_science_total = (home_science_pp1 + home_science_pp2 + home_science_pp3) / 170 * 100
    print("Home science:", + float(home_science_total))

if subject1 == "biology" and subject2 == "geography" and subject3 == "business":
    sub_total1 = biology_total + geography_total + business_total
    total = total1 + sub_total1
    mean = total / 8
    print(mean)
    
elif subject1 == "biology" and subject2 =="history" and  subject3 == "business":
    sub_total2 = biology_total + history_total + business_total
    total = total1 + sub_total2
    mean = total / 8
    print(mean) 
elif subject1 == "biology" and subject2 == "geography" and subject3 =="homescience":
    sub_total3 = biology_total + geography_total + home_science_total
    total = total1 + sub_total3
    mean = total / 8
    print(mean)
elif subject1 =="biology" and subject2 == "history" and subject3 == "homescience":
    sub_total4 = biology_total + history_total + home_science_total
    total = total1 + sub_total4
    mean = total / 8
    print(mean)    
elif subject1 == "physics" and subject2 == "geography" and subject3 == "business":
    sub_total5 = physics_total + geography_total + business_total
    total = total1 + sub_total5
    mean = total / 8
    print(mean)
elif subject1 == "physics" and subject2 == "history" and subject3 == "business":
    sub_total6 = physics_total + history_total + business_total
    total = total1 + sub_total6
    mean = total / 8
    print(mean)
elif subject1 =="physics" and subject2 =="geography" and subject3 == "homescience":
    sub_total7 = physics_total + geography_total + home_science_total
    total = total1 + sub_total7
    mean = total / 8
elif subject1 == "physics" and subject2 == "history" and subject3 == "homescience":
    sub_total8 = physics_total + history_total + home_science_total
    total = total1 + sub_total8
    mean = total / 8
    print(mean)
else:
    sub_total9 = biology_total + physics_total + geography_total + history_total + business_total + home_science_total
    total = total1 + sub_total9
    mean = total / 11
    print(mean) 

#grade
if 100 < mean > 80:
    print("Grade: A")
 
elif 79 < mean > 75:
    print("Grade: A-")

elif 74 < mean > 70:
    print("Grade: B+")

elif 69 < mean > 65:
    print("Grade: B")

elif 64 < mean >60:
    print("Grade: B-")

elif 59 < mean > 55:
    print("Grade: C+")

elif 54 < mean > 50:
    print("Grade: C")

elif 49 < mean >45:
    print("Grade: C-")

elif 44 < mean > 40:
    print("Grade: D+")

elif 39 < mean >35:
    print("Grade: D")

elif 34 < mean > 30:
    print("Grade: D-")

else:
    print("Grade: E")                                        

    
     

