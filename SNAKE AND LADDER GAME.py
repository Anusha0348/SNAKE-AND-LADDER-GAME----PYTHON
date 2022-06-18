# Python3 program to find minimum number of dice throws required to reach last cell from first cell of a given
# snake and ladder board

import time
import random
import sys
import tkinter.messagebox
from tkinter import *

# An entry in queue used in BFS
class QueueEntry(object):
    def __init__(self,v = 0, dist = 0):
        self.v = v
        self.dist = dist
    
'''This function returns minimum number of dice'''

def getMinDiceThrows(move, N):

    # The graph has N vertices. Mark all the vertices as not visited
    visited = [False] * N

    # Create a queue for BFS
    queue = []

    # Mark the node 0 as visited and enqueue it
    visited[0] = True
    
    # Distance of 0't vertex is also 0
    # Enqueue 0'th vertex
    queue.append(QueueEntry(0, 0))

    # Do a BFS starting from vertex at index 0
    qe = QueueEntry() # A queue entry (qe)
    while queue:
        qe = queue.pop(0)
        v = qe.v # Vertex no. of queue entry

        # If front vertex is the destination
        # vertex, we are done
        if v == N - 1:
            break

        # Otherwise dequeue the front vertex
        # and enqueue its adjacent vertices
        # (or cell numbers reachable through
        # a dice throw)
        j = v + 1
        while j <= v + 6 and j < N:
    
            # If this cell is already visited,
            # then ignore
            if visited[j] is False:

                # Otherwise calculate its
                # distance and mark it
                # as visited
                a = QueueEntry()
                a.dist = qe.dist + 1
                visited[j] = True

                # Check if there a snake or ladder
                # at 'j' then tail of snake or top
                # of ladder become the adjacent of 'i'
                a.v = move[j] if move[j] != -1 else j

                queue.append(a)
            j += 1

    # We reach here when 'qe' has last vertex
    # return the distance of vertex in 'qe
    return qe.dist

# driver code
N = 100
moves = [-1] * N

win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window
win.geometry('500x200') #setting the size of the window
            
def func():#function of the button
    tkinter.messagebox.showinfo("Greetings","Hello! Welcome to snake and ladder game \n")
    tkinter.messagebox.showinfo("Min Dice", "Min Dice throws required is {0}".
                                format(getMinDiceThrows(moves, N)))    
class snakesandladder(object):
    def __init__(self, position):
        self.position = position
        self.ladd = [4,24,48,67,86]
        self.lengthladd = [13,23,5,12,13]
        self.snake = [6,26,47,23,55,97]   
        self.lengthsnake = [4,1,7,5,8,9]        
        
    def dice(self):
        
        print("----------------LET'S START THE GAME----------------\n")
        while self.position <= 100: 
            roll = random.choice([1,2,3,4,5,6])  
            print('Dice number: ', roll)
            self.position = roll + self.position
            if self.position > 100:
                self.position = self.position - roll
            if self.position == 100:                
                print('Current position of the player : ', self.position, '\n')
                print('GAME COMPLETED')
                break
            
            if self.position in self.ladd:
                for n in range(len(self.ladd)):
                    if self.position == self.ladd[n]:
                        self.position = self.position + self.lengthladd[n]
            if self.position in self.snake:
                for n in range(len(self.snake)):
                    if self.position == self.snake[n]:
                        self.position = self.position - self.lengthsnake[n]
                        
            print('Current position of the player : ', self.position, '\n')


zack = snakesandladder(0)    
zack.dice()

btn=Button(win,text="Click Me", width=10,height=5,command=func)
btn.place(x=200,y=30)
win.mainloop()
