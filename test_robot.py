import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_south_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH


def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST


def test_north_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH


def test_illegal_move(robot):
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move1(robot):
    for i in range(3):
        robot.turn()
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move2(robot):
    robot._state = robot.State(Direction.NORTH, 1, 1)
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move3(robot):
    robot._state = robot.State(Direction.EAST, 10, 10)
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move4(robot):
    for i in range(3):
        robot.move()
    state = robot.state()
    assert state['row'] == 7
    assert state['col'] == 1


def test_move5(robot):
    robot.turn()
    for i in range(3):
        robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 4


def test_move6(robot):
    robot.turn()
    for i in range(3):
        robot.move()
    for i in range(3):
        robot.turn()
    for i in range(3):
        robot.move()
    state = robot.state()
    assert state['row'] == 7
    assert state['col'] == 4


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back1(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back2(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back3(robot):
    robot.turn()
    for i in range(3):
        robot.move()
    for i in range(3):
        robot.turn()
    for i in range(3):
        robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 8
    assert state['col'] == 4


def test_back4(robot):
    for i in range(3):
        robot.move()
    robot.turn()
    for i in range(3):
        robot.move()
    for i in range(7):
        robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1
