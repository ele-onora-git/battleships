import pytest
from battleships import *


def test_is_sunk1():  # vertical cruiser
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) is True

    
def test_is_sunk2():  # horizontal battleship
    s = (4, 2, True, 4, {(4, 2), (4, 3), (4, 4), (4, 5)})
    assert is_sunk(s) is True


def test_is_sunk3():  # horizontal submarine
    s = (9, 0, True, 1, {(9, 0)})
    assert is_sunk(s) is True


def test_is_sunk4():  # vertical destroyer
    s = (0, 8, False, 2, {(0, 8), (1, 8)})
    assert is_sunk(s) is True


def test_is_sunk5():  # vertical submarine
    s = (2, 5, False, 1, {(2, 5)})
    assert is_sunk(s) is True


def test_ship_type1():  # vertical battleship
    s = (6, 2, False, 1, {(6,2)})
    assert ship_type(s) == 'battleship'

    
def test_ship_type2():  # horizontal battleship
    s = (0, 0, True, 1, {(0,0)})
    assert ship_type(s) == 'battleship'
    

def test_ship_type3():  # vertical cruiser
    s = (2, 0, False, 2, {(2,0), (3,0)})
    assert ship_type(s) == 'cruiser'
    

def test_ship_type4():  # horizontal destroyer
    s = (8, 3, True, 3, {(8,3), (8,4), (8,5)})
    assert ship_type(s) == 'destroyer'
    

def test_ship_type5():  # vertical submarine
    s = (6, 9, False, 4, {(6,9), (7,9), (8,9), (9,9)})
    assert ship_type(s) == 'submarine'
    

def test_is_open_sea1():
    r = 0
    c = 0
    ship1 = 0, 2, True, 1, {}
    ship2 = 0, 8, True, 1, {}
    ship3 = 4, 3, True, 1, {}
    ship4 = 9, 1, True, 1, {}
    ship5 = 3, 6, False, 2, {}
    ship6 = 7, 1, True, 2, {}
    ship7 = 8, 4, True, 2, {}
    ship8 = 4, 8, False, 3, {}
    ship9 = 6, 4, True, 3, {}
    ship10 = 2, 1, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(r, c, f) is True


def test_is_open_sea2():
    r = 9
    c = 9
    ship1 = 1, 2, True, 1, {}
    ship2 = 2, 9, True, 1, {}
    ship3 = 4, 0, True, 1, {}
    ship4 = 8, 1, True, 1, {}
    ship5 = 3, 5, False, 2, {}
    ship6 = 9, 3, True, 2, {}
    ship7 = 7, 6, False, 2, {}
    ship8 = 4, 2, False, 3, {}
    ship9 = 4, 9, False, 3, {}
    ship10 = 0, 5, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(r, c, f) is True


def test_is_open_sea3():
    r = 0
    c = 9
    ship1 = 3, 8, True, 1, {}
    ship2 = 4, 6, True, 1, {}
    ship3 = 8, 4, True, 1, {}
    ship4 = 8, 6, True, 1, {}
    ship5 = 0, 0, True, 2, {}
    ship6 = 7, 0, True, 2, {}
    ship7 = 5, 4, False, 2, {}
    ship8 = 3, 0, False, 3, {}
    ship9 = 6, 6, True, 3, {}
    ship10 = 2, 3, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(r, c, f) is True


def test_is_open_sea4():
    r = 1
    c = 3  
    ship1 = 0, 0, True, 1, {}
    ship2 = 3, 2, True, 1, {}
    ship3 = 3, 4, True, 1, {}
    ship4 = 5, 5, True, 1, {}
    ship5 = 0, 7, True, 2, {}
    ship6 = 5, 8, False, 2, {}
    ship7 = 8, 6, True, 2, {}
    ship8 = 2, 6, True, 3, {}
    ship9 = 9, 2, True, 3, {}
    ship10 = 2, 0, False, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(r, c, f) is True


