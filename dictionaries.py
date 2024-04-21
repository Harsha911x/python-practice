# #declaring a dictionary
# dic={"two":"can be just as lonely as one",1:100}
# #adding to dictionary
# dic["one"]="one is the lonliest number"
# print(dic)
# print(dic["one"])
# print(dic[1])


#Exercise 1
student_scores={'a':98,'b':88,'c':67,'d':76,'e':49}
student_grades={}
def assign_grade(student_scores):
    for i in student_scores:
        if(student_scores[i]>90):
            student_grades[i]='Outstanding'
        elif(student_scores[i]>80):
            student_grades[i]='Very Good'
        elif(student_scores[i]>70):
            student_grades[i]='Good'
        elif(student_scores[i]>60):
            student_grades[i]='Average'   
        else:
            student_grades[i]='Pass'   
assign_grade(student_scores)
print(student_grades)


#Nesting a dictionaries inside list
travel_log=[
    {
        "country":"Germany",
        "cities":["Berlin","Stuttgart","Hamburg"],
        "total_visits":12
    },
    {
        "country":"France",
        "cities":["Paris","Lille","Djon"],
        "total_visits":9
    }
]
x=travel_log[1]
print(x["country"],x["cities"],x["total_visits"])


print(travel_log,"\n\n\n\n")
#Exercise 2
def add(country,cities,total_visits):
    new_travel={}
    new_travel["country"]=country,
    new_travel["cities"]=cities,
    new_travel["total_visits"]=total_visits
    travel_log.append(new_travel)
    
country="Russia"
cities=["Moscow","Saint.P","Kazan"]
total_visits=2
add(country,cities,total_visits)
print(travel_log)
