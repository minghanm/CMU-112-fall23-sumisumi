from cmu_graphics import *
from PIL import Image
import os, pathlib

from boardClass import Board
from leaderboardClass import Leaderboard

import random

##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_onAppStart(app):
    app.line1 = [
        {"name": app.nonbiImage, "x": 40, "y": 10, "width": 80, "height": 80},
        {"name": app.nyankoyakiImage, "x": 87+40, "y": 10, "width": 80, "height": 80},
        {"name": app.tokageImage, "x": 87*2+40, "y": 10, "width": 80, "height": 80},
        {"name": app.hokoriImage, "x": 87*3+40, "y": 10, "width": 80, "height": 80},
        {"name": app.jinbesanImage, "x": 87*4+40, "y": 10, "width": 80, "height": 80},
        {"name": app.mikanboyaImage, "x": 87*5+40, "y": 10, "width": 80, "height": 80},
        {"name": app.penguinImage, "x": 87*6+40, "y": 10, "width": 80, "height": 80},
        {"name": app.necolonImage, "x": 87*7+40, "y": 10, "width": 80, "height": 80},
        {"name": app.shirokumaImage, "x": 87*8+40, "y": 10, "width": 80, "height": 80}
    ]
    app.line2 = [
        {"name": app.nonbiImage, "x": 40, "y": 720, "width": 80, "height": 80},
        {"name": app.nyankoyakiImage, "x": 87+40, "y": 720, "width": 80, "height": 80},
        {"name": app.tokageImage, "x": 87*2+40, "y": 720, "width": 80, "height": 80},
        {"name": app.hokoriImage, "x": 87*3+40, "y": 720, "width": 80, "height": 80},
        {"name": app.jinbesanImage, "x": 87*4+40, "y": 720, "width": 80, "height": 80},
        {"name": app.mikanboyaImage, "x": 87*5+40, "y": 720, "width": 80, "height": 80},
        {"name": app.penguinImage, "x": 87*6+40, "y": 720, "width": 80, "height": 80},
        {"name": app.necolonImage, "x": 87*7+40, "y": 720, "width": 80, "height": 80},
        {"name": app.shirokumaImage, "x": 87*8+40, "y": 720, "width": 80, "height": 80}
    ]

def splashScreenMode_redrawAll(app):
    drawLabel("SUMI SUMI", 350, 350, fill='skyBlue', font="montserrat", bold=True, border="white", borderWidth=3, size=120)
    drawLabel("click to start", 350, 450, size=20)
    for image1 in app.line1:
        drawImage(image1["name"], image1["x"], image1["y"], width=image1["width"], height=image1["height"])
    for image2 in app.line2:
        drawImage(image2["name"], image2["x"], image2["y"], width=image2["width"], height=image2["height"])

def splashScreenMode_onStep(app):
    for image1 in app.line1:
        image1["x"] += 1

        if image1["x"] > app.width + image1["width"]//2:
            image1["x"] = -image1["width"]//2

    for image2 in app.line2:
        image2["x"] += 1

        if image2["x"] > app.width + image2["width"]//2:
            image2["x"] = -image2["width"]//2

#the use can press any key to enter the home page
def splashScreenMode_onMousePress(app, mouseX, mouseY):
    app.music.play(loop = True)
    app.playing = True
    setActiveScreen("homePageMode")

##########################################
# Home Page Mode
##########################################

def homePageMode_redrawAll(app):

    for i in range(1, 4):
        drawImage(app.buttonImage, 190, 80 + 150*i, width=300, height=100)
    
    drawLabel("Easy Mode", 340, 275, size=24, fill="white", bold=True)
    drawLabel("Normal Mode", 340, 275+150, size=24, fill="white", bold=True)
    drawLabel("AI to Play Against", 340, 275+300, size=24, fill="white", bold=True)
        # drawLabel(f"{i}", 100, 80 + 125*i, fill="white", size=25, bold=True)
         
        #if the user complete all the goals for that level,
        #they can have a flag on that level label
        # drawImage()

    # draw a button for how to play helper page
    drawImage(app.helperImage, 550, 100, width=50, height=50)

def homePageMode_onMousePress(app, mouseX, mouseY):
    #if the user click on the game level, go to game screen
    if 190 <= mouseX <= 500 and 230 <= mouseY <= 330:
        setActiveScreen("level1LeaderboardMode")

    if 190 <= mouseX <= 500 and 380 <= mouseY <= 480:
        setActiveScreen("level2LeaderboardMode")

    if 190 <= mouseX <= 500 and 530 <= mouseY <= 630:
        setActiveScreen("level3LeaderboardMode")

    #if the user click the instruction page, show instruction
    if 550 <= mouseX <= 600 and 100 <= mouseY <= 150:
        setActiveScreen("helperPageMode")

##########################################
# level1 Leaderboard Mode
##########################################
#reference: https://www.geeksforgeeks.org/read-json-file-using-python/

def level1LeaderboardMode_onAppStart(app):
    app.leaderboard1 = Leaderboard("leaderboard1.json")
    app.playerName = None

def level1LeaderboardMode_redrawAll(app):
    drawLabel("Leaderboard", 150, 150, size=20, fill="black", bold=True)
    y_position = 180

    for i, score_entry in enumerate(app.leaderboard1.scores, start=1):
        player_name = score_entry["player_name"]
        score = score_entry["score"]
        drawLabel(f"{i}. {player_name}: {score}", 150, y_position, size=14, fill="black")
        y_position += 20

def level1LeaderboardMode_onMousePress(app, mouseX, mouseY):
    setActiveScreen("level1Mode")

##########################################
# level2 Leaderboard Mode
##########################################
#reference: https://www.geeksforgeeks.org/read-json-file-using-python/

def level2LeaderboardMode_onAppStart(app):
    app.leaderboard2 = Leaderboard("leaderboard2.json")
    app.playerName = None

def level2LeaderboardMode_redrawAll(app):
    drawLabel("Leaderboard", 150, 150, size=20, fill="black", bold=True)
    y_position = 180

    for i, score_entry in enumerate(app.leaderboard2.scores, start=1):
        player_name = score_entry["player_name"]
        score = score_entry["score"]
        drawLabel(f"{i}. {player_name}: {score}", 150, y_position, size=14, fill="black")
        y_position += 20

def level2LeaderboardMode_onMousePress(app, mouseX, mouseY):
    setActiveScreen("level2Mode")

##########################################
# level3 Leaderboard Mode
##########################################
#reference: https://www.geeksforgeeks.org/read-json-file-using-python/

def level3LeaderboardMode_onAppStart(app):
    app.leaderboard3 = Leaderboard("leaderboard3.json")
    app.playerName = None

def level3LeaderboardMode_redrawAll(app):
    drawLabel("Leaderboard", 150, 150, size=20, fill="black", bold=True)
    y_position = 180

    for i, score_entry in enumerate(app.leaderboard3.scores, start=1):
        player_name = score_entry["player_name"]
        score = score_entry["score"]
        drawLabel(f"{i}. {player_name}: {score}", 150, y_position, size=14, fill="black")
        y_position += 20

def level3LeaderboardMode_onMousePress(app, mouseX, mouseY):
    setActiveScreen("level3Mode")

##########################################
# Helper Mode
##########################################

