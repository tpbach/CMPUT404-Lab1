# CMPUT 404 - W22
# Lab 1
# Created by: tpbach

import requests

def main():
    response = requests.get("https://raw.githubusercontent.com/tpbach/CMPUT404-Lab1/master/lab1.py")
    print(response.text)

main()