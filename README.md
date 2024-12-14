# Final_Project_SS
This is the final project for AI Algorithms. This game is Connect 4 with a minimax algorithm. 

The report must effectively communicate what you did for your project in a way that lets a technical bystander reproduce your work. Include:
Software and hardware requirements


**Software**: Python (Version 3.12.2)

**Hardware used:** Macbook Air; Chip: Apple M3; Memory: 8GB; Software Version on Macbook: Version 14.5 (Mac OS Sonoma)

**Links to any data sources:** 
No particular data sources as this project does not require one.

**Motivation for your project:**
I used to play Connect 4 a lot. I wanted to mesh that with my Computer Science background in order to build a functioning game. 
I also wanted to use some of the algorithms learned in this course (e.g., Alpha Beta pruning) in order to expand the game board and experiment with how big I can make the game board. 

**Explanation of what you accomplished:**
The basic structure of the connect 4 game works as the traditional rules of the game. To clarify, the basic structure of the game is the following: the players (which are the computer and the human) drops discs into different columns. The goal of the game is to build a continuous line of 4 checkers before your opponent does. This line can be diagnonal (leaning leftwards or rightwards), horizontal, or vertical. In my version of Connect 4, I have changed the traditional game by increasing the board size and increasing the number of discs that are found in a single line (e.g., I am increasing the number of discs from 4 to something larger). 

In this section, I will walk through 1) the basic structure of the game (while also highlighting any constraints or edge cases that I found), 2) how I changed the game to include a depth limited minimax with an evaluation heuristic, and 3) the results of the experiment I ran to see how large I can make the board. 

In regards to building the basic structure, I noticed that the number of columns needs to be at least 7 and the number of rows needs to be at least 6. You need this in order to just test for a horizontal win (when the number of discs required for a win is 4). 

In regards to the minimax function, 

In regards to how big I was able to make the board, I went to 10 X 10 with a depth of 4 and the number of discs I am looking for is 6. 

**How you measured your success (or failure):** I measured success if the game did not end in a tie and instead gave back a win for either of the players. I added files to the repo that show trial runs of the game running. You will see that if the game goes beyond 10 X 10, the file gets way too big to analyze and so it is best to not enlarge the game board any bigger than this and to just focus on changing the other variables instead. 