def helperPageMode_redrawAll(app):
    drawLabel("When there are two or more adjacent Sumisumi, click them to clear", 350, 40, size=17)
    drawLabel("New Sumisumi move in, pushing the others behind", 350, 65, size=17)
    for row in range(2):
        for col in range(3):
            cellWidth, cellHeight = 50, 50
            cellLeft = 60 + col * cellWidth
            cellTop = 80 + row * cellHeight
            cx, cy = (cellLeft + cellWidth/2), (cellTop + cellHeight/2)
            if (row, col) in [(0, 1), (1, 0), (1, 1), (1, 2)]:
                drawImage(app.necolonImage, cx-20, cy, width=70, height=70)
            else:
                drawImage(app.mikanboyaImage, cx-20, cy, width=70, height=70)
    drawImage(app.mouseImage, 140, 195, width=50, height=50)

    for row in range(2):
        for col in range(3):
            cellWidth, cellHeight = 50, 50
            cellLeft = 60 + col * cellWidth
            cellTop = 80 + row * cellHeight
            cx, cy = (cellLeft + cellWidth/2), (cellTop + cellHeight/2)
            if (row, col) in [(0, 1), (1, 0), (1, 1), (1, 2)]:
                drawImage(app.explosionImage, cx+185, cy+5, width=60, height=60)
            else:
                drawImage(app.mikanboyaImage, cx+180, cy, width=70, height=70)

    for col in range(3):
        cellWidth, cellHeight = 50, 50
        cellLeft = 60 + col * cellWidth
        cellTop = 80 + row * cellHeight
        cx, cy = (cellLeft + cellWidth/2), (cellTop + cellHeight/2)
        drawLine(cx+412, cy-60, cx+412, cy-50, fill='thistle', lineWidth=4, arrowEnd=True)

    for row in range(2):
        for col in range(3):
            cellWidth, cellHeight = 50, 50
            cellLeft = 60 + col * cellWidth
            cellTop = 80 + row * cellHeight
            cx, cy = (cellLeft + cellWidth/2), (cellTop + cellHeight/2)
            if (row, col) in [(1, 0), (1, 2)]:
                drawImage(app.mikanboyaImage, cx+380, cy, width=70, height=70)
            elif (row, col) in [(0, 0), (0, 2)]:
                drawImage(app.shirokumaImage, cx+380, cy, width=70, height=70)
            else:
                drawImage(app.nyankoyakiImage, cx+380, cy, width=70, height=70)
    
    for i in range(2):
        drawLine(255+i*200, 170, 260+i*200, 170, fill='mediumAquamarine', lineWidth=6, arrowEnd=True)

    drawLabel("If you clear more than 7 Sumisumi at the same time, you will have a powerUp!", 350, 260, size=17)
    for row in range(4):
        for col in range(4):
            cellWidth, cellHeight = 50, 50
            cellLeft = 60 + col * cellWidth
            cellTop = 250 + row * cellHeight
            cx, cy = (cellLeft + cellWidth/2), (cellTop + cellHeight/2)
            if (row, col) in [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 2)]:
                drawImage(app.shirokumaImage, cx, cy, width=70, height=70)
            elif (row, col) in [(0, 1), (0, 3), (2, 3), (3, 0), (3, 1)]:
                drawImage(app.penguinImage, cx, cy, width=70, height=70)
            else:
                drawImage(app.hokoriImage, cx, cy, width=70, height=70)
    drawImage(app.mouseImage, 210, 450, width=50, height=50)

    for row in range(4):
        for col in range(4):
            cellWidth, cellHeight = 50, 50
            cellLeft = 60 + col * cellWidth
            cellTop = 250 + row * cellHeight
            cx, cy = (cellLeft + cellWidth/2), (cellTop + cellHeight/2)
            if (row, col) in [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3)]:
                drawImage(app.explosionImage, cx+300, cy+10, width=50, height=50)
            elif (row, col) in [(0, 1), (0, 3)]:
                drawImage(app.penguinImage, cx+290, cy, width=70, height=70)
            else:
                drawImage(app.hokoriImage, cx+290, cy, width=70, height=70)
    drawLine(470, 460, 550, 460, fill='mediumSeaGreen', lineWidth=4, arrowStart=True, arrowEnd=True)

    drawLabel("The max number of moves you can", 250, 520, size=17)
    drawLabel("make is shown on the top left", 250, 540, size=17)
    drawImage(app.stepImage, 490, 500, width=60, height=60)
    drawLabel("20", 518, 528, fill="white", size=20, bold=True)

    drawLabel("Remove all the target", 500, 580, size=17)
    drawLabel("Sumisumi to win the game", 500, 600, size=17)
    drawRect(200, 560, 70, 70, fill="gold", opacity=80)
    drawCircle(235, 575, 10, fill="tan", opacity=80)
    drawLabel("20", 235, 575, size=16, fill="white", bold=True)
    drawImage(app.tokageImage, 210, 585, width=50, height=50)

    drawLabel("There is also a score on the top right", 250, 650, size=17)
    drawLabel("tracking your score, win a flag for yourself!", 250, 670, size=17)
    drawImage(app.flagImage, 500, 630, width=60, height=60)

    drawImage(app.buttonImage, 218, 700, width=270, height=80)
    drawLabel("Close", 350, 735, size=48, fill="white", bold=True)

def helperPageMode_onMousePress(app, mouseX, mouseY):
    if 218 <= mouseX <= 490 and 700 <= mouseY <= 780:
        setActiveScreen("homePageMode")
           
##########################################
# level 1 mode
##########################################
def level1Mode_onAppStart(app):
    return level1Mode_restartAll(app)

def level1Mode_restartAll(app):
    app.level1 = Board(5, 5, 3, 20, 20, 5000)
    app.selectedSumi = app.level1.selectSumi()

    #game start/over conditions
    app.gameOver = False
    app.gameWon = False

    #goal tracker
    app.goalSumiCount = 0
    app.bonusCount = 0
    app.level1Score = 0

    #remove delay effect
    app.counter = 0
    app.isExploded = False
    app.isEmpty = False

    app.rows = 5
    app.cols = 5
    app.tileSize = 120

    app.leaderboard1.load_scores()
    app.playerName = None

def level1Mode_redrawAll(app):
    for row in range(app.rows):
        for col in range(app.cols):
            level1Mode_draw_isometric_tile(app, row, col)
    
    level1Mode_drawSumi(app)
    #draw goal/step trackers
    level1Mode_drawStepCount(app)
    level1Mode_drawGoalTrack(app)
    drawTimePauseButton(app)

    if app.infoPage:
        drawImage(app.infoPageImage, 200, 200, width=300, height=300)
        drawLabel("Easy Mode", 350, 220, size=18, fill="white", bold=True)
        drawImage(app.retryImage, 280, 260, width=140, height=55)
        drawImage(app.playImage, 275, 330, width=150, height=55)
        drawImage(app.cancelImage, 280, 400, width=150, height=55)
    
    #game win/lose effect
    if app.gameOver and app.gameWon:
        drawImage(app.completeImage, 90, 150, width=500, height=500)
        drawLabel("click anywhere to get back the home page", 350, 20, size=20)
    if app.gameOver and not app.gameWon:
        drawImage(app.failImage, 90, 180, width=500, height=450)
        drawLabel("click anywhere to get back the home page", 350, 20, size=20)

