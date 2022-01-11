from battleships import *

sea = [['.'] * 10 for __ in range(10)]

    
def mark_hits(fleet):
    for ship in fleet:
        for fire in ship[4]:
            row, column = fire[0], fire[1]
            if is_sunk(ship):
                sea[row][column] = ship_type(ship)[:1] #if the ship is sunk, all the hits (the size of the ship) take form of the first letter of the ship's type
            else:
                sea[row][column] = '*' #if the ship is hit but not sunk, the hit changes the sea square from initial '.' to '*'
                
                
def draw_sea():
  print('  ' + ' '.join([str(i) for i in list(range(1))]))
  for i in range(len(sea)):
    print(sea[i][j], end=' ')
    print()
    

current_fleet = randomly_place_all_ships()
game_over = False
shots = 0

while not game_over:
    mark_hits(current_fleet)
    draw_sea()
    current_row, current_column = check_input()
    if current_row == -1:
        print('Player terminated the game.')
        break
    hit(current_row, current_column, current_fleet)
    shots += 1
    if check_if_hits(current_row, current_column, current_fleet):
        print('You have a hit!')
        (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
        if is_sunk(ship_hit):
            print('You sank a ' + ship_type(ship_hit) + "!")
    else:
        print('You missed!')
        sea[current_row][current_column] = '-'
    if not are_unsunk_ships_left(current_fleet):
        game_over = True
else:
    mark_hits(current_fleet)
    draw_sea()
    print(f'The game is over, you required {shots}. Your score is {int((100 - shots) ** 2)}')
