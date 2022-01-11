from random import randint, choice 


def ship_type(ship):
    length = ["battleship", "cruiser", "destroyer", "submarine"]
    return length[ship[3] - 1]


def is_sunk(ship):
    return len(ship[4]) == ship[3]


def is_open_sea(row, column, fleet):
    check_coord_list = []  # list that will contain checked squares
    for i in range(column - 1, column + 2):
        if 0 <= i <= 9:
            for j in range(row - 1, row + 2):
                if 0 <= j <= 9 and (column, row):
                    check_coord_list.append((j, i))
    fleet_area = []  # squares taken up by the fleet
    for ship in fleet:
        ship_row, ship_column, ship_horizontal, ship_length, ship_hits = ship[0], ship[1], ship[2], ship[3], ship[4]
        if ship_horizontal:
            for i in range(ship_column, ship_column + ship_length):
                fleet_area.append((ship_row, i))
        else:
            for i in range(ship_row, ship_row + ship_length):
                fleet_area.append((i, ship_column))
        for hits in ship_hits:  # deleting squares that received a hit
            fleet_area.remove(hits)
    res = True
    for square in fleet_area:
        if square in check_coord_list:
            res = False
    return res


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    check = column if horizontal else row  # condition to check if horizontal
    if check + length > 9:  # is there enough space in the sea for the ship
        return False
    if horizontal:
        for i in range(column, column + length):
            if not is_open_sea(row, i, fleet):
                return False
    else:
        for i in range(row, row + length):
            if not is_open_sea(i, column, fleet):
                return False
    return True


def place_ship_at(row, column, horizontal, length, fleet):
    if ok_to_place_ship_at(row, column, horizontal, length, fleet):
        fleet.append((row, column, horizontal, length, set()))
    return fleet


def randomly_place_all_ships():
    fleet = []
    for i in range(1, 5):  # will be used to calculate the length of the type of ship: 5-i
        for j in range(i):   # max number of ships that is allowed of that type
            try_add = False
            while try_add is not True:
                row, column, horizontal, length = randint(0, 9), randint(0, 9), choice([True, False]), 5 - i
                if ok_to_place_ship_at(row, column, horizontal, length, fleet):
                    place_ship_at(row, column, horizontal, length, fleet)
                    try_add = True
    return fleet


def check_if_hits(row, column, fleet):
    busy_set = set()
    for ship in fleet:
        row_ship, column_ship, horizontal, length = ship[0], ship[1], ship[2], ship[3]
        if horizontal:
            for i in range(column_ship, column_ship + length):
                busy_set.add((row_ship, i))
        else:
            for i in range(row_ship, row_ship + length):
                busy_set.add((i, column_ship))
    return (row, column) in busy_set


def hit(row, column, fleet):
    if check_if_hits(row, column, fleet):
        for ship in fleet:
            ship_set = set()
            row_ship, column_ship, horizontal, length = ship[0], ship[1], ship[2], ship[3]
            if horizontal:
                for i in range(column_ship, column_ship + length):
                    ship_set.add((row_ship, i))
            else:
                for i in range(row_ship, row_ship + length):
                    ship_set.add((i, column_ship))
            if (row, column) in ship_set:
                ship[4].add((row, column))
                return fleet, ship


def are_unsunk_ships_left(fleet):
    for ship in fleet:
        if len(ship[4]) != ship[3]:
            return True
    return False


def check_input():
    loc_str = input('Enter column and row for the shot (separated by space), or esc to exit the game: ')
    if loc_str == 'esc':
        return -1, 0
    if len(loc_str) != 3 or loc_str[1] != ' ' or not loc_str[0].isdigit() or not loc_str[2].isdigit():
        print('Incorrect input format.')
        return check_input()
    else:
        return int(loc_str[0]), int(loc_str[2])


def main():
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0

    while not game_over:

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
        if not are_unsunk_ships_left(current_fleet):
            game_over = True
    else:
        print(f'The game is over, you required {shots}')


if __name__ == '__main__': 
   main()