def level1Mode_drawSumi(app):
    for row in range(5):
        for col in range(5):
            
            #randomly load sumi character on the location
            app.level1.loadSumi(row, col)

            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4

            #draw the board
            if app.level1.board[row][col] == "Neko":
                drawImage(app.nekoImage, iso_x-35, iso_y-20, width=75, height=75)
            elif app.level1.board[row][col] == "Nonbi":
                drawImage(app.nonbiImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Nyankoyaki":
                drawImage(app.nyankoyakiImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Tokage":
                drawImage(app.tokageImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Hokori":
                drawImage(app.hokoriImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Jinbesan":
                drawImage(app.jinbesanImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Mikanboya":
                drawImage(app.mikanboyaImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Necolon":
                drawImage(app.necolonImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Penguin":
                drawImage(app.penguinImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level1.board[row][col] == "Shirokuma":
                drawImage(app.shirokumaImage, iso_x-50, iso_y-30, width=100, height=100)

            #after remove the same sumi, draw a "none"
            elif app.level1.board[row][col] == "empty":
                drawPolygon(iso_x, iso_y, 
                            iso_x + app.tileSize / 2, iso_y + app.tileSize / 4,
                            iso_x, iso_y + app.tileSize / 2, 
                            iso_x - app.tileSize / 2, iso_y + app.tileSize / 4, fill=None)
            elif app.level1.board[row][col] == "explosion":
                drawImage(app.spriteList[app.spriteCounter], iso_x, iso_y, align = 'center')

# a counter showing the remaining steps the user have to reach the goal
def level1Mode_drawStepCount(app):
    drawImage(app.stepImage, 38, 38, width=100, height=100)
    drawLabel(f"{app.level1.steps}", 85, 85, size=30, fill="white", bold=True)

# a tracker showing the remaining condition to win the game
# and showing the current score
def level1Mode_drawGoalTrack(app):
    drawRect(200+30, 25+15, 250, 90, fill="gold", opacity=80)

    # the counter of the remaining number of Sumi to remove to win the game
    drawCircle(235+30, 50+15, 16, fill="tan", opacity=80)
    drawLabel(f"{app.level1.goalNum}", 235+30, 50+15, size=16, fill="white", bold=True)

    # a small sumi indicator showing the target sumi the user need to remove
    if app.level1.goalSumi == "Neko":
        drawImage(app.nekoImage, 220+30, 75+15, width=35, height=35)
    elif app.level1.goalSumi == "Nonbi":
        drawImage(app.nonbiImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Nyankoyaki":
        drawImage(app.nyankoyakiImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Tokage":
        drawImage(app.tokageImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Hokori":
        drawImage(app.hokoriImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Jinbesan":
        drawImage(app.jinbesanImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Mikanboya":
        drawImage(app.mikanboyaImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Necolon":
        drawImage(app.necolonImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Penguin":
        drawImage(app.penguinImage, 210+30, 65+15, width=50, height=50)
    elif app.level1.goalSumi == "Shirokuma":
        drawImage(app.shirokumaImage, 210+30, 65+15, width=50, height=50)

    drawRect(300+30, 35+15, 140, 30, fill="tan", opacity=80)

    # if the users can eliminate more than 5 sumi characters at the same time,
    # they will have additional bonus on their score 
    # and their will be a label showing that
    if app.bonusCount >= 5:
        drawLabel("bonus", 370+30, 30+15, size=12, fill="darkOrange", bold=True)

    # showing score
    drawLabel(f"{app.level1Score}", 370+30, 50+15, size=16, fill="white", bold=True)

    # if the score reaches the target, showing a little flag
    if app.level1Score >= app.level1.goalScore:
        drawImage(app.flagImage, 390+30, 65+15, width=50, height=50)

def level1Mode_fillBoard(app):
    board = app.level1.board

    for row in range(5):
        # Find the first empty spot from the bottom
        for col in range(5):
            # Once we get that spot, drop all sumi above down to the bottom
            if board[row][col] == "empty":
                stack = [(row, col + 1)]
                while stack:
                    currentRow, currentCol = stack.pop()
                    if currentCol <= 4 and board[currentRow][currentCol] != "empty":
                        level1Mode_dropSumi(app, board[currentRow][currentCol], board, currentRow, currentCol)
                        stack.append((currentRow, currentCol + 1))

        # Fill the remaining empty spots with random sumi
        while board[row][4] == "empty":
            board[row][4] = random.choice(app.level1.selectedSumi)
            level1Mode_dropSumi(app, board[row][4], board, row, 4)

def level1Mode_dropSumi(app, sumi, board, row, col):
    if col - 1 >= 0 and board[row][col-1] == "empty":
        board[row][col-1] = sumi
        level1Mode_dropSumi(app, sumi, board, row, col-1)
        board[row][col] = "empty"

def level1Mode_onStep(app):
    app.spriteCounter = (app.spriteCounter + 1) % len(app.spriteList)

    # when the sumi is removed, start counting
    if app.isExploded:
        app.counter += 1

        #after the hitting a number, start to refill the board
        if app.counter >= 15:
            level1Mode_removeExplosion(app)
            app.counter = 0
            app.isExploded = False

    if app.isEmpty:
        app.counter += 1
        if app.counter >= 50:
            app.startRefill = True

            '''bonus point counting'''
            #everytime refilling the board, calculate the bonus point
            if app.startRefill:

                # if the user remove 5-7 sumi at the same time
                if 5 <= app.bonusCount <= 7:
                    app.level1Score += 200

                # if 8-10 at the same time
                if 8 <= app.bonusCount <= 10:
                    app.level1Score += 300

                # if more than 11 at the same time
                if app.bonusCount >= 11:
                    app.level1Score += 500
                
                # update current condition to win the game
                # ensure the goal won't get less than 0
                if app.level1.goalNum >= app.goalSumiCount:
                    app.level1.goalNum -= app.goalSumiCount
                else:
                    app.level1.goalNum = 0

                # game won condition
                if app.level1.steps == 0 and app.level1.goalNum != 0:
                    app.gameWon = False
                    app.gameOver = True
                
                # game lose condition
                if app.level1.goalNum == 0 and app.level1.steps >= 0:
                    app.gameWon = True
                    app.gameOver = True

                # refill the board FINALLY
                level1Mode_fillBoard(app)

                #reset all the counter to initial condition
                app.goalSumiCount = 0
                app.bonusCount = 0
                app.isEmpty = False
                app.counter = 0
    
    app.leaderboard1.save_scores()
            
def level1Mode_explodeSumiCells(app, board, startR, startC, sumi):
    #reference: https://www.programiz.com/dsa/stack
    #reference: https://codereview.stackexchange.com/questions/54534/flood-fill-algorithm
    rows, cols = len(board), len(board[0])
    
    stack = [(startR, startC)]

    while stack:
        row, col = stack.pop()

        # Base case: check if out of bounds or if the sumi is not the same
        if (
            0 <= row < rows
            and 0 <= col < cols
            and board[row][col] == sumi
        ):
            # Change the sumi into empty
            board[row][col] = "explosion"

            # Check if the sumi is the target sumi and update the win condition count
            if sumi == app.level1.goalSumi:
                app.goalSumiCount += 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]:
                newR, newC = row+dr, col+dc
                # Add cells around that cell to the stack
                stack.append((newR, newC))

def level1Mode_removeExplosion(app):
    for row in range(5):
        for col in range(5):
            if app.level1.board[row][col] == "explosion":
                app.level1.board[row][col] = "empty"

                # each time the user successfully remove the sumi
                # update the bonusCount
                app.bonusCount += 1
                # update the score
                app.level1Score += 100
    app.isEmpty = True
'''
the user can click on the sumi to eliminate the same sumi around it
'''
# to get the row, col of the mouse clicked sumi
def level1Mode_getCell(app, x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4

            # Define the polygon points for the current cell
            polygon_points = [(iso_x, iso_y), (iso_x + app.tileSize / 2, iso_y + app.tileSize / 4),
                              (iso_x, iso_y + app.tileSize / 2), (iso_x - app.tileSize / 2, iso_y + app.tileSize / 4)]

            # Check if the mouse coordinates are inside the polygon
            if point_inside_polygon(x, y, polygon_points):
                return row, col
            
    return (-1, -1)

# Function to draw isometric tiles
#reference: https://www.youtube.com/watch?v=04oQ2jOUjkU
#reference: https://www.youtube.com/watch?v=ukkbNKTgf5U

def level1Mode_draw_isometric_tile(app, row, col):
    iso_x = 350+(col - row) * app.tileSize / 2
    iso_y = 350+(col + row) * app.tileSize / 4
    drawPolygon(iso_x, iso_y, 
                iso_x + app.tileSize / 2, iso_y + app.tileSize / 4,
                iso_x, iso_y + app.tileSize / 2, 
                iso_x - app.tileSize / 2, iso_y + app.tileSize / 4, fill="pink")
    
def level1Mode_onMousePress(app, mouseX, mouseY):
    app.sound.play(restart = True)
    if 550 <= mouseX <= 550+80 and 80 <= mouseY <= 160:
        app.paused = True
        app.infoPage = True
    if app.infoPage:
        if 280 <= mouseX <= 280+140 and 260 <= mouseY <= 260+55:
            app.paused = False
            app.infoPage = False
            level1Mode_restartAll(app)
        if 275 <= mouseX <= 275+150 and 330 <= mouseY <= 330+55:
            app.infoPage = False
            app.paused = False
        if 280 <= mouseX <= 280+150 and 400 <= mouseY <= 400+55:
            app.paused = False
            app.infoPage = False
            setActiveScreen("homePageMode")
    elif not app.infoPage:
        row, col = level1Mode_getCell(app, mouseX, mouseY)
        if (row, col) != (-1, -1):
            app.level1.steps -= 1
            sumi = app.level1.board[row][col]
            if isSingle(app.level1.board, row, col, sumi):
                app.level1.steps += 1
                return
            #add 
            level1Mode_explodeSumiCells(app, app.level1.board, row, col, sumi)
            app.isExploded = True
        
    if app.gameOver:
        app.playerName = app.getTextInput('What is your name?')
        app.leaderboard1.add_score(app.playerName, app.level1Score)
        level1Mode_restartAll(app)
        setActiveScreen("homePageMode")

##########################################
# level 2 mode
##########################################
def level2Mode_onAppStart(app):
    return level2Mode_restartAll(app)

def level2Mode_restartAll(app):
    app.level2 = Board(6, 6, 3, 32, 20, 15000)
    app.selectedSumi = app.level2.selectSumi()
    #game start/over conditions
    app.gameOver = False
    app.gameWon = False

    #goal tracker
    app.goalSumiCount = 0
    app.bonusCount = 0
    app.score = 0
    app.drumCount = 0

    #remove delay effect
    app.counter = 0
    app.isExploded = False
    app.isEmpty = False

    app.hintBoard = [([None] * app.level2.col) for row in range(app.level2.row)]  # Create a copy of the board for simulation
    app.hintTimer = 0

    app.leaderboard2.load_scores()
    app.playerName = None

def level2Mode_redrawAll(app):
    # #draw hint
    for row in range(6):
        for col in range(6):
            level2Mode_draw_isometric_tile(app, row, col)
    
    level2Mode_drawSumi(app)

    level2Mode_drawHint(app)

    #draw goal/step trackers
    level2Mode_drawStepCount(app)
    level2Mode_drawGoalTrack(app)
    drawTimePauseButton(app)
    
    if app.infoPage:
        drawImage(app.infoPageImage, 200, 200, width=300, height=300)
        drawLabel("Normal Mode", 350, 220, size=18, fill="white", bold=True)
        drawImage(app.retryImage, 280, 260, width=140, height=55)
        drawImage(app.playImage, 275, 330, width=150, height=55)
        drawImage(app.cancelImage, 280, 400, width=150, height=55)

    #game win/lose effect
    if app.gameOver and app.gameWon:
        drawImage(app.completeImage, 90, 150, width=500, height=500)
        drawLabel("click anywhere to get back the home page", 350, 20, size=20)
    if app.gameOver and not app.gameWon:
        drawImage(app.failImage, 90, 180, width=500, height=450)
        drawLabel("click anywhere to get back the home page", 350, 20, size=20)

def level2Mode_drawHint(app):
    for row in range(len(app.hintBoard)):
        for col in range(len(app.hintBoard[0])):
            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4
            if app.hintBoard[row][col] == "hinted":
                drawPolygon(iso_x, iso_y-20, 
                            iso_x + app.tileSize / 2, iso_y + app.tileSize / 4 -20,
                            iso_x, iso_y + app.tileSize / 2 -20, 
                            iso_x - app.tileSize / 2, iso_y + app.tileSize / 4 -20, 
                            fill="orange", opacity=60)

def level2Mode_drawSumi(app):   
    for i in range(6):
        randR, randC = random.randint(0, 5), random.randint(0, 5)
        app.level2.loadWall(randR, randC)

    for row in range(6):
        for col in range(6):
            
            #randomly load sumi character on the location
            app.level2.loadSumi(row, col)

            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4

            #draw the board
            if app.level2.board[row][col] == "Neko":
                drawImage(app.nekoImage, iso_x-35, iso_y-20, width=75, height=75)
            elif app.level2.board[row][col] == "Nonbi":
                drawImage(app.nonbiImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Nyankoyaki":
                drawImage(app.nyankoyakiImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Tokage":
                drawImage(app.tokageImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Hokori":
                drawImage(app.hokoriImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Jinbesan":
                drawImage(app.jinbesanImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Mikanboya":
                drawImage(app.mikanboyaImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Necolon":
                drawImage(app.necolonImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Penguin":
                drawImage(app.penguinImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "Shirokuma":
                drawImage(app.shirokumaImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level2.board[row][col] == "wall":
                drawImage(app.wallImage, iso_x-50, iso_y-30, width=100, height=100)
            #after remove the same sumi, draw a "none"
            elif app.level2.board[row][col] == "empty":
                drawPolygon(iso_x, iso_y, 
                            iso_x + app.tileSize / 2, iso_y + app.tileSize / 4,
                            iso_x, iso_y + app.tileSize / 2, 
                            iso_x - app.tileSize / 2, iso_y + app.tileSize / 4, fill=None)
            elif app.level2.board[row][col] == "rowRemoval":
                drawImage(app.rowRemovalImage, iso_x-45, iso_y-25, width=80, height=80)
            elif app.level2.board[row][col] == "colRemoval":
                drawImage(app.colRemovalImage, iso_x-50, iso_y-30, width=90, height=90)
            elif app.level2.board[row][col] == "peripheryRemoval":
                drawImage(app.peripheryRemovalImage, iso_x-50, iso_y-30, width=90, height=90)
            elif app.level2.board[row][col] == "sameTypeRemoval":
                drawImage(app.sameTypeRemovalImage, iso_x-50, iso_y-25, width=90, height=90)
            elif app.level2.board[row][col] == "explosion":
                drawImage(app.spriteList[app.spriteCounter], iso_x, iso_y, align = 'center')

# a counter showing the remaining steps the user have to reach the goal
def level2Mode_drawStepCount(app):
    drawImage(app.stepImage, 38, 38, width=100, height=100)
    drawLabel(f"{app.level2.steps}", 85, 85, size=30, fill="white", bold=True)

# a tracker showing the remaining condition to win the game
# and showing the current score
def level2Mode_drawGoalTrack(app):
    drawRect(200+30, 25+15, 250, 90, fill="gold", opacity=80)

    # the counter of the remaining number of Sumi to remove to win the game
    drawCircle(235+30, 50+15, 16, fill="tan", opacity=80)
    drawLabel(f"{app.level2.goalNum}", 235+30, 50+15, size=16, fill="white", bold=True)

    # a small sumi indicator showing the target sumi the user need to remove
    if app.level2.goalSumi == "Neko":
        drawImage(app.nekoImage, 220+30, 75+15, width=35, height=35)
    elif app.level2.goalSumi == "Nonbi":
        drawImage(app.nonbiImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Nyankoyaki":
        drawImage(app.nyankoyakiImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Tokage":
        drawImage(app.tokageImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Hokori":
        drawImage(app.hokoriImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Jinbesan":
        drawImage(app.jinbesanImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Mikanboya":
        drawImage(app.mikanboyaImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Necolon":
        drawImage(app.necolonImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Penguin":
        drawImage(app.penguinImage, 210+30, 65+15, width=50, height=50)
    elif app.level2.goalSumi == "Shirokuma":
        drawImage(app.shirokumaImage, 210+30, 65+15, width=50, height=50)

    drawRect(300+30, 35+15, 140, 30, fill="tan", opacity=80)

    # if the users can eliminate more than 5 sumi characters at the same time,
    # they will have additional bonus on their score 
    # and their will be a label showing that
    if app.bonusCount >= 5:
        drawLabel("bonus", 370+30, 30+15, size=12, fill="darkOrange", bold=True)

    # showing score
    drawLabel(f"{app.score}", 370+30, 50+15, size=16, fill="white", bold=True)

    # if the score reaches the target, showing a little flag
    if app.score >= app.level2.goalScore:
        drawImage(app.flagImage, 390+30, 65+15, width=50, height=50)

# Function to draw isometric tiles
def level2Mode_draw_isometric_tile(app, row, col):
    iso_x = 350+(col - row) * app.tileSize / 2
    iso_y = 350+(col + row) * app.tileSize / 4
    drawPolygon(iso_x, iso_y, 
                iso_x + app.tileSize / 2, iso_y + app.tileSize / 4,
                iso_x, iso_y + app.tileSize / 2, 
                iso_x - app.tileSize / 2, iso_y + app.tileSize / 4, fill="pink")

def level2Mode_fillBoard(app):
    board = app.level2.board

    for row in range(6):
        # Find the first empty spot from the bottom
        for col in range(6):
            # Once we get that spot, drop all sumi above down to the bottom
            if board[row][col] == "empty":
                stack = [(row, col + 1)]
                while stack:
                    currentRow, currentCol = stack.pop()
                    if currentCol <= 5 and board[currentRow][currentCol] != "empty":
                        level2Mode_dropSumi(app, board[currentRow][currentCol], board, currentRow, currentCol)
                        stack.append((currentRow, currentCol + 1))

        # Fill the remaining empty spots with random sumi
        while board[row][5] == "empty":
            board[row][5] = random.choice(app.level2.selectedSumi)
            level2Mode_dropSumi(app, board[row][5], board, row, 5)

def level2Mode_dropSumi(app, sumi, board, row, col):
    if col - 1 >= 0 and board[row][col-1] == "empty":
        board[row][col-1] = sumi
        level2Mode_dropSumi(app, sumi, board, row, col-1)
        board[row][col] = "empty"

def level2Mode_onStep(app):
    app.spriteCounter = (app.spriteCounter + 1) % len(app.spriteList)

    if app.hintTimer >= 100*200*len(app.hintBoard)*len(app.hintBoard[0]):
        app.hintTimer = 0
    app.hintTimer += 1
    if app.hintTimer >= 200 and app.hintTimer % 200 == 0:
        if app.hintTimer > 200:
            for row in range(len(app.hintBoard)):
                for col in range(len(app.hintBoard[0])):
                    app.hintBoard[row][col] = None
        # hintPlace = app.hintTimer // 200 % (len(app.hintBoard)*len(app.hintBoard[0]))
        hintPlace = random.randint(0, len(app.hintBoard)*len(app.hintBoard[0])-1)
        hintRow = hintPlace//len(app.hintBoard)
        hintCol = hintPlace%len(app.hintBoard[0])
        while isSingle(app.level2.board, hintRow, hintCol, app.level2.board[hintRow][hintCol]) or app.level2.board[hintRow][hintCol] == "wall":
            # hintPlace += 1 
            # hintPlace = hintPlace % (len(app.hintBoard)*len(app.hintBoard[0]))
            hintPlace = random.randint(0, len(app.hintBoard)*len(app.hintBoard[0])-1)
            hintRow = hintPlace//len(app.hintBoard)
            hintCol = hintPlace%len(app.hintBoard[0])
        level2Mode_getHint(app, app.level2.board, hintRow, hintCol, app.level2.board[hintRow][hintCol])

    # when the sumi is removed, start counting
    if app.isExploded:
        app.counter += 1

        #after the hitting a number, start to refill the board
        if app.counter >= 15:
            level2Mode_removeExplosion(app)
            app.counter = 0
            app.isExploded = False

    if app.isEmpty:
        app.counter += 1
        if app.counter >= 35:
            app.startRefill = True

            '''bonus point counting'''
            #everytime refilling the board, calculate the bonus point
            if app.startRefill:

                # if the user remove 5-7 sumi at the same time
                if 5 <= app.bonusCount <= 7:
                    app.score += 200

                # if 8-10 at the same time
                if 8 <= app.bonusCount <= 10:
                    app.score += 300

                # if more than 11 at the same time
                if app.bonusCount >= 11:
                    app.score += 500
                
                # update current condition to win the game
                # ensure the goal won't get less than 0
                if app.level2.goalNum >= app.goalSumiCount:
                    app.level2.goalNum -= app.goalSumiCount
                else:
                    app.level2.goalNum = 0

                # game won condition
                if (app.level2.steps == 0 and 
                    not level2Mode_wallInBoard(app) and 
                    app.level2.goalNum == 0):
                    app.gameWon = True
                    app.gameOver = True
                
                if (not level2Mode_wallInBoard(app) and 
                    app.level2.goalNum == 0 and
                    app.level2.steps >= 0):
                    app.gameWon = True
                    app.gameOver = True
                
                elif app.level2.steps == 0:
                    app.gameOver = True
                    app.gameWon = False
                    
                # refill the board FINALLY
                level2Mode_fillBoard(app)

                #reset all the counter to initial condition
                app.goalSumiCount = 0
                app.bonusCount = 0
                app.isEmpty = False
                app.counter = 0
    
    app.leaderboard2.save_scores()
            
def level2Mode_wallInBoard(app):
    for row in range(app.level2.row):
        if "wall" in app.level2.board[row]:
            return True
    return False    

def level2Mode_explodeSumiCells(app, board, startR, startC, sumi):
    rows, cols = len(board), len(board[0])

    stack = [(startR, startC)]

    while stack:
        row, col = stack.pop()

        # Base case: check if out of bounds or if the cell is not the same sumi
        if (
            0 <= row < rows
            and 0 <= col < cols
            and board[row][col] == sumi
        ):
            # Check if the cell is a wall and update it to an explosion
            if board[row][col] == "wall":
                board[row][col] = "explosion"

            # Change the current cell into an explosion
            board[row][col] = "explosion"
            app.drumCount += 1

            # Check if the sumi is the target sumi and update the win condition count
            if sumi == app.level2.goalSumi:
                app.goalSumiCount += 1

            # Add adjacent unprocessed cells to the stack
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]:
                newR, newC = row+dr, col+dc
                # Add cells around that cell to the stack
                stack.append((newR, newC))

def level2Mode_removeExplosion(app):
    for row in range(app.level2.row):
        for col in range(app.level2.col):
            if app.level2.board[row][col] == "explosion":
                app.level2.board[row][col] = "empty"

                # each time the user successfully remove the sumi
                # update the bonusCount
                app.bonusCount += 1
                # update the score
                app.score += 100
    app.isEmpty = True

# to get the row, col of the mouse clicked sumi
def level2Mode_getCell(app, x, y):
    for row in range(6):
        for col in range(6):
            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4
            # Define the polygon points for the current cell
            polygon_points = [(iso_x, iso_y), (iso_x + app.tileSize / 2, iso_y + app.tileSize / 4),
                              (iso_x, iso_y + app.tileSize / 2), (iso_x - app.tileSize / 2, iso_y + app.tileSize / 4)]

            # Check if the mouse coordinates are inside the polygon
            if point_inside_polygon(x, y, polygon_points):
                return row, col
    return (-1, -1)

def level2Mode_onMousePress(app, mouseX, mouseY):
    app.sound.play(restart = True)
    app.hintTimer = 0

    for row in range(len(app.hintBoard)):
        for col in range(len(app.hintBoard[0])):
            app.hintBoard[row][col] = None
    
    if 550 <= mouseX <= 550+80 and 80 <= mouseY <= 160:
        app.paused = True
        app.infoPage = True

    if app.infoPage:
        if 280 <= mouseX <= 280+140 and 260 <= mouseY <= 260+55:
            app.paused = False
            app.infoPage = False
            level2Mode_restartAll(app)
        if 275 <= mouseX <= 275+150 and 330 <= mouseY <= 330+55:
            app.infoPage = False
            app.paused = False
        if 280 <= mouseX <= 280+150 and 400 <= mouseY <= 400+55:
            app.paused = False
            app.infoPage = False
            setActiveScreen("homePageMode")

    elif not app.infoPage:
        row, col = level2Mode_getCell(app, mouseX, mouseY)
        if (row, col) != (-1, -1):
            app.level2.steps -= 1
            sumi = app.level2.board[row][col]
            if sumi == "rowRemoval":
                for newR, newC in [(row - 1, col), (row + 1, col), 
                                   (row, col - 1), (row, col + 1), 
                                   (row + 1, col + 1), (row - 1, col - 1)]:                    
                    #ensure it's not out of bound
                    if 0 <= newR < 6 and 0 <= newC < 6:
                        if app.level2.board[newR][newC] =="rowRemoval" or app.level2.board[newR][newC] =="colRemoval":
                            level2Mode_colRemoval(app, app.level2.board, col)

                            for sideR, sideC in [(row-1, col-1), (row+1, col+1)]:
                                if app.level2.board[sideR][sideC] == "rowRemoval" or app.level2.board[sideR][sideC] == "colRemoval":
                                    app.level2.board[sideR][sideC] = "explosion"

                        if (app.level2.board[newR][newC] =="peripheryRemoval"):
                            level2Mode_peripheryRemoval(app, app.level2.board, row, col)
                            level2Mode_colRemoval(app, app.level2.board, col)

                        level2Mode_rowRemoval(app, app.level2.board, row)
                        app.isExploded = True

            if sumi == "colRemoval":
                for newR, newC in [(row - 1, col), (row + 1, col), 
                                   (row, col - 1), (row, col + 1), 
                                   (row + 1, col + 1), (row - 1, col - 1)]:                    
                    #ensure it's not out of bound
                    if 0 <= newR < 6 and 0 <= newC < 6:
                        if (app.level2.board[newR][newC] =="rowRemoval" or 
                            app.level2.board[newR][newC] =="colRemoval"):
                            level2Mode_rowRemoval(app, app.level2.board, row)
                            for sideR, sideC in [(row-1, col-1), (row+1, col+1)]:
                                if (app.level2.board[sideR][sideC] == "rowRemoval" or 
                                    app.level2.board[sideR][sideC] == "colRemoval"):
                                    app.level2.board[sideR][sideC] = "explosion"
                        if (app.level2.board[newR][newC] =="peripheryRemoval"):
                            level2Mode_rowRemoval(app, app.level2.board, row)
                            level2Mode_peripheryRemoval(app, app.level2.board, row, col)

                        level2Mode_colRemoval(app, app.level2.board, col)
                        app.isExploded = True

            if sumi == "peripheryRemoval":
                for newR, newC in [(row - 1, col), (row + 1, col), 
                                   (row, col - 1), (row, col + 1), 
                                   (row + 1, col + 1), (row - 1, col - 1)]:                    
                    #ensure it's not out of bound
                    if 0 <= newR < 6 and 0 <= newC < 6:
                        if (app.level2.board[newR][newC] == "rowRemoval" or 
                            app.level2.board[newR][newC] == "colRemoval"):
                            
                            level2Mode_rowRemoval(app, app.level2.board, row)
                            level2Mode_colRemoval(app, app.level2.board, col)

                        if (app.level2.board[newR][newC] =="peripheryRemoval"):
                            level2Mode_peripheryRemovalPlus(app, app.level2.board, row, col)

                        level2Mode_peripheryRemoval(app, app.level2.board, row, col)
                        app.isExploded = True

            if isSingle(app.level2.board, row, col, sumi):
                app.level2.steps += 1
                return
            
            if sumi == "wall":
                app.level2.steps += 1
                return
            
            #add 
            level2Mode_explodeSumiCells(app, app.level2.board, row, col, sumi)

            if app.drumCount == 7:
                app.level2.board[row][col] = "rowRemoval"
            elif app.drumCount == 8:
                app.level2.board[row][col] = "colRemoval"
            elif app.drumCount >= 9:
                app.level2.board[row][col] = "peripheryRemoval"

            app.drumCount = 0
            app.isExploded = True
        
    if app.gameOver:
        app.playerName = app.getTextInput('What is your name?')
        app.leaderboard2.add_score(app.playerName, app.score)
        level2Mode_restartAll(app)
        setActiveScreen("homePageMode")

def level2Mode_rowRemoval(app, board, row):
    for col in range(app.level2.col):
        if board[row][col] == app.level2.goalSumi:
                app.goalSumiCount += 1
        board[row][col] = "explosion"

def level2Mode_colRemoval(app, board, col):
    for row in range(app.level2.row):
        if board[row][col] == app.level2.goalSumi:
                app.goalSumiCount += 1
        board[row][col] = "explosion"

def level2Mode_peripheryRemoval(app, board, row, col):
    for dr, dc in [(1, -1), (1, 0), (1, 1), (0, 1), (0, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1)]:
        newR, newC = row+dr, col+dc
        if 0 <= newR < 6 and 0 <= newC < 6:
            if board[newR][newC] == app.level2.goalSumi:
                app.goalSumiCount += 1
            board[newR][newC] = "explosion"

def level2Mode_peripheryRemovalPlus(app, board, row, col):
    for dr, dc in [(1, -1), (1, 0), (1, 1), (0, 1), (0, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1),
                   (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, 2), (0, -2), (0, 2),
                   (1, -2), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]:
        newR, newC = row+dr, col+dc
        if 0 <= newR < 6 and 0 <= newC < 6:
            if board[newR][newC] == app.level2.goalSumi:
                app.goalSumiCount += 1
            board[newR][newC] = "explosion"

def level2Mode_getHint(app, board, startR, startC, sumi):
    rows, cols = len(board), len(board[0])

    stack = [(startR, startC)]
    while stack:
        row, col = stack.pop()

        # Base case: check if out of bounds or if the sumi is not the same
        if 0 <= row < rows and 0 <= col < cols and board[row][col] == sumi and app.hintBoard[row][col] != "hinted":
            # Change the sumi into hinted
            app.hintBoard[row][col] = "hinted"

            # Add adjacent unprocessed cells to the stack
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]:
                newR, newC = row+dr, col+dc
                # Add cells around that cell to the stack
                stack.append((newR, newC))
##########################################
# level 3 mode
##########################################

def level3Mode_onAppStart(app):
    return level3Mode_restartAll(app)

def level3Mode_restartAll(app):
    app.level3 = Board(5, 5, 3, 20, 20, 5000)
    app.selectedSumi = app.level3.selectSumi()
    
    #game start/over conditions
    app.gameOver = False
    app.gameWon = False
    app.isPlayer = True
    app.bonusCount = 0

    #goal tracker
    app.playerGoalNum = app.level3.goalNum
    app.playerGoalSumiCount = 0
    app.playerScore = 0
    app.playerStepCount = app.level3.steps

    app.aiGoalNum = app.level3.goalNum
    app.aiGoalSumiCount = 0
    app.aiPlayerScore = 0
    app.aiStepCount = app.level3.steps

    #remove delay effect
    app.counter = 0
    app.isExploded = False
    app.isEmpty = False

    app.leaderboard3.load_scores()
    app.playerName = None

def level3Mode_redrawAll(app):

    # #draw hint
    for row in range(5):
        for col in range(5):
            level3Mode_drawIsometricTile(app, row, col)
    
    level3Mode_drawSumi(app)

    #draw goal/step trackers
    level3Mode_drawGoalTrack(app)
    level3Mode_drawStepCount(app)
    drawTimePauseButton(app)

    if app.infoPage:
        drawImage(app.infoPageImage, 200, 200, width=300, height=300)
        drawLabel("AI Mode", 350, 220, size=18, fill="white", bold=True)
        drawImage(app.retryImage, 280, 260, width=140, height=55)
        drawImage(app.playImage, 275, 330, width=150, height=55)
        drawImage(app.cancelImage, 280, 400, width=150, height=55)
    
    #game win/lose effect
    if app.gameOver and app.gameWon:
        drawImage(app.completeImage, 90, 150, width=500, height=500)
        drawLabel("click anywhere to get back the home page", 350, 20, size=20)
    if app.gameOver and not app.gameWon:
        drawImage(app.failImage, 90, 180, width=500, height=450)
        drawLabel("click anywhere to get back the home page", 350, 20, size=20)

def level3Mode_drawSumi(app):
    for row in range(5):
        for col in range(5):
            
            #randomly load sumi character on the location
            app.level3.loadSumi(row, col)

            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4

            #draw the board
            if app.level3.board[row][col] == "Neko":
                drawImage(app.nekoImage, iso_x-35, iso_y-20, width=75, height=75)
            elif app.level3.board[row][col] == "Nonbi":
                drawImage(app.nonbiImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Nyankoyaki":
                drawImage(app.nyankoyakiImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Tokage":
                drawImage(app.tokageImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Hokori":
                drawImage(app.hokoriImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Jinbesan":
                drawImage(app.jinbesanImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Mikanboya":
                drawImage(app.mikanboyaImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Necolon":
                drawImage(app.necolonImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Penguin":
                drawImage(app.penguinImage, iso_x-50, iso_y-30, width=100, height=100)
            elif app.level3.board[row][col] == "Shirokuma":
                drawImage(app.shirokumaImage, iso_x-50, iso_y-30, width=100, height=100)
            #after remove the same sumi, draw a "none"
            elif app.level3.board[row][col] == "empty":
                drawPolygon(iso_x, iso_y, 
                            iso_x + app.tileSize / 2, iso_y + app.tileSize / 4,
                            iso_x, iso_y + app.tileSize / 2, 
                            iso_x - app.tileSize / 2, iso_y + app.tileSize / 4, fill=None)
            elif app.level3.board[row][col] == "explosion":
                drawImage(app.spriteList[app.spriteCounter], iso_x, iso_y, align = 'center')

def level3Mode_drawIsometricTile(app, row, col):
    iso_x = 350+(col - row) * app.tileSize / 2
    iso_y = 350+(col + row) * app.tileSize / 4
    drawPolygon(iso_x, iso_y, 
                iso_x + app.tileSize / 2, iso_y + app.tileSize / 4,
                iso_x, iso_y + app.tileSize / 2, 
                iso_x - app.tileSize / 2, iso_y + app.tileSize / 4, fill="pink")

def level3Mode_drawGoalTrack(app):
    drawRect(130, 25+15, 250, 90, fill="gold", opacity=80)

    # the counter of the remaining number of Sumi to remove to win the game
    drawCircle(135+30, 50+15, 16, fill="tan", opacity=80)
    drawLabel(f"{app.playerGoalNum}", 135+30, 50+15, size=16, fill="white", bold=True)
    drawLabel("Your Goal Track", 290, 90+15, size=20, fill="orange", bold=True)

    # a small sumi indicator showing the target sumi the user need to remove
    if app.level3.goalSumi == "Neko":
        drawImage(app.nekoImage, 120+30, 75+15, width=35, height=35)
    elif app.level3.goalSumi == "Nonbi":
        drawImage(app.nonbiImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Nyankoyaki":
        drawImage(app.nyankoyakiImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Tokage":
        drawImage(app.tokageImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Hokori":
        drawImage(app.hokoriImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Jinbesan":
        drawImage(app.jinbesanImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Mikanboya":
        drawImage(app.mikanboyaImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Necolon":
        drawImage(app.necolonImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Penguin":
        drawImage(app.penguinImage, 110+30, 65+15, width=50, height=50)
    elif app.level3.goalSumi == "Shirokuma":
        drawImage(app.shirokumaImage, 110+30, 65+15, width=50, height=50)

    drawRect(200+30, 35+15, 140, 30, fill="tan", opacity=80)
    drawLabel(f"{app.playerScore}", 230+100, 50+15, fill="white", size=18, bold=True)

    drawRect(130, 125+15, 250, 90, fill="gold", opacity=80)

    # the counter of the remaining number of Sumi to remove to win the game
    drawCircle(135+30, 150+15, 16, fill="tan", opacity=80)
    drawLabel(f"{app.aiGoalNum}", 135+30, 150+15, size=16, fill="white", bold=True)
    drawLabel("AI Goal Track", 290, 190+15, size=20, fill="orange", bold=True)

    # a small sumi indicator showing the target sumi the user need to remove
    if app.level3.goalSumi == "Neko":
        drawImage(app.nekoImage, 120+30, 175+15, width=35, height=35)
    elif app.level3.goalSumi == "Nonbi":
        drawImage(app.nonbiImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Nyankoyaki":
        drawImage(app.nyankoyakiImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Tokage":
        drawImage(app.tokageImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Hokori":
        drawImage(app.hokoriImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Jinbesan":
        drawImage(app.jinbesanImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Mikanboya":
        drawImage(app.mikanboyaImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Necolon":
        drawImage(app.necolonImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Penguin":
        drawImage(app.penguinImage, 110+30, 165+15, width=50, height=50)
    elif app.level3.goalSumi == "Shirokuma":
        drawImage(app.shirokumaImage, 110+30, 165+15, width=50, height=50)

    drawRect(200+30, 135+15, 140, 30, fill="tan", opacity=80)
    drawLabel(f"{app.aiPlayerScore}", 230+100, 150+15, fill="white", size=18, bold=True)

    # if the score reaches the target, showing a little flag
    if app.playerScore >= app.level3.goalScore:
        drawImage(app.flagImage, 290+30, 65+15, width=50, height=50)

    if app.aiPlayerScore >= app.level3.goalScore:
        drawImage(app.flagImage, 290+30, 265+15, width=50, height=50)

def level3Mode_drawStepCount(app):
    drawImage(app.stepImage, 35, 38, width=100, height=100)
    drawLabel(f"{app.playerStepCount}", 82, 85, size=30, fill="white", bold=True)

def level3Mode_fillBoard(app):
    board = app.level3.board

    for row in range(5):
        # Find the first empty spot from the bottom
        for col in range(5):
            # Once we get that spot, drop all sumi above down to the bottom
            if board[row][col] == "empty":
                stack = [(row, col + 1)]
                while stack:
                    currentRow, currentCol = stack.pop()
                    if currentCol <= 4 and board[currentRow][currentCol] != "empty":
                        level3Mode_dropSumi(app, board[currentRow][currentCol], board, currentRow, currentCol)
                        stack.append((currentRow, currentCol + 1))

        # Fill the remaining empty spots with random sumi
        while board[row][4] == "empty":
            board[row][4] = random.choice(app.level3.selectedSumi)
            level3Mode_dropSumi(app, board[row][4], board, row, 4)
    
    app.isPlayer = not app.isPlayer

def level3Mode_dropSumi(app, sumi, board, row, col):
    if col - 1 >= 0 and board[row][col-1] == "empty":
        board[row][col-1] = sumi
        level3Mode_dropSumi(app, sumi, board, row, col-1)
        board[row][col] = "empty"

def level3Mode_onStep(app):
    app.spriteCounter = (app.spriteCounter + 1) % len(app.spriteList)

    # when the sumi is removed, start counting
    if app.isExploded:
        app.counter += 1

        #after the hitting a number, start to refill the board
        if app.counter >= 15:
            level3Mode_removeExplosion(app)
            app.counter = 0
            app.isExploded = False

    if app.isEmpty:
        app.counter += 1
        if app.counter >= 50:
            app.startRefill = True

            '''bonus point counting'''
            #everytime refilling the board, calculate the bonus point
            if app.startRefill:

                # if the user remove 5-7 sumi at the same time
                if 5 <= app.bonusCount <= 7:
                    app.score += 200

                # if 8-10 at the same time
                if 8 <= app.bonusCount <= 10:
                    app.score += 300

                # if more than 11 at the same time
                if app.bonusCount >= 11:
                    app.score += 500
                
                # update current condition to win the game
                # ensure the goal won't get less than 0
                if app.playerGoalNum >= app.playerGoalSumiCount:
                    app.playerGoalNum -= app.playerGoalSumiCount
                else:
                    app.playerGoalNum = 0

                # game won condition
                if ((app.aiGoalNum == 0 and app.aiStepCount >= 0) and
                    (app.playerGoalNum != 0)):
                    app.gameWon = False
                    app.gameOver = True
                
                # game lose condition
                if ((app.playerGoalNum == 0 and app.playerStepCount >= 0) and 
                    app.aiGoalNum != 0):
                    app.gameWon = True
                    app.gameOver = True

                if ((app.playerGoalNum == 0 and app.playerStepCount >= 0) and 
                    (app.aiGoalNum == 0 and app.aiStepCount >= 0)):
                    if app.playerScore > app.aiPlayerScore:
                        app.gameWon = True
                    else:
                        app.gameWon = False
                    app.gameOver = True

                # refill the board FINALLY
                level3Mode_fillBoard(app)
                if not app.isPlayer:
                    level3Mode_takeAction(app)
                    app.aiStepCount -= 1

                #reset all the counter to initial condition
                app.playerGoalSumiCount = 0
                app.bonusCount = 0
                app.isEmpty = False
                app.counter = 0

    app.leaderboard1.save_scores()

def level3Mode_removeExplosion(app):
    for row in range(5):
        for col in range(5):
            if app.level3.board[row][col] == "explosion":
                app.level3.board[row][col] = "empty"

                # each time the user successfully remove the sumi
                if app.isPlayer:
                    app.playerScore += 100
                else:
                    app.aiPlayerScore += 100
    app.isEmpty = True

# to get the row, col of the mouse clicked sumi
def level3Mode_getCell(app, x, y):
    for row in range(6):
        for col in range(6):
            iso_x = 350+(col - row) * app.tileSize / 2
            iso_y = 350+(col + row) * app.tileSize / 4
            # Define the polygon points for the current cell
            polygon_points = [(iso_x, iso_y), (iso_x + app.tileSize / 2, iso_y + app.tileSize / 4),
                              (iso_x, iso_y + app.tileSize / 2), (iso_x - app.tileSize / 2, iso_y + app.tileSize / 4)]

            # Check if the mouse coordinates are inside the polygon
            if point_inside_polygon(x, y, polygon_points):
                return row, col
    return (-1, -1)

def level3Mode_onMousePress(app, mouseX, mouseY):
    app.sound.play(restart = True)
    if 550 <= mouseX <= 550+80 and 80 <= mouseY <= 160:
        app.paused = True
        app.infoPage = True

    if app.infoPage:
        if 280 <= mouseX <= 280+140 and 260 <= mouseY <= 260+55:
            app.paused = False
            app.infoPage = False
            level3Mode_restartAll(app)
        if 275 <= mouseX <= 275+150 and 330 <= mouseY <= 330+55:
            app.infoPage = False
            app.paused = False
        if 280 <= mouseX <= 280+150 and 400 <= mouseY <= 400+55:
            app.paused = False
            app.infoPage = False
            setActiveScreen("homePageMode")

    elif not app.infoPage:
        if app.isPlayer:
            row, col = level3Mode_getCell(app, mouseX, mouseY)
            if (row, col) != (-1, -1):
                app.playerStepCount -= 1
                sumi = app.level3.board[row][col]
                if isSingle(app.level3.board, row, col, sumi):
                    app.playerStepCount += 1
                    return
                #add 
                level3Mode_explodeSumiCells(app, app.level3.board, row, col, sumi)
                app.isExploded = True
        
    if app.gameOver:
        app.playerName = app.getTextInput('What is your name?')
        app.leaderboard3.add_score(app.playerName, app.playerScore)
        level3Mode_restartAll(app)
        setActiveScreen("homePageMode")

def level3Mode_takeAction(app):
    validSpot = checkValidSpot(app)
    idx = random.randrange(0, len(validSpot))
    row, col = validSpot[idx]

    level3Mode_explodeSumiCells(app, app.level3.board, row, col, app.level3.board[row][col])
    app.isExploded = True
    if app.aiGoalNum >= app.aiGoalSumiCount:
        app.aiGoalNum -= app.aiGoalSumiCount
    else:
        app.aiGoalNum = 0
    app.aiGoalSumiCount = 0

def level3Mode_explodeSumiCells(app, board, startR, startC, sumi):
    rows, cols = len(board), len(board[0])
    
    stack = [(startR, startC)]

    while stack:
        row, col = stack.pop()

        # Base case: check if out of bounds or if the sumi is not the same
        if (
            0 <= row < rows
            and 0 <= col < cols
            and board[row][col] == sumi
        ):
            # Change the sumi into empty
            board[row][col] = "explosion"

            # Check if the sumi is the target sumi and update the win condition count
            if app.isPlayer and sumi == app.level3.goalSumi:
                app.playerGoalSumiCount += 1
            if not app.isPlayer and sumi == app.level3.goalSumi:
                app.aiGoalSumiCount += 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]:
                newR, newC = row+dr, col+dc
                # Add cells around that cell to the stack
                stack.append((newR, newC))

##########################################
# Main App
##########################################

def onAppStart(app): 
    app.background = 'cornSilk'
    app.stepsPerSecond = 30

    app.rows = 6
    app.cols = 6
    app.tileSize = 120

    #initial board information
    app.width = 700
    app.height = 800

    app.paused = False
    app.infoPage = False


    #image & sounds @ sumisumi matching game
    app.buttonImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/buttonBackground.PNG"))
    app.buttonImage = CMUImage(app.buttonImage)

    app.pauseImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/pause.PNG"))
    app.pauseImage = CMUImage(app.pauseImage)

    app.infoPageImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/infoPage.PNG"))
    app.infoPageImage = CMUImage(app.infoPageImage)

    app.helperImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/help.PNG"))
    app.helperImage = CMUImage(app.helperImage)

    app.mouseImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/mouse.PNG"))
    app.mouseImage = CMUImage(app.mouseImage)

    app.retryImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/retryButton.PNG"))
    app.retryImage = CMUImage(app.retryImage)

    app.playImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/playButton.PNG"))
    app.playImage = CMUImage(app.playImage)

    app.cancelImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/cancelButton.PNG"))
    app.cancelImage = CMUImage(app.cancelImage)

    app.stepImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/moveTrack.PNG"))
    app.stepImage = CMUImage(app.stepImage)

    app.explosionImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/explosion.PNG"))
    app.explosionImage = CMUImage(app.explosionImage)

    app.wallImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/wall.PNG"))
    app.wallImage = CMUImage(app.wallImage)

    #all sumi images...
    app.nekoImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Neko.PNG"))
    app.nonbiImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Nonbi.PNG"))
    app.nyankoyakiImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Nyankoyaki.PNG"))
    app.tokageImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Tokage.PNG"))
    app.hokoriImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Hokori.PNG"))
    app.jinbesanImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Jinbesan.PNG"))
    app.mikanboyaImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Mikanboya.PNG"))
    app.penguinImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Penguin.PNG"))
    app.necolonImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Necolon.PNG"))
    app.shirokumaImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/Shirokuma.PNG"))
    
    #convert to cmu image
    app.nekoImage = CMUImage(app.nekoImage)
    app.nonbiImage = CMUImage(app.nonbiImage)
    app.nyankoyakiImage = CMUImage(app.nyankoyakiImage)
    app.tokageImage = CMUImage(app.tokageImage)
    app.hokoriImage = CMUImage(app.hokoriImage)
    app.jinbesanImage = CMUImage(app.jinbesanImage)
    app.mikanboyaImage = CMUImage(app.mikanboyaImage)
    app.penguinImage = CMUImage(app.penguinImage)
    app.necolonImage = CMUImage(app.necolonImage)
    app.shirokumaImage = CMUImage(app.shirokumaImage)

    app.rowRemovalImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/rowRemoval.PNG"))
    app.colRemovalImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/colRemoval.PNG"))
    app.peripheryRemovalImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/peripheryRemoval.PNG"))
    app.sameTypeRemovalImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/sameTypeRemoval.PNG"))

    app.rowRemovalImage = CMUImage(app.rowRemovalImage)
    app.colRemovalImage = CMUImage(app.colRemovalImage)
    app.peripheryRemovalImage = CMUImage(app.peripheryRemovalImage)
    app.sameTypeRemovalImage = CMUImage(app.sameTypeRemovalImage)

    app.explosionGif = Image.open('images/explode.gif')
    app.spriteList = []
    for frame in range(app.explosionGif.n_frames):
        #Set the current frame
        app.explosionGif.seek(frame)
        #Resize the image
        fr = app.explosionGif.resize((app.explosionGif.size[0]//3, app.explosionGif.size[1]//3))
        #Flip the image
        fr = fr.transpose(Image.FLIP_LEFT_RIGHT)
        #Convert to CMUImage
        fr = CMUImage(fr)
        #Put in our sprite list
        app.spriteList.append(fr)

    print(app.spriteList)

    app.spriteCounter = 0


    #game win/lose effect images
    app.completeImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/complete!.PNG"))
    app.failImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/fail!.PNG"))
    app.flagImage = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/flag.PNG"))

    #convert to cmu image
    app.completeImage = CMUImage(app.completeImage)
    app.failImage = CMUImage(app.failImage)
    app.flagImage = CMUImage(app.flagImage)

    #home Page Visual elements
    app.levelLabel = Image.open(os.path.join(pathlib.Path(__file__).parent,"images/levelLabel.PNG"))
    app.levelLabel = CMUImage(app.levelLabel)

    app.sound = loadSound("clickSound.mp3")
    app.music = loadSound("backgroundMusic.mp3")
    app.playing = False

def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)

def drawTimePauseButton(app):
    drawImage(app.pauseImage, 550, 50, width=80, height=80)

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def isSingle(board, row, col, sumi):
    rows = len(board)
    cols = len(board[0])

    #loop over the surrouding 4 cells.
    for newR, newC in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row + 1, col + 1), (row - 1, col - 1)]:
        #ensure it's not out of bound
        if 0 <= newR < rows and 0 <= newC < cols:
            neighbor = board[newR][newC]
            # if there is any neighbor being the same sumi type as the clicked one, return False
            if neighbor == sumi:
                return False
    #if all four are not the same sumi, it is alone
    return True

def checkValidSpot(app):
    validSpot = []
    for row in range(app.level3.row):
        for col in range(app.level3.col):
            if not isSingle(app.level3.board, row, col, app.level3.board[row][col]):
                validSpot.append((row, col))
    return validSpot

def main():
    runAppWithScreens(initialScreen="splashScreenMode")

main()