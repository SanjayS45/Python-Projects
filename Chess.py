'''

Created on July 13, 2022

@author: Sanjay Sundaram
@version: 2.0
@date: July 22, 2023
@change: Chess pieces can no longer capture same color pieces, no more bugs with knight movement! :)
@bug: Class CheckKing -> kingCheck() -> king escapes check when user clicks away from king (idk why)...
@note: Will be adding new features to account for all possible checks made on the king; soon there will be a way to checkmate (end the game).
@license: 

MIT License

Copyright (c) 2023 Sanjay Sundaram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
from pip._vendor.pygments.formatters import img
from webbrowser import BackgroundBrowser
import imghdr
from _overlapped import NULL
from tkinter.messagebox import askretrycancel

from tkinter import *
from PIL import Image  
from PIL import ImageTk 
import math
from pip._vendor.pygments.unistring import Sc


root = Tk()
root.title("CHESS - It's White's Turn")

frame = Frame(root)

global canvas, iskingCheck
canvas = Canvas(root, width = 800, height = 800)
isKingCheck = False

def createBoard():
    
    global background
    img = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/Chessboard.png")
    img = img.resize((800,800), Image.ANTIALIAS)
    background = ImageTk.PhotoImage(img)
    
    canvas.create_image(400, 400, image=background)
    canvas.pack()


def createBlackPawn():
    blckPawnImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/black_pawn.png")
    blckPawnImg = blckPawnImg.resize((50, 50), Image.ANTIALIAS)
        
    # Black Pawns
    global B_PAWN1
    global b_pawn1
    b_pawn1 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN1 = canvas.create_image(50,150, image=b_pawn1)
    
     
    global B_PAWN2   
    global b_pawn2
    b_pawn2 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN2 = canvas.create_image(150,150, image=b_pawn2)
        
    global B_PAWN3
    global b_pawn3
    b_pawn3 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN3 = canvas.create_image(250,150, image=b_pawn3)
       
    global B_PAWN4 
    global b_pawn4
    b_pawn4 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN4 = canvas.create_image(350,150, image=b_pawn4)
    
    global B_PAWN5
    global b_pawn5
    b_pawn5 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN5 = canvas.create_image(450,150, image=b_pawn5)
    
    global B_PAWN6   
    global b_pawn6
    b_pawn6 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN6 = canvas.create_image(550,150, image=b_pawn6)
        
    global B_PAWN7
    global b_pawn7
    b_pawn7 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN7 = canvas.create_image(650,150, image=b_pawn7)
        
    global B_PAWN8
    global b_pawn8
    b_pawn8 = ImageTk.PhotoImage(blckPawnImg)
    B_PAWN8 = canvas.create_image(750,150, image=b_pawn8)



def createWhitePawn():
    # White pawns
    global whtPawnImg
    whtPawnImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/white_pawn.png")
    whtPawnImg = whtPawnImg.resize((50, 50), Image.ANTIALIAS)
    
    global WHITE_PAWN1
    global w_pawn1
    w_pawn1 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN1 = canvas.create_image(50,650, image=w_pawn1, tags="w_pawn")
    
        
    global WHITE_PAWN2
    global w_pawn2
    w_pawn2 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN2 = canvas.create_image(150,650, image=w_pawn2)
        
    global WHITE_PAWN3
    global w_pawn3
    w_pawn3 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN3 = canvas.create_image(250,650, image=w_pawn3)
        
    global WHITE_PAWN4
    global w_pawn4
    w_pawn4 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN4 = canvas.create_image(350,650, image=w_pawn4)
    
    global WHITE_PAWN5
    global w_pawn5
    w_pawn5 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN5 = canvas.create_image(450,650, image=w_pawn5)
        
    global WHITE_PAWN6
    global w_pawn6
    w_pawn6 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN6 = canvas.create_image(550,650, image=w_pawn6)
     
    global WHITE_PAWN7   
    global w_pawn7
    w_pawn7 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN7 = canvas.create_image(650,650, image=w_pawn7)
      
    global WHITE_PAWN8  
    global w_pawn8
    w_pawn8 = ImageTk.PhotoImage(whtPawnImg)
    WHITE_PAWN8 = canvas.create_image(750,650, image=w_pawn8)

def createWhiteRook():
    # White rooks
    whtRookImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/white_rook.png")
    whtRookImg = whtRookImg.resize((100, 100), Image.ANTIALIAS)
    
    global W_ROOK1
    global w_rook1
    w_rook1 = ImageTk.PhotoImage(whtRookImg)
    W_ROOK1 = canvas.create_image(50, 750, image=w_rook1)
    
    global W_ROOK2  
    global w_rook2
    w_rook2 = ImageTk.PhotoImage(whtRookImg)
    W_ROOK2 = canvas.create_image(750, 750, image=w_rook2)

def createBlackRook():
    # Black rooks
    blckRookImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/black_rook.png")
    blckRookImg = blckRookImg.resize((80, 80), Image.ANTIALIAS)
    
    global B_ROOK1 
    global b_rook1
    b_rook1 = ImageTk.PhotoImage(blckRookImg)
    B_ROOK1 = canvas.create_image(50, 50, image=b_rook1)
       
    global B_ROOK2 
    global b_rook2
    b_rook2 = ImageTk.PhotoImage(blckRookImg)
    B_ROOK2 = canvas.create_image(750, 50, image=b_rook2)

def createWhiteKnight():
    # White knights
    whtKnightImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/white_knight.png")
    whtKnightImg = whtKnightImg.resize((80, 80), Image.ANTIALIAS)
       
    global W_KNIGHT1 
    global w_knight1
    w_knight1 = ImageTk.PhotoImage(whtKnightImg)
    W_KNIGHT1 = canvas.create_image(145, 750, image=w_knight1)
       
    global W_KNIGHT2 
    global w_knight2
    w_knight2 = ImageTk.PhotoImage(whtKnightImg)
    W_KNIGHT2 = canvas.create_image(650, 750, image=w_knight2)

def createBlackKnight():
    # Black knights
    blckKnightImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/black_knight.png")
    blckKnightImg = blckKnightImg.resize((80, 80), Image.ANTIALIAS)
        
    global B_KNIGHT1
    global b_knight1
    b_knight1 = ImageTk.PhotoImage(blckKnightImg)
    B_KNIGHT1 = canvas.create_image(145, 50, image=b_knight1)
      
    global B_KNIGHT2  
    global b_knight2
    b_knight2 = ImageTk.PhotoImage(blckKnightImg)
    B_KNIGHT2 = canvas.create_image(650, 50, image=b_knight2)


def createWhiteBishop():
    # White bishops
    whtBishopImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/white_bishop.png")
    whtBishopImg = whtBishopImg.resize((70, 80), Image.ANTIALIAS)
    
    global W_BISHOP1    
    global w_bishop1
    w_bishop1 = ImageTk.PhotoImage(whtBishopImg)
    W_BISHOP1 = canvas.create_image(250, 750, image=w_bishop1)
      
    global W_BISHOP2  
    global w_bishop2
    w_bishop2 = ImageTk.PhotoImage(whtBishopImg)
    W_BISHOP2 = canvas.create_image(550, 750, image=w_bishop2)
    

def createBlackBishop():
    # Black bishop
    blckBishopImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/black_bishop.png")
    blckBishopImg = blckBishopImg.resize((70, 80), Image.ANTIALIAS)
        
    global B_BISHOP1
    global b_bishop1
    b_bishop1 = ImageTk.PhotoImage(blckBishopImg)
    B_BISHOP1 = canvas.create_image(250, 50, image=b_bishop1)
    
    global B_BISHOP2 
    global b_bishop2
    b_bishop2 = ImageTk.PhotoImage(blckBishopImg)
    B_BISHOP2 = canvas.create_image(550, 50, image=b_bishop2)

def createwhiteKingnQueen():
    # White King/Queen
    whtKingImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/white_king.png")
    whtKingImg = whtKingImg.resize((70, 80), Image.ANTIALIAS)
    
    global W_KING
    global w_king
    w_king = ImageTk.PhotoImage(whtKingImg)
    W_KING = canvas.create_image(450, 750, image=w_king)
        
    whtQueenImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/white_queen.png")
    whtQueenImg = whtQueenImg.resize((70, 80), Image.ANTIALIAS)
    
    global W_QUEEN
    global w_queen
    w_queen = ImageTk.PhotoImage(whtQueenImg)
    W_QUEEN = canvas.create_image(350, 750, image=w_queen)

def createBlackKingnQueen():
    # Black King/Queen
    blckKingImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/black_king.png")
    blckKingImg = blckKingImg.resize((70, 80), Image.ANTIALIAS)
        
    blckQueenImg = Image.open("C:/Users/vsid3/eclipse-workspace/Chess_Game/src/black_queen.png")
    blckQueenImg = blckQueenImg.resize((70, 80), Image.ANTIALIAS)
        
    global B_KING
    global b_king
    b_king = ImageTk.PhotoImage(blckKingImg)
    B_KING = canvas.create_image(450, 50, image=b_king)
     
    global B_QUEEN   
    global b_queen
    b_queen = ImageTk.PhotoImage(blckQueenImg)
    B_QUEEN = canvas.create_image(350, 50, image=b_queen)

def createMatrix():
    global matrix
    matrix = [
        ["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
        ["b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn", "b_pawn"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn", "w_pawn"],
        ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"]
        ]
    
    global objMatrix
    objMatrix = [[b_rook1, b_knight1, b_bishop1, b_queen, b_king, b_bishop2, b_knight2, b_rook2],
                 [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8],
                 [w_rook1, w_knight1, w_bishop1, w_queen, w_king, w_bishop2, w_knight2, w_rook2]
        ]
    
    global canvasMatrix
    canvasMatrix = [[B_ROOK1, B_KNIGHT1, B_BISHOP1, B_QUEEN, B_KING, B_BISHOP2, B_KNIGHT2, B_ROOK2],
                 [B_PAWN1, B_PAWN2, B_PAWN3, B_PAWN4, B_PAWN5, B_PAWN6, B_PAWN7, B_PAWN8],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                 [WHITE_PAWN1, WHITE_PAWN2, WHITE_PAWN3, WHITE_PAWN4, WHITE_PAWN5, WHITE_PAWN6, WHITE_PAWN7, WHITE_PAWN8],
                 [W_ROOK1, W_KNIGHT1, W_BISHOP1, W_QUEEN, W_KING, W_BISHOP2, W_KNIGHT2, W_ROOK2]
        ]
    
    global generalMatrix
    global blackPiece
    blackPiece = "B"
    global whitePiece
    whitePiece = "W"
    generalMatrix = [
                     [blackPiece, blackPiece, blackPiece, blackPiece, blackPiece, blackPiece, blackPiece, blackPiece],
                     [blackPiece, blackPiece, blackPiece, blackPiece, blackPiece, blackPiece, blackPiece, blackPiece],
                     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
                     [whitePiece, whitePiece, whitePiece, whitePiece, whitePiece, whitePiece, whitePiece, whitePiece],
                     [whitePiece, whitePiece, whitePiece, whitePiece, whitePiece, whitePiece, whitePiece, whitePiece] 
                    ]
    
class CheckKing():
    
    def kingCheck(self, Posx, Posy, xCurrent, yCurrent):
        global isKingCheck, kingY, kingX, queenY, queenX, bishopY, bishopX, knightY, knightX, rookY, rookX
        global pieceCheck
        global title  
        title = ""
        pieceCheck = ""
        
        # Finding King Location without using yCurrent and xCurrent values.
        for y in range(0, 8):
            for x in range(0, 8):
                if matrix[y][x] == "w_king":
                    kingY = y
                    kingX = x
                    break
                
        for y in range(0, 8):
            for x in range(0, 8):
                if matrix[y][x] == "b_rook":
                    rookY = y
                    rookX = x
                    break
                
        for y in range(0, 8):
            for x in range(0, 8):
                if matrix[y][x] == "b_knight":
                    knightY = y
                    knightX = x
                    break
        
        for y in range(0, 8):
            for x in range(0, 8):
                if matrix[y][x] == "b_bishop":
                    bishopY = y
                    bishopX = x
                    break
        
        for y in range(0, 8):
            for x in range(0, 8):
                if matrix[y][x] == "b_queen":
                    queenY = y
                    queenX = x
                    break
        
        topY = knightY - 2
        topLeftX = knightX - 1
        topRightX = knightX + 1
            
        topMidY = knightY - 1 
        topMidRightX = knightX + 2
        topMidLeftX = knightX - 2
            
        bottomMidY = knightY + 1
        bottomMidRightX = knightX + 2
        bottomMidLeftX = knightX - 2
            
        bottomY = knightY + 2
        bottomRightX = knightX + 1
        bottomLeftX = knightX - 1
        
            
        # Checks every square from the rook to the top of the board.
        for y in range(0, rookY):
            if matrix[rookY-(y+1)][rookX] == "w_king":
                isKingCheck = True
                pieceCheck = "b_rook"
            elif matrix[rookY-(y+1)][rookX] != "":
                break
        # Checks every square from the rook to the bottom of the board.
        for y in range(rookY+1, 8):
            if matrix[y][rookX] == "w_king":
                isKingCheck = True
                pieceCheck = "b_rook"
            elif matrix[y][rookX] != "":
                break
        # Checks every square from the rook to the left side of the board.   
        for x in range(0, rookX):
            if matrix[rookY][rookX-(x+1)] == "w_king":
                isKingCheck = True
                pieceCheck = "b_rook"
            elif matrix[rookY][rookX-(x+1)] != "":
                break
            
        # Checks every square from the rook to the right side of the board.
        for x in range(rookX+1, 8):
            if matrix[rookY][x] == "w_king":
                isKingCheck = True
                pieceCheck = "b_rook"
            elif matrix[rookY][x] != "":
                break
                
        
        # Knight Check
        if ((kingY == topY and kingX == topLeftX) or (kingY == topY and kingX == topRightX) or (kingY == topMidY and kingX == topMidLeftX) or (kingY == topMidY and kingX == topMidRightX) or (kingY == bottomMidY and kingX ==  bottomMidLeftX) or (kingY == bottomMidY and kingX == bottomMidRightX) or (kingY == bottomY and kingX == bottomLeftX) or (kingY == bottomY and kingX == bottomRightX)):     
            isKingCheck = True
            pieceCheck = "b_knight"
            
        # Pawn Check
        if kingY == 7 and kingX == 0:
            if matrix[kingY - 1][kingX + 1] == "b_pawn":
                isKingCheck = True
                pieceCheck = "b_pawn"
            
        elif kingY == 7 and kingX == 7:
            if matrix[kingY - 1][kingX - 1] == "b_pawn":
                isKingCheck = True
                pieceCheck = "b_pawn"
           
        elif kingX < 7 and kingX > 0 and kingY < 7 and kingY > 0:
            if matrix[kingY + 1][kingX - 1] == "b_pawn" or matrix[kingY + 1][kingX + 1] == "b_pawn":
                isKingCheck = True
                pieceCheck = "b_pawn"
            
           
        add = 1
        # Checking the top right diagonal of bishop movement.
        for y in range(0, bishopY): 
            for x in range(bishopX + add, bishopX + add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (matrix[bishopY - y][x] != "w_king" and matrix[bishopY - y][x] != ""):
                        break
                        
                    elif (matrix[bishopY - y][x] == "w_king"):
                        isKingCheck = True
                        pieceCheck = "b_bishop"
            else:
                continue
            break
            
        add = 1
                
        # Checking the bottom right diagonal of bishop movement.  
        for y in range(bishopY+1, 8):  
            for x in range(bishopX + add, bishopX + add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (matrix[y][x] != "w_king" and matrix[y][x] != ""):
                        break
                        
                    elif (matrix[y][x] == "w_king"):
                        isKingCheck = True
                        pieceCheck = "b_bishop"
            else:
                continue
            break
                           
        add = 1
               
        # Checking the top left diagonal of bishop movement.    
        for y in range(0, bishopY):   
            for x in range(bishopX - add, bishopX - add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (matrix[bishopY - y][x] != "w_king" and matrix[bishopY - y][x] != ""):
                        break
                        
                    elif (matrix[bishopY - y][x] == "w_king"):
                        isKingCheck = True
                        pieceCheck = "b_bishop"
            else:
                continue
            break                     
            
        add = 1
        # Checking the bottom left diagonal of bishop movement.   
        for y in range(bishopY+1, 8):   
            for x in range(bishopX - add, bishopX - add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (matrix[y][x] != "w_king" and matrix[y][x] != ""):
                        break
                        
                    elif (matrix[y][x] == "w_king"):
                        isKingCheck = True
                        pieceCheck = "b_bishop"
            else:
                continue
            break
            
        add = 1
            
                        
        # This is used if a discovered check were to ever happen. Example: Black Pawn moves from e4 to e6 resulting in a check by the black bishop.
        if matrix[yCurrent][xCurrent] != "":
            # ROOK CHECK WITH KING POSITION
            # Checks every square from the king to the top of the board.
            
            for y in range(0, kingY):
                if matrix[kingY-(y+1)][kingX] == "b_rook":
                    isKingCheck = True
                    pieceCheck = "b_rook"
                elif matrix[kingY-(y+1)][kingX] != "":
                    break
            # Checks every square from the king to the bottom of the board.
            for y in range(kingY+1, 8):
                if matrix[y][kingX] == "b_rook":
                    isKingCheck = True
                    pieceCheck = "b_rook"
                elif matrix[y][kingX] != "":
                    break
            # Checks every square from the king to the left side of the board.   
            for x in range(0, kingX):
                if matrix[kingY][kingX-(x+1)] == "b_rook":
                    isKingCheck = True
                    pieceCheck = "b_rook"
                elif matrix[kingY][kingX-(x+1)] != "":
                    break
            # Checks every square from the king to the right side of the board.
            for x in range(kingX+1, 8):
                if matrix[kingY][x] == "b_rook":
                    isKingCheck = True
                    pieceCheck = "b_rook"
                elif matrix[kingY][x] != "":
                    break
            
            # BISHOP CHECK FROM KING POSITION
            add = 1
            # Checking the top right diagonal of bishop movement.
            for y in range(0, kingY): 
                for x in range(kingX + add, kingX + add+1):
                    add += 1
                    if (x < 8 and y < 8):
                        if (matrix[kingY - y][x] == "b_bishop"):
                            isKingCheck = True
                            pieceCheck = "b_bishop"
                        elif matrix[kingY - y][x] != "":
                            break
                else:
                    continue
                break
            
            add = 1
                
            # Checking the bottom right diagonal of bishop movement.  
            for y in range(kingY, 8):  
                for x in range(kingX + add, kingX + add+1):
                    add += 1
                    if (x < 8 and y < 8):
                        if (matrix[y][x] == "b_bishop"):
                            isKingCheck = True
                            pieceCheck = "b_bishop"
                        elif (matrix[y][x] != ""):
                            break
                else:
                    continue
                break
            
            add = 1
               
            # Checking the top left diagonal of bishop movement.    
            for y in range(0, kingY):   
                for x in range(kingX - add, kingX - add+1):
                    add += 1
                    if (x < 8 and y < 8):
                        if (matrix[kingY - y][x] == "b_bishop"):
                            isKingCheck = True
                            pieceCheck = "b_bishop"
                        elif (matrix[kingY - y][x] != ""):
                            break
                else:
                    continue
                break
            
            add = 1
            # Checking the bottom left diagonal of bishop movement.   
            for y in range(kingY, 8):   
                for x in range(kingX - add, kingX - add+1):
                    add += 1
                    if (x < 8 and y < 8):
                        if (matrix[y][x] == "b_bishop"):
                            isKingCheck = True
                            pieceCheck = "b_bishop" 
                        elif (matrix[y][x] != ""):
                            break
                else:
                    continue
                break
         
        # None of the pieces are checking the King.       
        return isKingCheck
     
    def blockCheck(self, xCurrent, yCurrent):
        global isKingCheck
        pieceY = -1
        pieceX = -1
        
        for y in range(kingY, rookY):
            if rookY-(y+1) == yCurrent and rookX == xCurrent:
                pieceY = yCurrent 
                pieceX = xCurrent
                break
            else:
                continue
        # Checks every square from the rook to the bottom of the board.
        for y in range(rookY+1, kingY):
            if y == yCurrent and rookX == xCurrent:
                pieceY = yCurrent 
                pieceX = xCurrent
                break
            else:
                continue
        # Checks every square from the rook to the left side of the board.   
        for x in range(kingX, rookX):
            if rookY == yCurrent and rookX-(x+1) == xCurrent:
                pieceY = yCurrent
                pieceX = xCurrent 
                break
            else:
                continue
                
        # Checks every square from the rook to the right side of the board.
        for x in range(rookX+1, kingX):
            if rookY == yCurrent and x == xCurrent:
                pieceY = yCurrent
                pieceX = xCurrent 
                break
            else:
                continue
        
        add = 1
        # Checking the top right diagonal of bishop movement.
        for y in range(kingY, bishopY): 
            for x in range(bishopX + add, bishopX + add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (bishopY - y != yCurrent and x != xCurrent):
                        break
                        
                    elif (bishopY - y == yCurrent and x == xCurrent):
                        pieceY = yCurrent
                        pieceX = xCurrent
            else:
                continue
            break
            
        add = 1
                
        # Checking the bottom right diagonal of bishop movement.  
        for y in range(bishopY+1, kingY):  
            for x in range(bishopX + add, bishopX + add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (y != yCurrent and x != xCurrent):
                        break
                        
                    elif (y == yCurrent and x == xCurrent):
                        pieceY = yCurrent
                        pieceX = xCurrent
            else:
                continue
            break
                           
        add = 1
               
        # Checking the top left diagonal of bishop movement.    
        for y in range(kingY, bishopY):   
            for x in range(bishopX - add, bishopX - add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (bishopY - y != yCurrent and x != xCurrent):
                        break
                        
                    elif (bishopY - y == yCurrent and x == xCurrent):
                        pieceY= yCurrent
                        pieceX = xCurrent
            else:
                continue
            break                     
            
        add = 1
        # Checking the bottom left diagonal of bishop movement.   
        for y in range(bishopY+1, kingY):   
            for x in range(bishopX - add, bishopX - add+1):
                add += 1
                if (x < 8 and y < 8):
                    if (y != yCurrent and x != xCurrent):
                        break
                        
                    elif (y == yCurrent and x == xCurrent):
                        pieceY = yCurrent 
                        pieceX = xCurrent
            else:
                continue
            break
            
        add = 1
        
        if pieceCheck == "b_rook" or pieceCheck == "b_bishop":
            if pieceY != -1 and pieceX != -1:
                isKingCheck = False
                return True
        
        if (bishopY == yCurrent and bishopX == xCurrent) or (rookY == yCurrent and rookX == xCurrent):
            isKingCheck = False
            return True 

        
        else:
            return False    
        
class movePiece:
    
    global isFirstClick
    isFirstClick = True 
    global isWhite
    isWhite = True
    global Check
    Check = CheckKing()
    
    
    def captureBlackPiece(self, Posx, Posy, xCurrent, yCurrent):
        if generalMatrix[yCurrent][xCurrent] != whitePiece:

            matrix[yCurrent][xCurrent] = pieceStr
            matrix[preY][preX] = ""
            
            canvas.delete(canvasMatrix[yCurrent][xCurrent])  
            canvasMatrix[yCurrent][xCurrent] = NULL 
                            
            canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image=piece)
            canvas.delete(canvasMatrix[preY][preX])
            canvasMatrix[preY][preX] = NULL
                            
                                                
            objMatrix[yCurrent][xCurrent] = piece
            objMatrix[preY][preX] = NULL    
                                        
            generalMatrix[yCurrent][xCurrent] = whitePiece
            generalMatrix[preY][preX] = NULL 
    
    def captureWhitePiece(self, Posx, Posy, xCurrent, yCurrent): 
        if generalMatrix[yCurrent][xCurrent] != blackPiece:
            
            matrix[yCurrent][xCurrent] = pieceStr
            matrix[preY][preX] = ""
                                         
                            
            localCanvasId = canvasMatrix[yCurrent][xCurrent]
            canvas.delete(localCanvasId)   
                            
            canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image=piece)
            canvas.delete(canvasMatrix[preY][preX])
            canvasMatrix[preY][preX] = NULL
                            
                                                
            objMatrix[yCurrent][xCurrent] = piece
            objMatrix[preY][preX] = NULL    
                                        
            generalMatrix[yCurrent][xCurrent] = blackPiece
            generalMatrix[preY][preX] = NULL 
        
    def paintWhitePiece(self, Posx, Posy, xCurrent, yCurrent, preY, preX):
        
        matrix[yCurrent][xCurrent] = pieceStr
        matrix[preY][preX] = ""
                                        
        objMatrix[yCurrent][xCurrent] = piece
        objMatrix[preY][preX] = NULL
                                        
        generalMatrix[yCurrent][xCurrent] = whitePiece
        generalMatrix[preY][preX] = NULL
        
        localCanvasId = canvasMatrix[yCurrent][xCurrent]
          
        canvas.delete(canvasId)
                                        
        canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image=piece)
        canvasMatrix[preY][preX] = NULL
    
    def paintBlackPiece(self, Posx, Posy, xCurrent, yCurrent, preY, preX):
        
        matrix[yCurrent][xCurrent] = pieceStr
        matrix[preY][preX] = ""
                                        
                                        
        objMatrix[yCurrent][xCurrent] = piece
        objMatrix[preY][preX] = NULL
                                        
        generalMatrix[yCurrent][xCurrent] = blackPiece
        generalMatrix[preY][preX] = NULL
                                
        canvas.delete(canvasId)
                                        
        canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image=piece)
        canvasMatrix[preY][preX] = NULL
    
    def movePawn(self, Posx, Posy, xCurrent, yCurrent, preX, preY, moveTwo):
        global isWhite
        global title
        global isKingCheck
        Check.blockCheck(xCurrent, yCurrent)
        if ((Check.blockCheck(xCurrent, yCurrent) or isKingCheck == False) and isWhite and ((matrix[preY][preX] == "w_pawn" and generalMatrix[yCurrent][xCurrent] != whitePiece) or (matrix[yCurrent][xCurrent] == "" and matrix[preY][preX] == "w_pawn"))):
                
            if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                    
                if ((yCurrent + 1) == preY) and ((xCurrent + 1) == preX or (xCurrent - 1) == preX):
                        
                    matrix[yCurrent][xCurrent] = pieceStr
                    matrix[preY][preX] = ""
                         
                    localCanvasId = canvasMatrix[yCurrent][xCurrent]
                    canvas.delete(localCanvasId)   
                                
                    objMatrix[yCurrent][xCurrent] = piece
                    objMatrix[preY][preX] = NULL    
                        
                    generalMatrix[yCurrent][xCurrent] = whitePiece
                    generalMatrix[preY][preX] = NULL
                        
                    if (yCurrent == 0): 
                        canvas.delete(canvasMatrix[preY][preX])       
                        canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image = w_queen)
                        
                        matrix[yCurrent][xCurrent] = "w_queen"
                                    
                        objMatrix[yCurrent][xCurrent] = w_queen
                            
                        generalMatrix[yCurrent][xCurrent] = whitePiece
                    else:
                            
                        canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image=piece)
                            
                        canvas.delete(canvasMatrix[preY][preX])
                        canvasMatrix[preY][preX] = NULL 
                      
            # If the user is attempting to move the white pawn.   
            if canvas.bind("<Button-1>") and matrix[preY][preX] == pieceStr:
                # Ensures that no piece hopping is allowed.
                if (matrix[preY-1][preX] == ""):
                        
                    if (preY < 6):
                        moveTwo = False
                     
                           
                    if (preY - yCurrent) < 3 and abs(preX - xCurrent) < 1 and moveTwo == True:
                        if yCurrent < preY:
                                
                            self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                            
                    elif ((preY - yCurrent) < 2  and abs(preX - xCurrent) < 1 and moveTwo == False and generalMatrix[yCurrent][xCurrent] != blackPiece):
                        if yCurrent < preY:
                            
                            self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                            
                        if (yCurrent == 0): 
                            
                            canvas.delete(canvasMatrix[preY][preX])       
                            canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image = w_queen)
                            
                            matrix[yCurrent][xCurrent] = "w_queen"
                                        
                            objMatrix[yCurrent][xCurrent] = w_queen
                                
                            generalMatrix[yCurrent][xCurrent] = whitePiece 
            if (Check.kingCheck(Posx, Posy, xCurrent, yCurrent)):
                self.paintWhitePiece(Posx, Posy, preX, preY, yCurrent, xCurrent)
                
            isWhite = False
        # 2nd click, checks to see where user is trying to move the black pawn.
        elif (isWhite == False and ((matrix[preY][preX] == "b_pawn"and generalMatrix[yCurrent][xCurrent] != blackPiece) or (matrix[yCurrent][xCurrent] == "" and matrix[preY][preX] == "b_pawn"))):
                    
            if (generalMatrix[yCurrent][xCurrent] == whitePiece):
                    
                if ((yCurrent - 1) == preY) and ((xCurrent + 1) == preX or (xCurrent - 1) == preX):
                        
                    matrix[yCurrent][xCurrent] = pieceStr
                    matrix[preY][preX] = ""
                         
                        
                    localCanvasId = canvasMatrix[yCurrent][xCurrent]
                    canvas.delete(localCanvasId)       
                                
                    objMatrix[yCurrent][xCurrent] = piece
                    objMatrix[preY][preX] = NULL
                        
                    generalMatrix[yCurrent][xCurrent] = blackPiece
                    generalMatrix[preY][preX] = NULL
                                
                    if (yCurrent == 7): 
                        canvas.delete(canvasMatrix[preY][preX])       
                        canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image = b_queen)
                        
                        matrix[yCurrent][xCurrent] = "b_queen"
                                    
                        objMatrix[yCurrent][xCurrent] = b_queen
                            
                        generalMatrix[yCurrent][xCurrent] = blackPiece
                        
                    else:
                            
                        canvasMatrix[yCurrent][xCurrent] = canvas.create_image(Posx, Posy, image=piece)
                            
                        canvas.delete(canvasMatrix[preY][preX])
                        canvasMatrix[preY][preX] = NULL
                        
            elif canvas.bind("<Button-1>") and matrix[preY][preX] == pieceStr:
                # Ensures that no piece hopping is allowed.
                if (matrix[preY+1][preX] == ""):
                    if (preY > 1):
                        moveTwo = False 

                    if (yCurrent - preY) < 3 and abs(preX - xCurrent) < 1 and moveTwo == True:
                        if preY < yCurrent:
                            
                            self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                            
                    elif ((yCurrent - preY) < 2 and abs(preX - xCurrent) < 1 and moveTwo == False and generalMatrix[yCurrent][xCurrent] != whitePiece):
                        if preY < yCurrent:
                            
                            self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            isWhite = True
        
        if (Check.kingCheck(Posx, Posy, xCurrent, yCurrent)):
            title = "Check: "
            print("WHITE KING IS IN CHECK")
        
    def moveRook(self, Posx, Posy, xCurrent, yCurrent, preX, preY):

        global isWhite
        pieceX = -1
        pieceY = -1
        global title, isKingCheck
        
        
        
        if yCurrent - preY != 0:
            for y in range(preY, yCurrent + int((yCurrent-preY)/abs(preY-yCurrent)), int((yCurrent-preY)/abs(preY-yCurrent))):
                if y == preY: continue
                if (generalMatrix[y][xCurrent] == whitePiece or generalMatrix[y][xCurrent] == blackPiece):
                    pieceX = xCurrent
                    pieceY = y
                    break    
           
        if xCurrent - preX != 0:            
            for x in range(preX, xCurrent + int((xCurrent-preX)/abs(xCurrent-preX)), int((xCurrent-preX)/abs(xCurrent-preX))):
                if x == preX: continue
                if (generalMatrix[yCurrent][x] == whitePiece or generalMatrix [yCurrent][x] == blackPiece):
                    pieceX = x
                    pieceY = yCurrent
                    break
           
        Check.kingCheck(Posx, Posy, xCurrent, yCurrent)
                 
        # USER CLICKS ON A WHITE ROOK
        if isKingCheck == False and matrix[preY][preX] == "w_rook" and isWhite:      
                 
            if (pieceY < preY):
                if (yCurrent >= pieceY):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE BLACK PIECE WITHOUT PIECE HOPPING!
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) < 1):
                
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                        
                    elif generalMatrix[yCurrent][xCurrent] != whitePiece and abs(xCurrent - preX) < 1:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                                
            if (pieceY > preY):
                if (yCurrent <= pieceY):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE BLACK PIECE WITHOUT PIECE HOPPING!
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) < 1):
                
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                        
                    elif generalMatrix[yCurrent][xCurrent] != whitePiece and abs(xCurrent - preX) < 1:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                    
            if (pieceX < preX):
                if (xCurrent >= pieceX):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE BLACK PIECE WITHOUT PIECE HOPPING!
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(yCurrent - preY) < 1):
                
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
    
    
                    elif generalMatrix[yCurrent][xCurrent] != whitePiece and abs(yCurrent - preY) < 1:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            if (pieceX > preX):
                if (xCurrent <= pieceX):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE BLACK PIECE WITHOUT PIECE HOPPING!  
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(yCurrent - preY) < 1):
                
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                        
                    elif generalMatrix[yCurrent][xCurrent] != whitePiece and abs(yCurrent - preY) < 1:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            isWhite = False
                         
        # USER CLICKS ON BLACK PAWN
        elif matrix[preY][preX] == "b_rook" and isWhite == False:      
                 
            if (pieceY < preY):
                if (yCurrent >= pieceY):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE WHITE PIECE WITHOUT PIECE HOPPING!
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) < 1):
                
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                        
                    elif generalMatrix[yCurrent][xCurrent] != blackPiece and abs(xCurrent - preX) < 1:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                                
            if (pieceY > preY):
                if (yCurrent <= pieceY):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE WHITE PIECE WITHOUT PIECE HOPPING!
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) < 1):
                
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                        
                    elif generalMatrix[yCurrent][xCurrent] != blackPiece and abs(xCurrent - preX) < 1:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            if (pieceX < preX):
                if (xCurrent >= pieceX):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE WHITE PIECE WITHOUT PIECE HOPPING!
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(yCurrent - preY) < 1):
                
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
    
    
                    elif generalMatrix[yCurrent][xCurrent] != blackPiece and abs(yCurrent - preY) < 1:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            if (pieceX > preX):
                if (xCurrent <= pieceX):
                    
                    #TRYING TO FIGURE OUT HOW TO CAPTURE WHITE PIECE WITHOUT PIECE HOPPING!  
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(yCurrent - preY) < 1):
                
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                        
                    elif generalMatrix[yCurrent][xCurrent] != blackPiece and abs(yCurrent - preY) < 1:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            isWhite = True
            
            if (Check.kingCheck(Posx, Posy, xCurrent, yCurrent)):
                title = "Check: "
                print("WHITE KING IS IN CHECK")
          
    def moveKnight(self, Posx, Posy, xCurrent, yCurrent, preX, preY):
        global isWhite, isKingCheck
        topY = preY - 2
        topLeftX = preX - 1
        topRightX = preX + 1
            
        topMidY = preY - 1 
        topMidRightX = preX + 2
        topMidLeftX = preX - 2
            
        bottomMidY = preY + 1
        bottomMidRightX = preX + 2
        bottomMidLeftX = preX - 2
            
        bottomY = preY + 2
        bottomRightX = preX + 1
        bottomLeftX = preX - 1
        
        CheckKing.kingCheck(self, Posx, Posy, xCurrent, yCurrent)
        
        if (isKingCheck == False and matrix[preY][preX] == "w_knight" and isWhite):
            
            if ((yCurrent == topY and xCurrent == topLeftX) or (yCurrent == topY and xCurrent == topRightX) or (yCurrent == topMidY and xCurrent == topMidLeftX) or (yCurrent == topMidY and xCurrent == topMidRightX) or (yCurrent == bottomMidY and xCurrent ==  bottomMidLeftX) or (yCurrent == bottomMidY and xCurrent == bottomMidRightX) or (yCurrent == bottomY and xCurrent == bottomLeftX) or (yCurrent == bottomY and xCurrent == bottomRightX)):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
            
            isWhite = False
                                                                                                                                                                                                                                                                                                                                                                     
        # BLACK KNIGHT MOVEMENT    
        if (matrix[preY][preX] == "b_knight" and isWhite == False):
            
            if ((yCurrent == topY and xCurrent == topLeftX) or (yCurrent == topY and xCurrent == topRightX) or (yCurrent == topMidY and xCurrent == topMidLeftX) or (yCurrent == topMidY and xCurrent == topMidRightX) or (yCurrent == bottomMidY and xCurrent ==  bottomMidLeftX) or (yCurrent == bottomMidY and xCurrent == bottomMidRightX) or (yCurrent == bottomY and xCurrent == bottomLeftX) or (yCurrent == bottomY and xCurrent == bottomRightX)):
                        
                self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)     
                
            isWhite = True 
            
        if (Check.kingCheck(Posx, Posy, xCurrent, yCurrent)):
            title = "Check: "
            print("WHITE KING IS IN CHECK")
                                                                                                                                                                     
    def moveBishop(self, Posx, Posy, xCurrent, yCurrent, preX, preY):
        global isWhite, isKingCheck
        pieceX = -1
        pieceY = -1
        tempXCurrent = xCurrent
        xMultiplier = 0
        global title
        
        if yCurrent - preY != 0 and xCurrent - preX != 0:
            for y in range(preY, yCurrent + int((yCurrent-preY)/abs(preY-yCurrent)), int((yCurrent-preY)/abs(preY-yCurrent))):
                    
                if y == preY: continue
                    
                xMultiplier += 1
                if (generalMatrix[y][preX + xMultiplier*int((tempXCurrent-preX)/abs(tempXCurrent-preX))] == whitePiece or generalMatrix[y][preX + xMultiplier*int((tempXCurrent-preX)/abs(tempXCurrent-preX))] == blackPiece):
                    
                    pieceX = tempXCurrent
                    pieceY = y
                    tempXCurrent += int((tempXCurrent-preX)/abs(tempXCurrent-preX))
                    break
                
        if isKingCheck == False and matrix[preY][preX] == "w_bishop" and isWhite:
            
            if pieceX == -1 and pieceY == -1 and abs(xCurrent - preX) == abs(yCurrent - preY):
                
                self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                 
            if pieceY < preY and pieceX > preX:
                
                if yCurrent >= pieceY and xCurrent <= pieceX:
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent) 
                        
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            if pieceY < preY and pieceX < preX:
                    
                if yCurrent >= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                            
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                            
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)

            if pieceY > preY and pieceX < preX:
                    
                if yCurrent <= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                            
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent) 
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                            
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX) 
                        
            if pieceY > preY and pieceX > preX:
                    
                if yCurrent <= pieceY and xCurrent <= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                            
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)  
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                            
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)                                              
            isWhite = False
            
        # Black Bishop Movement
        if matrix[preY][preX] == "b_bishop" and isWhite == False:
            
            if pieceX == -1 and pieceY == -1 and abs(xCurrent - preX) == abs(yCurrent - preY):
                
                self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                 
            if pieceY < preY and pieceX > preX:
                
                if yCurrent >= pieceY and xCurrent <= pieceX:
                    
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent) 
                        
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            if pieceY < preY and pieceX < preX:
                    
                if yCurrent >= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                            
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                            
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)

            if pieceY > preY and pieceX < preX:
                    
                if yCurrent <= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                            
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent) 
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                            
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX) 
                        
            if pieceY > preY and pieceX > preX:
                    
                if yCurrent <= pieceY and xCurrent <= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY)):
                            
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)  
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY):
                            
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)                                              
            isWhite = True
            
        if (Check.kingCheck(Posx, Posy, xCurrent, yCurrent)):
            title = "Check: "
            print("WHITE KING IS IN CHECK")
                    
    def moveQueen(self, Posx, Posy, xCurrent, yCurrent, preX, preY):
        
        global isWhite, isKingCheck
        global queenX
        global queenY
        pieceX = -1
        pieceY = -1
        tempXCurrent = xCurrent
        xMultiplier = 0
        

        
        if yCurrent - preY != 0 and xCurrent - preX != 0:
            for y in range(preY, yCurrent + int((yCurrent-preY)/abs(preY-yCurrent)), int((yCurrent-preY)/abs(preY-yCurrent))):
                    
                if y == preY: continue
                    
                xMultiplier += 1
                xDiagonal = preX + xMultiplier*int((tempXCurrent-preX)/abs(tempXCurrent-preX))
                if (xDiagonal <= 7 and generalMatrix[y][xDiagonal] != NULL):
                    
                    pieceX = tempXCurrent
                    pieceY = y
                    tempXCurrent += int((tempXCurrent-preX)/abs(tempXCurrent-preX))
                    break
                
        if (yCurrent - preY != 0 and xCurrent - preX < 1):   
            
            for y in range(preY, yCurrent + int((yCurrent-preY)/abs(preY-yCurrent)), int((yCurrent-preY)/abs(preY-yCurrent))):
                
                if y == preY: continue
                
                if (abs(yCurrent - preY) > 0 and abs(xCurrent - preX) < 1) and (generalMatrix[y][xCurrent] != NULL):
                    
                    pieceX = tempXCurrent
                    pieceY = y
                    break
             
        elif (xCurrent - preX != 0 and yCurrent - preY < 1):
            for x in range(preX, xCurrent + int((xCurrent-preX)/abs(preX-xCurrent)), int((xCurrent-preX)/abs(preX-xCurrent))):
                
                if x == preX: continue
                
                if (abs(xCurrent - preX) > 0 and abs(yCurrent - preY) < 1) and (generalMatrix[yCurrent][x] != NULL):
                    
                    pieceX = x
                    pieceY = yCurrent
                    break
             
        CheckKing.kingCheck(self, Posx, Posy, xCurrent, yCurrent)
                
        if isKingCheck == False and matrix[preY][preX] == "w_queen" and isWhite:
            
            # Piece is not found.
            if pieceX == -1 and pieceY == -1 and (abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                
                self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            # Piece is found in front and to the right of the queen.
            elif pieceY <= preY and pieceX >= preX:
                
                if yCurrent >= pieceY and xCurrent <= pieceX:
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent) 
                        
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(yCurrent - preY) < 1:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            # Piece is found in front and to the left of the queen.     
            elif pieceY <= preY and pieceX <= preX:
                    
                if yCurrent >= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                            
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY)or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                            
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            # Piece is found behind and to the left of the queen
            elif pieceY >= preY and pieceX <= preX:
                    
                if yCurrent <= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                            
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent) 
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                            
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX) 
            
            # Piece is found behind and to the right of the queen.           
            elif pieceY >= preY and pieceX >= preX:
                    
                if yCurrent <= pieceY and xCurrent <= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                                
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)  
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                            
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)                                              
            isWhite = False

        if matrix[preY][preX] == "b_queen" and isWhite == False:
            
            # Piece is not found.
            if pieceX == -1 and pieceY == -1 and (abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                
                self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            # Piece is found in front and to the right of the queen.
            elif pieceY <= preY and pieceX >= preX:
                
                if yCurrent >= pieceY and xCurrent <= pieceX:
                    
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent) 
                        
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            # Piece is found in front and to the left of the queen.     
            elif pieceY <= preY and pieceX <= preX:
                    
                if yCurrent >= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                            
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                            
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            # Piece is found behind and to the left of the queen
            elif pieceY >= preY and pieceX <= preX:
                    
                if yCurrent <= pieceY and xCurrent >= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                            
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent) 
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                            
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX) 
            
            # Piece is found behind and to the right of the queen.           
            elif pieceY >= preY and pieceX >= preX:
                    
                if yCurrent <= pieceY and xCurrent <= pieceX:
                        
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece and abs(xCurrent - preX) == abs(yCurrent - preY) or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1):
                                
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)  
                            
                    elif generalMatrix[yCurrent][xCurrent] == NULL and abs(xCurrent - preX) == abs(yCurrent - preY)or abs(xCurrent - preX) < 1 or abs(yCurrent - preY) < 1:
                            
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)                                              
            isWhite = True
        queenX = xCurrent
        queenY = yCurrent
        
    def moveKing(self, Posx, Posy, xCurrent, yCurrent, preX, preY):
        
        global isWhite
        pieceX = -1
        pieceY = -1

        difX = xCurrent - preX  
        difY = yCurrent - preY
        
        forwardY = preY-1
        backwardY = preY + 1
        normalX = preX
        normalY = preY
        rightX = preX+1
        leftX = preX-1
        
        
        if matrix[preY][preX] == "w_king" and isWhite:
            
            # no forward piece hopping
            
            if preY == 7 and preX == 0:
                
                if (generalMatrix[forwardY][normalX] != whitePiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[forwardY][rightX] != whitePiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[normalY][rightX] != whitePiece and yCurrent == normalY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preY == 7 and preX == 7:
                
                if (generalMatrix[forwardY][normalX] != whitePiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != whitePiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[forwardY][leftX] != whitePiece and yCurrent == forwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                
            elif preY == 0 and preX == 0:

                if (generalMatrix[backwardY][normalX] != whitePiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != whitePiece and yCurrent == backwardY and xCurrent == rightX) or (generalMatrix[normalY][rightX] != whitePiece and yCurrent == normalY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            elif preY == 0 and preX == 7:

                if (generalMatrix[backwardY][normalX] != whitePiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != whitePiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[backwardY][leftX] != whitePiece and yCurrent == backwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            elif preY == 7:
                
                if (generalMatrix[forwardY][normalX] != whitePiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != whitePiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[normalY][rightX] != whitePiece and yCurrent == normalY and xCurrent == rightX) or (generalMatrix[forwardY][rightX] != whitePiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[forwardY][leftX] != whitePiece and yCurrent == forwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preY == 0:

                bottomLeft = matrix[preY + 1][preX - 1]
                
                if (generalMatrix[backwardY][normalX] != whitePiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != whitePiece and yCurrent == backwardY and xCurrent == rightX) or (generalMatrix[backwardY][leftX] != whitePiece and yCurrent == backwardY and xCurrent == leftX) or (generalMatrix[normalY][leftX] != whitePiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[normalY][rightX] != whitePiece and yCurrent == normalY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preX == 7:
                
                if (generalMatrix[forwardY][normalX] != whitePiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != whitePiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[forwardY][leftX] != whitePiece and yCurrent == forwardY and xCurrent == leftX) or (generalMatrix[backwardY][normalX] != whitePiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][leftX] != whitePiece and yCurrent == backwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preX == 0:
                
                
                if (generalMatrix[forwardY][normalX] != whitePiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][rightX] != whitePiece and yCurrent == normalY and xCurrent == rightX) or (generalMatrix[forwardY][rightX] != whitePiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[backwardY][normalX] != whitePiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != whitePiece and yCurrent == backwardY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            else:
            
                                
                if (generalMatrix[forwardY][normalX] != whitePiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][rightX] != whitePiece and yCurrent == normalY and xCurrent == rightX) or (generalMatrix[forwardY][rightX] != whitePiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[backwardY][normalX] != whitePiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != whitePiece and yCurrent == backwardY and xCurrent == rightX) or (generalMatrix[normalY][leftX] != whitePiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[forwardY][leftX] != whitePiece and yCurrent == forwardY and xCurrent == leftX) or (generalMatrix[backwardY][leftX] != whitePiece and yCurrent == backwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureBlackPiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintWhitePiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            isWhite = False   
        
        if matrix[preY][preX] == "b_king" and isWhite == False:
            
            # no forward piece hopping
            
            if preY == 7 and preX == 0:
   
                if (generalMatrix[forwardY][normalX] != blackPiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[forwardY][rightX] != blackPiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[normalY][rightX] != blackPiece and yCurrent == normalY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preY == 7 and preX == 7:

                if (generalMatrix[forwardY][normalX] != blackPiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != blackPiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[forwardY][leftX] != blackPiece and yCurrent == forwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                
            elif preY == 0 and preX == 0:
                
                if (generalMatrix[backwardY][normalX] != blackPiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != blackPiece and yCurrent == backwardY and xCurrent == rightX) or (generalMatrix[normalY][rightX] != blackPiece and yCurrent == normalY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            elif preY == 0 and preX == 7:
  
                if (generalMatrix[backwardY][normalX] != blackPiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != blackPiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[backwardY][leftX] != blackPiece and yCurrent == backwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            elif preY == 7:

                if (generalMatrix[forwardY][normalX] != blackPiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != blackPiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[normalY][rightX] != blackPiece and yCurrent == normalY and xCurrent == rightX) or (generalMatrix[forwardY][rightX] != blackPiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[forwardY][leftX] != blackPiece and yCurrent == forwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preY == 0:
                
                if (generalMatrix[backwardY][normalX] != blackPiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != blackPiece and yCurrent == backwardY and xCurrent == rightX) or (generalMatrix[backwardY][leftX] != blackPiece and yCurrent == backwardY and xCurrent == leftX) or (generalMatrix[normalY][leftX] != blackPiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[normalY][rightX] != blackPiece and yCurrent == normalY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            elif preX == 7:

                if (generalMatrix[forwardY][normalX] != blackPiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][leftX] != blackPiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[forwardY][leftX] != blackPiece and yCurrent == forwardY and xCurrent == leftX) or (generalMatrix[backwardY][normalX] != blackPiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][leftX] != blackPiece and yCurrent == backwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                            
            elif preX == 0:

                if (generalMatrix[forwardY][normalX] != blackPiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][rightX] != blackPiece and yCurrent == normalY and xCurrent == rightX) or (generalMatrix[forwardY][rightX] != blackPiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[backwardY][normalX] != blackPiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != blackPiece and yCurrent == backwardY and xCurrent == rightX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == blackPiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
            
            else:
                
                if (generalMatrix[forwardY][normalX] != blackPiece and yCurrent == forwardY and xCurrent == normalX) or (generalMatrix[normalY][rightX] != blackPiece and yCurrent == normalY and xCurrent == rightX) or (generalMatrix[forwardY][rightX] != blackPiece and yCurrent == forwardY and xCurrent == rightX) or (generalMatrix[backwardY][normalX] != blackPiece and yCurrent == backwardY and xCurrent == normalX) or (generalMatrix[backwardY][rightX] != blackPiece and yCurrent == backwardY and xCurrent == rightX) or (generalMatrix[normalY][leftX] != blackPiece and yCurrent == normalY and xCurrent == leftX) or (generalMatrix[forwardY][leftX] != blackPiece and yCurrent == forwardY and xCurrent == leftX) or (generalMatrix[backwardY][leftX] != blackPiece and yCurrent == backwardY and xCurrent == leftX):
                    
                    if (generalMatrix[yCurrent][xCurrent] == whitePiece):
                        
                        self.captureWhitePiece(Posx, Posy, xCurrent, yCurrent)
                
                    elif generalMatrix[yCurrent][xCurrent] == NULL:
                        
                        self.paintBlackPiece(Posx, Posy, xCurrent, yCurrent, preY, preX)
                        
            isWhite = True   
            
    def getOrigin(self, eventorigin):      
        
        global pieceStr, piece, canvasId, moveTwo, preY , preX, isFirstClick, title
        xCurrent = math.ceil(eventorigin.x/100)-1
        yCurrent = math.ceil(eventorigin.y/100)-1
        Posy = yCurrent*100+50
        Posx = xCurrent*100+50
        moveTwo = True
        
        
        if (isFirstClick):
            # Selects White piece on first click
            if matrix[yCurrent][xCurrent] != "" and generalMatrix[yCurrent][xCurrent] != blackPiece:
                    
                pieceStr = matrix[yCurrent][xCurrent]
                        
                preY = yCurrent
                preX = xCurrent
                
                        
                piece = objMatrix[yCurrent][xCurrent]
                canvasId = canvasMatrix[yCurrent][xCurrent]
                    
            # Selects Black piece on first piece
            elif matrix[yCurrent][xCurrent] != "" and generalMatrix[yCurrent][xCurrent] != whitePiece:
                      
                   
                pieceStr = matrix[yCurrent][xCurrent]
                        
                preY = yCurrent
                preX = xCurrent
                
                        
                piece = objMatrix[yCurrent][xCurrent]
                canvasId = canvasMatrix[yCurrent][xCurrent]
                
            isFirstClick = False
        
        elif (isFirstClick == False):   
            Check.kingCheck(Posx, Posy, xCurrent, yCurrent)
                
            # 2nd click, checks to see where user is trying to move the white pawn.
            if canvas.bind("<Button-1>") and (matrix[preY][preX] == "w_pawn" or matrix[preY][preX] == "b_pawn"):
                self.movePawn(Posx, Posy, xCurrent, yCurrent, preX, preY, moveTwo)
            
            # White Rook Movement
            if canvas.bind("<Button-1>") and matrix[preY][preX] == "w_rook" or matrix[preY][preX] == "b_rook":
                self.moveRook(Posx, Posy, xCurrent, yCurrent, preX, preY)
            
            if canvas.bind("<Button-1>") and matrix[preY][preX] == "w_knight" or matrix[preY][preX] == "b_knight":
                self.moveKnight(Posx, Posy, xCurrent, yCurrent, preX, preY)
            
            if canvas.bind("<Button-1>") and matrix[preY][preX] == "w_bishop" or matrix[preY][preX] == "b_bishop":
                self.moveBishop(Posx, Posy, xCurrent, yCurrent, preX, preY)
                
            if canvas.bind("<Button-1>") and matrix[preY][preX] == "w_queen" or matrix[preY][preX] == "b_queen":
                self.moveQueen(Posx, Posy, xCurrent, yCurrent, preX, preY)
        
            if canvas.bind("<Button-1>") and matrix[preY][preX] == "w_king" or matrix[preY][preX] == "b_king":
                self.moveKing(Posx, Posy, xCurrent, yCurrent, preX, preY)
                
            if isWhite:
                root.title( "CHESS - " + title + "It's White's Turn")
            else:
                root.title("CHESS - " + title + "It's Black's Turn")
            title = ""
            
            
            
            isFirstClick = True
            
# Creating board and pieces
createBoard()
createWhitePawn()   
createWhiteRook()
createWhiteKnight()
createWhiteBishop()
createwhiteKingnQueen()
createBlackPawn()
createBlackRook()
createBlackKnight()
createBlackBishop()
createBlackKingnQueen()
createMatrix()

canvas2 = Canvas(root, width = 800, height = 800)
canvas2.bind()
move = movePiece()
canvas.bind("<Button-1>", move.getOrigin)

frame.pack()
root.geometry("800x800")
root.mainloop()