def test_is_open_sea5():
    r = 0
    c = 0  
    ship1 = 0, 2, True, 1, {}
    ship2 = 2, 0, True, 1, {}
    ship3 = 9, 2, True, 1, {}
    ship4 = 0, 6, True, 1, {}
    ship5 = 4, 6, True, 2, {}
    ship6 = 9, 7, True, 2, {}
    ship7 = 0, 4, False, 2, {}
    ship8 = 2, 2, False, 3, {}
    ship9 = 4, 0, False, 3, {}
    ship10 = 7, 4, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(r, c, f) is True


def test_ok_to_place_ship_at1():
    r = 6
    c = 2
    h = True
    l = 4
    ship1 = 1, 3, True, 1, {}
    ship2 = 9, 0, True, 1, {}
    ship3 = 9, 8, True, 1, {}
    ship4 = 9, 5, True, 1, {}
    ship5 = 1, 6, True, 2, {}
    ship6 = 3, 1, False, 2, {}
    ship7 = 5, 8, False, 2, {}
    ship8 = 3, 3, True, 3, {}
    ship9 = 1, 9, False, 3, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(r, c, h, l, f) is True


def test_ok_to_place_ship_at2():
    r = 0
    c = 0
    h = True
    l = 1
    ship1 = 9, 0, True, 1, {}
    ship2 = 9, 8, True, 1, {}
    ship3 = 9, 5, True, 1, {}
    ship4 = 1, 6, True, 2, {}
    ship5 = 3, 1, False, 2, {}
    ship6 = 5, 8, False, 2, {}
    ship7 = 3, 3, True, 3, {}
    ship8 = 1, 9, False, 3, {}
    ship9 = 6, 2, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(r, c, h, l, f) is True


def test_ok_to_place_ship_at3():
    r = 5
    c = 8
    h = False
    l = 2
    ship1 = 1, 3, True, 1, {}
    ship2 = 9, 0, True, 1, {}
    ship3 = 9, 8, True, 1, {}
    ship4 = 9, 5, True, 1, {}
    ship5 = 1, 6, True, 2, {}
    ship6 = 3, 1, False, 2, {}
    ship7 = 3, 3, True, 3, {}
    ship8 = 1, 9, False, 3, {}
    ship9 = 6, 2, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(r, c, h, l, f) is True


def test_ok_to_place_ship_at4():
    r = 1
    c = 5
    h = True
    l = 4
    f = []
    assert ok_to_place_ship_at(r, c, h, l, f) is True


def test_ok_to_place_ship_at5():
    r = 0
    c = 0
    h = True
    l = 2
    ship1 = 6, 2, True, 4, {}
    f = [ship1]
    assert ok_to_place_ship_at(r, c, h, l, f) is True
    

def test_place_ship_at1():
    r = 0
    c = 3
    h = True
    l = 3
    ship1 = 8, 8, True, 1, {}
    ship2 = 6, 5, True, 1, {}
    ship3 = 5, 8, True, 1, {}
    ship4 = 9, 0, True, 1, {}
    ship5 = 2, 0, True, 2, {}
    ship6 = 9, 3, True, 2, {}
    ship7 = 4, 0, False, 2, {}
    ship8 = 4, 2, False, 3, {}
    ship9 = 3, 5, True, 4, {}
    ship10 = r, c, h, l, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert place_ship_at(r, c, h, l, f) == [(8, 8, True, 1, {}), (6, 5, True, 1, {}),
                                            (5, 8, True, 1, {}), (9, 0, True, 1, {}),
                                            (2, 0, True, 2, {}), (9, 3, True, 2, {}),
                                            (4, 0, False, 2, {}), (4, 2, False, 3, {}),
                                            (3, 5, True, 4, {}), (0, 3, True, 3, {})]


def test_place_ship_at2():
    r = 3
    c = 5
    h = True
    l = 4
    ship1 = r, c, h, l, {}
    f = [ship1]
    assert place_ship_at(r, c, h, l, f) == [(3, 5, True, 4, {})]


def test_place_ship_at3():
    r = 9
    c = 0
    h = True
    l = 1
    ship1 = 8, 8, True, 1, {}
    ship2 = r, c, h, l, {}
    f = [ship1, ship2]
    assert place_ship_at(r, c, h, l, f) == [(8, 8, True, 1, {}), (9, 0, True, 1, {})]


