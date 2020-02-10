# 8-Puzzle-Solver
## Solver for the famous 8-puzzle problem using using A* Search Algorithm (Artificial Intelligence)

An 8-puzzle is a 3x3 grid of tiles, numbered 1-8, with the last square in the grid being empty.  A tile can be slid into the blank spot, thus changing the configuration of the puzzle.  For example,
```
2  4  7
1  3 
5  6  8
```
Can become any of these:
```
2  4  7                     2  4                   2  4  7
1     3                     1  3  7                1  3  8
5  6  8                     5  6  8                5  6  
```
The goal is to arrange the tiles in this order:
```
1  2  3
4  5  6
7  8
```
