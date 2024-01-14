import pandas as pd
import random as rd

global item


class Bakery:
    global item

    def __init__(self,token,password):
        self.token_number=token
        self.email=password

    def product(self, cake_name, price):
        return cake_name,price
    def ID(self,name,email):
        return name,email

    def already_token(self,token_ID):
        swap_tk=self.token_number
        swap_email=swap_tk

        if token_ID==swap_email:
            print(f'You order for {item} with Price {price_}.')


        else:
            print("Not valid Token number")




    def token_generate(self):
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'Z']
        index1 = rd.randint(0, 5)
        index2 = rd.randint(6, 11)
        rnd = rd.randint(100 * 3, 100 ** 6)
        t1 = letter[index1]
        t2 = letter[index2]
        self.token_number = t1 + t2 + str(rnd)

    def token(self):
        pass

    def ThankYou(self):
        main_token=self.token_number
        wish=f"Good wish {username}. You Orderd for {item} with Price {price_}.\nThanks For Visiting.\nVed Bakery."
        print(f'You got your token id {main_token}')
        print(wish)






    def stars(self):
        for i in range(2):
            i -= 1
            print('    *' * 10)
            if (i % 2 == 0):
                print('    *' * i)
    def start(self):
        print('\nA :- Chocolate\n',
              '\nB :-Angel cake \n',
              '\nC :-Banana cake \n',
              '\nD :-Butter cake \n',
              '\nE :-Coconut cake \n',
              '\nF :-Genoise \n',
              )





Bakery.stars(Bakery)
print('      -:Welcome To Ved bakery and Cake center:-   ')
Bakery.stars(Bakery)





cakes = {
    'A': 'Chocolate cake',
    'B': 'Angel cake ',
    'C': 'Banana cake ',
    'D': 'Butter cake',
    'E': 'Coconut cake ',
    'F': 'Genoise',
}

price = {
    'A': 600,
    'B': 230,
    'C': 400,
    'D': 550,
    'E': 120,
    'F': 150,
}
order=''
users=20
price_ = 0

while(users>=1):

    users-=1
    tkn=int(input("Already have Token, press '0'. else '1' "))
    username=''
    email=''

    if tkn==0:
        token_ID=input("Enter token ID: ")
        Bakery.already_token(Bakery,token_ID)

    elif(tkn==1):
        username=input("name: ")
        email=input("E-mail: ")



        Bakery.start(Bakery)

        num_of_cake=int(input("How many cake do you want ? "))
        for i in range(num_of_cake):
            order = input("Which Cakes     Note:-(Use Alphabets) ")
            if order == 'a' or 'A':
                price_ += 600
            elif order == 'b' or 'B':
                price_ += 100
            elif order == 'b' or 'C':
                price_ += 100
            elif order == 'b' or "D":
                price_ += 100
            elif order == 'b' or "E":
                price_ += 100
            elif order == 'b' or "F":
                price_ += 100

            else:
                price_ += 0

            print(f'Your order price is {price_}')



        item = cakes[order.capitalize()]



        Bakery.product(Bakery,cake_name=item,price=price_)
        Bakery.token_generate(Bakery)
        Bakery.ID(Bakery,username,email)
        Bakery.ThankYou(Bakery)

    else:
        print('Give valid Option.')