# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r', encoding='utf-8')
animals_new = open('animals_new.txt', 'w', encoding='utf-8')
for animal in animals:
    if animal == 'turtle\n':
        animals_new.write(''.join(animal.rstrip('\n')))  
        break
    else:
        animals_new.write(''.join(animal.rstrip('\n')) + ' ')
animals_new.close()
animals.close()
