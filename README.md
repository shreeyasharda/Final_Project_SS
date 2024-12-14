# Final_Project_SS
This is the final project for AI Algorithms. This game is Connect 4 with a minimax algorithm. 

The report must effectively communicate what you did for your project in a way that lets a technical bystander reproduce your work. Include:
Software and hardware requirements


**Software**: Python (Version 3.12.2)

**Hardware used:** Macbook Air; Chip: Apple M3; Memory: 8GB; Software Version on Macbook: Version 14.5 (Mac OS Sonoma)

**Links to any data sources:** 
Link to Video I used to help me build an outline for the Connect 4 game: https://www.youtube.com/watch?v=UYgyRArKDEs&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV

**Motivation for your project:**
I used to play Connect 4 a lot. I wanted to mesh that with my Computer Science background in order to build a functioning game. 
I also wanted to use some of the algorithms learned in this course (e.g., Alpha Beta pruning) in order to expand the game board and experiment with how big I can make the game board. 

**Explanation of what you accomplished:**
The basic structure of the connect 4 game works as the traditional rules of the game. To clarify, the basic structure of the game is the following: the players (which are the computer and the human) drops discs into different columns. The goal of the game is to build a continuous line of 4 checkers before your opponent does. This line can be diagnonal (leaning leftwards or rightwards), horizontal, or vertical. In my version of Connect 4, I have changed the traditional game by increasing the board size and increasing the number of discs that are found in a single line (e.g., I am increasing the number of discs from 4 to something larger). 

In this section, I will walk through 1) the basic structure of the game (while also highlighting any constraints or edge cases that I found), 2) how I changed the game to include a depth limited minimax with an evaluation heuristic, and 3) the results of the experiment I ran to see how large I can make the board. 

In regards to building the basic structure, I noticed that the number of columns needs to be at least 7 and the number of rows needs to be at least 6. You need this in order to just test for a horizontal win (when the number of discs required for a win is 4). 

**How you measured your success (or failure):** I measured success by the number of wins by the computer for each game board size. 
