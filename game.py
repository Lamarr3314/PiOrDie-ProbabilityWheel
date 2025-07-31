from pn532.api import PN532
import sys

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1017",
  database="pi"
)

def insertUser(name, first_score, second_score, third_score, total_score):
    global mydb
    mycursor = mydb.cursor()

    sql = "INSERT INTO user_info (user_name, first_score, second_score, third_score, total_score) VALUES (%s, %s, %s, %s, %s)"
    val = (name, first_score, second_score, third_score, total_score)
    mycursor.execute(sql, val)

    mydb.commit()


from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from enum import Enum
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)




class genericButton(QPushButton):
    def __init__(self, names, color):
        super().__init__(names)
        self.setStyleSheet("QPushButton"
                             "{"
                            "border-radius: 16px;"
                            "height:100px;"
                            "width:800px;"
                            "max-width:800px;"
                            f'{color}'
                            "font-size:50px"
                             "}"
                             )




def enterNamePage():
    global user
    genericEnterPage(NameWidget())
   
def enterSpinPage():
    global user
    user.setName(nameTextBox.text())
    genericEnterPage(SpinWidget())
   
def enterEndScreenPage():
    genericEnterPage(EndWidget())
   
def enterHomePageFinish():
    global user
    insertUser(user.getName(), user.getFirstPoints(), user.getSecondPoints(), user.getThirdPoints(), user.getPoints())
    genericEnterPage(HomeWidget())
    user = User()
   
def enterHomePageLeaderBoard():
    genericEnterPage(HomeWidget())
   
def enterSpinPageAgain():
    genericEnterPage(SpinWidget())
   
def enterSpunPage():
    continueWidget = ContinueWidget()
    continueWidget.generateWidget()
    genericEnterPage(continueWidget)


def enterInstructionsPage():
    genericEnterPage(InstructionsWidget())


class StartButton(genericButton):
    def __init__(self):
        super().__init__("Start", "background-color : rgb(78, 242, 110);")
        self.pressed.connect(enterNamePage)




class LeaderBoardButton(genericButton):
    def __init__(self):
        super().__init__("LeaderBoard", "background-color : rgb(242, 226, 78);")


class DoneButton(genericButton):
    def __init__(self):
        super().__init__("Done", "background-color : rgb(128, 255, 240);")
        self.pressed.connect(enterSpinPage)
       
class NextTurnButton(QPushButton):
    def __init__(self):
        super().__init__("Next Turn")
        self.setStyleSheet("QPushButton"
                             "{"
                            "border-radius: 16px;"
                            "height:100px;"
                            "width:800px;"
                            "max-width:800px;"
                            "margin-left: 500px;"
                            "background-color : rgb(212, 255, 105);"
                            "font-size:50px"
                             "}"
                             )
        self.pressed.connect(enterSpinPageAgain)
       
       
class EndGameButton(QPushButton):
    def __init__(self):
        super().__init__("End Game")
        self.setStyleSheet("QPushButton"
                             "{"
                            "border-radius: 16px;"
                            "height:100px;"
                            "width:800px;"
                            "max-width:800px;"
                            "margin-left: 500px;"
                            "background-color : rgb(57, 237, 225);"
                            "font-size:50px"
                             "}"
                             )
        self.pressed.connect(enterEndScreenPage)
class InstructionsButton(genericButton):
    def __init__(self):
        super().__init__("Instructions", "background-color : rgb(207, 205, 190);")
        self.pressed.connect(enterInstructionsPage)
       
class SpunButton(genericButton):
    def __init__(self):
        super().__init__("I Spun", "background-color : rgb(78, 242, 110);")
        self.pressed.connect(enterSpunPage)
       
class HomeButtonLeaderBoard(genericButton):
    def __init__(self):
        super().__init__("Home", "background-color : rgb(237, 204, 57);")
        self.pressed.connect(enterHomePageLeaderBoard)




