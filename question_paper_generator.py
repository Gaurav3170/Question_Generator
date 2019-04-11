#This file is used to generate question paper of specified subjects. 

import random
import os
print("Enter the Subject Name for which you want to generate question paper?")
subject=input().upper()
section_a=list()
section_b=list()
section_c=list()
file_name=os.getcwd()+"\\Subjects\\"+subject+".txt"
try:
	with open(file_name,'r') as file:
		data = file.read().split("\n")
except:
	print("File does not exists! Please make questions list of the subject first .")
	exit()
for inputs in data:
	inp=inputs.split("::")
	question=inp[0]
	category=inp[1]
	if(category=='E'):
		section_a.append(question)
	elif(category=='M'):
		section_b.append(question)
	else:
		section_c.append(question)
if(len(section_a)<10 or len(section_b)<6 or len(section_c)<3):
	print("Please enter atleast 10 questions of Easy Category, 6 Questions of Medium Category and 4 Questions of Hard Category!")
else:
	output_text_name=os.getcwd()+"\\Subjects\\"+subject+" Question Paper.txt"
	f = open(output_text_name,'w')
	print("Enter the Subject Code?")
	subject_code=input().upper()
	print("Enter the Semester and SessionYear seperated by double_colon(::) . eg: 5::2018-2019 ")
	input_s=input().split("::")
	semester=input_s[0]
	SessionYear=input_s[1]
	firstLine="----------------------------------------------"+SessionYear+"----------------------------------------------\n"
	secondLine="----------------------------------------"+subject+" "+subject_code+"-----------------------M.M=30-------\n"
	thirdLine="----------------------------------------------Semester-"+semester+"---------------------------------------------\n"
	f.write(firstLine)
	f.write(secondLine)
	f.write(thirdLine)
	f.write("__SECTION A__:(Attempt All Questions) \n")
	count=1
	length=len(section_a)
	list_range=random.sample(range(0,length),10)
	for x in list_range:
		temp_str=(str)(count)+")"+section_a[x]+"    [1]\n"
		f.write(temp_str)
		count+=1
	f.write("\n__SECTION B__:(Attempt any 4 Questions) \n")
	count=1
	length=len(section_b)
	list_range=random.sample(range(0,length),6)
	for x in list_range:
		temp_str=(str)(count)+")"+section_b[x]+"    [3]\n"
		f.write(temp_str)
		count+=1
	f.write("\n__SECTION C__:(Attempt any 2 Questions) \n")
	count=1
	length=len(section_c)
	list_range=random.sample(range(0,length),3)
	for x in list_range:
		temp_str=(str)(count)+")"+section_c[x]+"    [4]\n"
		f.write(temp_str)
		count+=1
	f.write("------------------------------------------------The End----------------------------------------------\n")
	f.close()
file.close()