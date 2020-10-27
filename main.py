import collections
import functools
from functools import cmp_to_key
from operator import add 



"""
 Rules for Cross the Board:

 2 players alternate placing different colored stones
 on a 5x5 play field

 Stones may be played in *any* empty spot on the play field

 A stone is captured if each of the adjacent spaces are
 occupied by the opposite colored stone. See Diagram 1 below.

 (Diagram 1)
 (Three examples of a black piece being captured)

   a b c d e         a b c d e
 1 . . . . .       1 . . . . .
 2 . . . . .       2 . . . . .
 3 . . . w .  -->  3 . . . w .
 4 . . w B w       4 . . w W w
 5 . . . w .       5 . . . w .

   a b c d e         a b c d e
 1 . . . . .       1 . . . . .
 2 . . . . .       2 . . . . .
 3 . . . . W  -->  3 . . . . W
 4 . . . W B       4 . . . W W
 5 . . . . W       5 . . . . W
 
   a b c d e         a b c d e
 1 . . . W B       1 . . . W W
 2 . . . . W       2 . . . . W
 3 . . . . .  -->  3 . . . . .
 4 . . . . .       4 . . . . .
 5 . . . . .       5 . . . . .

 (Note that this scenario does not count as a capture)
   a b c d e
 1 . . . . .
 2 . . . W .
 3 . . W B W
 4 . . w B w
 5 . . . w .

 There are a few special edge cases.
 If a player places their piece on a square where they are surrounded
 on all available sides by the opponent's pieces, that player's piece
 is captured immediately. See Diagram 2 below.
 
  (Diagram 2)
   (before)       (black's move)     (end result)
   a b c d e         a b c d e         a b c d e 
 1 . . . . .       1 . . . . .       1 . . . . . 
 2 . . . . .       2 . . . . .       2 . . . . . 
 3 . . . w .  -->  3 . . . w .  -->  3 . . . w . 
 4 . . w . w       4 . . w B w       4 . . w W w 
 5 . . . w .       5 . . . w .       5 . . . w . 

 The player that is in-turn will have prioritization on capturing, as show in Diagram 3.
 
  (Diagram 3)
   (before)       (black's move)     (end result)
   a b c d e         a b c d e         a b c d e
 1 . . . . .       1 . . . . .       1 . . . . .
 2 . . . . .       2 . . . . .       2 . . . . .
 3 . . B w .  -->  3 . . B w .  -->  3 . . B w .
 4 . B w . w       4 . B w B w       4 . B B B w
 5 . . B w .       5 . . B w .       5 . . B w . 


 Goal: Create a contiguous path of stones from any edge of
 the board to the opposite edge.  Either player may connect
 any two opposite edges of the board. The player that 
 establishes contiguous stones from left to right or 
 top to bottom first wins. See Diagram 4 for examples of 
 winning configurations.

 (Diagram 4)
 Black has won:   White has won:
   a b c d e        a b c d e
 1 . . B . .      1 . . W W W
 2 . . . B .      2 B W . B .
 3 . . W B .      3 . B W B .
 4 . W . W B      4 W W B . .
 5 . . . W B      5 . B . . .
 
 In the game the players will enter
 coordinates for the grid location to play in, so for example
 "a1" would indicate the upper-left corner and "e5" would
 indicate the lower-right corner.
 """

Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])