class HomeButtonFinish(genericButton):
    def __init__(self):
        super().__init__("Home", "background-color : rgb(237, 204, 57);")
        self.pressed.connect(enterHomePageFinish)




class NameTextBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("QLineEdit"
                           "{"
                           "border-radius: 30px;"
                           "font: bold;"
                           "font-size: 70px;"
                           "height: 100px;"
                           "max-width: 800px;"
                           "}")




       
class genericWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(2400)
        self.setFixedHeight(1400)
        self.layouts = QVBoxLayout()
        self.layouts.setAlignment(QtCore.Qt.AlignCenter)




class specialTokens(Enum):
    DoublePoints = 1,
    PI = 2
   
app = QApplication([])
mainWidget=object




class User():
    def __init__(self):
        self.name = ""
        self.points = 0
        self.turns = 3
        self.nextMessage = ""
        self.pointMessage =""
        self.firstPoints =0
        self.secondPoints =0
        self.thirdPoints = 0
        self.continueMessage = ""
        self.nextButton = StartButton()
       
    def setName(self, value):
        self.name = value
   
    def resetTurns(self):
        self.turns = 0
   
    def resetPoints(self):
        self.points = 0
       
    def addPoints(self, point):
        self.points +=point
   
    def hasTurns(self):
        return self.turns !=0
   
    def subtractTurn(self):
        self.turns-=1
       
    def doublePoints(self):
        self.points*=2
   
    def setNextMessage(self, message):
        self.nextMessage = message
       
    def setPointMessage(self, message):
        self.pointMessage = message        
   
    def setContinueMessage(self, message):
        self.continueMessage = message
       
    def getPointLabel(self):
        label = QLabel(self.pointMessage)
        label.setStyleSheet("font-size :80px;padding-left: 50px;")
        return label
   
   
    def getNextLabel(self):
        label = QLabel(self.nextMessage)
        label.setStyleSheet("font-size :80px; padding-left: 50px;")
        return label
   
    def setNextButton(self, button):
        self.nextButton = button
       
    def getNextButton(self):
        return self.nextButton
   
    def getTurns(self):
        return self.turns
   
    def getName(self):
        return self.name
   
    def getPoints(self):
        return self.points
        
    def setSecondTurn(self, value):
        self.secondPoints = value
    def setFirstTurn(self, value):
        self.firstPoints = value
    def setThirdTurn(self, value):
        self.thirdPoints = value
    def getFirstPoints(self):
        return self.firstPoints
    def getSecondPoints(self):
        return self.secondPoints
    def getThirdPoints(self):
        return self.thirdPoints
   
   
user = User()


def getFirstPercentile(points):
    return points /1


def getSecondPercentile(points):
    return points/2
    
def getThirdPercentile(points):
    return points/3


class TokenManager():
    def __init__(self):
        self.pointMap ={84:100, 3:100, 233:200, 27:300, 249:300, 96:500, 101:1000, 57:specialTokens.PI, 69: specialTokens.DoublePoints, 173:-500}
        self.pointResult = 0
       
    def registerPoint(self, token):
        global user
        user.subtractTurn()
        self.pointResult = self.pointMap[token]
        name = user.getName()
        if(self.pointResult==specialTokens.PI):
            user.setNextMessage("Get PI'd bud, Your score is now reset ¯\_(ツ)_/¯")
            user.resetPoints()
            user.resetTurns()
        elif(self.pointResult == specialTokens.DoublePoints):
            user.setNextMessage("Double Points")
            user.doublePoints()
        else:
            user.addPoints(self.pointResult)
            if(self.pointResult<0):
                user.setNextMessage("Goofy, you just lost some points")
            else:
                user.setNextMessage(f'Great work getting {self.pointResult} points')
        percentile= 0
        if(user.getTurns()==2):
            user.setFirstTurn(user.getPoints())
            percentile = getFirstPercentile(user.getPoints())
        elif(user.getTurns() ==1):
            user.setSecondTurn(user.getPoints())
            percentile = getSecondPercentile(user.getPoints())
        elif(user.getTurns()==0):
            user.setThirdTurn(user.getPoints())
            percentile = getThirdPercentile(user.getPoints())
        
        user.setPointMessage(f'{name}, you are in the {percentile} of all contestants')
       
           
        if(not user.hasTurns()):
            user.setNextButton(EndGameButton())
        else:
            user.setNextButton(NextTurnButton())




       
