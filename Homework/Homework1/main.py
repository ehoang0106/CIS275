from Customer import *


def main():

    khoa = Customer("Khoa Hoang", True)
    ethan = Customer("Ethan Nguyen", False)
    anh = Customer("Anh Hoang", True)


    khoa.make_purchase("Snack Lays classic", 5.3)
    khoa.make_purchase("Tylenol ", 25.3)
    khoa.make_purchase("Cup Noodle", 2.5)


    ethan.make_purchase("Pencil", 8.0)
    ethan.make_purchase("Ruler", 5.3)
    ethan.make_purchase("Construction paper", 12.5)


    anh.make_purchase("Napkin", 30.0)
    anh.make_purchase("TH True Milk", 7.5)

    
    print(khoa)
    print(ethan)
    print(anh)
    
main()