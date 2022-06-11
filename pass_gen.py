from random import randint, choice, shuffle

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# easy way- format: alphabets-numeric-special characters
def new_pass():
    pwd_letters = [choice(alphabets) for _ in range(randint(3, 7))]
    pwd_numbers = [choice(numbers) for _ in range(randint(3, 7))]
    pwd_symbols = [choice(characters) for _ in range(randint(3, 7))]
    pwd_list = pwd_letters+pwd_numbers+pwd_symbols
    shuffle(pwd_list)
    easy_pwd = ''.join(pwd_list)
    return easy_pwd