def test_place_ship_at4():
    r = 2
    c = 1
    h = True
    l = 4
    ship1 = 0, 2, True, 1, {}
    ship2 = 0, 8, True, 1, {}
    ship3 = 4, 3, True, 1, {}
    ship4 = 9, 1, True, 1, {}
    ship5 = 3, 6, False, 2, {}
    ship6 = 7, 1, True, 2, {}
    ship7 = 8, 4, True, 2, {}
    ship8 = 4, 8, False, 3, {}
    ship9 = 6, 4, True, 3, {}
    ship10 = r, c, h, l, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert place_ship_at(r, c, h, l, f) == [(0, 2, True, 1, {}), (0, 8, True, 1, {}),
                                            (4, 3, True, 1, {}), (9, 1, True, 1, {}),
                                            (3, 6, False, 2, {}), (7, 1, True, 2, {}),
                                            (8, 4, True, 2, {}), (4, 8, False, 3, {}),
                                            (6, 4, True, 3, {}), (2, 1, True, 4, {})]


def test_place_ship_at5():
    r = 9
    c = 3
    h = True
    l = 2
    ship1 = 1, 2, True, 1, {}
    ship2 = 2, 9, True, 1, {}
    ship3 = 4, 0, True, 1, {}
    ship4 = 8, 1, True, 1, {}
    ship5 = 3, 5, False, 2, {}
    ship6 = r, c, h, l, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6]
    assert place_ship_at(r, c, h, l, f) == [(1, 2, True, 1, {}), (2, 9, True, 1, {}),
                                            (4, 0, True, 1, {}), (8, 1, True, 1, {}),
                                            (3, 5, False, 2, {}), (9, 3, True, 2, {})]
    
    
def test_check_if_hits1():
    r = 6
    c = 7
    ship1 = 3, 8, True, 1, {}
    ship2 = 4, 6, True, 1, {}
    ship3 = 8, 4, True, 1, {}
    ship4 = 8, 6, True, 1, {}
    ship5 = 0, 0, True, 2, {}
    ship6 = 7, 0, True, 2, {}
    ship7 = 5, 4, False, 2, {}
    ship8 = 3, 0, False, 3, {}
    ship9 = 6, 6, True, 3, {}
    ship10 = 2, 3, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(r, c, f) is True


def test_check_if_hits2():
    r = 5
    c = 0
    ship1 = 8, 8, True, 1, {}
    ship2 = 6, 5, True, 1, {}
    ship3 = 5, 8, True, 1, {}
    ship4 = 9, 0, True, 1, {}
    ship5 = 2, 0, True, 2, {}
    ship6 = 9, 3, True, 2, {}
    ship7 = 4, 0, False, 2, {}
    ship8 = 4, 2, False, 3, {}
    ship9 = 0, 3, True, 3, {}
    ship10 = 3, 5, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(r, c, f) is True


def test_check_if_hits3():
    r = 0
    c = 8
    ship1 = 0, 2, True, 1, {}
    ship2 = 0, 8, True, 1, {}
    ship3 = 4, 3, True, 1, {}
    ship4 = 9, 1, True, 1, {}
    ship5 = 3, 6, False, 2, {}
    ship6 = 7, 1, True, 2, {}
    ship7 = 8, 4, True, 2, {}
    ship8 = 4, 8, False, 3, {}
    ship9 = 6, 4, True, 3, {}
    ship10 = 2, 1, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(r, c, f) is True


def test_check_if_hits4():
    r = 5
    c = 0
    ship1 = 0, 0, True, 1, {}
    ship2 = 3, 2, True, 1, {}
    ship3 = 3, 4, True, 1, {}
    ship4 = 5, 5, True, 1, {}
    ship5 = 0, 7, True, 2, {}
    ship6 = 5, 8, False, 2, {}
    ship7 = 8, 6, True, 2, {}
    ship8 = 2, 6, True, 3, {}
    ship9 = 9, 2, True, 3, {}
    ship10 = 2, 0, False, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(r, c, f) is True


