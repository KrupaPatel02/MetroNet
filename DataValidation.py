import json
import re
from collections import defaultdict


errors = []


def validEmail(email):
    """
    Validates email value with the regular expression
    :param email:
    :return: 1 for Valid, 0 for InValid
    """
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        return 1
    else:
        return 0


def validPhone(phone):
    """
    Validates phone number with regular expression
    :param phone:
    :return: 1 for Valid, 0 for Invalid
    """
    regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s-]\d{3}[\s-]\d{4}$'
    if re.search(regex, phone):
        return 1
    else:
        return 0


def listContact(data):
    """
    Lists out all Contact records with output :
    - Output "Valid" if both email and phone are valid.
    - Output "Email is invalid." if email is invalid and phone is valid.
    - Output "Phone is invalid." if phone is invalid and email is valid.
    - Output "Email and Phone are invalid." if both phone and email are invalid.

    :param data: list passed from Contacts.json after loading and sorting it by Contact Name in ascending order
    :return: prints Validation messages
    """

    print("LIST OUT ALL CONTACT RECORDS WITH ERRORS : ")
    for i in range(len(data)):
        print("Name: " + data[i]['name'])
        ve = validEmail(data[i]['email'])
        pe = validPhone(data[i]['phone'])
        if ve == 1 and pe == 1:
            print("Valid")
            citywithErrors(data[i]['city'], 0)
        elif ve == 0 and pe == 1:
            print("Email is invalid")
            citywithErrors(data[i]['city'], 1)
        elif ve == 1 and pe == 0:
            print("Phone is invalid")
            citywithErrors(data[i]['city'], 1)
        else:
            print("Email and Phone are invalid")
            citywithErrors(data[i]['city'], 2)
        print("\n")


def listCity(city_data):
    """
    Lists out each city name and number of validation errors
    :param city_data: list passed with tuples(city, num_of_errors)
    :return: prints final output after sorting it by number of validation errors in descending order
    """
    print("*"*50, end='\n\n')
    print("LISTS OUT ALL CITIES WITH NUMBER OF VALIDATION ERRORS : ")
    final_city_data = defaultdict(int)
    for k, v in city_data:
        final_city_data[k] += v
    # print(final_city_data)
    final_city_data = sorted(final_city_data.items(), key=lambda x: x[1], reverse=True)
    for k,v in final_city_data:
        print("City Name: " + k)
        print("Number of Validation errors {}".format(v))
        print("\n")


def citywithErrors(city, num_of_errors):
    """
    Appends the contact records having errors with there city names in list
    :param city: city_name
    :param num_of_errors: number of errors
    :return: appends to list "errors"
    """
    # print(city)
    # print(num_of_errors)
    errors.append((city, num_of_errors))


with open('Contacts.json', 'r') as file:
    data = json.load(file)
    data = sorted(data, key=lambda x: x['name'])
    print(type(data))
    listContact(data)
    listCity(errors)
