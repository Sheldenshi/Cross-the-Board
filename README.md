# Cross-the-Board
```
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
 ```
