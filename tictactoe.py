import random

class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name

class TicTacToe:
    empty_tile = "[ ]"
    turn = 0
    def __init__(self, player_x, player_o):
        self.board = []
        self.player_x = player_x
        self.player_o = player_o

    def generate_board(self):
        for r in range(3):
            row = []
            for c in range(3):
                row.append(self.empty_tile)
            self.board.append(row)

    def random_first_player(self):
        return random.randint(0,1)

    def choose_spot(self, row, column, player):
        self.board[row][column] = player.symbol
    
    def has_player_won(self, player):
        #Checking Winning Arrangements
        win = None
        
        iteration = len(self.board)
        
        #Checking rows
        for r in range(iteration):
            win = True
            for c in range(iteration):
                if self.board[r][c] != player.symbol:
                    win = False
                    break
            if win:
                return win
        
        #Checking columns
        for r in range(iteration):
            win = True
            for c in range(iteration):
                if self.board[r][c] != player.symbol:
                    win = False
                    break
            if win:
                return win
        
        #Checking diagonals
        win = True
        for r in range(iteration):
            if self.board[r][r] != player.symbol:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(iteration):
            if self.board[r][iteration - 1 - r] != player.symbol:
                win = False
                break
        if win:
            return win
        return False
        
        for row in self.board:
            for item in row:
                if item == self.empty_tile:
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == self.empty_tile:
                    return False
        return True

    def change_player_turn(self, player):
        return self.player_x if player == self.player_o else self.player_o
    
    def display_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print("\n")
    
    def start(self):
        self.generate_board()

        current_player = self.player_x if self.random_first_player() == 1 else self.player_o

        while True:
            print("{player}'s turn".format(player = current_player.name))

            self.display_board()

            #Asking the player for input
            row, col = list(
                map(int, input("{player_name}, Enter row and column numbers to fix spot: ".format(player_name = current_player.name)).split()))
            print()

            self.choose_spot(row -1, col -1, current_player)

            #Each turn check if player has won
            if self.has_player_won(current_player):
                print("{} wins the game".format(current_player.name))
                break
            
            #Check if the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            #Change player's turn
            current_player = self.change_player_turn(current_player)

        # Showing the board at end of game
        print()
        self.display_board()

#Asking for names
print("X player: ")
name_1 = input()
player_1 = Player(name_1, "[X]")
print("O player: ")
name_2 = input()
player_2 = Player(name_2, "[O]")

#Starting the game
tic_tac_toe = TicTacToe(player_1, player_2)
tic_tac_toe.start()
