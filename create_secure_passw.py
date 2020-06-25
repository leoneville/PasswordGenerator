import string
import random
import pyperclip
import os
from time import sleep


class PasswordGenerator:
    def __init__(self):
        self.site = ''
        self.size = 0

    def start(self):
        self.dados_collector()
        self.create_password()


    def dados_collector(self):
        try:
            self.site = str(input('which site do you want to create a password for? (ex: www.facebook.com)\n--> '))
            self.size = int(input('How long is the password?\n--> '))
        except ValueError:
            os.system('cls')
            print('Only int numbers !!')
            sleep(3)
            os.system('cls')
            self.dados_collector()


    def create_password(self):
        dots = string.punctuation
            # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        letters = string.ascii_letters
            # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

        characters = dots + letters

        password = ''.join(random.sample(characters, self.size))

        arq = open('passwords.txt','a')
        arq.write(self.site + ' : ' + password)
        arq.write('\n')
        arq.close()

        pyperclip.copy(password)
        print('\nPassword: {}'.format(password))
        print('\nPassword copied to clipboard.')
        a = input('\n\nPress ENTER to close the window')


Password = PasswordGenerator()
Password.start()