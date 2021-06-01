#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program formats an adress in the standart form


def adress_converter(name, street_number, street_name, city, province,
                     postal_code, apartment_number=None):
    # This function formats an adress in the standart form
    if apartment_number is not None:
        adress = name + "\n" + apartment_number + "-" + street_number + " "
        adress = adress + street_name + "\n" + city + " " + province + "  "
        adress = adress + postal_code
    else:
        adress = name + "\n" + street_number + " " + street_name + "\n" + city
        adress = adress + " " + province + "  " + postal_code

    return adress.upper()


def main():
    # Is the main function
    print("This program formats your address as a mailing address.\n")

    try:
        name = input("Insert your full name: ")
        apartment = input("Do you live in an apartment?(Y/n): ")
        if apartment[0].upper() == "Y":
            apartment_number = input("Insert your apartment number: ")
        street_number = input("Insert your street number: ")
        street_name = input("Insert your street name: ")
        city = input("Insert your city: ")
        province = input("Insert your province(as an abbreviation): ")
        postal_code = input("Insert your postal code(123 456): ")

        if apartment[0].upper() == "Y":
            adress = adress_converter(name, street_number, street_name,
                                      city, province, postal_code,
                                      apartment_number)
        else:
            adress = adress_converter(name, street_number, street_name,
                                      city, province, postal_code)

        print("\n{}".format(adress))
    except Exception:
        print("\nThe input is invalid, try again.")


if __name__ == "__main__":
    main()
