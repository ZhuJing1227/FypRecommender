# from PyQt5.QtWidgets import *
# # import sys
# # from pprint import pprint as pp
# #
# # from PyQt5.QtGui import QPixmap, QFont
# # from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QGroupBox, QLabel, \
#     QFormLayout, QLineEdit, QVBoxLayout, QRadioButton
# from PyQt5.uic.properties import QtCore
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     #main window design
#     def __init__(self):
#         super().__init__()
#
#         self.centralwidget = QWidget()
#         self.setCentralWidget(self.centralwidget)
#         self.setMinimumHeight(890)
#         self.setMinimumWidth(1500)
#         # self.setContentsMargins(500,0,500,0)
#         self.pushButton1 = QPushButton("Start", self.centralwidget)
#         self.pushButton1.clicked.connect(self.show_new_window)
#         self.pushButton2 = QPushButton("Exit", self.centralwidget)
#         self.pushButton2.clicked.connect(self.comeout)
#
#         #buttonstyle
#         self.pushButton1.setStyleSheet("QPushButton::hover"
#                              "{"
#                              "background-color : lightgreen;"
#                              "}")
#         self.pushButton2.setStyleSheet("QPushButton::hover"
#                              "{"
#                              "background-color : orange;"
#
#                              "}")
#
#         # self.setGeometry(0,0,500,500)
#         self.pushButton2.setMinimumHeight(40)
#         self.pushButton1.setMinimumHeight(40)
#         self.pushButton2.setMinimumWidth(200)
#         self.pushButton1.setMinimumWidth(200)
#         self.pushButton1.resize(300,300)
#         self.pushButton2.resize(300,300)
#
#
#         lay = QHBoxLayout(self.centralwidget)
#         lay.setContentsMargins(550,0,550,0)
#         lay.addWidget(self.pushButton1)
#         lay.addWidget(self.pushButton2)
#         lay.setSpacing(30)
#
#     def show_new_window(self, checked):
#         self.w = foodwindow()
#         self.w.show()
#         self.close()
#
#     def comeout(self, checked):
#          button = QMessageBox.critical(
#             self,
#             "Exiting Confirmation",
#             "Are you sure you want to exit?",
#             buttons=QMessageBox.No | QMessageBox.Yes ,
#             defaultButton=QMessageBox.No,)
#
#          if button == QMessageBox.No:
#             print("Rejected exit confirmation")
#          elif button == QMessageBox.Yes:
#             print("Exit")
#             self.close()
#
#
#
# #food pics
# class foodwindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     def __init__(self):
#         super().__init__()
#         # self.setStyleSheet()
#         self.setStyleSheet("background-color: beige;")
#
#         self.horizontalGroupBox = QGroupBox("Grid")
#
#         values = [  '1', '2', '3', '4', '5', '6' ,'7','8'  ]
#
#         positions = [(r, c) for r in range(2) for c in range(4)]
#
#         layoutGrid = QGridLayout()
#         self.setLayout(layoutGrid)
#         layoutGrid.setVerticalSpacing(50)
#         layoutGrid.setHorizontalSpacing(50)
#         # layoutGrid.setColumnMinimumWidth(80,50)
#         layoutGrid.setContentsMargins(50, 50, 50, 50)
#         self.setMinimumHeight(890)
#         self.setMinimumWidth(1500)
#
#         for positions, value in zip(positions, values):
#             button = QGroupBox()
#             # button.setTitle("Hello")
#             # button.setAlignment(Qt.AlignHCenter)
#             button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#             layoutGrid.addWidget(button, *positions)
#             vbox = QVBoxLayout()
#             button.setLayout(vbox)
#             foodname=QLabel("Chicken")
#             foodname.setAlignment(Qt.AlignHCenter)
#             # foodname.setStyleSheet("background-color: blue;")
#             foodname.setFont(QFont('Arial', 10))
#             foodname.setStyleSheet("background-color: lightgreen")
#
#             # foodname.setStyleSheet("font-size: 24px;")
#
#             foodname.setMaximumHeight(30)
#             vbox.addWidget(foodname)
#             vbox.setSpacing(0)
#
#             images=QLabel()
#             # images.setGeometry(100, 150, 100, 40)
#             images.setStyleSheet("border-image : url(images/Bak Kut Teh.png);")
#             vbox.addWidget(images)
#             vbox.setContentsMargins(0,0,0,0)
#
#
#     def main_menu(self, checked):
#         self.a = MainWindow()
#         self.a.show()
#         self.close()
#
#
#
#
#
#
# #main window stylesheet
# stylesheet = """
#     MainWindow {
#         border-image: url("whatsfordinner.png");
#         background-repeat: no-repeat;
#         background-position: center;
#     }
# """
#
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     app.setStyleSheet(stylesheet)     # <---
#     window = foodwindow()
#     window.resize(640, 640)
#     window.show()
#     sys.exit(app.exec_())
#
#
#
#
#
#
import os
import threading
import time
import webbrowser

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QGroupBox, QLabel, \
    QFormLayout, QLineEdit, QVBoxLayout, QRadioButton, QMainWindow, QHBoxLayout
import tobii_research as tr
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *

from collections import Counter
from PyQt5.QtGui import QPixmap, QFont, QCursor
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QGroupBox, QLabel, \
    QFormLayout, QLineEdit, QVBoxLayout, QRadioButton
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import Qt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sb
from past.builtins import execfile

import Style_Recommender as CollaborativeRecomender1
import random

