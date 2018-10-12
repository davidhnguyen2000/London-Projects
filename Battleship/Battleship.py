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
                    # print('placed something')
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
                    # print('placed something')
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
    direction = int(input("direction\n 0: left\n 1: up\n 2: right\n 3: down\n choice:"))
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

def guessPlayer(totalHitsPlayer):
    guessX = int(input("x coordinate: "))
    guessY = int(input("y coordinate: "))
    if computerGameBoard[guessX][guessY] == BATTLESHIP_CHAR:
        computerGameBoard[guessX][guessY] = "X"
        print("HIT")
        totalHitsPlayer = totalHitsPlayer + 1
    else:
        computerGameBoard[guessX][guessY] = "o"
        print("SPLASH")

def guessComputer(totalHitsComputer, lastGuessX, lastGuessY, hitLastTurn): # preliminary AI code --> look at using binary tree for decision making
    if not hitLastTurn:
        guessX = random.randint(0, 9)
        guessY = random.randint(0, 9)
    else:
        direction = random.randint(0, 3)
        if direction == 0 and lastGuessX + 1 < 10:
            guessX = lastGuessX + 1
        elif direction == 1 and lastGuessX - 1 >= 0:
            guessX = lastGuessX - 1
        elif direction == 2 and lastGuessY + 1 < 10:
            guessY = lastGuessY + 1
        elif direction == 3 and lastGuessY -1 >= 0:
            guessY = lastGuessY -1


    if playerGameBoard[guessX][guessY] == BATTLESHIP_CHAR:
        playerGameBoard[guessX][guessY] = "X"
        print("HIT")
        totalHitsComputer = totalHitsComputer + 1
        lastGuessX = guessX
        lastGuessY = guessY
        hitLastTurn = True
    else:
        playerGameBoard[guessX][guessY] = "o"
        print("SPLASH")
        hitLastTurn = False


def createPlayerGameboard(gameBoardSize):
    "This creates the game board of the player through user input"
    playerBoard = makeGameboard(gameBoardSize)
    return playerBoard


GAME_BOARD_SIZE = 10
BATTLESHIP_1_SIZE = 5
BATTLESHIP_2_SIZE = 4
BATTLESHIP_3_SIZE = 3
BATTLESHIP_4_SIZE = 2
playerHits = 0
computerHits = 0
lastGuessX = 0
lastGuessY = 0
hitLastTurn = False


computerGameBoard = makeGameboard(GAME_BOARD_SIZE)

placeBoatComputer(BATTLESHIP_1_SIZE, GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_2_SIZE, GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_3_SIZE, GAME_BOARD_SIZE)
placeBoatComputer(BATTLESHIP_4_SIZE, GAME_BOARD_SIZE)

displayGameboardWithBoats(computerGameBoard)

playerGameBoard = createPlayerGameboard(GAME_BOARD_SIZE)
displayGameboard(playerGameBoard)

placeBoatPlayer(BATTLESHIP_1_SIZE, GAME_BOARD_SIZE)
displayGameboardWithBoats(playerGameBoard)
placeBoatPlayer(BATTLESHIP_2_SIZE, GAME_BOARD_SIZE)
displayGameboardWithBoats(playerGameBoard)
placeBoatPlayer(BATTLESHIP_3_SIZE, GAME_BOARD_SIZE)
displayGameboardWithBoats(playerGameBoard)
placeBoatPlayer(BATTLESHIP_4_SIZE, GAME_BOARD_SIZE)
displayGameboardWithBoats(playerGameBoard)


while playerHits < 13 and computerHits < 13:
    displayGameboard(computerGameBoard)
    guess(totalHits)
    print()
print("You win!")
