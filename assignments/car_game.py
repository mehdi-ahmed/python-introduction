started = False

while True:
    car_game = input('> ').lower()
    if car_game == 'quit':
        break
    elif car_game == 'help':
        print("""
            start - to start the car
            stop  - to stop the car
            quit  - to exit""")

    elif car_game == 'stop':
        if not started:
            print('Car already stopped..')
        else:
            print('Car stopped..')
            started = False
    elif car_game == 'start':
        if started:
            print('Car already started ! ')
        else:
            print('Car started..Ready to go ! ')
            started = True
    else:
        print('I cannot understand that !')
