def cheek_the_level_of_water(water, planet_name):
    if water == 20:
        planet_name = '20%воды.png'
    elif 30 <= water <= 40:
        planet_name = '40%воды.png'
    elif 40 <= water <= 60:
        planet_name = '60%воды.png'
    elif 60 <= water <= 80:
        planet_name = '80%воды.png'
    elif 90 <= water <= 100:
        planet_name = '100%воды.png'
    return water, planet_name


def cheek_temperature(temperature, planet_name, previous_planet_name):
    if temperature <= 30:
        planet_name = 'снежная_планета.png'
    elif temperature > 30 and planet_name == 'снежная_планета.png':
        planet_name = previous_planet_name
    return temperature, planet_name, previous_planet_name


def change_on(name):
    planet_name = name
    return planet_name