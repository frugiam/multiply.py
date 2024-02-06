#Author: Michelle Frugia
#GitHub username: frugiam
#Date: 02/07/2024
#Descrtiption: Project 5a

def multiply(num, n):
    # if n == 1 then return num --> base condition
    if n == 1:
        return num
    else:
        # recursively multiply the number until 1
        return num + multiply(num, n-1)
print(multiply(7,4))
