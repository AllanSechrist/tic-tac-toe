
class Game(object):
    def __init__(self):
        self.board = { 1:"1", # 1-3 are the first row 
                       2:"2",
                       3:"3",
                       4:"4", # 4-6 are the second row
                       5:"5",
                       6:"6",
                       7:"7", # 7-9 are the third row
                       8:"8",
                       9:"9", }
        # self.keys = [key for key, value in self.board.items()]
        self.player_x = True
        self.player_o = False


    def update_game_state(self):
        self.draw_board()
        user_input = None
        while user_input == None:
            try:
                user_input = int(input("please select the place you would like to mark: "))
            except ValueError:
                print("input must be a number between 1 and 9")

            # check if the spot has already been marked by a player. 
            if self.board[user_input] == "X" or self.board[user_input] == "O":
                user_input = None
                print("That spot is already taken! please pick a new spot!")

        if self.player_x == True: # mark the board
            self.board[user_input] = "X"
        else:
            self.board[user_input] = "O"

        game_over = self.win_logic() # check if the game has ended
        self.switch_turn() # set the turn
        return game_over


    def draw_board(self):
        # draws the game board
        divider = "------------"
        position = 1
        # make rows
        for j in range(3):
            row = ''
            for i in range(3):
                cell = f" {self.board[position]} " # update cell
                if i < 2:
                    row = row + cell + "|" # formatting
                else:
                    row = row + cell
                position += 1 # keep track of position
    
            print(row)
            print(divider)


    def switch_turn(self): # This is called in update_board
        if self.player_x == True:
            self.player_x = False
            self.player_o = True
        else:
            self.player_x = True
            self.player_o = False


    def win_logic(self): # This is called in update_board
        x = "XXX"
        o = "OOO"
        row_one = self.board[1] + self.board[2] + self.board[3]
        row_two = self.board[4] + self.board[5] + self.board[6]
        row_three = self.board[7] + self.board[8] + self.board[9]

        col_one = self.board[1] + self.board[4] + self.board[7]
        col_two = self.board[2] + self.board[5] + self.board[8]
        col_three = self.board[3] + self.board[6] + self.board[9]

        dia_one = self.board[1] + self.board[5] + self.board[9]
        dia_two = self.board[3] + self.board[5] + self.board[7]

        win_states = [row_one, row_two, row_three, col_one, col_two, col_three, dia_one, dia_two]

        # check for a winning board state
        for state in win_states:
            if state == x:
                print("player X has won!")
                return True
            elif state == o:
                print("player O has won!")
                return True
        
        # Check for Draw
        values = [value for key, value in self.board.items()]
        keys = [str(key) for key, value in self.board.items()]
        count = 0
        for key in keys:
            if key in values:
                count = 0
                # print(f"Broke at {key}")
                break
            else:
                count += 1
            if count == 9:
                print("the game is a draw")
                return True
        return False


    def play_game(self):
        finished = False
        while not finished:
            finished = self.update_game_state()
        
            
my_board = Game()
my_board.play_game()
