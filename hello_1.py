print("John Njuguna") #this is my first code in python

""" Variable """
age = 30
print(age)
new_patient = "steve jobs"
print(age , new_patient)

""" Getting input from user """
name = input("Enter your age: ")
print("Age = ", name)

""" Number/Arithmetic in python """
# +, -, *, /, //, %
print("2 + 2 =", 2+2)
print("2 - 2 = ", 2-2)
print((2 + 3) * 4)
print(2 + 3 * 4)

""" Strings """
first_name = "steve"
last_name = "jobs"
full_name = first_name + last_name #concatenation
print(full_name)

""" List """
fav_language = ["python", "C", "javascript", "Mysql", "Html"]
print(fav_language[-1]) #indexing
hard_language = ["AI", "ML" "data science"]
all_languages = fav_language + hard_language
print(all_languages)
print(all_languages[0:3]) #slicing
print(all_languages.append("Typescript")) # Many other like sort, reverse, insert, del
print(all_languages)

""" Tuples """
years = (1990, 1989, 1995, 2000)
print(years[0])
print(len(years))
print(min(years))
print(max(years))

""" dictionary """
movies = {"Iron man": "tony stark", "Captain america": "ben", "Money heights": "Tokyo"}
print(movies)
print(movies["Iron man"])
print(len(movies))
print(movies.values())
print(movies.keys())