def test_check_if_hits5():
    r = 4
    c = 7
    ship1 = 0, 2, True, 1, {}
    ship2 = 2, 0, True, 1, {}
    ship3 = 9, 2, True, 1, {}
    ship4 = 0, 6, True, 1, {}
    ship5 = 4, 6, True, 2, {}
    ship6 = 9, 7, True, 2, {}
    ship7 = 0, 4, False, 2, {}
    ship8 = 2, 2, False, 3, {}
    ship9 = 4, 0, False, 3, {}
    ship10 = 7, 4, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(r, c, f) is True
    

def test_hit1():
    r = 1
    c = 0
    ship1 = 1, 0, True, 1, {(r, c)}
    f1 = [ship1]
    assert hit(r, c, f1) == ([(1, 0, True, 1, {(1, 0)})], (1, 0, True, 1, {(1, 0)}))


def test_hit2():
    r = 7
    c = 5
    ship1 = 1, 0, True, 1, {(1, 0)}
    ship2 = 9, 4, True, 1, {(9, 4)}
    ship3 = 7, 5, True, 1, {(r, c)}
    f1 = [ship1, ship2, ship3]
    assert hit(r, c, f1) == ([(1, 0, True, 1, {(1, 0)}), (9, 4, True, 1, {(9, 4)}), (7, 5, True, 1, {(7, 5)})],
                             (7, 5, True, 1, {(7, 5)}))


def test_hit3():
    r = 5
    c = 2
    ship1 = 1, 0, True, 1, {(1, 0)}
    ship2 = 9, 4, True, 1, {(9, 4)}
    ship3 = 7, 5, True, 1, {}
    ship4 = 7, 9, True, 1, {}
    ship5 = 4, 2, False, 2, {(r, c)}
    f1 = [ship1, ship2, ship3, ship4, ship5]
    assert hit(r, c, f1) == ([(1, 0, True, 1, {(1, 0)}), (9, 4, True, 1, {(9, 4)}),
                              (7, 5, True, 1, {}), (7, 9, True, 1, {}),
                              (4, 2, False, 2, {(5, 2)})], (4, 2, False, 2, {(5, 2)}))


def test_hit4():
    r = 4
    c = 2
    ship1 = 1, 0, True, 1, {(1, 0)}
    ship2 = 9, 4, True, 1, {(9, 4)}
    ship3 = 7, 5, True, 1, {}
    ship4 = 7, 9, True, 1, {}
    ship5 = 4, 2, False, 2, {(5, 2), (r, c)}
    f1 = [ship1, ship2, ship3, ship4, ship5]
    assert hit(r, c, f1) == ([(1, 0, True, 1, {(1, 0)}), (9, 4, True, 1, {(9, 4)}),
                              (7, 5, True, 1, {}), (7, 9, True, 1, {}),
                              (4, 2, False, 2, {(5, 2), (4, 2)})], (4, 2, False, 2, {(5, 2), (4, 2)}))


def test_hit5():
    r = 5
    c = 7
    ship1 = 1, 0, True, 1, {(1, 0)}
    ship2 = 9, 4, True, 1, {(9, 4)}
    ship3 = 7, 5, True, 1, {(7, 5)}
    ship4 = 7, 9, True, 1, {(7, 9)}
    ship5 = 4, 2, False, 2, {(5, 2), (4, 2)}
    ship6 = 4, 5, False, 2, {(4, 5), (5, 5)}
    ship7 = 9, 7, True, 2, {(9, 7), (9, 8)}
    ship8 = 3, 0, False, 3, {(3, 0), (4, 0), (5, 0)}
    ship9 = 7, 1, True, 3, {(7, 1), (7, 2), (7, 3)}
    ship10 = 3, 7, False, 4, {(3, 7), (4, 7), (6, 7), (r, c)}
    f1 = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(r, c, f1) == ([(1, 0, True, 1, {(1, 0)}), (9, 4, True, 1, {(9, 4)}),
                              (7, 5, True, 1, {(7, 5)}), (7, 9, True, 1, {(7, 9)}),
                              (4, 2, False, 2, {(5, 2), (4, 2)}), (4, 5, False, 2, {(4, 5), (5, 5)}),
                              (9, 7, True, 2, {(9, 7), (9, 8)}), (3, 0, False, 3, {(3, 0), (4, 0), (5, 0)}),
                              (7, 1, True, 3, {(7, 1), (7, 2), (7, 3)}), (3, 7, False, 4, {(3, 7), (4, 7), (6, 7), (5, 7)})],
                             (3, 7, False, 4, {(3, 7), (4, 7), (6, 7), (5, 7)}))
    
    
    def test_are_unsunk_ships_left1():
    ship1 = 3, 8, True, 1, {}
    ship2 = 4, 6, True, 1, {}
    ship3 = 8, 4, True, 1, {}
    ship4 = 8, 6, True, 1, {}
    ship5 = 0, 0, True, 2, {}
    ship6 = 7, 0, True, 2, {}
    ship7 = 5, 4, False, 2, {}
    ship8 = 3, 0, False, 3, {}
    ship9 = 6, 6, True, 3, {}
    ship10 = 2, 3, True, 4, {}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert are_unsunk_ships_left(f) is True


