with open('planets.txt', 'w', encoding='utf-8') as file:
    for planet in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        file.writelines(planet + '\n')
