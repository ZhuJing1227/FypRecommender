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

import CCA_Recommender as CollaborativeRecomender1
import random

most_looked = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # string value
        title = "CCA Recommender App"

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
                                       "background-color : #96B8F6;"
                                       "}")
        self.pushButton2.setStyleSheet("QPushButton::hover"
                                       "{"
                                       "background-color : #5E636D;"

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
        execfile("face.py")
        self.w = GridDemo()
        self.okk = okk()

        self.ccawindow = ccawindow()

        self.ccawindow.show()
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


# cca pics
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        title = "CCA Recommender App"

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

        imagechooser = "imagechooser%d" % (random.randint(1, 11))
        #imagechooser = "imagechooser6"

        with open('imagechooser.txt', 'w') as out:
            line1 = imagechooser
            out.write(line1)
        if imagechooser == "imagechooser1":
            print("1")
            self.image.setStyleSheet("border-image: url(CCACata1.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser2":
            print("2")
            self.image.setStyleSheet("border-image: url(CCACata2.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser3":
            print("3")
            self.image.setStyleSheet("border-image: url(CCACata3.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser4":
            print("4")
            self.image.setStyleSheet("border-image: url(CCACata4.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser5":
            print("5")
            self.image.setStyleSheet("border-image: url(CCACata5.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser6":
            print("6")
            self.image.setStyleSheet("border-image: url(CCACata6.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser7":
            print("7")
            self.image.setStyleSheet("border-image: url(CCACata7.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser8":
            print("8")
            self.image.setStyleSheet("border-image: url(CCACata8.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser9":
            print("9")
            self.image.setStyleSheet("border-image: url(CCACata9.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser10":
            print("10")
            self.image.setStyleSheet("border-image: url(CCACata10.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser11":
            print("11")
            self.image.setStyleSheet("border-image: url(CCACata11.png);")
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
            sasclub = 0
            pianoensemble = 0
            danzinc = 0
            communityserviceclub = 0
            aikido = 0
            adventureclub = 0
            archery = 0
            ambassadorialteam = 0

            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    sasclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    pianoensemble += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    danzinc += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    communityserviceclub += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    aikido += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    adventureclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    archery += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    ambassadorialteam += 1

            rank.append(sasclub)
            rank.append(pianoensemble)
            rank.append(danzinc)
            rank.append(communityserviceclub)
            rank.append(aikido)
            rank.append(adventureclub)
            rank.append(archery)
            rank.append(ambassadorialteam)

            if max(rank) == rank[0]:
                most_looked = 'SAS Club'
                most_looked = 'SAS Club'
            elif max(rank) == rank[1]:
                most_looked = 'Piano Ensemble'
            elif max(rank) == rank[2]:
                most_looked = 'Danz Inc'
            elif max(rank) == rank[3]:
                most_looked = 'Community Service Club'
            elif max(rank) == rank[4]:
                most_looked = 'Aikido'
            elif max(rank) == rank[5]:
                most_looked = 'Adventure Club'
            elif max(rank) == rank[6]:
                most_looked = 'Archery'
            elif max(rank) == rank[7]:
                most_looked = 'Ambassadorial Team'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser2':
            rank = []
            most_looked = ''
            sbmclub = 0
            chineseculturalgroup = 0
            crewstudio = 0
            nypprimers = 0
            basketball = 0
            athletics = 0
            badminton = 0
            astronomyclub = 0

            """

            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    sbmclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    chineseculturalgroup += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    crewstudio += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    nypprimers += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    basketball += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    athletics += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    badminton += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    astronomyclub += 1

            rank.append(sbmclub)
            rank.append(chineseculturalgroup)
            rank.append(crewstudio)
            rank.append(nypprimers)
            rank.append(basketball)
            rank.append(athletics)
            rank.append(badminton)
            rank.append(astronomyclub)

            if max(rank) == rank[0]:
                most_looked = 'SBM Club'
            elif max(rank) == rank[1]:
                most_looked = 'Chinese Cultural Group'
            elif max(rank) == rank[2]:
                most_looked = 'Crew Studio'
            elif max(rank) == rank[3]:
                most_looked = 'NYP Primers'
            elif max(rank) == rank[4]:
                most_looked = 'Basketball'
            elif max(rank) == rank[5]:
                most_looked = 'Athletics'
            elif max(rank) == rank[6]:
                most_looked = 'Badminton'
            elif max(rank) == rank[7]:
                most_looked = 'Astronomy Club'
            else:
                print("Smth went very wrong")
        if imagechooser == 'imagechooser3':

            rank = []
            most_looked = ''
            sdmclub = 0
            symphonyorchestra = 0
            sakuranjapaneseculturalclub = 0
            mentoringclub = 0
            beiquandao = 0
            canoespint = 0
            hockey = 0
            currentaffairsdebatingclub = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    sdmclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    symphonyorchestra += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    sakuranjapaneseculturalclub += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    mentoringclub += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    beiquandao += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    canoespint += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    hockey += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    currentaffairsdebatingclub += 1

            rank.append(sdmclub)
            rank.append(symphonyorchestra)
            rank.append(sakuranjapaneseculturalclub)
            rank.append(mentoringclub)
            rank.append(beiquandao)
            rank.append(canoespint)
            rank.append(hockey)
            rank.append(currentaffairsdebatingclub)

            if max(rank) == rank[0]:
                most_looked = 'SDM Club'
            elif max(rank) == rank[1]:
                most_looked = 'Symphony Orchestra'
            elif max(rank) == rank[2]:
                most_looked = 'Sakuran Japanese Cultural Club'
            elif max(rank) == rank[3]:
                most_looked = 'Mentoring Club'
            elif max(rank) == rank[4]:
                most_looked = 'Bei Quan Dao'
            elif max(rank) == rank[5]:
                most_looked = 'Canoe Sprint'
            elif max(rank) == rank[6]:
                most_looked = 'Hockey'
            elif max(rank) == rank[7]:
                most_looked = 'Current Affairs & Debating Club'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser4':

            rank = []
            most_looked = ''
            segclub = 0
            sketchartclub = 0
            foreignbodies = 0
            servicelearninggroup = 0
            bowling = 0
            liondragondancetroupe = 0
            dragonboat = 0
            entrepreneurshipclub = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    segclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    sketchartclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    foreignbodies += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    servicelearninggroup += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    bowling += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    liondragondancetroupe += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    dragonboat += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    entrepreneurshipclub += 1

            rank.append(segclub)
            rank.append(sketchartclub)
            rank.append(foreignbodies)
            rank.append(servicelearninggroup)
            rank.append(bowling)
            rank.append(liondragondancetroupe)
            rank.append(dragonboat)
            rank.append(entrepreneurshipclub)

            if max(rank) == rank[0]:
                most_looked = 'SEG Club'
            elif max(rank) == rank[1]:
                most_looked = 'Sketch Art Club'
            elif max(rank) == rank[2]:
                most_looked = 'Foreign Bodies'
            elif max(rank) == rank[3]:
                most_looked = 'Service Learning Group'
            elif max(rank) == rank[4]:
                most_looked = 'Bowling'
            elif max(rank) == rank[5]:
                most_looked = 'Lion & Dragon Dance Troupe'
            elif max(rank) == rank[6]:
                most_looked = 'Dragonboat'
            elif max(rank) == rank[7]:
                most_looked = 'Entrepreneurship Club'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser5':

            rank = []
            most_looked = ''
            shssclub = 0
            lhexagonefrenchclub = 0
            malayculturalgroup = 0
            emceeclub = 0
            floorball = 0
            lifesaving = 0
            kendo = 0
            librarychampions = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    shssclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    lhexagonefrenchclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    malayculturalgroup += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    emceeclub += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    floorball += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    lifesaving += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    kendo += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    librarychampions += 1

            rank.append(shssclub)
            rank.append(lhexagonefrenchclub)
            rank.append(malayculturalgroup)
            rank.append(emceeclub)
            rank.append(floorball)
            rank.append(lifesaving)
            rank.append(kendo)
            rank.append(librarychampions)

            if max(rank) == rank[0]:
                most_looked = 'SHSS Club'
            elif max(rank) == rank[1]:
                most_looked = 'L Hexagone French Club'
            elif max(rank) == rank[2]:
                most_looked = 'Malay Cultural Group'
            elif max(rank) == rank[3]:
                most_looked = 'Emcee Club'
            elif max(rank) == rank[4]:
                most_looked = 'Floorball'
            elif max(rank) == rank[5]:
                most_looked = 'Life Saving'
            elif max(rank) == rank[6]:
                most_looked = 'Kendo'
            elif max(rank) == rank[7]:
                most_looked = 'Library Champions'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser6':

            rank = []
            most_looked = ''
            sitclub = 0
            chineseorchestra = 0
            laballroomenmasse = 0
            geocouncil = 0
            tchoukball = 0
            mindsports = 0
            judo = 0
            studentsunion = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    sitclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    chineseorchestra += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    laballroomenmasse += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    geocouncil += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    tchoukball += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    mindsports += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    judo += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    studentsunion += 1

            rank.append(sitclub)
            rank.append(chineseorchestra)
            rank.append(laballroomenmasse)
            rank.append(geocouncil)
            rank.append(tchoukball)
            rank.append(mindsports)
            rank.append(judo)
            rank.append(studentsunion)

            if max(rank) == rank[0]:
                most_looked = 'SIT Club'
            elif max(rank) == rank[1]:
                most_looked = 'Chinese Orchestra'
            elif max(rank) == rank[2]:
                most_looked = 'La Ballroom En Masse'
            elif max(rank) == rank[3]:
                most_looked = 'Geo Council'
            elif max(rank) == rank[4]:
                most_looked = 'Tchoukball'
            elif max(rank) == rank[5]:
                most_looked = 'Mindsports'
            elif max(rank) == rank[6]:
                most_looked = 'Judo'
            elif max(rank) == rank[7]:
                most_looked = 'Students Union'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser7':

            rank = []
            most_looked = ''
            dancecompany = 0
            harmonicaensemble = 0
            leoclub = 0
            runningclub = 0
            netball = 0
            streetworkoutclub = 0
            photographyclub = 0
            astronomyclub = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    dancecompany += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    harmonicaensemble += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    leoclub += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    runningclub += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    netball += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    streetworkoutclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    photographyclub += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    astronomyclub += 1

            rank.append(dancecompany)
            rank.append(harmonicaensemble)
            rank.append(leoclub)
            rank.append(runningclub)
            rank.append(netball)
            rank.append(streetworkoutclub)
            rank.append(photographyclub)
            rank.append(astronomyclub)

            if max(rank) == rank[0]:
                most_looked = 'Dance Company'
            elif max(rank) == rank[1]:
                most_looked = 'Harmonica Ensemble'
            elif max(rank) == rank[2]:
                most_looked = 'Leo Club'
            elif max(rank) == rank[3]:
                most_looked = 'Running Club'
            elif max(rank) == rank[4]:
                most_looked = 'Netball'
            elif max(rank) == rank[5]:
                most_looked = 'Street Workout Club'
            elif max(rank) == rank[6]:
                most_looked = 'Photography Club'
            elif max(rank) == rank[7]:
                most_looked = 'Astronomy Club'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser8':

            rank = []
            most_looked = ''
            makeupartistry = 0
            liveaudio = 0
            nyaastudentsclub = 0
            squash = 0
            soccer = 0
            strongmanclub = 0
            makersinnovatorstribe = 0
            nypcru = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    makeupartistry += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    liveaudio += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    nyaastudentsclub += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    squash += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    soccer += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    strongmanclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    makersinnovatorstribe += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    nypcru += 1

            rank.append(makeupartistry)
            rank.append(liveaudio)
            rank.append(nyaastudentsclub)
            rank.append(squash)
            rank.append(soccer)
            rank.append(strongmanclub)
            rank.append(makersinnovatorstribe)
            rank.append(nypcru)

            if max(rank) == rank[0]:
                most_looked = 'Makeup Artistry'
            elif max(rank) == rank[1]:
                most_looked = 'Live Audio'
            elif max(rank) == rank[2]:
                most_looked = 'Nyaa Students Club'
            elif max(rank) == rank[3]:
                most_looked = 'Squash'
            elif max(rank) == rank[4]:
                most_looked = 'Soccer'
            elif max(rank) == rank[5]:
                most_looked = 'Strongman Club'
            elif max(rank) == rank[6]:
                most_looked = 'Makers Innovators Tribe'
            elif max(rank) == rank[7]:
                most_looked = 'NYP Cru'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser9':

            rank = []
            most_looked = ''
            dertreffgermanclub = 0
            guitarclub = 0
            peersupporterclub = 0
            tabletennis = 0
            touchfootball = 0
            swimming = 0
            thecommunicators = 0
            catholicyouthcommunity = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    dertreffgermanclub += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    guitarclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    peersupporterclub += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    tabletennis += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    touchfootball += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    swimming += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    thecommunicators += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    catholicyouthcommunity += 1

            rank.append(dertreffgermanclub)
            rank.append(guitarclub)
            rank.append(peersupporterclub)
            rank.append(tabletennis)
            rank.append(touchfootball)
            rank.append(swimming)
            rank.append(thecommunicators)
            rank.append(catholicyouthcommunity)

            if max(rank) == rank[0]:
                most_looked = 'Der Treff German Club'
            elif max(rank) == rank[1]:
                most_looked = 'Guitar Club'
            elif max(rank) == rank[2]:
                most_looked = 'Peer Supporter Club'
            elif max(rank) == rank[3]:
                most_looked = 'Table Tennis'
            elif max(rank) == rank[4]:
                most_looked = 'Touch Football'
            elif max(rank) == rank[5]:
                most_looked = 'Swimming'
            elif max(rank) == rank[6]:
                most_looked = 'The Communicators'
            elif max(rank) == rank[7]:
                most_looked = 'Catholic Youth Community'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser10':

            rank = []
            most_looked = ''
            voiceensemble = 0
            kwavekoreanclub = 0
            mentoringclub = 0
            ultimatefrisbee = 0
            volleyball = 0
            zhonghuawushu = 0
            ambassadorialteam = 0
            buddhistsociety = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    voiceensemble += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    kwavekoreanclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    mentoringclub += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    ultimatefrisbee += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    volleyball += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    zhonghuawushu += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    ambassadorialteam += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    buddhistsociety += 1

            rank.append(voiceensemble)
            rank.append(kwavekoreanclub)
            rank.append(mentoringclub)
            rank.append(ultimatefrisbee)
            rank.append(volleyball)
            rank.append(zhonghuawushu)
            rank.append(ambassadorialteam)
            rank.append(buddhistsociety)

            if max(rank) == rank[0]:
                most_looked = 'Voice Ensemble'
            elif max(rank) == rank[1]:
                most_looked = 'K-Wave Korean Club'
            elif max(rank) == rank[2]:
                most_looked = 'Mentoring Club'
            elif max(rank) == rank[3]:
                most_looked = 'Ultimate Frisbee'
            elif max(rank) == rank[4]:
                most_looked = 'Volleyball'
            elif max(rank) == rank[5]:
                most_looked = 'Zhong Hua Wushu'
            elif max(rank) == rank[6]:
                most_looked = 'Ambassadorial Team'
            elif max(rank) == rank[7]:
                most_looked = 'Buddhist Society'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser11':

            rank = []
            most_looked = ''
            soundcard = 0
            stageartdramatheatremanagementclub = 0
            indianculturalgroup = 0
            cdlionhearters = 0
            taekwondo = 0
            tennis = 0
            silat = 0
            studentsunion = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    soundcard += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    stageartdramatheatremanagementclub += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    indianculturalgroup += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    cdlionhearters += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    taekwondo += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    tennis += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    silat += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    studentsunion += 1

            rank.append(soundcard)
            rank.append(stageartdramatheatremanagementclub)
            rank.append(indianculturalgroup)
            rank.append(cdlionhearters)
            rank.append(taekwondo)
            rank.append(tennis)
            rank.append(silat)
            rank.append(studentsunion)

            if max(rank) == rank[0]:
                most_looked = 'Soundcard'
            elif max(rank) == rank[1]:
                most_looked = 'Stagearts Drama & Theatre Management Club'
            elif max(rank) == rank[2]:
                most_looked = 'Indian Cultural Group'
            elif max(rank) == rank[3]:
                most_looked = 'CD Lionhearters'
            elif max(rank) == rank[4]:
                most_looked = 'Taekwondo'
            elif max(rank) == rank[5]:
                most_looked = 'Tennis'
            elif max(rank) == rank[6]:
                most_looked = 'Silat'
            elif max(rank) == rank[7]:
                most_looked = 'Students Union'
            else:
                print("Smth went very wrong")


        print("Most looked CCA: ", most_looked)
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
        title = "CCA Recommender App"

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
            mp_img = mpimg.imread("CCACata1.png")
        elif image == "imagechooser2":
            mp_img = mpimg.imread("CCACata2.png")
        elif image == "imagechooser3":
            mp_img = mpimg.imread("CCACata3.png")
        elif image == "imagechooser4":
            mp_img = mpimg.imread("CCACata4.png")
        elif image == "imagechooser5":
            mp_img = mpimg.imread("CCACata5.png")
        elif image == "imagechooser6":
            mp_img = mpimg.imread("CCACata6.png")
        elif image == "imagechooser7":
            mp_img = mpimg.imread("CCACata7.png")
        elif image == "imagechooser8":
            mp_img = mpimg.imread("CCACata8.png")
        elif image == "imagechooser9":
            mp_img = mpimg.imread("CCACata9.png")
        elif image == "imagechooser10":
            mp_img = mpimg.imread("CCACata10.png")
        elif image == "imagechooser11":
            mp_img = mpimg.imread("CCACata11.png")

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


class ccawindow(QWidget):

    def __init__(self):
        super().__init__()
        global most_looked
        title = "CCA Recommender App"

        # set the title
        self.setWindowTitle(title)
        # self.setStyleSheet()
        self.setStyleSheet("background-color: #B4C8EF;")

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

        cca = []
        for i in values:
            cca.append(i)
        imgList = []
        print(cca)
        df1 = pd.read_csv('CCA_signup_link.csv', encoding='mac_roman')

        website = []
        # Storing img paths to match the recommendations, locations, and ratings
        for activity in cca:
            for x in range(len(df1['name'])):
                if df1['name'][x] == activity:
                    imgFile = "ccaimages/" + activity + ".png"
                    print('imgfile=', imgFile)

                    imgList.append("ccaimages/" + activity + ".png")
                    # self.rating.append(df1['rating'][x])
                    locate = (df1['location'][x])
                    website.append(locate)
        print(website)

        print("Image List = ", imgList)

        positions = [(r, c) for r in range(4) for c in range(5)]

        layoutGrid = QGridLayout()

        self.setLayout(layoutGrid)
        # layoutGrid.setVerticalSpacing(50)
        layoutGrid.setHorizontalSpacing(20)
        # layoutGrid.setColumnMinimumWidth(80,50)
        layoutGrid.setContentsMargins(20, 20, 20, 20)
        self.setFixedHeight(570)
        self.setMinimumWidth(1282.5)

        tittle = QLabel("Your Recommendations")
        tittle.setFont(QFont('Times New Roman', 25))
        tittle.setFixedHeight(55)
        tittle.setAlignment(Qt.AlignHCenter)
        tittle.setStyleSheet(
            "color: #5E636D;border-bottom: 1px solid white; padding-bottom:15px; border-bottom-width: 10px;")
        # tittle.setFont(QFont('Times', 11))
        layoutGrid.addWidget(tittle, 0, 0, 1, 0)
        ccachoice = QLabel("You've chosen: ")

        ccachoice1 = QPushButton(most_looked)
        maps = { 'Adventure Club': 'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/adventure-club.html',
                 'Aikido':"https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/aikido.html" ,
                 'Ambassadorial Team':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/ambassadorial-team.html',
                 'Archery': 'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/archery.html',
                 'Astronomy Club':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/astronomy-club.html',
                 'Athletics':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/athletics.html',
                 'Badminton':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/badminton.html',
                 'Basketball':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/basketball.html',
                 'Bei Quan Dao':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/bei-quan-dao.html',
                 'Bowling':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/bowling.html',
                 'Buddhist Society':'https://www.nyp.edu.sg/student-life/cca/societies/buddhist-society.html',
                 'Canoe Sprint':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/canoe-sprint.html',
                 'Catholic Youth Community':'https://www.nyp.edu.sg/student-life/cca/societies/legion-of-mary.html',
                 'CD Lionhearters':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/cd-lionhearters.html',
                 'Chinese Cultural Group':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/chinese-cultural-group.html',
                 'Chinese Orchestra':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/chinese-orchestra.html',
                 'Community Service Club':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/community-service-club.html',
                 'Crew Studio':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/crew-studio.html',
                 'Current Affairs & Debating Club':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/current-affairs-and-debating-club.html',
                 'Dance Company':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/dance-company.html',
                 'Danz Inc':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/danz-inc.html',
                 'Der Treff German Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/der-treff-german-club.html',
                 'Dragonboat':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/dragonboat.html',
                 'Emcee Club':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/emcee-club.html',
                 'Entrepreneurship Club':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/entrepreneurship-club.html',
                 'Floorball':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/floorball.html',
                 'Foreign Bodies':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/foreign-bodies.html',
                 'Geo Council':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/geo-council.html',
                 'Guitar Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/guitar-club.html',
                 'Harmonica Ensemble':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/harmonica-ensemble.html',
                 'Hockey':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/hockey.html',
                 'Indian Cultural Group':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/indian-cultural-group.html',
                 'Judo':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/judo.html',
                 'Kendo':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/kendo.html',
                 'K-Wave Korean Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/k-wave-korean-club.html',
                 'L Hexagone French Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/l-hexagone-french-club.html',
                 'La Ballroom En Masse':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/la-ballroom-en-masse.html',
                 'Leo Club':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/leo-club.html',
                 'Library Champions':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/library-champion.html',
                 'Life Saving':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/life-saving.html',
                 'Lion & Dragon Dance Troupe':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/lion-and-dragon-dance-troupe.html',
                 'Live Audio':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/live-audio.html',
                 'Makers Innovators Tribe':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/makers-innovators-tribe.html',
                 'Makeup Artistry':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/makeup-artistry.html',
                 'Malay Cultural Group':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/malay-cultural-group.html',
                 'Mentoring Club':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/mentoring-club.html',
                 'Mindsports':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/mindsports.html',
                 'Netball':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/netball.html',
                 'Nyaa Students Club':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/nyaa-students-club.html',
                 'NYP Cru':'https://www.nyp.edu.sg/student-life/cca/societies/nyp-cru.html',
                 'NYP Primers':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/bb-primers.html',
                 'Peer Supporter Club':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/peer-supporter-club.html',
                 'Photography Club':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/photography-club.html',
                 'Piano Ensemble':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/piano-ensemble.html',
                 'Running Club':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/running-club.html',
                 'Sakuran Japanese Cultural Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/sakuran-japanese-cultural-club.html',
                 'SAS Club':'https://www.nyp.edu.sg/student-life/cca/academic-clubs/sas-club.html',
                 'SBM Club':'https://www.nyp.edu.sg/student-life/cca/academic-clubs/sbm-club.html',
                 'SDM Club':'https://www.nyp.edu.sg/student-life/cca/academic-clubs/sdm-club.html',
                 'SEG Club':'https://www.nyp.edu.sg/student-life/cca/academic-clubs/seg-club.html',
                 'Service Learning Group':'https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/service-learning-group.html',
                 'SHSS Club':'https://www.nyp.edu.sg/student-life/cca/academic-clubs/shss-club.html',
                 'Silat':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/silat.html',
                 'SIT Club':'https://www.nyp.edu.sg/student-life/cca/academic-clubs/sit-club.html',
                 'Sketch Art Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/sketch-arts-club.html',
                 'Soccer':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/soccer.html',
                 'Soundcard':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/soundcard.html',
                 'Squash':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/squash.html',
                 'Stagearts Drama & Theatre Management Club':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/stagearts.html',
                 'Street Workout Club':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/street-workout-club.html',
                 'Strongman Club':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/strongman-club.html',
                 'Students Union':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/students-union.html',
                 'Swimming':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/swimming.html',
                 'Symphony Orchestra':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/symphony-orchestra.html',
                 'Table Tennis':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/table-tennis.html',
                 'Taekwondo':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/taekwondo.html',
                 'Tchoukball':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/tchoukball.html',
                 'Tennis':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/tennis.html',
                 'The Communicators':'https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/the-communicators.html',
                 'Touch Football':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/touch-football.html',
                 'Ultimate Frisbee':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/ultimate-frisbee.html',
                 'Voice Ensemble':'https://www.nyp.edu.sg/student-life/cca/arts-and-culture/voice-ensemble.html',
                 'Volleyball':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/volleyball.html',
                 'Zhong Hua Wushu':'https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/zhong-hua-wushu.html'
                }

        ccachoice.setStyleSheet("color: #878280; margin-left:200px; border:0px solid black;")
        ccachoice1.clicked.connect(lambda: webbrowser.open(maps[most_looked]))
        ccachoice1.setCursor(QCursor(Qt.PointingHandCursor))
        ccachoice1.setFixedHeight(50)
        ccachoice1.setStyleSheet(
            "color: #284379; border:0px solid black;margin-right:400px; margin-left:120px; text-align:left; font-weight:bold;text-decoration: underline;")
        # ccachoice.setAlignment(Qt.AlignHCenter)
        ccachoice.setFont(QFont('Times', 11))
        ccachoice1.setFont(QFont("Times", 12))
        ccachoice2 = QLabel("(Click to Sign Up!)")
        ccachoice2.setAlignment(Qt.AlignHCenter)
        ccachoice2.setFixedHeight(60)
        ccachoice2.setStyleSheet(
            "color: #9D8978; border:0px solid black; background-color: none;padding-bottom: 15px; margin-right:10px;")

        # ccachoice.setAlignment(Qt.AlignHCenter)
        ccachoice.setFont(QFont('Times', 12))
        ccachoice2.setFont(QFont('Arial', 11))
        layoutGrid.addWidget(ccachoice, 1, 1, 1, 2)
        layoutGrid.addWidget(ccachoice1, 1, 2, 1, 3)
        layoutGrid.addWidget(ccachoice2, 2, 0, 1, 0, )
        # layoutGrid.addWidget(ccachoice1,1,0,1,0)
        # layoutGrid.addWidget(ccachoice1,1,0,1,1)

        a = positions[15:]

        for a, value in zip(a, cca):

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
            ccaname = QLabel(value)
            ccaname.setAlignment(Qt.AlignHCenter)
            ccaname.setWordWrap(True)
            ccaname.setFixedHeight(10)
            # ccaname.setStyleSheet("background-color: blue;")
            ccaname.setFont(QFont('Times', 10))
            ccaname.setStyleSheet("color: #5E636D;  padding :10px; font-weight: bold;")
            ccaname.setToolTip('<font color="red" >Click on the <b>Image</b> to view the sign up link</font>')

            # ccaname.setStyleSheet("font-size: 24px;")

            ccaname.setMaximumHeight(50)
            vbox.addWidget(ccaname)
            vbox.setSpacing(0)

            images = QPushButton()
            # pixmap = QPixmap('images/Bak Kut Teh.png')
            # pixmap.scaledToHeight(images)

            # adding image to label
            # images.setPixmap(pixmap)
            images.setGeometry(100, 150, 100, 40)
            if value == "Adventure Club":
                images.setStyleSheet("border-image : url(ccaimages/Adventure Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/adventure-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Aikido":
                images.setStyleSheet("border-image : url(ccaimages/Aikido.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/aikido.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Ambassadorial Team":
                images.setStyleSheet("border-image : url(ccaimages/Ambassadorial Team.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/ambassadorial-team.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Archery":
                images.setStyleSheet("border-image : url(ccaimages/Archery.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/archery.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Astronomy Club":
                images.setStyleSheet("border-image : url(ccaimages/Astronomy Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/astronomy-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Athletics":
                images.setStyleSheet("border-image : url(ccaimages/Athletics.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/athletics.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Badminton":
                images.setStyleSheet("border-image : url(ccaimages/Badminton.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/badminton.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Basketball":
                images.setStyleSheet("border-image : url(ccaimages/Basketball.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/basketball.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Bei Quan Dao":
                images.setStyleSheet("border-image : url(ccaimages/Bei Quan Dao.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/bei-quan-dao.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Bowling":
                images.setStyleSheet("border-image : url(ccaimages/Bowling.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/bowling.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Buddhist Society":
                images.setStyleSheet("border-image : url(ccaimages/Buddhist Society.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/societies/buddhist-society.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SOCIETIES")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Canoe Sprint":
                images.setStyleSheet("border-image : url(ccaimages/Canoe Sprint.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/canoe-sprint.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Catholic Youth Community":
                images.setStyleSheet("border-image : url(ccaimages/Catholic Youth Community.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/societies/legion-of-mary.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SOCIETIES")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "CD Lionhearters":
                images.setStyleSheet("border-image : url(ccaimages/CD Lionhearters.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/cd-lionhearters.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Chinese Cultural Group":
                images.setStyleSheet("border-image : url(ccaimages/Chinese Cultural Group.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/chinese-cultural-group.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Chinese Orchestra":
                images.setStyleSheet("border-image : url(ccaimages/Chinese Orchestra.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/chinese-orchestra.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Community Service Club":
                images.setStyleSheet("border-image : url(ccaimages/Community Service Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/community-service-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Crew Studio":
                images.setStyleSheet("border-image : url(ccaimages/Crew Studio.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/crew-studio.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Current Affairs & Debating Club":
                images.setStyleSheet("border-image : url(ccaimages/Current Affairs & Debating Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/current-affairs-and-debating-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Dance Company":
                images.setStyleSheet("border-image : url(ccaimages/Dance Company.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/dance-company.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Danz Inc":
                images.setStyleSheet("border-image : url(ccaimages/Danz Inc.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/danz-inc.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Der Treff German Club":
                images.setStyleSheet("border-image : url(ccaimages/Der Treff German Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/der-treff-german-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Dragonboat":
                images.setStyleSheet("border-image : url(ccaimages/Dragonboat.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/dragonboat.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Emcee Club":
                images.setStyleSheet("border-image : url(ccaimages/Emcee Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/emcee-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Entrepreneurship Club":
                images.setStyleSheet("border-image : url(ccaimages/Entrepreneurship Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/entrepreneurship-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Floorball":
                images.setStyleSheet("border-image : url(ccaimages/Floorball.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/floorball.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Foreign Bodies":
                images.setStyleSheet("border-image : url(ccaimages/Foreign Bodies.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/foreign-bodies.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Geo Council":
                images.setStyleSheet("border-image : url(ccaimages/Geo Council.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/geo-council.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Guitar Club":
                images.setStyleSheet("border-image : url(ccaimages/Guitar Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/guitar-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Harmonica Ensemble":
                images.setStyleSheet("border-image : url(ccaimages/Harmonica Ensemble.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/harmonica-ensemble.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Hockey":
                images.setStyleSheet("border-image : url(ccaimages/Hockey.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/hockey.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Indian Cultural Group":
                images.setStyleSheet("border-image : url(ccaimages/Indian Cultural Group.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/indian-cultural-group.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Judo":
                images.setStyleSheet("border-image : url(ccaimages/Judo.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/judo.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "K-Wave Korean Club":
                images.setStyleSheet("border-image : url(ccaimages/K-Wave Korean Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/k-wave-korean-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Kendo":
                images.setStyleSheet("border-image : url(ccaimages/Kendo.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/kendo.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "L Hexagone French Club":
                images.setStyleSheet("border-image : url(ccaimages/L Hexagone French Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/l-hexagone-french-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "La Ballroom En Masse":
                images.setStyleSheet("border-image : url(ccaimages/La Ballroom En Masse.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/la-ballroom-en-masse.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Leo Club":
                images.setStyleSheet("border-image : url(ccaimages/Leo Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/leo-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Library Champions":
                images.setStyleSheet("border-image : url(ccaimages/Library Champions.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/library-champion.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Life Saving":
                images.setStyleSheet("border-image : url(ccaimages/Life Saving.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/life-saving.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Lion & Dragon Dance Troupe":
                images.setStyleSheet("border-image : url(ccaimages/Lion & Dragon Dance Troupe.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/lion-and-dragon-dance-troupe.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Live Audio":
                images.setStyleSheet("border-image : url(ccaimages/Live Audio.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/live-audio.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Makers Innovators Tribe":
                images.setStyleSheet("border-image : url(ccaimages/Makers Innovators Tribe.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/makers-innovators-tribe.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Makeup Artistry":
                images.setStyleSheet("border-image : url(ccaimages/Makeup Artistry.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/makeup-artistry.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Malay Cultural Group":
                images.setStyleSheet("border-image : url(ccaimages/Malay Cultural Group.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/malay-cultural-group.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Mentoring Club":
                images.setStyleSheet("border-image : url(ccaimages/Mentoring Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/mentoring-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Mindsports":
                images.setStyleSheet("border-image : url(ccaimages/Mindsports.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/mindsports.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Netball":
                images.setStyleSheet("border-image : url(ccaimages/Netball.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/netball.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Nyaa Students Club":
                images.setStyleSheet("border-image : url(ccaimages/Nyaa Students Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/nyaa-students-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "NYP Cru":
                images.setStyleSheet("border-image : url(ccaimages/NYP Cru.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/societies/nyp-cru.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SOCIETIES")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "NYP Primers":
                images.setStyleSheet("border-image : url(ccaimages/NYP Primers.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/bb-primers.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Peer Supporter Club":
                images.setStyleSheet("border-image : url(ccaimages/Peer Supporter Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/peer-supporter-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Photography Club":
                images.setStyleSheet("border-image : url(ccaimages/Photography Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/photography-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Piano Ensemble":
                images.setStyleSheet("border-image : url(ccaimages/Piano Ensemble.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/piano-ensemble.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Running Club":
                images.setStyleSheet("border-image : url(ccaimages/Running Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/running-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Sakuran Japanese Cultural Club":
                images.setStyleSheet("border-image : url(ccaimages/Sakuran Japanese Cultural Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/sakuran-japanese-cultural-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "SAS Club":
                images.setStyleSheet("border-image : url(ccaimages/SAS Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/academic-clubs/sas-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ACADEMIC CLUBS")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "SBM Club":
                images.setStyleSheet("border-image : url(ccaimages/SBM Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/academic-clubs/sbm-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ACADEMIC CLUBS")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "SDM Clu":
                images.setStyleSheet("border-image : url(ccaimages/SDM Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/academic-clubs/sdm-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ACADEMIC CLUBS")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "SEG Club":
                images.setStyleSheet("border-image : url(ccaimages/SEG Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/academic-clubs/seg-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ACADEMIC CLUBS")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Service Learning Group":
                images.setStyleSheet("border-image : url(ccaimages/Service Learning Group.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/community-service-and-environment/service-learning-group.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : COMMUNITY SERVICE & ENVIRONMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "SHSS Club":
                images.setStyleSheet("border-image : url(ccaimages/SHSS Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/academic-clubs/shss-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ACADEMIC CLUBS")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Silat":
                images.setStyleSheet("border-image : url(ccaimages/Silat.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/silat.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "SIT Club":
                images.setStyleSheet("border-image : url(ccaimages/SIT Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/academic-clubs/sit-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ACADEMIC CLUBS")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Sketch Art Club":
                images.setStyleSheet("border-image : url(ccaimages/Sketch Art Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/sketch-arts-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Soccer":
                images.setStyleSheet("border-image : url(ccaimages/Soccer.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/soccer.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Soundcard":
                images.setStyleSheet("border-image : url(ccaimages/Soundcard.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/soundcard.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Squash":
                images.setStyleSheet("border-image : url(ccaimages/Squash.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/squash.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Stagearts Drama & Theatre Management Club":
                images.setStyleSheet("border-image : url(ccaimages/Stagearts Drama & Theatre Management Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/stagearts.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Street Workout Club":
                images.setStyleSheet("border-image : url(ccaimages/Street Workout Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/street-workout-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Strongman Club":
                images.setStyleSheet("border-image : url(ccaimages/Strongman Club.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/strongman-club.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Students Union":
                images.setStyleSheet("border-image : url(ccaimages/Students Union.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/students-union.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Swimming":
                images.setStyleSheet("border-image : url(ccaimages/Swimming.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/swimming.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Symphony Orchestra":
                images.setStyleSheet("border-image : url(ccaimages/Symphony Orchestra.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/symphony-orchestra.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Table Tennis":
                images.setStyleSheet("border-image : url(ccaimages/Table Tennis.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/table-tennis.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Taekwondo":
                images.setStyleSheet("border-image : url(ccaimages/Taekwondo.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/taekwondo.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Tchoukball":
                images.setStyleSheet("border-image : url(ccaimages/Tchoukball.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/tchoukball.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Tennis":
                images.setStyleSheet("border-image : url(ccaimages/Tennis.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/tennis.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "The Communicators":
                images.setStyleSheet("border-image : url(ccaimages/The Communicators.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/leadership-and-character-development/the-communicators.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : LEADERSHIP & CHARACTER DEVELOPMENT")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Touch Football":
                images.setStyleSheet("border-image : url(ccaimages/Touch Football.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/touch-football.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Ultimate Frisbee":
                images.setStyleSheet("border-image : url(ccaimages/Ultimate Frisbee.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/ultimate-frisbee.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Voice Ensemble":
                images.setStyleSheet("border-image : url(ccaimages/Voice Ensemble.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/arts-and-culture/voice-ensemble.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : ARTS & CULTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Volleyball":
                images.setStyleSheet("border-image : url(ccaimages/Volleyball.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/volleyball.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)
            elif value == "Zhong Hua Wushu":
                images.setStyleSheet("border-image : url(ccaimages/Zhong Hua Wushu.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/student-life/cca/sports-and-adventure/zhong-hua-wushu.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                website = QLabel("Type of CCA : SPORTS AND ADVENTURE")
                website.setWordWrap(True)
                vbox.addWidget(website)

            images.setFixedHeight(200)
            website.setFixedHeight(55)
            website.setAlignment(Qt.AlignHCenter)
            website.setStyleSheet("color: #5E636D;background-color: #96B8F6 ; padding: 10px; opacity: 0.3;")

        backbutton = QPushButton("Quit")
        backbutton.setCursor(QCursor(Qt.PointingHandCursor))
        backbutton.clicked.connect(self.comeout)
        backbutton.setStyleSheet("background-color: white")

        layoutGrid.addWidget(backbutton, 4, 2, 1, 1)
        # choice=QLabel("You've picked")
        # foodchoice.setAlignment(Qt.AlignRight)
        # foodchoice.setFont(QFont('Times', 11))
        # layoutGrid.addWidget(foodchoice)
        # foodchoice1=QLabel(most_looked)
        # foodchoice1.setAlignment(Qt.AlignLeft)
        # foodchoice1.setFont(QFont('Times', 11))

        # foodchoice.setAlignment(Qt.AlignHCenter)
        # layoutGrid.addWidget(foodchoice1)

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
        border-image: url("CCAMain.png");
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
