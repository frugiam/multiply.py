# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/07/2024
# Description: Project 2c

def multiply(num, n):
    if n == 1:
        return num
    else:
        return num + multiply(num, n-1)