class HomeWidget(genericWidget):
    def __init__(self):
        super().__init__()
        self.titleLabel = QLabel("Pi or Di")
        self.titleLabel.setStyleSheet("font-size :80px; padding-left:250px;")
        self.layouts.addWidget(self.titleLabel)
        self.label = QLabel(self)
        self.pixmap = QPixmap("gold-wheel.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.setStyleSheet("padding-left :150px")
        self.layouts.addWidget(self.label)
        startButton = StartButton()
        self.layouts.addWidget(startButton)
        self.layouts.addWidget(LeaderBoardButton())
        self.layouts.addWidget(InstructionsButton())
        self.setLayout(self.layouts)
        global nameTextBox
        nameTextBox = NameTextBox()
               
   
       
class NameWidget(genericWidget):
    def __init__(self):
        super().__init__()
        global nameTextBox
        self.titleLabel = QLabel("Enter Your Name")
        self.titleLabel.setStyleSheet("font-size: 80px;padding-left: 75px;")
        self.layouts.addWidget(self.titleLabel)
        self.layouts.addWidget(nameTextBox)
        self.layouts.addWidget(DoneButton())
        self.setLayout(self.layouts)
       
class SpinWidget(genericWidget):
    def __init__(self):
        super().__init__()        
        self.titleLabel = QLabel("Spin the Wheel!")
        self.titleLabel.setStyleSheet("font-size :80px;padding-left: 75px;")
        self.layouts.addWidget(self.titleLabel)
        self.layouts.addWidget(SpunButton())
        self.setLayout(self.layouts)
       
class ContinueWidget(genericWidget):
    def __init__(self):
        super().__init__()
   
    def generateWidget(self):
        global user
        TokenManager().registerPoint(readSensor())
        self.pointLabel = user.getPointLabel()
        self.nextLabel = user.getNextLabel()
        self.layouts.addWidget(self.pointLabel)
        self.layouts.addWidget(self.nextLabel)
        self.button =user.getNextButton()
        self.layouts.addWidget(self.button)
        self.setLayout(self.layouts)
       
class EndWidget(genericWidget):
    def __init__(self):
        global user
        super().__init__()
        self.original = QLabel(f'Your Score: {user.getPoints()}pts')
        self.original.setStyleSheet("font-size: 80px")
        self.first = QLabel(f'You scored better than or equal to {getPercentile(user.getPoints())} ')
        self.first.setStyleSheet("font-size: 60px")
        self.endButton = HomeButtonFinish()
       
        self.layouts.addWidget(self.original)
        self.layouts.addWidget(self.first)
        self.layouts.addWidget(self.endButton)
        self.setLayout(self.layouts)
        
class InstructionsWidget(genericWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.pixmap = QPixmap("qrcode.png")
        self.betterpixmap = self.pixmap.scaled(500,500, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(self.betterpixmap)
        self.label.setStyleSheet("padding-left:150px;padding-bottom: 150px")
        self.layouts.addWidget(self.label)
        self.layouts.addWidget(HomeButtonLeaderBoard())
        self.setLayout(self.layouts)
       
class LeaderBoardWidget(genericWidget):
    def __init__(self):
        super().__init__()
        self.grid = QTableWidget()
       
       
       
def getPercentile(points):
    return points/2




def readSensor():
    nfc = PN532()
    read = nfc.read()
    return read[6]




def genericEnterPage(object):
    global mainWidget
    mainWidget.hide()
    mainWidget = object
    mainWidget.show()








mainWidget = HomeWidget()




mainWidget.show()#static implementation of the main window
