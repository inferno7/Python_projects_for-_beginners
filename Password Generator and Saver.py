import random
import sys



print("Welcome to password Generator and Saver!!")

x = int(input("Please chose from one of the following :\n 1 . Create a Password \n 2 . Store a password \n 3 . Display Your stored passwords \n"))

if x==1 :
    y = int(input("Please chose from one of the following : \n 1 . Hexadecimal Password \n 2 . n-pin Password \n"))

    if y==1 :

        keylist = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        password = []
        length = 8

        while len(password) < length:
            a_char = random.choice(keylist)
            password.append(a_char)
        print("The randomly generated password is : \t")
        print(''.join(password))

    elif y==2 :

        keylist = '0123456789'
        password = []
        length = int(input("Please enter the length of the password you desire :"))

        while len(password) < length:
            a_char = random.choice(keylist)
            password.append(a_char)
        print("The randomly generated password is : \t")
        print(''.join(password))

    else :
        print("PLease chose the correct response!!")

elif x==2 :

    pass_name = str(input("Please enter the reference name for the password :\n"))

   # file_name = input("Please enter the file name: \n")

    pass_pass = input("Please enter the password : \n")

    pass_pass1 = input("Please enter the password again : \n")

    if pass_pass == pass_pass1 :

        #file_name = raw_input("Please enter the file name to be saved : \n")
        filename = input("Please enter the file name : \n")+ '.txt'
        fw = open(filename, 'a')

        fw.write('\n \n \t \t \t \t \t \t \t \t \t Welcome to password Storer : \n \n \n')
        fw.write('\n The details are as follows :')
        fw.write('\n Reference name :  ')
        fw.write( pass_name )
        fw.write("\n Password :  ")
        fw.write( pass_pass )
        fw.write('\n \n \n \n \n \n \n \nThank you for using Password Generator and Saver')
        fw.close()



    else :
        print("Password and Confirm password are not matching!!! Please try again!!")


elif x==3 :

    file_name = input("Please enter the file name to open : \n")

    fr = open(file_name + '.txt', 'r')

    text = fr.read()

    print(text)

    fr.close()







