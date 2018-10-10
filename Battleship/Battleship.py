import random
BATTLESHIP_CHAR = "@"
OPEN_SPACE_CHAR = "*"


def makeGameboard(gameBoardSize):
    "This creates the game board"
    board = [[]]
    for yCoor in range(gameBoardSize):
        board.append([])
        for xCoor in range(gameBoardSize):
            board[yCoor].append(xCoor)
            board[yCoor][xCoor] = "*"
    return board


def placeBoat(startX, startY, direction, battleshipSize, gameBoardSize, gameBoard):
    noShip = True
    onBoard = True
    if gameBoard[startX][startY] == OPEN_SPACE_CHAR: # starts placement of the boat if there is a free space
        if direction == 0 or direction == 2:
            if direction == 0:
                direction2 = -1
            else:
                direction2 = 1
            for xCoor in range(battleshipSize):  # check if boat placement is good
                newXCoor = startX + direction2*xCoor
                onBoard = newXCoor < gameBoardSize and newXCoor >= 0
                if onBoard:
                    noShip = gameBoard[newXCoor][startY] == OPEN_SPACE_CHAR
                if not noShip or not onBoard:
                    return False
            if noShip and onBoard:  # places boat
                for xCoor in range(battleshipSize):
                    newXCoor = startX + direction2 * xCoor
                    gameBoard[newXCoor][startY] = BATTLESHIP_CHAR
                    print('placed something')
        elif direction == 1 or direction == 3:
            if direction == 1:
                direction2 = -1
            else:
                direction2 = 1
            for yCoor in range(battleshipSize): # check if boat placement is good
                newYCoor = startY + direction2 * yCoor
                onBoard = newYCoor < gameBoardSize and newYCoor >= 0
                if onBoard:
                    noShip = gameBoard[startX][newYCoor] == OPEN_SPACE_CHAR
                if not noShip or not onBoard:
                    # print('failed placement')
                    return False
            if noShip and onBoard: # places boat
                for yCoor in range(battleshipSize):
                    newYCoor = startY + direction2 * yCoor
                    gameBoard[startX][newYCoor] = BATTLESHIP_CHAR
                    print('placed something')
        return True
    else:
        return False


def placeBoatComputer(battleshipSize, gameBoardSize):
    "This places one boat on the computer gameBoard randomly"
    startXCoordinate = random.randint(0, 9)
    startYCoordinate = random.randint(0, 9)
    direction = random.randint(0, 3)
    if not placeBoat(startXCoordinate, startYCoordinate, direction, battleshipSize, gameBoardSize, computerGameBoard):
        placeBoatComputer(battleshipSize, gameBoardSize)
    return

def placeBoatPlayer(battleshipSize, gameBoardSize):
    startX = int(input("X coordinate of start:"))
    startY = int(input("Y coordinate of start:"))
    direction = int(input("direction\n 1: up\n 2: down\n 3: right\n 4: left\n choice:"))
    if not placeBoat(startX, startY, direction, battleshipSize, gameBoardSize, playerGameBoard):
        print("Invalid placement")
        placeBoatPlayer(battleshipSize, gameBoardSize)
    return

def displayGameboardWithBoats(board):
    "This displays the board"
    print('  0 1 2 3 4 5 6 7 8 9')
    for y in range(GAME_BOARD_SIZE):
        print(y, end=' ')
        for x in range(GAME_BOARD_SIZE):
            print(board[x][y], end=' ')
        print()
    return

def displayGameboard(board):
    "This displays the board"
    print('  0 1 2 3 4 5 6 7 8 9')
    for y in range(GAME_BOARD_SIZE):
        print(y, end=' ')
        for x in range(GAME_BOARD_SIZE):
            if board[x][y] == BATTLESHIP_CHAR:
                print(OPEN_SPACE_CHAR, end=' ')
            else:
                print(board[x][y], end=' ')
        print()
    return

def guess(totalHits):
    guessX = int(input("x coordinate: "))
    guessY = int(input("y coordinate: "))
    if computerGameBoard[guessX][guessY] == BATTLESHIP_CHAR:
        computerGameBoard[guessX][guessY] = "X"
        print("HIT")
        totalHits = totalHits + 1
    else:
        computerGameBoard[guessX][guessY] = "o"
        print("SPLASH")

def createPlayerGameboard(gameBoardSize):
    "This creates the game board of the player through user input"
    playerBoard = makeGameboard(gameBoardSize)

    return playerBoard


GAME_BOARD_SIZE = 10
BATTLESHIP_1_SIZE = 5
BATTLESHIP_2_SIZE = 4
BATTLESHIP_3_SIZE = 3
BATTLESHIP_4_SIZE = 2
totalHits = 0


computerGameBoard = makeGameboard(GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_1_SIZE, GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_2_SIZE, GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_3_SIZE, GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_4_SIZE, GAME_BOARD_SIZE)
playerGameBoard = createPlayerGameboard(GAME_BOARD_SIZE)

displayGameboardWithBoats(computerGameBoard)
displayGameboard(playerGameBoard)
placeBoatPlayer(BATTLESHIP_1_SIZE, GAME_BOARD_SIZE)
displayGameboardWithBoats(playerGameBoard)
# while totalHits < 13:
#     displayGameboard(computerGameBoard)
#     guess(totalHits)
#     print()
# print("You win!")
