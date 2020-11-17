import random

user_choice = input('choose a random number between 0 to 10 :-')
rand_num_gen = random.randint(0,10)

if user_choice == rand_num_gen:
    print(rand_num_gen)
    print('congratulations!! you matched the number.')
else:
    print(rand_num_gen)
    print('Better Luck Next Time!!')