from random import randint

# Method that asks for the number
def ask_for_number():
    random_number = randint(0, 10)
    valid = False

    while not valid:
        number = input('\n¿En qué número del 1 al 10 estoy pensando? ')

        try:
            if 10 < int(number) < 0:
                raise ValueError
            elif int(number) == random_number:
                print('Enhorabuena! Lo adivinaste')
                valid = True
            else:
                print('No tienes ni idea jajaja. ¡Inténtalo de nuevo!')

        except ValueError:
            print('Debes escribir un número entre el 1 y el 10')


# Method that welcomes the player.
def welcome_text():
    valid = False

    while not valid:
        response = input('¡Hola! Bienvenido al juego de la adivinanza. ¿Quieres jugar? Escribe "si" o "no": ')

        if response.lower() == 'si':
            valid = True
        elif response.lower() == 'no':
            print('Bueno pues nada, ¡ABURRIDO!')
            exit()


welcome_text()
ask_for_number()

