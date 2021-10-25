try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

#Getting filename from user
filename = input("Input the HTML filename: ")    

#Opening the file and reading the code
with open(filename, "r", encoding='utf-8') as f:
	code = f.read()

parsed_html = BeautifulSoup(code, "lxml")

print("The tags used in the given HTML file: ")


#Creating and adding tags without duplication into a list
tags = []
for tag in parsed_html.find_all():
    if tag.name not in tags:
        tags.append(tag.name)

#Printing all the HTML tags        
print(tags)
