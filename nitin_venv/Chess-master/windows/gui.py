from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_chessboard import Ui_MainWindow
from components.board import Board
from response import *
from request import *
import sys
import threading

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

selected_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(9, 130, 19, 255), stop:1 rgba(35, 179, 9, 255));"
selectable_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(189, 189, 0, 255), stop:1 rgba(204, 204, 0, 255));"
destroyable_stylesheet = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(203, 0, 0, 255), stop:1 rgba(220, 85, 85, 255));"
black_stylesheet = "border: 2px solid;\n background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(123, 119, 120, 255), stop:1 rgba(125, 121, 122, 255));"
white_stylesheet = "border: 2px solid;\n background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(231, 231, 231, 255), stop:1 rgba(246, 251, 247, 255));"
hoverEnter = "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffff00;\">"
hoverLeave = "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">"
hoverEnd = "</span></p></body></html>"


def ButtonToPosition(button):
    alphabet = 'ABCDEFGH'
    for letter in alphabet:
        if letter == button.objectName()[0]:
            return (int(button.objectName()[1]) - 1, alphabet.index(letter))


def PositionToButton(position):
    return 'ABCDEFGH'[position[1]] + str(position[0] + 1)


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent, window):
        QtWidgets.QPushButton.__init__(self, parent)
        self.window = window

    def mousePressEvent(self, event):
        self.window.action(self)

    def enterEvent(self, event):
        column = self.parent().parent().columns
        row = self.parent().parent().rows
        for i in range(column.count()):
            if column.itemAt(i).widget().objectName() == self.objectName()[0]:
                column.itemAt(i).widget().setText(hoverEnter + column.itemAt(i).widget().objectName() + hoverEnd)
        for i in range(row.count()):
            if row.itemAt(i).widget().objectName()[1] == self.objectName()[1]:
                row.itemAt(i).widget().setText(hoverEnter + row.itemAt(i).widget().objectName()[1] + hoverEnd)

    def leaveEvent(self, event):
        column = self.parent().parent().columns
        row = self.parent().parent().rows
        for i in range(column.count()):
            column.itemAt(i).widget().setText(hoverLeave + column.itemAt(i).widget().objectName() + hoverEnd)
            row.itemAt(i).widget().setText(hoverLeave + row.itemAt(i).widget().objectName()[1] + hoverEnd)


# board = Board()

class ChessWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, mainwindow, id, color):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.mainwindow = mainwindow
        self.id = id
        self.board = Board()
        self.setupUi(self)
        self.setWindowTitle("Chess")
        self.initializeButtons()
        self.selected = None
        self.currentColor = 'W'
        self.selectable = []
        self.destroyable = []
        self.createGridColor()
        self.createIcons()
        self.yourColor = color

        try:
            t1 = threading.Thread(target=self.action1, args=())
            t1.start()
        except:
            print ("create thread error")


    def action1(self):
        while True:
            opponentMoveResponseObject: ActiveResponse = self.mainwindow.getActiveResponse("OPMV");
            if opponentMoveResponseObject:
                moveResponse = json.loads(opponentMoveResponseObject.data)    
                inputAlgebra = moveResponse["move"]

                alphabet = 'ABCDEFGH'
                
                for words in alphabet:    #xử lí các tình huống algebra có thể xảy ra 
                    if words == inputAlgebra[2]:
                        position1 = (int(inputAlgebra[1])-1,alphabet.index(words))
                    if 'x' == inputAlgebra[3]:
                        if words == inputAlgebra[5]:
                            position2 = (int(inputAlgebra[4])-1,alphabet.index(words))
                    elif words == inputAlgebra[4]:
                        position2 = (int(inputAlgebra[3])-1,alphabet.index(words))


                button1 = self.buttons[position1[1]][position1[0]]
                button2 = self.buttons[position2[1]][position2[0]]
                if (self.board.hasPiece(position1)):
                    if (self.board.board[position1[0]][position1[1]].color == self.currentColor):
                        self.movingAnimation(button1,button2)
                        self.board.move(position1,position2)
                        self.switchColor()  #đổi màu 
                        self.createIcons()

                # TO DO: lay reply cua move -> if move ++ -> show notification: "You lose!" -> click ok -> close window, check database xem co luu match khong
                if "++" in inputAlgebra:
                    self.printText("You lose! Continue?")
                    self.yes.setGeometry(QtCore.QRect(self.yes.x(), 920, 100, 60))                    
                    self.no.setGeometry(QtCore.QRect(self.no.x(), 920, 100, 60))
                    # self.no.clicked.connect(self.closeThread)
                    

    def action(self, button):
        self.printText("")
        position = ButtonToPosition(button)
        previousColour = self.otherColor()
        if self.selected is None:   #nếu chọn được vị trí trên bàn cờ
            if self.board.hasPiece(position):   #check xem có quân cờ ở position ko
                if self.board.board[position[0]][position[1]].color == self.currentColor:   #check xem vị trí có quân cờ đấy có đúng màu của mình không
                    if self.currentColor == self.yourColor:
                        if self.board.isCheck(self.currentColor):   #check xem có vua của màu hiện tại có bị chiếu không
                            if self.currentColor == 'W':
                                self.printText("White king is in check!")
                            else:
                                self.printText("Black king is in check!")
                        #nếu không bị chiếu thì quân cờ đi bình thường
                        self.selected = button
                        LegalMovesList = self.board.board[position[0]][position[1]].getLegalMoves(self.board.board)
                        for LegalNull in LegalMovesList[0]:    #kiểm tra quân cờ được đi nước nào
                            self.selectable.append(PositionToButton(LegalNull.position))
                        for LegalDestroyable in LegalMovesList[1]:    #kiểm tra quân cờ ăn được quân cờ nào
                            self.destroyable.append(PositionToButton(LegalDestroyable.position))
                else:   #nếu quân cờ không đúng màu của mình
                        self.printText("Not your turn!")
        else:   # nếu đã chọn quân cờ
            if button != self.selected:    # nếu không click vào vị trí của quân cờ
                if button.objectName() in self.selectable or button.objectName() in self.destroyable:   #nếu nước đi của quân cờ này di chuyển được hoặc ăn được quân cờ khác 
                    #algebraicNotation
                    alphabet = 'ABCDEFGH'
                    position1 = ButtonToPosition(self.selected)
                    algebraicNotation = self.board.whatPiece(position1).getName()[2]    #get piece name
                    algebraicNotation += str(position1[0]+1) + str(alphabet[position1[1]])    #get prex prey
                    position2 = ButtonToPosition(button)
                    if(self.board.hasPiece(position2)):
                        algebraicNotation += "x"
                    algebraicNotation += str(position2[0]+1) + str(alphabet[position2[1]])    #get postx posty
                    self.movingAnimation(self.selected, button)    #animation di chuyển
                    self.board.move(ButtonToPosition(self.selected), position)  #di chuyển quân cờ được chọn tới position
                    if (self.board.isCheck(previousColour)):
                        algebraicNotation += "+"
                    if self.board.isCheck(self.currentColor):   #kiểm tra xem màu hiện tại có bị chiếu tướng không
                        algebraicNotation += "++"
                    self.switchColor()  #đổi màu 
                    print(algebraicNotation)
                    matchid = self.id
                    createMoveObject = CreateMoveObject(matchid, algebraicNotation)
                    self.mainwindow.sendRequest(createRequest("MOVE",createMoveObject))

                    moveResponse: NormalResponse = self.mainwindow.getResponse("MOVE")
                    if moveResponse:
                        if(moveResponse.code < 400):
                            responseObject = json.loads(moveResponse.data)
                            move = responseObject["move"]
                            if "++" in move:
                                self.printText("You win! Continue?")
                                self.yes.setGeometry(QtCore.QRect(self.yes.x(), 920, 100, 60))
                                self.no.setGeometry(QtCore.QRect(self.no.x(), 920, 100, 60))
                                # self.no.clicked.connect(self.closeChessWindow)
                    # TO DO: get reply
                    # TO DO: if move has ++ -> show notification: You win! -> click ok -> close window
                else:   #nước đi này không khả dĩ
                    self.printText("Can't move at this position!")
            # nếu click phải vị trí quân cờ thì unselect và quay về trạng thái chưa chọn quân cờ nào.
            self.selected = None
            self.selectable = []
            self.destroyable = []
        self.createGridColor()
        self.createIcons()

    # def closeChessWindow(self):
    #     # threading.currentThread.exit()
    #     self.close()
        
    def otherColor(self):
        if self.currentColor == 'B':
            return 'W'
        return 'B'
    def switchColor(self):
        if self.currentColor == 'B':
            self.currentColor = 'W'
        else:
            self.currentColor = 'B'

    def movingAnimation(self, button1, button2):
        fluidity = 20
        position = ButtonToPosition(button1)
        self.moving.setGeometry(QtCore.QRect(button1.x(), button1.y(), 90, 90))
        icon = QtGui.QIcon()
        button1.setIcon(icon)
        piece = self.board.board[position[0]][position[1]]

        self.moving.setIcon(self.convertToImage(piece))
        incX = (button2.x() - button1.x()) / fluidity
        incY = (button2.y() - button1.y()) / fluidity
        newX = button1.x()
        newY = button1.y()
        if "_N" not in piece.name:
            for _ in range(fluidity):
                newX += incX
                newY += incY
                self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                QtTest.QTest.qWait(10)
        else:
            """Moving 2 tiles abroad first, then 1 tile only for the Knight."""
            if abs(button2.x() - button1.x()) == 180:
                for _ in range(fluidity):
                    newX += incX
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(10)
                for _ in range(fluidity):
                    newY += incY
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(10)
            else:
                for _ in range(fluidity):
                    newY += incY
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(10)
                for _ in range(fluidity):
                    newX += incX
                    self.moving.setGeometry(QtCore.QRect(newX, newY, 90, 90))
                    QtTest.QTest.qWait(10)
        self.moving.setGeometry(QtCore.QRect(-100, -100, 90, 90))
        self.moving.setIcon(icon)

    def createIcons(self):
        for rowButton in self.buttons:
            for button in rowButton:
                for row in self.board.board:
                    for tile in row:
                        if ButtonToPosition(button) == tile.position:
                            button.setIcon(self.convertToImage(tile))

    def convertToImage(self, tile):
        icon = QtGui.QIcon()
        if tile.isNull():
            pass
        elif "B_Q" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_queen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_K" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_king.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_B" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_bishop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_N" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_knight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_R" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_rook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "B_P" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/black_pawn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_Q" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_queen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_K" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_king.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_B" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_bishop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_N" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_knight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_R" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_rook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif "W_P" == tile.name:
            icon.addPixmap(QtGui.QPixmap(":/Images/white_pawn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def createGridColor(self):
        i = 1
        j = 1
        for row in self.buttons:
            for button in row:
                if j % 2 == 1:
                    if i % 2 == 1:
                        button.setStyleSheet(white_stylesheet)
                    else:
                        button.setStyleSheet(black_stylesheet)
                else:
                    if i % 2 == 1:
                        button.setStyleSheet(black_stylesheet)
                    else:
                        button.setStyleSheet(white_stylesheet)
                if i % 8 == 0:
                    j += 1
                i += 1
                for tile in self.selectable:
                    if button.objectName() == tile:
                        button.setStyleSheet(button.styleSheet() + selectable_stylesheet)
                for tile in self.destroyable:
                    if button.objectName() == tile:
                        button.setStyleSheet(button.styleSheet() + destroyable_stylesheet)
                if self.selected is not None and button.objectName() == self.selected.objectName():
                    button.setStyleSheet(button.styleSheet() + selected_stylesheet)

    def printText(self, text):
        self.text.setText("<html><head/><body><p align=\"center\"><span style=\"font-size:28pt;font-weight:600;color:#ffffff;\">" + text + "</span></p></body></html>")

    def startNewGame(self):
        self.board.__init__()
        self.currentColor = 'W'
        self.printText("")
        self.yes.setGeometry(QtCore.QRect(self.yes.x(), -100, 100, 60))
        self.no.setGeometry(QtCore.QRect(self.no.x(), -100, 100, 60))
        self.createGridColor()
        self.createIcons()

    def initializeButtons(self):
        self.buttons = []
        for _ in range(8):
            row = [CustomButton(self.centralwidget, self) for _ in range(8)]
            self.buttons.append(row)
        new_x = 60
        i = 0
        for row in self.buttons:
            new_y = 60
            j = 0
            for button in row:
                button.setGeometry(QtCore.QRect(new_x, new_y, 90, 90))
                button.setObjectName(PositionToButton((j, i)))
                button.setIconSize(QtCore.QSize(60, 60))
                button.setCheckable(False)
                button.setDefault(False)
                button.setFlat(False)
                button.raise_()
                new_y += 90
                j += 1
            new_x += 90
            i += 1
        self.moving.raise_()
        self.yes.clicked.connect(lambda: self.startNewGame())
        self.no.clicked.connect(lambda: self.close())

