a="!!!Aryan!!!!!   !!!! Aspire"
print(len(a))
print(a)
# print(a.uppercase())
# print(a.lowercase())
print(a.rstrip("!"))
print(a.lstrip("!"))
print(a.replace("Aryan", "Jerry"))

blogheading="introduction tO web devlopmet"
print(blogheading.capitalize())

str1= "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))

print(a.count("!"))
print(str1.endswith("to", 4, 10))

str2 = "He's name is Dan. He is an honest man."
print(str2)

print(str2.find("is"))
print(str2.find("hhh"))
print(str2.index("is"))
print(str1.isalnum())
print(str1.isalpha())
print(str1.isupper())
print(str1.islower())
print(str1.isprintable())
print(str2.isprintable())
print(str1.isdigit())
print(str2.isdigit())

str3 = "We wish a very happy durga puja to you and your family\n"
print(str3)
print(str3.isprintable())
print(str3.isnumeric())
print(str3.isspace())
print(str1.isspace())
print(str2.isspace())

str4 = "World health organisation"
print(str4)
print(str4.istitle())