most_looked = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # string value
        title = "Style Recommender App"

        # set the title
        self.setWindowTitle(title)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.setMinimumHeight(890)
        self.setMinimumWidth(1500)
        self.pushButton1 = QPushButton("START", self.centralwidget)
        self.pushButton1.clicked.connect(self.show_new_window)
        self.pushButton2 = QPushButton("EXIT", self.centralwidget)
        self.pushButton2.clicked.connect(self.comeout)
        self.pushButton1.setFont(QFont('Times', 15))
        self.pushButton2.setFont(QFont('Times', 15))
        self.pushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2.setCursor(QCursor(Qt.PointingHandCursor))


        # buttonstyle
        self.pushButton1.setStyleSheet("QPushButton::hover"
                                       "{"
                                       "background-color : #CECEE3;"
                                       "}")
        self.pushButton2.setStyleSheet("QPushButton::hover"
                                       "{"
                                       "background-color : #D4CDC4;"
                                       "}")

        # self.setGeometry(0,0,500,500)
        self.pushButton2.setMinimumHeight(40)
        self.pushButton1.setMinimumHeight(40)
        self.pushButton2.setMinimumWidth(200)
        self.pushButton1.setMinimumWidth(200)
        self.pushButton1.resize(300, 300)
        self.pushButton2.resize(300, 300)
        self.showMaximized()

        lay = QHBoxLayout(self.centralwidget)
        lay.setContentsMargins(450, 0, 450, 0)
        lay.addWidget(self.pushButton1)
        lay.addWidget(self.pushButton2)
        lay.setSpacing(30)

    def show_new_window(self, checked):
        execfile("face_updated.py")
        self.w = GridDemo()
        self.okk = okk()

        self.stylewindow = stylewindow()

        self.stylewindow.show()
        self.close()

    def comeout(self, checked):
        button = QMessageBox.critical(
            self,
            "Exiting Confirmation",
            "Are you sure you want to exit?",
            buttons=QMessageBox.No | QMessageBox.Yes,
            defaultButton=QMessageBox.No, )

        if button == QMessageBox.No:
            print("Rejected exit confirmation")
        elif button == QMessageBox.Yes:
            print("Exit")
            self.close()

    def plot(self):
        def xcord():
            with open('cords.txt', 'r') as f:
                content_list = [line.rstrip('\n') for line in f]
                ok1 = content_list[0]
                print(type(ok1))
                ok2 = eval(ok1)
                x = list(ok2)
                print(type(x))
            return x

        def ycord():
            with open('cords.txt', 'r') as f:
                last_line = f.readlines()[-1]
                ycord = last_line
            x = eval(ycord)
            y = list(x)
            print(type(y))
            return y

        x = xcord()
        y = ycord()
        print("x", x)
        print("y", y)

        counter = 0
        mp_img = mpimg.imread("Untitled.png")

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])

        test = sb.kdeplot(x, y, shade=True, cmap="Reds", alpha=0.7)
        test.collections[0].set_alpha(0)
        plt.imshow(mp_img, zorder=0, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
        ax.invert_yaxis()
        plt.axis('off')

        self.canvas = FigureCanvas(fig)
        self.canvas.draw()
        self.layoutGrid.addWidget(self.canvas)
        self.canvas.draw()

def get_gender_start():
    with open('combined.txt', 'r') as f:
        last_line = f.readlines()[-1]
        q = last_line.strip('\n')

    splitted = q.split(",")

    gender = splitted[1]
    return gender

# style pics
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        title = "Style Recommender App"

        # set the title
        self.setWindowTitle(title)
        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)
        self.layoutGrid.setVerticalSpacing(50)
        self.layoutGrid.setHorizontalSpacing(50)
        self.setMinimumHeight(890)
        self.setMinimumWidth(1500)
        self.showMaximized()

        global most_looked
        global fig

        self.ui()
        self.show()
        app.processEvents()
        thread1 = threading.Thread(target=self.eyetracker)  # so that the ui display first then scan the eyes
        # thread42 = threading.Thread(target=self.aa)# so that the ui display first then scan the eyes

        thread1.start()
        thread1.join()
        self.hide()
        # thread42.start()

    def ui(self):
        self.image = QLabel()
        global imagechooser
        gender = get_gender_start()

        if gender == 'Female':
            imagechooser = "imagechooser%d" % (random.randint(1, 3))

        elif gender == 'Male':
            imagechooser = "imagechooser%d" % (random.randint(4, 6))
        #imagechooser = "imagechooser1"

        with open('imagechooser.txt', 'w') as out:
            line1 = imagechooser
            out.write(line1)
        if imagechooser == "imagechooser1":
            print("1")
            self.image.setStyleSheet("border-image: url(StyleCataF1.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser2":
            print("2")
            self.image.setStyleSheet("border-image: url(StyleCataF2.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser3":
            print("3")
            self.image.setStyleSheet("border-image: url(StyleCataF3.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser4":
            print("4")
            self.image.setStyleSheet("border-image: url(StyleCataM1.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser5":
            print("5")
            self.image.setStyleSheet("border-image: url(StyleCataM2.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser6":
            print("6")
            self.image.setStyleSheet("border-image: url(StyleCataM3.png);")
            self.layoutGrid.addWidget(self.image)
        else:
            print("Error")

    def eyetracker(self):
        global most_looked
        import time
        time.sleep(2)
        self.gaze = []
        self.Cord = []
        self.xCord = []
        self.yCord = []
        self.counter = 0

        found_eyetrackers = tr.find_all_eyetrackers()
        my_eyetracker = found_eyetrackers[0]

        def gaze_data_callback(i):
            self.gaze.append(i)
            for i in self.gaze:
                self.Cord.append(self.gaze[self.counter]['left_gaze_point_on_display_area'])
                self.counter += 1

        my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
        time.sleep(5)
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

        print("This is the count on the counter: ", self.Cord)
        for x in self.Cord:
            self.xCord.append(x[0])
            self.yCord.append(x[1])
        self.xCord = [x for x in self.xCord if str(x) != 'nan']
        self.yCord = [x for x in self.yCord if str(x) != 'nan']
        print(self.xCord)
        print(self.yCord)
        with open('target.txt', 'w') as out:
            line1 = self.xCord
            line2 = self.yCord
            out.write('{}\n{}'.format(line1, line2))
        if imagechooser == 'imagechooser1':
            """
            Display parts of poster that was looked at the most
            """
            rank = []
            most_looked = ''
            casualf = 0
            bikerf = 0
            preppyf = 0
            vintagef = 0
            indief = 0
            chicf = 0
            sportyf = 0
            sexyf = 0

            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    casualf += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    bikerf += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    preppyf += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    vintagef += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    indief += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    chicf += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    sportyf += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    sexyf += 1

            rank.append(casualf)
            rank.append(bikerf)
            rank.append(preppyf)
            rank.append(vintagef)
            rank.append(indief)
            rank.append(chicf)
            rank.append(sportyf)
            rank.append(sexyf)

            if max(rank) == rank[0]:
                most_looked = 'Casual Style (F)'
            elif max(rank) == rank[1]:
                most_looked = 'Biker Style (F)'
            elif max(rank) == rank[2]:
                most_looked = 'Preppy Style (F)'
            elif max(rank) == rank[3]:
                most_looked = 'Vintage Style (F)'
            elif max(rank) == rank[4]:
                most_looked = 'Indie Style (F)'
            elif max(rank) == rank[5]:
                most_looked = 'Chic Style (F)'
            elif max(rank) == rank[6]:
                most_looked = 'Sporty Style (F)'
            elif max(rank) == rank[7]:
                most_looked = 'Sexy Style (F)'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser2':
            rank = []
            most_looked = ''
            streetwearf = 0
            classyf = 0
            ethnicf = 0
            y2kf = 0
            vacationf = 0
            eveningf = 0
            comfyf = 0
            artsyf = 0

            """

            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    streetwearf += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    classyf += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    ethnicf += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    y2kf += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    vacationf += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    eveningf += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    comfyf += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    artsyf += 1

            rank.append(streetwearf)
            rank.append(classyf)
            rank.append(ethnicf)
            rank.append(y2kf)
            rank.append(vacationf)
            rank.append(eveningf)
            rank.append(comfyf)
            rank.append(artsyf)

            if max(rank) == rank[0]:
                most_looked = 'Streetwear Style (F)'
            elif max(rank) == rank[1]:
                most_looked = 'Classy Style (F)'
            elif max(rank) == rank[2]:
                most_looked = 'Ethnic Style (F)'
            elif max(rank) == rank[3]:
                most_looked = 'Y2k Style (F)'
            elif max(rank) == rank[4]:
                most_looked = 'Vacation Style (F)'
            elif max(rank) == rank[5]:
                most_looked = 'Evening Style (F)'
            elif max(rank) == rank[6]:
                most_looked = 'Comfy Style (F)'
            elif max(rank) == rank[7]:
                most_looked = 'Artsy Style (F)'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser3':

            rank = []
            most_looked = ''
            hiphopf = 0
            punkf = 0
            lolitaf = 0
            bohemianf = 0
            girlnextdoorf = 0
            formalofficef = 0
            grungef = 0
            kpopf = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    hiphopf += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    punkf += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    lolitaf += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    bohemianf += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    girlnextdoorf += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    formalofficef += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    grungef += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    kpopf += 1

            rank.append(hiphopf)
            rank.append(punkf)
            rank.append(lolitaf)
            rank.append(bohemianf)
            rank.append(girlnextdoorf)
            rank.append(formalofficef)
            rank.append(grungef)
            rank.append(kpopf)

            if max(rank) == rank[0]:
                most_looked = 'Hip Hop Style (F)'
            elif max(rank) == rank[1]:
                most_looked = 'Punk Style (F)'
            elif max(rank) == rank[2]:
                most_looked = 'Lolita Style (F)'
            elif max(rank) == rank[3]:
                most_looked = 'Bohemian Style (F)'
            elif max(rank) == rank[4]:
                most_looked = 'Girl Next Door Style (F)'
            elif max(rank) == rank[5]:
                most_looked = 'Formal Office Style (F)'
            elif max(rank) == rank[6]:
                most_looked = 'Grunge Style (F)'
            elif max(rank) == rank[7]:
                most_looked = 'Kpop Style (F)'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser4':

            rank = []
            most_looked = ''
            casualm = 0
            artsym = 0
            streetwearm = 0
            sportym = 0
            ivym = 0
            chicm = 0
            grungem = 0
            formalofficem = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    casualm += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    artsym += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    streetwearm += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    sportym += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    ivym += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    chicm += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    grungem += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    formalofficem += 1

            rank.append(casualm)
            rank.append(artsym)
            rank.append(streetwearm)
            rank.append(sportym)
            rank.append(ivym)
            rank.append(chicm)
            rank.append(grungem)
            rank.append(formalofficem)

            if max(rank) == rank[0]:
                most_looked = 'Casual Style (M)'
            elif max(rank) == rank[1]:
                most_looked = 'Artsy Style (M)'
            elif max(rank) == rank[2]:
                most_looked = 'Streetwear Style (M)'
            elif max(rank) == rank[3]:
                most_looked = 'Sporty Style (M)'
            elif max(rank) == rank[4]:
                most_looked = 'Ivy Style (M)'
            elif max(rank) == rank[5]:
                most_looked = 'Chic Style (M)'
            elif max(rank) == rank[6]:
                most_looked = 'Grunge Style (M)'
            elif max(rank) == rank[7]:
                most_looked = 'Formal Office Style (M)'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser5':

            rank = []
            most_looked = ''
            comfym = 0
            y2km = 0
            punkm = 0
            varsitym = 0
            preppym = 0
            eveningm = 0
            ruggedm = 0
            ethnicm = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    comfym += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    y2km += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    punkm += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    varsitym += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    preppym += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    eveningm += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    ruggedm += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    ethnicm += 1

            rank.append(comfym)
            rank.append(y2km)
            rank.append(punkm)
            rank.append(varsitym)
            rank.append(preppym)
            rank.append(eveningm)
            rank.append(ruggedm)
            rank.append(ethnicm)

            if max(rank) == rank[0]:
                most_looked = 'Comfy Style (M)'
            elif max(rank) == rank[1]:
                most_looked = 'Y2k Style (M)'
            elif max(rank) == rank[2]:
                most_looked = 'Punk Style (M)'
            elif max(rank) == rank[3]:
                most_looked = 'Varsity Style (M)'
            elif max(rank) == rank[4]:
                most_looked = 'Preppy Style (M)'
            elif max(rank) == rank[5]:
                most_looked = 'Evening Style (M)'
            elif max(rank) == rank[6]:
                most_looked = 'Rugged Style (M)'
            elif max(rank) == rank[7]:
                most_looked = 'Ethnic Style (M)'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser6':

            rank = []
            most_looked = ''
            boynextdoorm = 0
            vintagem = 0
            bikerm= 0
            hiphopm = 0
            indiem = 0
            classym = 0
            bohemianm = 0
            vacationm = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    boynextdoorm += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    vintagem += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    bikerm += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    hiphopm += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    indiem += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    classym += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    bohemianm += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    vacationm += 1

            rank.append(boynextdoorm)
            rank.append(vintagem)
            rank.append(bikerm)
            rank.append(hiphopm)
            rank.append(indiem)
            rank.append(classym)
            rank.append(bohemianm)
            rank.append(vacationm)

            if max(rank) == rank[0]:
                most_looked = 'Boy Next Door Style (M)'
            elif max(rank) == rank[1]:
                most_looked = 'Vintage Style (M)'
            elif max(rank) == rank[2]:
                most_looked = 'Biker Style (M)'
            elif max(rank) == rank[3]:
                most_looked = 'Hip Hop Style (M)'
            elif max(rank) == rank[4]:
                most_looked = 'Indie Style (M)'
            elif max(rank) == rank[5]:
                most_looked = 'Classy Style (M)'
            elif max(rank) == rank[6]:
                most_looked = 'Bohemian Style (M)'
            elif max(rank) == rank[7]:
                most_looked = 'Vacation Style (M)'
            else:
                print("Smth went very wrong")

        print("Most looked style: ", most_looked)
        print("mostlooked type:", type(most_looked))
        with open('mostlooked.txt', 'w') as out:
            line1 = most_looked
            out.write(line1)

    def plot(self):
        def xcord():
            with open('cords.txt', 'r') as f:
                content_list = [line.rstrip('\n') for line in f]
                ok1 = content_list[0]
                print(type(ok1))
                ok2 = eval(ok1)
                x = list(ok2)
                print(type(x))
            return x

        def ycord():
            with open('cords.txt', 'r') as f:
                last_line = f.readlines()[-1]
                ycord = last_line
            x = eval(ycord)
            y = list(x)
            print(type(y))
            return y

        x = xcord()
        y = ycord()
        print("x", x)
        print("y", y)

        counter = 0
        mp_img = mpimg.imread("Untitled.png")

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])

        test = sb.kdeplot(x, y, shade=True, cmap="Reds", alpha=0.7)
        test.collections[0].set_alpha(0)
        plt.imshow(mp_img, zorder=0, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
        ax.invert_yaxis()
        plt.axis('off')

        self.canvas = FigureCanvas(fig)
        self.canvas.draw()
        self.layoutGrid.addWidget(self.canvas)
        self.canvas.draw()


class okk(QWidget):
    def __init__(self):
        super().__init__()
        title = "Style Recommender App"

        # set the title
        self.setWindowTitle(title)
        self.horizontalGroupBox = QGroupBox("Grid")
        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)
        self.layoutGrid.setVerticalSpacing(50)
        self.layoutGrid.setHorizontalSpacing(50)
        self.setMinimumHeight(890)
        self.setMinimumWidth(1500)
        self.showMaximized()

        self.ui2()

    def ui2(self):
        def xcord():
            with open('target.txt', 'r') as f:
                content_list = [line.rstrip('\n') for line in f]
                ok1 = content_list[0]
                print(type(ok1))
                ok2 = eval(ok1)
                x = list(ok2)
                print(type(x))
            return x

        def ycord():
            with open('target.txt', 'r') as f:
                last_line = f.readlines()[-1]
                ycord = last_line
            x = eval(ycord)
            y = list(x)
            print(type(y))
            return y

        x = xcord()
        y = ycord()
        print("x", x)
        print("y", y)

        counter = 0

        def getimagechooser():
            with open('imagechooser.txt', 'r') as f:
                last_line = f.readlines()[-1]
            return last_line

        image = getimagechooser()
        if image == "imagechooser1":
            mp_img = mpimg.imread("StyleCataF1.png")
        elif image == "imagechooser2":
            mp_img = mpimg.imread("StyleCataF2.png")
        elif image == "imagechooser3":
            mp_img = mpimg.imread("StyleCataF3.png")
        elif image == "imagechooser4":
            mp_img = mpimg.imread("StyleCataM1.png")
        elif image == "imagechooser5":
            mp_img = mpimg.imread("StyleCataM2.png")
        elif image == "imagechooser6":
            mp_img = mpimg.imread("StyleCataM3.png")

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])

        test = sb.kdeplot(x, y, shade=True, cmap="Reds", alpha=0.7)
        test.collections[0].set_alpha(0)
        plt.imshow(mp_img, zorder=0, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
        ax.invert_yaxis()
        plt.axis('off')
        canvas = FigureCanvas(fig)
        canvas.draw()
        self.layoutGrid.addWidget(canvas)


class stylewindow(QWidget):

    def __init__(self):
        super().__init__()
        global most_looked
        title = "Style Recommender App"

        # set the title
        self.setWindowTitle(title)
        # self.setStyleSheet()
        self.setStyleSheet("background-color: #F6F6F6;")

        self.horizontalGroupBox = QGroupBox("Grid")

        def get_age():
            with open('combined.txt', 'r') as f:
                last_line = f.readlines()[-1]
            splitted = last_line.split(",")
            age = splitted[0]

            return age

        def get_gender():
            with open('combined.txt', 'r') as f:
                last_line = f.readlines()[-1]
                q = last_line.strip('\n')

            splitted = q.split(",")

            gender = splitted[1]
            return gender

        def get_mostlooked():
            with open('mostlooked.txt', 'r') as f:
                last_line = f.readlines()[-1]
                q = last_line.strip('\n')

            return q

        most_looked = get_mostlooked()
        age = get_age()
        gender = get_gender()
        print(age)
        print(gender)
        print(get_mostlooked())
        print("age: ", get_age())
        print("gender: ", get_gender())
        recommendations = CollaborativeRecomender1.recommend(get_gender(), age, most_looked,
                                                             CollaborativeRecomender1.sim_mat_dic, 5)
        print("here is the recommendations: ", recommendations)
        values = recommendations

        style = []
        for i in values:
            style.append(i)
        imgList = []
        print(style)

        df1 = pd.read_csv('Style_Shopping_Website.csv', encoding='mac_roman')

        website = []
        # Storing img paths to match the recommendations and website
        for fashion in style:
            for x in range(len(df1['name'])):
                if df1['name'][x] == fashion:
                    imgFile = "styleimages/" + fashion + ".PNG"
                    print('imgfile=', imgFile)

                    imgList.append("styleimages/" + fashion + ".PNG")
                    # self.rating.append(df1['rating'][x])
                    locate = (df1['website'][x])
                    website.append(locate)
        print(website)

        print("Image List = ", imgList)

        positions = [(r, c) for r in range(4) for c in range(5)]

        layoutGrid = QGridLayout()

        self.setLayout(layoutGrid)
        # layoutGrid.setVerticalSpacing(50)
        layoutGrid.setHorizontalSpacing(30)
        # layoutGrid.setColumnMinimumWidth(80,50)
        layoutGrid.setContentsMargins(20, 20, 20, 20)
        self.setFixedHeight(570)
        self.setMinimumWidth(1282.5)

        tittle = QLabel("Your Recommendations")
        tittle.setFont(QFont('Times New Roman', 25))
        tittle.setFixedHeight(55)
        tittle.setAlignment(Qt.AlignHCenter)
        tittle.setStyleSheet(
            "color: #6C756F;border-bottom: 1px solid white; padding-bottom:15px; border-bottom-width: 10px;")
        # tittle.setFont(QFont('Times', 11))
        layoutGrid.addWidget(tittle, 0, 0, 1, 0)
        stylechoice = QLabel("You've picked: ")

        stylechoice1 = QPushButton(most_looked)
        maps = {"Casual Style (F)": "https://www.uniqlo.com/us/en/products/E422990-000/00?rrec=true&colorDisplayCode=52&sizeDisplayCode=003",
                "Biker Style (F)": "https://www.selfridges.com/SG/en/cat/allsaints-luna-leather-biker-jacket_R03711014/#colour=BLACK",
                "Preppy Style (F)": "https://shopee.sg/2022-HOT-Sweet-Autumn-Long-Sleeve-Women-Dress-Preppy-Style-Vintage-Bow-plaid-dress-Sailor-collar-Retro-female-dresses-i.474162938.17962206205",
                "Vintage Style (F)": "https://sg.shein.com/Plus-Floral-Pattern-Embroidery-Mesh-Panel-Grommet-Lace-Up-Front-Dress-p-10800765-cat-1889.html?src_identifier=st%3D2%60sc%3Dvintage%20dress%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_search1656296263462&attr_ids=&scici=Search~~EditSearch~~1~~vintage_20dress~~~~0",
                "Indie Style (F)": "https://www.unifclothing.com/products/liv-sweater-green",
                "Chic Style (F)": "https://sea.banggood.com/Solid-Loose-Belt-Button-Long-Sleeve-Lapel-Shirt-Dress-p-1941039.html?utm_source=googleshopping&utm_medium=cpc_organic&gmcCountry=SG&utm_content=minha&utm_campaign=aceng-pmax-sg-sea-en-pc&currency=SGD&cur_warehouse=CN&createTmp=1&ID=62878456287621",
                "Sporty Style (F)": "https://www.lululemon.com.hk/en-hk/p/power-pivot-everlux-tank-top-motif/prod11080057.html?dwvar_prod11080057_color=53919",
                "Sexy Style (F)": "https://sg.shein.com/SHEIN-Solid-Cami-Top-p-1776611-cat-1779.html?src_identifier=st%3D2%60sc%3Dstrap%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_real_class1656400189716&attr_ids=&scici=Search~~EditSearch~~1~~strap~~~~0",
                "Streetwear Style (F)": "https://www.asos.com/topshop/topshop-oversized-collared-bomber-jacket-in-chocolate/prd/201640262?ctaref=recently+viewed",
                "Classy Style (F)": "https://shop.mango.com/sg/women/jackets-and-suit-jackets-jackets-and-suit-jackets/pocket-tweed-jacket_27021152.html",
                "Ethnic Style (F)": "https://www.sareeo.com/products/new-lengha-choli-indian-wedding-designer-lehenga-bollywood-ethnic-wear-for-women-2337-sr388?visitor=SG",
                "Y2k Style (F)": "https://www.unifclothing.com/products/pixie-skirt?variant=39557939101893",
                "Vacation Style (F)": "https://cottonon.com/SG/tie-shoulder-shirred-beach-top/6332569-01.html?dwvar_6332569-01_color=6332569-01&cgid=&originalPid=6332569-01",
                "Evening Style (F)": "https://www.lightinthebox.com/en/p/sheath-column-minimalist-sexy-engagement-formal-evening-dress-strapless-sleeveless-sweep-brush-train-satin-with-split-2020_p8356140.html?currency=SGD&litb_from=paid_adwords_shopping&sku=1_45%7C20_55&country_code=sg",
                "Comfy Style (F)": "https://www.ssense.com/en-sg/women/product/essentials/gray-crewneck-sweatshirt/9313721",
                "Artsy Style (F)": "https://www.etsy.com/sg-en/listing/1215378251/van-gogh-sunflowers-oversized-cardigan?click_key=66a23338cbcf14dd09f3323ff97bd2090f586294%3A1215378251&click_sum=4ee32c6f&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=van+gogh+cardigan&ref=sr_gallery-1-1&pro=1",
                "Hip Hop Style (F)": "https://www.asos.com/asos-design/asos-design-oversized-t-shirt-in-washed-black/prd/201689511?ctaref=we+recommend+grid_1&featureref1=we+recommend+pers",
                "Punk Style (F)": "https://sg.shein.com/ROMWE-X-JRart-Punk-Rock-Letter-Skull-Graphic-Tee-p-10059033-cat-1738.html?src_identifier=st%3D2%60sc%3Dpunk%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_home1656320144866&attr_ids=&scici=Search~~EditSearch~~1~~punk~~~~0&main_attr=27_112&main_attr=27_336&main_attr=27_334",
                "Lolita Style (F)": "https://www.etsy.com/sg-en/listing/1196880413/gold-lolita-dress-cute-jsk-lolita-dress?click_key=415ee18e6e6688359caabe9d654aef2dcf90c914%3A1196880413&click_sum=615be90a&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=lolita+dress&ref=sr_gallery-1-20&pro=1&frs=1",
                "Bohemian Style (F)": "https://bohemianbae.com/products/boho-maxi-dress-floral?currency=USD&variant=32124392734791&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping",
                "Girl Next Door Style (F)": "https://www.everlane.com/products/womens-ovr-ctn-ribbed-cardigan-clay",
                "Formal Office Style (F)": "https://www.g2000.com.sg/asymmetic-neck-ruffles-sleeveless-blouse-1924104001.html",
                "Grunge Style (F)": "https://cosmiquestudio.com/fairy-grunge-patchwork-skirt/?sku=CS1005003334429775-Brown-M",
                "Kpop Style (F)": "https://en.mixxmix.com/product/heart-clubcontrast-edge-black-crop-top/56946/category/2882/display/1/",
                "Casual Style (M)": "https://www2.hm.com/en_sg/productpage.0608945001.html?gclid=CjwKCAjwzeqVBhAoEiwAOrEmzWhch8lerr_qVoih1MGR-Nzb57upKLP3Rurqjq3j6Cb3Yc3gDCfwXRoCABMQAvD_BwE",
                "Artsy Style (M)": "https://www.asos.com/asos-design/asos-design-stretch-skinny-shirt-in-mesh-with-van-gogh-art-placement-print/prd/202648219?colourWayId=202648227&SearchQuery=artsy",
                "Streetwear Style (M)": "https://www.kooding.com/big-pocket-leather-jacket/p/219662",
                "Sporty Style (M)": "https://www.nike.com/sg/t/dri-fit-academy-short-sleeve-football-top-CL7xCd/CW6101-010",
                "Ivy Style (M)": "https://www.lazada.sg/products/polo-ralph-lauren-cable-knit-cotton-sweater-vest-mnposwe1cm20038400-i2229770271-s12809622498.html?exlaz=d_1:mm_150050845_51350205_2010350205::12:13754226424!119527776210!!!pla-297963845945!c!297963845945!12809622498!250346986&gclid=Cj0KCQjw8O-VBhCpARIsACMvVLOQCjXEgrBtxXrjk8_LbtBC2j5MjPKv6ntQ9UY3cnh-D44pVx6N2q8aAtesEALw_wcB",
                "Chic Style (M)": "https://www.zara.com/sg/en/oversize-trench-coat-p08288631.html?v1=147711124&v2=2112330",
                "Grunge Style (M)": "https://sg.urbanoutfitters.com/en-sg/product/bdg-vintage-wash-cotton-flannel-shirt/UO-62857578-001?color=tan&size=s",
                "Formal Office Style (M)": "https://www.g2000.com.sg/cvc-spandex-2-tone-shirt-2112104272.html",
                "Comfy Style (M)": "https://www.ssense.com/en-sg/men/product/essentials/grey-pullover-hoodie/8059551",
                "Y2k Style (M)": "https://www.asos.com/asos-design/asos-design-muscle-t-shirt-in-pink-printed-mesh/prd/202598380?colourWayId=202598383&cid=13498",
                "Punk Style (M)": "https://www.palaleather.com/products/p-palaleather-casual-vegetable-tanned-goatskin-sapphire-moto-jacket",
                "Varsity Style (M)": "https://www.asos.com/asos-design/asos-design-oversized-varsity-bomber-jacket-in-navy-with-mushroom-faux-leather-sleeves/prd/201185943?ctaref=we+recommend+grid_2&featureref1=we+recommend+pers",
                "Preppy Style (M)": "https://cottonon.com/SG/vacay-short-sleeve-shirt/9359194918563.html",
                "Evening Style (M)": "https://shop.mango.com/sg/men/blazers-formal/super-slim-fit-suit-blazer_37020089.html?c=99&talla=44&gclid=CjwKCAjwk_WVBhBZEiwAUHQCmR8KGoinwYrqInpMYUpThax5virIj9Fk2ZiGXl8bAlfh0swd9-nolhoCXfUQAvD_BwE&gclsrc=aw.ds",
                "Rugged Style (M)": "https://www.ssense.com/en-sg/men/product/carhartt-work-in-progress/brown-michigan-jacket/8692361",
                "Ethnic Style (M)": "https://eur.shein.com/Men-Mock-Neck-Button-Half-Placket-Longline-Shirt-p-9877683-cat-1977.html",
                "Boy Next Door Style (M)": "https://cottonon.com/SG/garfield-rugby-polo/9359194914503.html",
                "Vintage Style (M)": "https://www.asos.com/asos-design/asos-design-skinny-collarless-suit-jacket-in-brown-irregular-crinkle/prd/201935003?ctaref=we+recommend+grid_3&featureref1=we+recommend+pers",
                "Biker Style (M)": "https://www.zalora.sg/harley-davidson-lisbon-debossed-leather-jacket-black-2836311.html",
                "Hip Hop Style (M)": "https://www.asos.com/asos-design/asos-design-2-pack-oversized-longline-t-shirt-with-roll-sleeve-in-multi/prd/201527319?colourWayId=201527320&CTAref=Complete+the+Look+Carousel_1&featureref1=complete+the+look",
                "Indie Style (M)": "https://www.kooding.com/vent-over-knit-vest/p/218874?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLMiPIMZrIKBbc5hzGryZ8i_sMU8rHAztmfsyGW1naV2IrY-HYOXdTYaAgxhEALw_wcB",
                "Classy Style (M)": "https://www.kooding.com/overfit-two-button-jacket/p/219676?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLMnYW8qUaFdqHeeOtfMhct06fZxU3P9onTZXZatZDX4D3ULo2GRS7UaAn-YEALw_wcB",
                "Bohemian Style (M)": "https://www.asos.com/reclaimed-vintage/reclaimed-vintage-inspired-crochet-shirt-in-cream/prd/203016282?ctaref=recently+viewed",
                "Vacation Style (M)": "https://www.kooding.com/hawaiian-cotton-shirt/p/262721?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLNyiSCxPjD1Bmb-JVwNZ8HNc5bX-IZt5cBu_INWFEL2Lj9f3pHM49QaAnJVEALw_wcB"

                }
        stylechoice.setStyleSheet("color: #878280; margin-left:200px; border:0px solid black;")
        stylechoice1.clicked.connect(lambda: webbrowser.open(maps[most_looked]))
        stylechoice1.setCursor(QCursor(Qt.PointingHandCursor))
        stylechoice1.setFixedHeight(50)
        stylechoice1.setStyleSheet(
            "color: #545454; border:0px solid black;margin-right:400px; margin-left:120px; text-align:left; font-weight:bold;text-decoration: underline;")
        # stylechoice.setAlignment(Qt.AlignHCenter)
        stylechoice.setFont(QFont('Times', 11))
        stylechoice1.setFont(QFont("Times", 12))
        stylechoice2 = QLabel("(Click Here to Start Shopping!)")
        stylechoice2.setAlignment(Qt.AlignHCenter)
        stylechoice2.setFixedHeight(60)
        stylechoice2.setStyleSheet(
            "color: #9D8978; border:0px solid black; background-color: none;padding-bottom: 15px; margin-right:10px;")

        # stylechoice.setAlignment(Qt.AlignHCenter)
        stylechoice.setFont(QFont('Times', 12))
        stylechoice2.setFont(QFont('Arial', 11))
        layoutGrid.addWidget(stylechoice, 1, 1, 1, 2)
        layoutGrid.addWidget(stylechoice1, 1, 2, 1, 3)
        layoutGrid.addWidget(stylechoice2, 2, 0, 1, 0, )
        # layoutGrid.addWidget(stylechoice1,1,0,1,0)
        # layoutGrid.addWidget(stylechoice1,1,0,1,1)

        a = positions[15:]

        for a, value in zip(a, style):

            print(value)
            button = QGroupBox()
            button.setStyleSheet("border:none;")
            button.setFixedHeight(300)
            # button.setTitle("Hello")
            # button.setAlignment(Qt.AlignHCenter)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layoutGrid.addWidget(button, *a)
            vbox = QVBoxLayout()
            button.setLayout(vbox)
            stylename = QLabel(value)
            stylename.setAlignment(Qt.AlignHCenter)
            stylename.setWordWrap(True)
            stylename.setFixedHeight(10)
            # stylename.setStyleSheet("background-color: blue;")
            stylename.setFont(QFont('Times', 12))
            stylename.setStyleSheet("color: #545454;  padding :10px; font-weight: Bold;")
            stylename.setToolTip('<font color="red" >Click on the <b>Image</b> to view the shopping website</font>')

            # stylename.setStyleSheet("font-size: 24px;")

            stylename.setMaximumHeight(50)
            vbox.addWidget(stylename)
            vbox.setSpacing(0)

            images = QPushButton()
            # pixmap = QPixmap('images/Bak Kut Teh.png')
            # pixmap.scaledToHeight(images)

            # adding image to label
            # images.setPixmap(pixmap)
            images.setGeometry(100, 150, 100, 40)
            if value == "Casual Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Casual Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.uniqlo.com/us/en/products/E422990-000/00?rrec=true&colorDisplayCode=52&sizeDisplayCode=003'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Uniqlo")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Biker Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Biker Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.selfridges.com/SG/en/cat/allsaints-luna-leather-biker-jacket_R03711014/#colour=BLACK'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Selfridges")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Preppy Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Preppy Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://shopee.sg/2022-HOT-Sweet-Autumn-Long-Sleeve-Women-Dress-Preppy-Style-Vintage-Bow-plaid-dress-Sailor-collar-Retro-female-dresses-i.474162938.17962206205'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Shopee")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Vintage Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Vintage Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://sg.shein.com/Plus-Floral-Pattern-Embroidery-Mesh-Panel-Grommet-Lace-Up-Front-Dress-p-10800765-cat-1889.html?src_identifier=st%3D2%60sc%3Dvintage%20dress%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_search1656296263462&attr_ids=&scici=Search~~EditSearch~~1~~vintage_20dress~~~~0'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Shien")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Indie Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Indie Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.unifclothing.com/products/liv-sweater-green'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Unif Clothing")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Chic Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Chic Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://sea.banggood.com/Solid-Loose-Belt-Button-Long-Sleeve-Lapel-Shirt-Dress-p-1941039.html?utm_source=googleshopping&utm_medium=cpc_organic&gmcCountry=SG&utm_content=minha&utm_campaign=aceng-pmax-sg-sea-en-pc&currency=SGD&cur_warehouse=CN&createTmp=1&ID=62878456287621'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Banggood")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Sporty Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Sporty Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.lululemon.com.hk/en-hk/p/power-pivot-everlux-tank-top-motif/prod11080057.html?dwvar_prod11080057_color=53919'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Lululemon")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Sexy Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Sexy Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://sg.shein.com/SHEIN-Solid-Cami-Top-p-1776611-cat-1779.html?src_identifier=st%3D2%60sc%3Dstrap%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_real_class1656400189716&attr_ids=&scici=Search~~EditSearch~~1~~strap~~~~0'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Shien")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Streetwear Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Streetwear Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/topshop/topshop-oversized-collared-bomber-jacket-in-chocolate/prd/201640262?ctaref=recently+viewed'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Classy Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Classy Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://shop.mango.com/sg/women/jackets-and-suit-jackets-jackets-and-suit-jackets/pocket-tweed-jacket_27021152.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Mango")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Ethnic Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Ethnic Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.sareeo.com/products/new-lengha-choli-indian-wedding-designer-lehenga-bollywood-ethnic-wear-for-women-2337-sr388?visitor=SG'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Sareeo")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Y2k Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Y2k Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.unifclothing.com/products/pixie-skirt?variant=39557939101893'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Unif Clothing")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Vacation Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Vacation Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://cottonon.com/SG/tie-shoulder-shirred-beach-top/6332569-01.html?dwvar_6332569-01_color=6332569-01&cgid=&originalPid=6332569-01'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Cotton On")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Evening Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Evening Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.lightinthebox.com/en/p/sheath-column-minimalist-sexy-engagement-formal-evening-dress-strapless-sleeveless-sweep-brush-train-satin-with-split-2020_p8356140.html?currency=SGD&litb_from=paid_adwords_shopping&sku=1_45%7C20_55&country_code=sg'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Light In The Box")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Comfy Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Comfy Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.ssense.com/en-sg/women/product/essentials/gray-crewneck-sweatshirt/9313721'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Ssense")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Artsy Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Artsy Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.etsy.com/sg-en/listing/1215378251/van-gogh-sunflowers-oversized-cardigan?click_key=66a23338cbcf14dd09f3323ff97bd2090f586294%3A1215378251&click_sum=4ee32c6f&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=van+gogh+cardigan&ref=sr_gallery-1-1&pro=1'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Etsy")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Hip Hop Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Hip Hop Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/asos-design/asos-design-oversized-t-shirt-in-washed-black/prd/201689511?ctaref=we+recommend+grid_1&featureref1=we+recommend+pers'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Punk Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Punk Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://sg.shein.com/ROMWE-X-JRart-Punk-Rock-Letter-Skull-Graphic-Tee-p-10059033-cat-1738.html?src_identifier=st%3D2%60sc%3Dpunk%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_home1656320144866&attr_ids=&scici=Search~~EditSearch~~1~~punk~~~~0&main_attr=27_112&main_attr=27_336&main_attr=27_334'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Shien")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Lolita Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Lolita Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.etsy.com/sg-en/listing/1196880413/gold-lolita-dress-cute-jsk-lolita-dress?click_key=415ee18e6e6688359caabe9d654aef2dcf90c914%3A1196880413&click_sum=615be90a&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=lolita+dress&ref=sr_gallery-1-20&pro=1&frs=1'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Etsy")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Bohemian Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Bohemian Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://bohemianbae.com/products/boho-maxi-dress-floral?currency=USD&variant=32124392734791&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Bohemian Bae")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Girl Next Door Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Girl Next Door Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.everlane.com/products/womens-ovr-ctn-ribbed-cardigan-clay'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Everlane")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Formal Office Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Formal Office Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.g2000.com.sg/asymmetic-neck-ruffles-sleeveless-blouse-1924104001.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: G2000")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Grunge Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Grunge Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://cosmiquestudio.com/fairy-grunge-patchwork-skirt/?sku=CS1005003334429775-Brown-M'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Cosmique Studio")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Kpop Style (F)":
                images.setStyleSheet("border-image : url(styleimages/Kpop Style (F).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://en.mixxmix.com/product/heart-clubcontrast-edge-black-crop-top/56946/category/2882/display/1/'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Mixxmix")
                website.setWordWrap(True)
                vbox.addWidget(website)


            elif value == "Casual Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Casual Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www2.hm.com/en_sg/productpage.0608945001.html?gclid=CjwKCAjwzeqVBhAoEiwAOrEmzWhch8lerr_qVoih1MGR-Nzb57upKLP3Rurqjq3j6Cb3Yc3gDCfwXRoCABMQAvD_BwE'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: H&M")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Artsy Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Artsy Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/asos-design/asos-design-stretch-skinny-shirt-in-mesh-with-van-gogh-art-placement-print/prd/202648219?colourWayId=202648227&SearchQuery=artsy'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Streetwear Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Streetwear Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.kooding.com/big-pocket-leather-jacket/p/219662'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Kooding")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Sporty Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Sporty Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nike.com/sg/t/dri-fit-academy-short-sleeve-football-top-CL7xCd/CW6101-010'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Nike")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Ivy Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Ivy Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.lazada.sg/products/polo-ralph-lauren-cable-knit-cotton-sweater-vest-mnposwe1cm20038400-i2229770271-s12809622498.html?exlaz=d_1:mm_150050845_51350205_2010350205::12:13754226424!119527776210!!!pla-297963845945!c!297963845945!12809622498!250346986&gclid=Cj0KCQjw8O-VBhCpARIsACMvVLOQCjXEgrBtxXrjk8_LbtBC2j5MjPKv6ntQ9UY3cnh-D44pVx6N2q8aAtesEALw_wcB'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Lazada")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Chic Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Chic Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.zara.com/sg/en/oversize-trench-coat-p08288631.html?v1=147711124&v2=2112330'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Zara")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Grunge Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Grunge Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://sg.urbanoutfitters.com/en-sg/product/bdg-vintage-wash-cotton-flannel-shirt/UO-62857578-001?color=tan&size=s'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Urban Outfitters")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Formal Office Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Formal Office Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.g2000.com.sg/cvc-spandex-2-tone-shirt-2112104272.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: G2000")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Comfy Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Comfy Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.ssense.com/en-sg/men/product/essentials/grey-pullover-hoodie/8059551'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Ssense")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Y2k Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Y2k Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/asos-design/asos-design-muscle-t-shirt-in-pink-printed-mesh/prd/202598380?colourWayId=202598383&cid=13498'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Punk Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Punk Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.palaleather.com/products/p-palaleather-casual-vegetable-tanned-goatskin-sapphire-moto-jacket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Palaleather")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Varsity Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Varsity Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/asos-design/asos-design-oversized-varsity-bomber-jacket-in-navy-with-mushroom-faux-leather-sleeves/prd/201185943?ctaref=we+recommend+grid_2&featureref1=we+recommend+pers'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Preppy Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Preppy Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://cottonon.com/SG/vacay-short-sleeve-shirt/9359194918563.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Cotton On")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Evening Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Evening Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://shop.mango.com/sg/men/blazers-formal/super-slim-fit-suit-blazer_37020089.html?c=99&talla=44&gclid=CjwKCAjwk_WVBhBZEiwAUHQCmR8KGoinwYrqInpMYUpThax5virIj9Fk2ZiGXl8bAlfh0swd9-nolhoCXfUQAvD_BwE&gclsrc=aw.ds'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Mango")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Rugged Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Rugged Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.ssense.com/en-sg/men/product/carhartt-work-in-progress/brown-michigan-jacket/8692361'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Ssense")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Ethnic Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Ethnic Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://eur.shein.com/Men-Mock-Neck-Button-Half-Placket-Longline-Shirt-p-9877683-cat-1977.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Shein")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Boy Next Door Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Boy Next Door Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://cottonon.com/SG/garfield-rugby-polo/9359194914503.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Cotton On")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Vintage Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Vintage Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/asos-design/asos-design-skinny-collarless-suit-jacket-in-brown-irregular-crinkle/prd/201935003?ctaref=we+recommend+grid_3&featureref1=we+recommend+pers'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Biker Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Biker Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.zalora.sg/harley-davidson-lisbon-debossed-leather-jacket-black-2836311.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Zalora")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Hip Hop Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Hip Hop Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/asos-design/asos-design-2-pack-oversized-longline-t-shirt-with-roll-sleeve-in-multi/prd/201527319?colourWayId=201527320&CTAref=Complete+the+Look+Carousel_1&featureref1=complete+the+look'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Indie Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Indie Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.kooding.com/vent-over-knit-vest/p/218874?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLMiPIMZrIKBbc5hzGryZ8i_sMU8rHAztmfsyGW1naV2IrY-HYOXdTYaAgxhEALw_wcB'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Kooding")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Classy Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Classy Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.kooding.com/overfit-two-button-jacket/p/219676?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLMnYW8qUaFdqHeeOtfMhct06fZxU3P9onTZXZatZDX4D3ULo2GRS7UaAn-YEALw_wcB'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Kooding")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Bohemian Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Bohemian Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.asos.com/reclaimed-vintage/reclaimed-vintage-inspired-crochet-shirt-in-cream/prd/203016282?ctaref=recently+viewed'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Asos")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Vacation Style (M)":
                images.setStyleSheet("border-image : url(styleimages/Vacation Style (M).PNG);")
                images.clicked.connect(lambda: webbrowser.open('https://www.kooding.com/hawaiian-cotton-shirt/p/262721?gclid=Cj0KCQjw8O-VBhCpARIsACMvVLNyiSCxPjD1Bmb-JVwNZ8HNc5bX-IZt5cBu_INWFEL2Lj9f3pHM49QaAnJVEALw_wcB'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Shopping Site: Kooding")
                website.setWordWrap(True)
                vbox.addWidget(website)

            images.setFixedHeight(250)
            website.setFixedHeight(55)
            website.setAlignment(Qt.AlignHCenter)
            website.setStyleSheet("color: #6C756F;background-color: #DAD9EB ; padding: 10px; opacity: 0.3;")

        backbutton = QPushButton("Quit")
        backbutton.setCursor(QCursor(Qt.PointingHandCursor))
        backbutton.clicked.connect(self.comeout)
        backbutton.setStyleSheet("background-color: white")

        layoutGrid.addWidget(backbutton, 4, 2, 1, 1)
        # stylechoice=QLabel("You've picked")
        # stylechoice.setAlignment(Qt.AlignRight)
        # stylechoice.setFont(QFont('Times', 11))
        # layoutGrid.addWidget(stylechoice)
        # stylechoice1=QLabel(most_looked)
        # stylechoice1.setAlignment(Qt.AlignLeft)
        # stylechoice1.setFont(QFont('Times', 11))

        # stylechoice.setAlignment(Qt.AlignHCenter)
        # layoutGrid.addWidget(stylechoice1)

    def comeout(self, checked):
        button = QMessageBox.critical(
            self,
            "Exiting Confirmation",
            "<font color =red>Are you sure you want to exit?</font>",
            buttons=QMessageBox.No | QMessageBox.Yes,
            defaultButton=QMessageBox.No, )

        if button == QMessageBox.No:
            print("Rejected exit confirmation")
        elif button == QMessageBox.Yes:
            print("Back")
            self.close()
            window.show()

    # def main_menu(self, checked):
    #     self.a = MainWindow()
    #     self.a.show()
    #     self.close()


# main window stylesheet
stylesheet = """
    MainWindow {
        border-image: url("StyleMain.png");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)  # <---
    window = MainWindow()
    window.resize(640, 640)
    window.show()
    sys.exit(app.exec_())

# this is the working one , some changes has been done in sprint 4 to make it better
