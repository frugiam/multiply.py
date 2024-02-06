# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/07/2024
# Description: Project 5a

def multiply(num, n):
    if n == 1:
        return num
    else:
        return num + multiply(num, n-1)