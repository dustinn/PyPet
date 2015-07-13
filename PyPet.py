#Credits to: https://www.thinkful.com/learn/intro-to-python-tutorial/Conclusion-and-Resources#For-Loops
#First Program @Python featuring above tutorial (input,output,variable,dictionary,function,if-else statements, list,for loop)
# and some additional programming basics (while, or, break, str convertion, comment, global, to upper case)
#Python v2.7.10
#Note: this is a trash program from a trashgrammer

from sys import exit,stdin
from random import randint
print '\tWelcome to Pypet'

yourPet = ''
yourPetName = ''

#below are some samples of dictionaries @Python
cat = {
    'name': 'Garfield',
    'age': 6,
    'weight': 8.5,
    'hungry': True,
    'photo': '''\n\t _     _
    \t  |\\_,-~/
    \t / _  _ |    ,--.
    \t(  @  @ )   / ,-'
    \t \  _t_/-._( (
    \t /         `. \ 
    \t|         _  \ |
    \t \ \ ,  /      |
    \t  || |-_\__   /
    \t ((_/`(____,-'\n''',
    'asleep': True, 
}

mouse = {
    'name': 'Stuart',
    'age': 4,
    'weight': .8,
    'hungry': False,
    'photo': '''\n\t  )
    \t (__
    \t   )_
    \t(_)_(_)
    \t (o o)
    \t==\o/==\n''',
    'asleep': False
}

fox = {
    'name': 'Swiper',
    'age': 7,
    'weight': 13,
    'hungry': True,
    'photo':'''\n\t|\_/|,,_____,~~`
    \t(.".)~~     )`~}}
    \t \o/\ /---~\\ ~}}
    \t   _//    _// ~}\n''',
    'asleep': True
}

snoopy = {
    'name': 'Snoopy',
    'age': 5,
    'weight': 10,
    'hungry': False,
    'photo':  '''\n\t   ___.---
    \t / |  '     \         
    \t(  )         o  
    \t \_/-, ,----'            
    \t    ====      
    \t   /  \-'~;    
    \t  /  __/~|        
    \t=(___  _____|\n''',
    'asleep': False
}

bunny = {
    'name': 'Bugs Bunny',
    'age': 4,
    'weight': 4.4,
    'hungry': True,
    'photo':'''\n\t(\__/)
    \t(='.'=)
    \t(")_(")\n''',
    'asleep': True
}

petInfo = ''  #for my while loop at checking Pet infos. Repeating if the user input an unknown pet or being stupid
adopt = False #to know if the user already adopt a pet or not and will pick again from pet infos


#A sample function that ask if you want to adopt the pet. Python reads from top then starts memorizing, thats why you need to type the functions before you call them
def adoptPet(pet):
    print '\nDo you want to adopt this cute and lonely ' + pet['name'] + '. Type yes if you like to take home your new pet or no to choose another one.'
    petAdopt = raw_input('>> ')
    if petAdopt.upper() == 'YES':
        print 'Congratulations ' + pet['name'] + ' is now your pet. Take care of him.'
        global adopt #Python mostly understand variable as local variable so I need to make the variable adopt global for this function otherwise it will throw an error.
        global yourPetName
        adopt = True
        global yourPet
        if (pet['name'] == 'Garfield'):
            yourPet = 'cat'
            yourPetName = 'Garfield'
        elif (pet['name'] == 'Stuart'):
            yourPetName = 'Stuart'
            yourPet = 'mouse'
        elif (pet['name'] == 'Swiper'):
            yourPetName = 'Swiper'
            yourPet = 'fox'
        elif (pet['name'] == 'Snoopy'):
            yourPetName = 'Snoopy'
            yourPet == 'snoopy'
        elif (pet['name'] == 'Bugs Bunny'):
            yourPetName = 'Bugs Bunny'
            yourPet = 'bunny'
    elif petAdopt.upper() == 'NO':
        return
    else:
        print 
        adoptPet(pet)

print '\nWhat kind of pet do you want to adopt?'
while ((petInfo == 'cat' or 'mouse' or 'fox' or 'snoopy' or 'bunny')):
    print '\nType the info of the pet you want to know more about.\nYou can choose from cat, mouse, fox, snoopy, or bunny.'
    petInfo = raw_input('>> ')
    if petInfo == 'cat':
        print cat['photo']
        print '\tName:\t' + cat['name']
        print '\tAge:\t' + str(cat['age']) + ' yrs. old'
        print '\tWeight:\t' + str(cat['weight']) + ' lbs.'
        adoptPet(cat) #call adoptPet function
        if (adopt == True):
            break
    
    elif petInfo == 'mouse':
        print mouse['photo']
        print '\tName:\t' + mouse['name']
        print '\tAge:\t' + str(mouse['age']) + ' yrs. old'
        print '\tWeight:\t' + str(mouse['weight']) + ' lbs.'
        adoptPet(mouse)
        if (adopt == True):
            break
    
    elif petInfo == 'fox':
        print fox['photo']
        print '\tName:\t' + fox['name']
        print '\tAge:\t' + str(fox['age']) + ' yrs. old'
        print '\tWeight:\t' + str(fox['weight']) + ' lbs.'
        adoptPet(fox)
        if (adopt == True):
            break
        
    elif petInfo == 'snoopy':
        print snoopy['photo']
        print '\tName:\t' + snoopy['name']
        print '\tAge:\t' + str(snoopy['age']) + ' yrs. old'
        print '\tWeight:\t' + str(snoopy['weight']) + ' lbs.'
        adoptPet(snoopy)
        if (adopt == True):
            break
        
    elif petInfo == 'bunny':
        print bunny['photo']
        print '\tName:\t' + bunny['name']
        print '\tAge:\t' + str(bunny['age']) + ' yrs. old'
        print '\tWeight:\t' + str(bunny['weight']) + ' lbs.'
        adoptPet(bunny)
        if (adopt == True):
            break
    else:
        print 'You have chosen an unavailable pet. Kindly try again.'
        
pets = [cat,mouse,fox,snoopy,bunny]

def menu(pet):
    print '\n\t\tMenu'
    print '[1] Feed\t[2] Sleep\t[3] Talk\t[4] Exit'
    print pet['photo']
    menuCommand = '' 
    while (menuCommand == 1 or 2 or 3 or 4):
        menuCommand =raw_input('>> ')
        if (menuCommand == '1'):
            if pet['hungry'] == True:
                pet['hungry'] = False
                pet['weight'] += 1
                print pet['name']+' is now full. He now weighs ' + str(pet['weight']) +' lbs.' 
                menu(pet)
            else:
                print pet['name']+' is not hungry!'
                menu(pet)
        elif (menuCommand == '2'):
            if (pet['asleep'] == True):
                print pet['name'] +' is now awake.'
                pet['asleep'] = False
                menu(pet)
            else:
                print pet['name'] +' is now sleeping.'
                pet['asleep'] = True
                menu(pet)
        elif (menuCommand == '3'):
            chat = ['omnomom.','Hello, have a nice day!', 'Hi let\'s go outside.', 'How are you?']
            print '\t'+pet['name']+ ': ' +chat[randint(0,3)] #random
        elif (menuCommand == '4'):
            exit()
for pet in pets:
    if pet['name'] == yourPetName:
        menu(pet)     # Need to think of another way to access a dictionary from the list. This for statement sucks, i mean no fcking end.
    
#stdin.read(1) #stop the program from autoclosing, this will wait til user press enter.


