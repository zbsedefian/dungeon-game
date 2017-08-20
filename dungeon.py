import os
import random

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4) ]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)
    # global player, monster, door
    # monster = random.choice(CELLS)
    # door = random.choice(CELLS)
    # while door == monster:
    #     door = random.choice(CELLS)
    # player = list(random.choice(CELLS))
    # while player == monster or player == door:
    #     player = random.choice(CELLS)
    # return monster, door, player

def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        x -= 1
        print(player)
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    return x, y

def get_moves(player):
    global moves
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    return moves

def draw_map(player):
    print(" _"*5)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def game_loop():
    monster, player, door = get_locations()

    while True:
        draw_map(player)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))

        move = input("> ").upper()

        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                clear_screen()
                print("You touched the monster, which was at {}.".format(monster))
                for i in range(10):
                    print("You got eaten! >:(")
                input("Go home.")
                break
            if player == door:
                clear_screen()
                print(" *** You went out the door, which was at {}. You win. ***".format(door))
                for i in range(10):
                    print("You win!")
                break  
        else:
            input("\nCan't go that way. Press return.")
        clear_screen()

    move_player(player, move)
    

def main():
    print("Welcome to the dungeon!")
    print("One monster and one door -- invisible to you -- are in the dungeon.")
    print("You must navigate to the door while avoiding the monster.")
    print("Enter QUIT at any time to quit")
    input("Press return to start")
    clear_screen()
    game_loop()

main() 