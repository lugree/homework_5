from datetime import datetime
import os
from random_words import random_list


# 1. Write a function that sorts a list in ascending. Additionally, the function may take a keyword argument that will
# reverse the sort.
# Գրել ֆունկցիա, որը կվերադարձնի վերցված լիստի աճման կարգով սորտավորված տաարբերակը։ Կարող եք ավելացնել keyword արգումենտ
# որը փոփոխելով կստանանք լիստը սորտավորված նվազման կարգով։

# def list_sort(li, keyword):
#     li.sort(reverse=keyword)
#     return li
#
#
# print(list_sort([3, 6, 1, 9, 7, 5], False))


# 2. Write a function which will take a list as an argument. If the list is monotonic, return True. Return False
# otherwise.
# Գրել ֆունկցիա, որը կվերադարձնի True, եթե տրված լիստը մոնոտոն է, և False` հակառակ դեպքում։



"""MODULES"""

# 1. Hangman!
# Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# length of the word.

# Guess a letter!
# _ _ _
#
# if we input 'a', the program will output:

# Guess a letter!
# _ a _

# and so on.

# Ստեղծում ենք մեր սեփական "Կախաղան" խաղը։ Ծրագիրը պահելու է պատահական բառ տրված "random_words" ֆայլից: Խաղացողը պետք է
# գուշակի տառ։ Եթե տառը բառի մեջ գոյություն չունի, խաղացողը կորցնում է "կյանք" (կյանքերը բառի երկարության չափ են): Եթե
# տառը կա, այն բացվում է և խաղացողը անցնում է հաջորդ տառը գուշակելուն։ Ծրագրի աշխատանքը պետք է հետևյալ տեսքն ունենա։
# Ենթադրենք բառը car է։ Կոնսոլում հետևյալ տեսքստն ենք տեսնելու

# Guess a letter!
# _ _ _

# Եթե ներմուծենք a, կստանանք հետևյալ տեսքստը

# Guess a letter!
# _ a _

# և այդպես շարունակ։ Եթե խաղացողի կյանքերը սպառվեն, տեղեկացրեք նրան և խաղից դուրս եկեք։ Հաղթելու դեպքում տպեք
# շնորհավորանք

# 2. Write a function that will return the longest word in the random words file from the previous exercise.
# Գրել ֆունկցիա, որը կվերադարձնի "random_words" ֆայլի ամենաերկար բառը։

# def longest_word():
#     max_word = ''
#     for i in random_list:
#         if len(max_word) < len(i):
#             max_word = i
#     return max_word
#
#
# print(longest_word())

# 3. Write a function that will take a string containing the path to a file as an argument and return its size in
# kilobytes.
# Գրել ֆունկցիա, որը կվերցնի սթրինգ արգումենտ։ Սթրինգը պետք է լինի որոշակի ֆայլի path-ը։ Ապա վերադարձնել այդ ֆայլի
# չափսերը կիլոբայթերով։ Հուշում՝ օգտվել os մոդուլից:


# def get_file_size(path):
#     size_in_bytes = os.path.getsize(path)
#     return size_in_bytes/1024
#
#
# print(get_file_size(r"C:\Users\Admin\PycharmProjects\pythonProject2\homework_5.py"))


# 4. Create a random number generator without using random module. The implementation is up to you. You may use
# current timestamp as a random seed.
# Գրել ֆունկցիա, որը կվերադարձնի պատահական թիվ։ Պատահական թվերի գեներատոր պարունակող մոդուլ չօգտագործել։ Իմպլեմենտացիան
# կախված է ձեզնից։ Մտածեք որոշակի ալգորիթմ և ըստ դրա գեներացրեք թիվ։ Կարող եք օգտագործել մեր անցած seed-ի գաղափարը։

# 5. Create a file and put your shopping list in it. The file must start with current day's date.
# Ստեղծել ֆայլ, որը կպահի ձեր գնումների ցուցակը (ինչ ապրանք։ քանի հատ)։ Ֆայլը պետք է սկսվի տվյալ օրվա ամսաթվով։

# 6. Create a function that will take two datetime objects as parameters and return the difference in days between
# these dates.
# Գրել ֆունկիա, որը կվերցնի երկու datetime տիպի պարամետրեր և կվերադարձնի այդ ամսաթվերի միջև տարբերությունը օրերով։

# def date_diff(date_1, date_2):
#     d_1 = datetime.strptime(date_1, '%d/%m/%Y')
#     d_2 = datetime.strptime(date_2, '%d/%m/%Y')
#     delta = abs(d_2 - d_1)
#     return delta.days
#
#
# print(date_diff('03/07/2022', '05/10/2021'))
# print(datetime.strptime('03/07/2022', '%d/%m/%Y'))