def test_are_unsunk_ships_left2():
    ship1 = 8, 8, True, 1, {(8, 8)}
    ship2 = 6, 5, True, 1, {(6, 5)}
    ship3 = 5, 8, True, 1, {(5, 8)}
    ship4 = 9, 0, True, 1, {(9, 0)}
    ship5 = 2, 0, True, 2, {(2, 0), (2, 1)}
    ship6 = 9, 3, True, 2, {(9, 3), (9, 4)}
    ship7 = 4, 0, False, 2, {(4, 0), (5, 0)}
    ship8 = 4, 2, False, 3, {(4, 2), (5, 2), (6, 2)}
    ship9 = 0, 3, True, 3, {(0, 3), (1, 3), (2, 3)}
    ship10 = 3, 5, True, 4, {(3, 5), (4, 5), (5, 5)}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert are_unsunk_ships_left(f) is True


def test_are_unsunk_ships_left3():
    ship1 = 0, 2, True, 1, {(0, 2)}
    ship2 = 0, 8, True, 1, {(0, 8)}
    ship3 = 4, 3, True, 1, {(4, 3)}
    ship4 = 9, 1, True, 1, {(9, 1)}
    ship5 = 3, 6, False, 2, {(3, 6), (4, 6)}
    ship6 = 7, 1, True, 2, {(7, 1), (7, 2)}
    ship7 = 8, 4, True, 2, {(8, 4), (8, 5)}
    ship8 = 4, 8, False, 3, {(4, 8), (5, 8), (6, 8)}
    ship9 = 6, 4, True, 3, {(6, 4), (6, 5), (6, 6)}
    ship10 = 2, 1, True, 4, {}
    f = [ship1,ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert are_unsunk_ships_left(f) is True


def test_are_unsunk_ships_left4():
    ship1 = 1, 2, True, 1, {}
    ship2 = 2, 9, True, 1, {}
    ship3 = 4, 0, True, 1, {}
    ship4 = 8, 1, True, 1, {(8, 1)}
    ship5 = 3, 5, False, 2, {(3, 5), (4, 5)}
    ship6 = 9, 3, True, 2, {(9, 3), (9, 4)}
    ship7 = 7, 6, False, 2, {(7, 6), (8, 6)}
    ship8 = 4, 2, False, 3, {(4, 2), (6, 2)}
    ship9 = 4, 9, False, 3, {(4, 9), (5, 9), (6, 9)}
    ship10 = 0, 5, True, 4, {(0, 5), (0, 6), (0, 7), (0, 8)}
    f = [ship1,ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert are_unsunk_ships_left(f) is True


def test_are_unsunk_ships_left5():
    ship1 = 0, 0, True, 1, {}
    ship2 = 3, 2, True, 1, {(3, 2)}
    ship3 = 3, 4, True, 1, {(3, 4)}
    ship4 = 5, 5, True, 1, {(5, 5)}
    ship5 = 0, 7, True, 2, {(0, 7), (0, 8)}
    ship6 = 5, 8, False, 2, {(5, 8), (6, 8)}
    ship7 = 8, 6, True, 2, {(8, 6), (8, 7)}
    ship8 = 2, 6, True, 3, {(2, 8)}
    ship9 = 9, 2, True, 3, {(9, 2)}
    ship10 = 2, 0, False, 4, {(2, 0)}
    f = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert are_unsunk_ships_left(f) is True