class CrossTheBoard:
    WHITE = 'W'
    BLACK = 'B'
    PLAYERS = [WHITE, BLACK]
    SIZE = 5

    

    def __init__(self):
        self.spaces = [[None] * CrossTheBoard.SIZE for x in range(CrossTheBoard.SIZE)]
        
        self.turn = 0

    def render(self):
        print(' ', *(chr(ord('a') + x) for x in range(CrossTheBoard.SIZE)))
        for y in range(CrossTheBoard.SIZE):
            print(y + 1, *(self.spaces[x][y] or ' ' for x in range(CrossTheBoard.SIZE)))

    def getMoveInput(self):
        while True:
            try:
                row, col = input(f'{CrossTheBoard.PLAYERS[self.turn]}\'s turn:')
                x = max(0, min(CrossTheBoard.SIZE-1, ord(row) - ord('a')))
                y = max(0, min(CrossTheBoard.SIZE-1, ord(col) - ord('1')))
            except ValueError as e:
                print(e)
            else:
                return Coordinate(x, y)


    def check_move(self, coordinate):
        if self.spaces[coordinate.x][coordinate.y]:
            print(f"Invalid move. Coordinate taken by {self.spaces[coordinate.x][coordinate.y]}")
            return False
        else:
            return True

    def play(self):
        while True:
            self.render()
            coordinate = self.getMoveInput()
            if self.check_move(coordinate):
                self.spaces[coordinate.x][coordinate.y] = CrossTheBoard.PLAYERS[self.turn]
                self.check_caputuring(coordinate)
                    
                if self.check_winner():
                    print(f"Game Over!\nThe wnner is {CrossTheBoard.PLAYERS[self.turn]}")
                    break


                self.turn = (self.turn + 1) % 2
   
    def check_caputuring(self, coordinate):
        loction_filters = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def check_capturing_one_spot(coordinate, piece):
            neighbours = []
            for fil in loction_filters:
                next_loc = Coordinate(coordinate.x + fil[0], coordinate.y + fil[1]) 
                #check if the location is out of bound
                if not(next_loc.x < 0 or next_loc.x > CrossTheBoard.SIZE - 1 or
                next_loc.y < 0 or next_loc.y >  CrossTheBoard.SIZE - 1):
                    neighbours.append(self.spaces[next_loc.x][next_loc.y])
            for neighbour in neighbours:
                if neighbour != CrossTheBoard.PLAYERS[(piece + 1) % 2]:
                    return
            self.spaces[coordinate.x][coordinate.y] = CrossTheBoard.PLAYERS[(piece + 1) % 2]

        neighbour_oppsits = []
        reslts = []

        for fil in loction_filters:
            next_loc = Coordinate(coordinate.x + fil[0], coordinate.y + fil[1]) 
            #check if the location is out of bound
            if not(next_loc.x < 0 or next_loc.x > CrossTheBoard.SIZE - 1 
                or next_loc.y < 0 or next_loc.y >  CrossTheBoard.SIZE - 1) and self.spaces[next_loc.x][next_loc.y] == CrossTheBoard.PLAYERS[(self.turn + 1) % 2]:
                    neighbour_oppsits.append(next_loc)
        
        for oppsit in neighbour_oppsits:
            reslts.append(check_capturing_one_spot(oppsit, (self.turn + 1) % 2))
        check_capturing_one_spot(coordinate, self.turn)
        

    def check_winner(self):

        def search(location, destination):
            destination = [d for d in destination]
            visited = [[False] * CrossTheBoard.SIZE for x in range(CrossTheBoard.SIZE)]
            stack = [location]
            loction_filters = [[-1, 1], [0, 1], [1, 1],
                            [-1, 0], [1, 0],
                            [-1, -1], [0, -1], [1, -1]]
            while stack:
                curr_loc = stack.pop(0)
                if not visited[curr_loc.x][curr_loc.y]:
                    visited[curr_loc.x][curr_loc.y] = True

                    if curr_loc in destination:
                        return True

                    # add all neighbours.
                    for fil in loction_filters:
                        next_loc = Coordinate(curr_loc.x + fil[0], curr_loc.y + fil[1]) 
                        #check if the location is out of bound
                        if not(next_loc.x < 0 or next_loc.x > CrossTheBoard.SIZE - 1 
                            or next_loc.y < 0 or next_loc.y >  CrossTheBoard.SIZE - 1) and self.spaces[next_loc.x][next_loc.y] == CrossTheBoard.PLAYERS[self.turn]:

                            stack.append(next_loc)
            return False


        # [left, right, top, bottom]
        board_edges = [[], [], [], []]
        for i in range(CrossTheBoard.SIZE):
            if self.spaces[0][i] == CrossTheBoard.PLAYERS[self.turn]:
                board_edges[0].append(Coordinate(0, i))
            if self.spaces[CrossTheBoard.SIZE - 1][i] == CrossTheBoard.PLAYERS[self.turn]:
                board_edges[1].append(Coordinate(CrossTheBoard.SIZE - 1, i))
            if self.spaces[i][CrossTheBoard.SIZE - 1] == CrossTheBoard.PLAYERS[self.turn]:
                board_edges[2].append(Coordinate(i, CrossTheBoard.SIZE - 1))
            if self.spaces[i][0] == CrossTheBoard.PLAYERS[self.turn]:
                board_edges[3].append(Coordinate(i, 0))

        # if this player has at least a piece on the left edge and one on the right.
        if len(board_edges[0]) > 0 and len(board_edges[1]) > 0:
            for location in board_edges[0]:
                return search(location, board_edges[1])
                    
        if len(board_edges[2]) > 0 and len(board_edges[3]) > 0:
            for location in board_edges[2]:
                return search(location, board_edges[3])
                    
        return False

if __name__ == '__main__':

    CrossTheBoard = CrossTheBoard()
    CrossTheBoard.play()
