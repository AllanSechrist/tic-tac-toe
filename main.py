

class Cell(object):
    """creates a cell to be placed on the game board"""
    def __init__(self, id):
        self.id = id
        self.taken = False


class Game(object):
    """Keeps track of the board, player turns, and if the game has finished and if it is a drawn game"""
    def __init__(self):
        self.board = []
        self.cells = []
        self.player_x_turn = True
        self.gameover = False
        self.draw = False


    def create_board(self, size):
        "Creats a matrix with cell objects to keep track of player moves"
        id = 1
        for row in range(size):
            self.board.append([])
            for col in range(size):
                cell = Cell(id)
                self.cells.append(cell)
                self.board[row].append(cell)
                id += 1


    def update_game_state(self):
        "Handles input from the play and changes the game state accordingly"
        self.draw_board()
        user_input = None
        while user_input == None:
            try:
                user_input = int(input("please select the place you would like to mark: "))
                
            except:
                print("input must be a number between 1 and 9")

            try:
                # check if the spot has already been marked by a player.
                if self.cells[user_input - 1].taken:
                    user_input = None
                    print("That spot is already taken! please pick a new spot!")
            except:
                user_input = None

        self.cells[user_input - 1].taken = True   
        if self.player_x_turn:
            self.cells[user_input - 1].id = "X"
        else:
            self.cells[user_input - 1].id = "O"

        self.gameover = self.win_logic() # check if the game has ended
        
        if not self.gameover:
            self.switch_turn()
        


    def draw_board(self):
        """Draws the board to the Terminal"""
        divider = '------------'
        for row in range(len(self.board)):
            row_to_draw = ''
            for col in range(len(self.board)):
                cell = f' {self.board[row][col].id} '
                if col < 2:
                    row_to_draw = row_to_draw + cell + "|"
                else:
                    row_to_draw = row_to_draw + cell
        
            print(row_to_draw)
            print(divider)


    def switch_turn(self): # This is called in update_board
        """Changes the Turn"""
        if self.player_x_turn:
            self.player_x_turn = False
            print("It is now O's turn")
        else:
            self.player_x_turn = True
            print("It is now X's turn")


    def win_logic(self):
        """Checks the board for a winning or drawn game state"""
        for row in self.board:
            if all([cell.id == 'X' for cell in row]) or all([cell.id == 'O' for cell in row]):
                return True
            
        for col in range(len(self.board)):
            column = [row[col] for row in self.board] # get values from the columns of the game board
            if all([cell.id == 'X' for cell in column]) or all([cell.id == 'O' for cell in column]):
                return True

        # get values from cells along the diagonal of the game board
        lr_diag = [self.board[x][x] for x in range(len(self.board))]
        rl_diag = [self.board[x][len(self.board) - x -1] for x in range(len(self.board))]

        if all([cell.id == 'X' for cell in lr_diag]) or all([cell.id == 'X' for cell in rl_diag]) or all([cell.id == 'O' for cell in lr_diag]) or all([cell.id == 'O' for cell in rl_diag]):
            return True

        # Check for a Drawn Game
        if all([cell.taken for cell in self.cells]):
            self.draw = True
            return True
        

    def play_game(self):
        """Main game loop"""
        self.create_board(3)
        while not self.gameover:
            self.update_game_state()
        
        self.draw_board() # Shows the final game board

        if self.draw:
            print("The game has ended in a draw")
        else:
            if self.player_x_turn == True:
                print("Player X Wins!")
            else:
                print("Player O Wins!")
        
            
my_board = Game()
my_board.play_game()