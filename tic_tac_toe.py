from re import M
import time

class Game:
    def __init__(self):
        self.initialise_game()
    
    def initialise_game(self):
        self.current_state = [[0,0,0],[0,0,0],[0,0,0]]

        self.current_player = 1
    
    def draw_board(self):
        for i in range(0,3):
            for j in range(0,3):
                print(f"|{self.current_state[i][j]}|", end=" ")
            print()
        print()

    def is_valid_move(self, px, py):
        if 2 < px < 0 or 2 < py < 0:
            return False

        elif self.current_state[px][py] != 0:
            return False
        
        return True
    
    def has_won(self):

        # returns number of winning player, or 0 if no one has won but game can continue, or -1 if its a draw
       
        for i in range(0,3):
             # handling a vertical win (y axis)
            if (self.current_state[0][i] != 0 
            and self.current_state[0][i] == self.current_state[1][i] 
            and self.current_state[1][i] == self.current_state[2][i]):

                return self.current_state[0][i]
            
             # handling a horizontal win (x axis)
            if all(v == 1 for v in self.current_state[i]):
                return 1
            elif all(v == 2 for v in self.current_state[i]):
                return 2 
        
        # Main diagonal win
        if (self.current_state[0][0] != 0 and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != 0 and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
        
        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == 0):
                    return -1

        return 0
    
    def max(self):
        # player 1 is max
        # possible maxv values are:
        # -1 = loss
        # 0 = tie
        # 1 = win

        # set to -2 initially as worse than worse case
        maxv = -2

        px = None
        py = None

        result = self.has_won()

        # if the game has ended, the fn returns the evaluation fn of the end (-1,0,1)

        # below format = (max_v, px, py)
        # maxv = maximum found value that can be acheived for player 1
        # px = the x position where this is obtained
        # py = the y position where this is obtained

        if result == 2:
            return(-1,0,0)
        elif result == 1:
            return(1,0,0)
        elif result == 0:
            return (0,0,0)
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j] == 0:
                    # since this spot isn't taken, player 1 takes it and calls min
                    # represents one branch of the game tree
                    self.current_state[i][j] = 1
                    (m, min_i, min_j) = self.min()

                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    
                    self.current_state[i][j] = 0

        return (maxv, px, py)
    
    def min(self):
        # player 2 is min
        # possible minv values are:
        # -1 = win for player 1
        # 0 = tie
        # 1 = loss for player 1

        # set to 22 initially as worse than worse case (for player 1)
        minv = 2

        px = None
        py = None

        result = self.has_won()

        # if the game has ended, the fn returns the evaluation fn of the end (-1,0,1)

        # below format = (min_v, px, py)
        # minv = minimum found value that can be acheived for player 1
        # px = the x position where this is obtained
        # py = the y position where this is obtained

        if result == 2:
            return(-1,0,0)
        elif result == 1:
            return(1,0,0)
        elif result == 0:
            return (0,0,0)
        
        for i in range(0,3):
            for j in range(0,3):
                if self.current_state[i][j] == 0:
                    # since this spot isn't taken, player 2 takes it and calls max
                    # represents one branch of the game tree
                    self.current_state[i][j] = 2
                    (m, max_i, max_j) = self.max()

                    if m < minv:
                        minv = m
                        px = i
                        py = j
                    
                    self.current_state[i][j] = 0

        return (minv, px, py)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.has_won()

            if self.result >= 0:
                if self.result == 2:
                    print("The winner is player 2")
                elif self.result == 1:
                    print("The winner is player 1")
                else:
                    print("The game is a tie")
                
                self.initialise_game()
                return
            
            if self.current_player == 2:
                while True:

                    px = int(input('Insert the X coordinate:'))
                    py = int(input('Insert the Y coordinate:'))

                    if self.is_valid_move(px, py):
                        self.current_state[px][py] = 2
                        self.current_player = 1
                        break
                    else:
                        print("Invalid move! Try again.")

            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 1
                self.current_player = 2

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()
                    



            

                

