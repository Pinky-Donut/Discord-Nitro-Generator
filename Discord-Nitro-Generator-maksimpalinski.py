import string
import random
import webbrowser

def random_string(length=15, uppercae=True, lowercase=False, numbers=True):
    character_set = ''
    if uppercae:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits
    return ''.join(random.choice(character_set) for i in range(length))

print('\n')
print("\n              maksimpalinski's Discord Nitro Generator\n")
print('                             maksim#1337\n')
print('\n')
amount = input('Enter number of links to generate(not more than 150): ')

if amount.isdigit():
    if int(amount) > 1:
        prefix = 'https://discord.gift/'
        f = open('discord_keys.txt','a')
        for i in range(int(amount)):
            generation = random_string(length=8, uppercae=True, lowercase=True, numbers=False)
            discord_key = prefix + generation
            f.write(discord_key + '\n')

        f.close()

        open_links = input('Should the Bot test the links?(y/n): ')
        if open_links == 'y':

            with open('discord_keys.txt') as f:
                for line in f:
                    webbrowser.open(line)

            print('\nDone!\n')
            print("Check out Discord! maksim#1337\n")

        else:
            print('\nDone!\n')
            print("Check out Discord! maksim#1337\n")

else:
    print('need to use a number!')
