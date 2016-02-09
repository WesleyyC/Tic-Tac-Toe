import tic_tac_toe
import RPi.GPIO as GPIO
import time

# Look-up table for GPIO ports
# This may vary depending on how you wire up your circuit
red = {(0, 0): 26, (0, 1): 6, (0, 2): 5, (1, 0): 9, (1, 1): 27, (1, 2): 17, (2, 0): 20, (2, 1): 16, (2, 2): 8}
green = {(0, 0): 19, (0, 1): 13, (0, 2): 11, (1, 0): 10, (1, 1): 22, (1, 2): 4, (2, 0): 21, (2, 1): 12, (2, 2): 7}
buttons = {'fw': 0, 'bk': 1, 'ok': 2}

def light_up_led(activePlayer, coordinate):
    if activePlayer == tic_tac_toe.USER:
        led = green[coordinate]
    else:
        led = red[coordinate]

    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 1)

######################################################################
#####################         Main Function        ###################
######################################################################
def main():
    # Prepare
    winner = tic_tac_toe.UNKNOWN

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Starter
    print "Welcome to the tic tac toe game!"

    # Loop
    while winner == tic_tac_toe.UNKNOWN and tic_tac_toe.count != 9:
        if tic_tac_toe.count % 2 == tic_tac_toe.isComputerFirst:
            tic_tac_toe.printBoard()
            newCoordinate = tic_tac_toe.userMove()
            light_up_led(tic_tac_toe.USER, newCoordinate)
        else:
            newCoordinate = tic_tac_toe.programMove()
            light_up_led(tic_tac_toe.COMPUTER, newCoordinate)

        winner = tic_tac_toe.checkWinner(newCoordinate)

    print ''

    if winner == tic_tac_toe.USER:
        print "You Win! And please report you strategy to the author!"
    elif winner == tic_tac_toe.COMPUTER:
        print "The Computer Wins!"
    else:
        print "It's a tie!"

    tic_tac_toe.printBoard()

    GPIO.cleanup()


if __name__ == '__main__':
    main()




