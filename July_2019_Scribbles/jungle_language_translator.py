'''
Jungle Language

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

consonants -> 'consonant' + 'a'

'''


def translate():
    translation = ''
    count = 0
    try:
        while True:
            phrase = input('Enter phrase: ')    
            for letter in phrase:
                if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
                    translation = translation + letter + 'a'
                elif letter.lower() in 'a':
                    translation = translation + '1'
                elif letter.lower() in 'e':
                    translation = translation + '2'
                elif letter.lower() in 'i':
                    translation = translation + '3'
                elif letter.lower() in 'o':
                    translation = translation + '4'
                elif letter.lower() in 'u':
                    translation = translation + '5'
                else:
                    translation = translation + letter
            print(translation)
            translation = ''
            count += 1
    except KeyboardInterrupt:
        exit_prompt = input('\nExit Translator? (Y/N): ')
        if exit_prompt.lower() in 'y':
            SystemExit()
        elif exit_prompt.lower() in 'n':
            translate()
        else:
            print('Invalid Selection\n')
            translate()


print('JUNGLE LANGUAGE TRANSLATOR 1.3\n(C)2019 Gideon Anyalewechi\n\nTo exit, press CTRL+C and hit ENTER\n')
translate()