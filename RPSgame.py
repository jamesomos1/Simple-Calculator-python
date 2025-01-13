import random  #import for random generator

# Options for the computer move
opt = ("rock", "paper", "scissors")

# While loop to keep running game until player opts out
run = True
while run:

    # Call for computer's random choice
    computer = random.choice(opt)

    player = None
    # While(everlasting) loop if player doesn't input rock, paper, or scissors
    while player not in opt:
    # Player's input
        player = input('Enter an input (rock, paper, scissors): ')

    # Print statements
    print(f'Player: {player}')
    print(f'Computer: {computer}')


    # If statement functions

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print('You won the game!')
    elif player == "paper" and computer == "rock":
        print('You won the game!')
    elif player == "scissors" and computer == "paper":
        print('You won the game!')
    else:
        print('You lost the game. Sickening')

# Prompts player if they want to play again. .lower() means to lowercase user input
# playagain = input('Play again? (y/n): ').lower()
# if not playagain == 'y':
# Breaks us out of the loop if the player doesnt choose y

    if not input('Play again? (y/n): ') == 'y':
        run = False
print('Thanks for playing.')
