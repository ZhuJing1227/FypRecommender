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
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sb
from past.builtins import execfile
import threading
from PyQt5 import QtTest

import SG_Recommender as CollaborativeRecomender1
import random

most_looked = ''

class Thread(QThread):
    progressChanged = pyqtSignal(int)
    def run(self):
        for i in range(100):
            QThread.msleep(100)
            self.progressChanged.emit(i)

class Function:
    def loading(self):
        self.screen = SplashScreen()
        self.screen.show()
        for i in range(80):
            self.screen.progressBar.setValue(i)
            QApplication.processEvents()
            time.sleep(0.19)
        self.screen.close()


class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spash Screen Example')
        self.setFixedSize(900, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        # center labels
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)  # x, y
        self.labelTitle.setText('Facial Recognition')
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Working on loading Facial Recognition with camera!</strong>')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(50, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, 70)
        self.progressBar.setValue(20)


        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('Loading...')

        self.setStyleSheet('''
                        #LabelTitle {
                            font-size: 55px;
                            color: #505050;
                            text-align: center;
                        }

                        #LabelDesc {
                            font-size: 25px;
                            color: #929093;
                            text-align: center;
                        }

                        #LabelLoading {
                            font-size: 30px;
                            color: #929093;
                            text-align: center;
                        }

                        QFrame {
                            background-color: #EFF0F3;  
                            color: rgb(220, 220, 220);
                            text-align: center;
                        }

                        QProgressBar {
                            background-color: #9BC2DB;
                            color: rgb(200, 200, 200);
                            border-style: none;
                            border-radius: 10px;
                            text-align: center;
                            font-size: 30px;
                        }

                        QProgressBar::chunk {
                            border-radius: 10px;
                            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #5C7484, stop:1 #364752);
                            text-align: center;
                        }
                    ''')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # string value
        title = "Singapore Recommender App"

        # set the title
        self.setWindowTitle(title)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.setMinimumHeight(890)
        self.setMinimumWidth(1500)
        self.pushButton1 = QPushButton("START", self.centralwidget)
        self.pushButton1.clicked.connect(self.Splashscreenwindow)
        self.pushButton2 = QPushButton("EXIT", self.centralwidget)
        self.pushButton2.clicked.connect(self.comeout)
        self.pushButton1.setFont(QFont('Times', 15))
        self.pushButton2.setFont(QFont('Times', 15))
        self.pushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2.setCursor(QCursor(Qt.PointingHandCursor))

        # buttonstyle
        self.pushButton1.setStyleSheet("QPushButton::hover"
                                       "{"
                                       "background-color : #EEC3C7;"
                                       "}")
        self.pushButton2.setStyleSheet("QPushButton::hover"
                                       "{"
                                       "background-color : #F6F6F6;"

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

        self.singaporewindow = singaporewindow()

        self.singaporewindow.show()
        self.close()

    def Splashscreenwindow(self, checked):
        t1 = threading.Thread(target=self.Facialrec1)
        t1.start()
        self.function = Function()
        self.function.loading()
        # time.sleep(10)
        # t2 = threading.Thread(target=self.Restofapp)
        # t2.start()

        QtTest.QTest.qWait(9000)
        self.w = GridDemo()
        self.okk = okk()
        self.singaporewindow = singaporewindow()
        self.singaporewindow.show()

    def Facialrec1(self):
        print("starting latest facial recognition")
        os.system('python face_updated.py')
        # time.sleep(10)

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


# style pics
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        title = "Singapore Recommender App"

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

        imagechooser = "imagechooser%d" % (random.randint(1, 7))
        #imagechooser = "imagechooser3"

        with open('imagechooser.txt', 'w') as out:
            line1 = imagechooser
            out.write(line1)
        if imagechooser == "imagechooser1":
            print("1")
            self.image.setStyleSheet("border-image: url(SingaporeCata1.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser2":
            print("2")
            self.image.setStyleSheet("border-image: url(SingaporeCata2.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser3":
            print("3")
            self.image.setStyleSheet("border-image: url(SingaporeCata3.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser4":
            print("4")
            self.image.setStyleSheet("border-image: url(SingaporeCata4.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser5":
            print("5")
            self.image.setStyleSheet("border-image: url(SingaporeCata5.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser6":
            print("6")
            self.image.setStyleSheet("border-image: url(SingaporeCata6.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser == "imagechooser7":
            print("7")
            self.image.setStyleSheet("border-image: url(SingaporeCata7.png);")
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
            singaporezoo = 0
            universalstudiosingapore = 0
            singaporeflyer = 0
            sentosamerliontower = 0
            singaporebotanicgardens = 0
            buddhatoothrelictempleandmuseum = 0
            asiancivilisationmuseum = 0
            palawanbeach = 0

            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    singaporezoo += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    universalstudiosingapore += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    singaporeflyer += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    sentosamerliontower += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    singaporebotanicgardens += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    buddhatoothrelictempleandmuseum += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    asiancivilisationmuseum += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    palawanbeach += 1

            rank.append(singaporezoo)
            rank.append(universalstudiosingapore)
            rank.append(singaporeflyer)
            rank.append(sentosamerliontower)
            rank.append(singaporebotanicgardens)
            rank.append(buddhatoothrelictempleandmuseum)
            rank.append(asiancivilisationmuseum)
            rank.append(palawanbeach)

            if max(rank) == rank[0]:
                most_looked = 'Singapore Zoo'
            elif max(rank) == rank[1]:
                most_looked = 'Universal Studios Singapore'
            elif max(rank) == rank[2]:
                most_looked = 'Singapore Flyer'
            elif max(rank) == rank[3]:
                most_looked = 'Sentosa Merlion Tower'
            elif max(rank) == rank[4]:
                most_looked = 'Singapore Botanic Gardens'
            elif max(rank) == rank[5]:
                most_looked = 'Buddha Tooth Relic Temple and Museum'
            elif max(rank) == rank[6]:
                most_looked = 'Asian Civilisations Museum'
            elif max(rank) == rank[7]:
                most_looked = 'Palawan Beach'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser2':
            rank = []
            most_looked = ''
            nightsafarinocturnalwildlifepark = 0
            megazip = 0
            singaporeairzone = 0
            marinabaysingapore = 0
            treetopwalkatmacritchiereservoir = 0
            bugisstreet = 0
            altitudesightseeingexperience = 0
            tanjongbeach = 0

            """

            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    nightsafarinocturnalwildlifepark += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    megazip += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    singaporeairzone += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    marinabaysingapore += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    treetopwalkatmacritchiereservoir += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    bugisstreet += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    altitudesightseeingexperience += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    tanjongbeach += 1

            rank.append(nightsafarinocturnalwildlifepark)
            rank.append(megazip)
            rank.append(singaporeairzone)
            rank.append(marinabaysingapore)
            rank.append(treetopwalkatmacritchiereservoir)
            rank.append(bugisstreet)
            rank.append(altitudesightseeingexperience)
            rank.append(tanjongbeach)

            if max(rank) == rank[0]:
                most_looked = 'Night Safari Nocturnal Wildlife Park'
            elif max(rank) == rank[1]:
                most_looked = 'Megazip'
            elif max(rank) == rank[2]:
                most_looked = 'Singapore Airzone'
            elif max(rank) == rank[3]:
                most_looked = 'Marina Bay Singapore'
            elif max(rank) == rank[4]:
                most_looked = 'Tree-top Walk at MacRitchie Reservoir'
            elif max(rank) == rank[5]:
                most_looked = 'Bugis Street'
            elif max(rank) == rank[6]:
                most_looked = '1-Altitude Sightseeing Experience'
            elif max(rank) == rank[7]:
                most_looked = 'Tanjong Beach'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser3':

            rank = []
            most_looked = ''
            jurongbirdpark = 0
            drivingonthef1track = 0
            singaporecablecar = 0
            gardensbythebay = 0
            mountfaberpark = 0
            chinatown = 0
            adventurecovewaterpark = 0
            silosobeach = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    jurongbirdpark += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    drivingonthef1track += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    singaporecablecar += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    gardensbythebay += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    mountfaberpark += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    chinatown += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    adventurecovewaterpark += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    silosobeach += 1

            rank.append(jurongbirdpark)
            rank.append(drivingonthef1track)
            rank.append(singaporecablecar)
            rank.append(gardensbythebay)
            rank.append(mountfaberpark)
            rank.append(chinatown)
            rank.append(adventurecovewaterpark)
            rank.append(silosobeach)

            if max(rank) == rank[0]:
                most_looked = 'Jurong Bird Park'
            elif max(rank) == rank[1]:
                most_looked = 'Driving on the F1 Track'
            elif max(rank) == rank[2]:
                most_looked = 'Singapore Cable Car'
            elif max(rank) == rank[3]:
                most_looked = 'Gardens By The Bay'
            elif max(rank) == rank[4]:
                most_looked = 'Mount Faber Park'
            elif max(rank) == rank[5]:
                most_looked = 'China Town'
            elif max(rank) == rank[6]:
                most_looked = 'Adventure Cove Waterpark'
            elif max(rank) == rank[7]:
                most_looked = 'Siloso Beach'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser4':

            rank = []
            most_looked = ''
            dolphinislandinteractionprogram = 0
            iflysingapore = 0
            singaporerivercruise = 0
            sentosaisland = 0
            nationalorchidgarden = 0
            marinabaysandscasino = 0
            tigerbrewery = 0
            pulauubin = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    dolphinislandinteractionprogram += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    iflysingapore += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    singaporerivercruise += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    sentosaisland += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    nationalorchidgarden += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    marinabaysandscasino += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    tigerbrewery += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    pulauubin += 1

            rank.append(dolphinislandinteractionprogram)
            rank.append(iflysingapore)
            rank.append(singaporerivercruise)
            rank.append(sentosaisland)
            rank.append(nationalorchidgarden)
            rank.append(marinabaysandscasino)
            rank.append(tigerbrewery)
            rank.append(pulauubin)

            if max(rank) == rank[0]:
                most_looked = 'Dolphin Island Interaction Program'
            elif max(rank) == rank[1]:
                most_looked = 'IFly Singapore'
            elif max(rank) == rank[2]:
                most_looked = 'Singapore River Cruise'
            elif max(rank) == rank[3]:
                most_looked = 'Sentosa Island'
            elif max(rank) == rank[4]:
                most_looked = 'National Orchid Garden'
            elif max(rank) == rank[5]:
                most_looked = 'Marina Bay Sands Casino'
            elif max(rank) == rank[6]:
                most_looked = 'Tiger Brewery'
            elif max(rank) == rank[7]:
                most_looked = 'Pulau Ubin'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser5':

            rank = []
            most_looked = ''
            riverwonderssingapore = 0
            indoorsurfingwavehousesentosa = 0
            kidzaniasingapore = 0
            merlionpark = 0
            butterflyparkandinsectkingdom = 0
            clarkequay = 0
            trickeyemuseum = 0
            kusuisland = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    riverwonderssingapore += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    indoorsurfingwavehousesentosa += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    kidzaniasingapore += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    merlionpark += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    butterflyparkandinsectkingdom += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    clarkequay += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    trickeyemuseum += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    kusuisland += 1

            rank.append(riverwonderssingapore)
            rank.append(indoorsurfingwavehousesentosa)
            rank.append(kidzaniasingapore)
            rank.append(merlionpark)
            rank.append(butterflyparkandinsectkingdom)
            rank.append(clarkequay)
            rank.append(trickeyemuseum)
            rank.append(kusuisland)

            if max(rank) == rank[0]:
                most_looked = 'River Wonders Singapore'
            elif max(rank) == rank[1]:
                most_looked = 'Indoor Surfing Wave House Sentosa'
            elif max(rank) == rank[2]:
                most_looked = 'Kidzania Singapore'
            elif max(rank) == rank[3]:
                most_looked = 'Merlion Park'
            elif max(rank) == rank[4]:
                most_looked = 'Butterfly Park And Insect Kingdom'
            elif max(rank) == rank[5]:
                most_looked = 'Clarke Quay'
            elif max(rank) == rank[6]:
                most_looked = 'Trick Eye Museum'
            elif max(rank) == rank[7]:
                most_looked = 'Kusu Island'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser6':

            rank = []
            most_looked = ''
            lunchwithparrots = 0
            ajhackettsentosabungyjump = 0
            theoriginalducktourssentosa= 0
            thehelixbridge = 0
            bukittimahnaturereserve = 0
            srimariammantemple = 0
            madametussaudswaxmuseum = 0
            lazarusisland = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    lunchwithparrots += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    ajhackettsentosabungyjump += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    theoriginalducktourssentosa += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    thehelixbridge += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    bukittimahnaturereserve += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    srimariammantemple += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    madametussaudswaxmuseum += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    lazarusisland += 1

            rank.append(lunchwithparrots)
            rank.append(ajhackettsentosabungyjump)
            rank.append(theoriginalducktourssentosa)
            rank.append(thehelixbridge)
            rank.append(bukittimahnaturereserve)
            rank.append(srimariammantemple)
            rank.append(madametussaudswaxmuseum)
            rank.append(lazarusisland)

            if max(rank) == rank[0]:
                most_looked = 'Lunch with Parrots'
            elif max(rank) == rank[1]:
                most_looked = 'AJ Hackett Sentosa Bungy Jump'
            elif max(rank) == rank[2]:
                most_looked = 'The Original Duck Tours Sentosa'
            elif max(rank) == rank[3]:
                most_looked = 'The Helix Bridge'
            elif max(rank) == rank[4]:
                most_looked = 'Bukit Timah Nature Reserve'
            elif max(rank) == rank[5]:
                most_looked = 'Sri Mariamman Temple'
            elif max(rank) == rank[6]:
                most_looked = 'Madame Tussauds Wax Museum'
            elif max(rank) == rank[7]:
                most_looked = 'Lazarus Island'
            else:
                print("Smth went very wrong")

        if imagechooser == 'imagechooser7':

            rank = []
            most_looked = ''
            singaporezoojunglebreakfast = 0
            skylineluge = 0
            royalalbatrosssunsetsail= 0
            wingsoftime = 0
            singaporebotanicgardens = 0
            littleindia = 0
            seaaquarium = 0
            infinitypoolatmarinabaysands = 0
            """
            Setup image map
            """
            for i in self.Cord:
                if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                    singaporezoojunglebreakfast += 1

                elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                    skylineluge += 1

                elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                    royalalbatrosssunsetsail += 1

                elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                    wingsoftime += 1

                elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                    singaporebotanicgardens += 1

                elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                    littleindia += 1

                elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                    seaaquarium += 1

                elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                    infinitypoolatmarinabaysands += 1

            rank.append(singaporezoojunglebreakfast)
            rank.append(skylineluge)
            rank.append(royalalbatrosssunsetsail)
            rank.append(wingsoftime)
            rank.append(singaporebotanicgardens)
            rank.append(littleindia)
            rank.append(seaaquarium)
            rank.append(infinitypoolatmarinabaysands)

            if max(rank) == rank[0]:
                most_looked = 'Singapore Zoo Jungle Breakfast'
            elif max(rank) == rank[1]:
                most_looked = 'Skyline Luge'
            elif max(rank) == rank[2]:
                most_looked = 'Royal Albatross Sunset Sail'
            elif max(rank) == rank[3]:
                most_looked = 'Wings of Time'
            elif max(rank) == rank[4]:
                most_looked = 'Singapore Botanic Gardens'
            elif max(rank) == rank[5]:
                most_looked = 'Little India'
            elif max(rank) == rank[6]:
                most_looked = 'SEA Aquarium'
            elif max(rank) == rank[7]:
                most_looked = 'Infinity Pool at Marina Bay Sands'
            else:
                print("Smth went very wrong")

        print("Most looked place: ", most_looked)
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
        title = "Singapore Recommender App"

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
            mp_img = mpimg.imread("SingaporeCata1.png")
        elif image == "imagechooser2":
            mp_img = mpimg.imread("SingaporeCata2.png")
        elif image == "imagechooser3":
            mp_img = mpimg.imread("SingaporeCata3.png")
        elif image == "imagechooser4":
            mp_img = mpimg.imread("SingaporeCata4.png")
        elif image == "imagechooser5":
            mp_img = mpimg.imread("SingaporeCata5.png")
        elif image == "imagechooser6":
            mp_img = mpimg.imread("SingaporeCata6.png")
        elif image == "imagechooser7":
            mp_img = mpimg.imread("SingaporeCata7.png")

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


class singaporewindow(QWidget):

    def __init__(self):
        super().__init__()
        global most_looked
        title = "Singapore Recommender App"

        # set the title
        self.setWindowTitle(title)
        # self.setStyleSheet()
        self.setStyleSheet("background-color: #EEC3C7;")

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

        singapore = []
        for i in values:
            singapore.append(i)
        imgList = []
        print(singapore)
        df1 = pd.read_csv('Singapore_location.csv', encoding='mac_roman')

        location = []
        # Storing img paths to match the recommendations and location
        for place in singapore:
            for x in range(len(df1['name'])):
                if df1['name'][x] == place:
                    imgFile = "sgimages/" + place + ".png"
                    print('imgfile=', imgFile)

                    imgList.append("sgimages/" + place + ".png")
                    # self.rating.append(df1['rating'][x])
                    locate = (df1['location'][x])
                    location.append(locate)
        print(location)

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
        singaporechoice = QLabel("You've picked: ")

        singaporechoice1 = QPushButton(most_looked)
        maps = {"Singapore Zoo": "https://www.thrillophilia.com/tours/singapore-zoo-attraction-ticket",
                "Universal Studios Singapore": "https://www.thrillophilia.com/tours/universal-studios-singapore-attraction-tickets",
                "Singapore Flyer": "https://www.thrillophilia.com/tours/singapore-flyer-tickets",
                "Sentosa Merlion Tower": "https://www.thrillophilia.com/tours/sentosa-merlion-e-ticket",
                "Singapore Botanic Gardens": "https://www.thrillophilia.com/tours/botanic-garden-singapore-tickets",
                "Buddha Tooth Relic Temple and Museum": "https://www.thrillophilia.com/attractions/buddha-tooth-relic-temple-and-museum",
                "Asian Civilisations Museum": "https://www.thrillophilia.com/tours/asian-civilisations-museum-singapore-tickets",
                "Palawan Beach": "https://www.thrillophilia.com/attractions/palawan-beach",
                "Night Safari Nocturnal Wildlife Park": "https://www.thrillophilia.com/tours/night-safari",
                "Megazip": "https://www.thrillophilia.com/tours/singapore-ziplining-and-megajump",
                "Singapore Airzone": "https://www.thrillophilia.com/tours/airzone-singapore-tickets",
                "Marina Bay Singapore": "https://www.thrillophilia.com/tours/nightout-at-marina-bay-in-singapore",
                "Tree-top Walk at MacRitchie Reservoir": "https://www.thrillophilia.com/attractions/macritchie-reservoir",
                "Bugis Street": "https://www.thrillophilia.com/attractions/bugis-street",
                "1-Altitude Sightseeing Experience": "https://www.thrillophilia.com/tours/1-altitude-gallery-bar-singapore",
                "Tanjong Beach": "https://www.tanjongbeachclub.com/",
                "Jurong Bird Park": "https://www.thrillophilia.com/tours/wings-of-colour-jurong-bird-park",
                "Driving on the F1 Track": "https://www.viator.com/en-SG/tours/Singapore/F1-Street-Circuit-Driving-Experience-in-Singapore/d18-46827P5",
                "Singapore Cable Car": "https://www.thrillophilia.com/tours/sentosa-cable-car-2-way-att",
                "Gardens By The Bay": "https://www.thrillophilia.com/tours/gardens-by-the-bay-tickets-includes-both-domes-singapore-attraction-ticket",
                "Mount Faber Park": "https://www.thrillophilia.com/attractions/mount-faber-park",
                "China Town": "https://www.thrillophilia.com/attractions/china-town",
                "Adventure Cove Waterpark": "https://www.thrillophilia.com/tours/adventure-cove-waterpark",
                "Siloso Beach": "https://www.sentosa.com.sg/en/things-to-do/attractions/siloso-beach/",
                "Dolphin Island Interaction Program": "https://www.thrillophilia.com/tours/dolphin-island-interaction-program-attraction-ticket",
                "IFly Singapore": "https://www.thrillophilia.com/tours/ifly-singapore",
                "Singapore River Cruise": "https://www.thrillophilia.com/tours/singapore-river-cruise",
                "Sentosa Island": "https://www.thrillophilia.com/tours/sentosa-tourist-pack",
                "National Orchid Garden": "https://www.thrillophilia.com/attractions/national-orchid-garden",
                "Marina Bay Sands Casino": "https://www.thrillophilia.com/attractions/marina-bay-sands-casino",
                "Tiger Brewery": "https://www.thrillophilia.com/tours/tiger-brewery-tour",
                "Pulau Ubin": "https://www.thrillophilia.com/tours/pulau-ubin-kayaking-singapore-tickets",
                "River Wonders Singapore": "https://www.thrillophilia.com/tours/river-safari",
                "Indoor Surfing Wave House Sentosa": "https://www.thrillophilia.com/tours/wave-house-sentosa",
                "Kidzania Singapore": "https://www.thrillophilia.com/tours/ticket-to-kidzania-singapore",
                "Merlion Park": "https://www.tripadvisor.com.sg/Attraction_Review-g294265-d644919-Reviews-Merlion_Park-Singapore.html",
                "Butterfly Park And Insect Kingdom": "https://www.thrillophilia.com/tours/buttertly-park-insect-kingdom-singapore-attraction-tickets",
                "Clarke Quay": "https://www.thrillophilia.com/attractions/clarke-quay",
                "Trick Eye Museum": "https://www.thrillophilia.com/tours/trick-eye-museum-attraction-tickets",
                "Kusu Island": "https://www.thrillophilia.com/attractions/kusu-island",
                "Lunch with Parrots": "https://www.thrillophilia.com/tours/lunch-with-parrots-in-singapore",
                "AJ Hackett Sentosa Bungy Jump": "https://www.thrillophilia.com/tours/aj-hackett-sentosa-bungy-jump",
                "The Original Duck Tours Sentosa": "https://www.thrillophilia.com/tours/the-original-ducktours-singapore",
                "The Helix Bridge": "https://www.thrillophilia.com/attractions/helix-bridge",
                "Bukit Timah Nature Reserve": "https://www.thrillophilia.com/attractions/bukit-timah-nature-reserve",
                "Sri Mariamman Temple": "https://www.thrillophilia.com/attractions/sri-mariamman-temple-singapore",
                "Madame Tussauds Wax Museum": "https://www.thrillophilia.com/tours/madame-tussauds-singapore",
                "Lazarus Island": "https://www.thrillophilia.com/attractions/lazarus-island",
                "Singapore Zoo Jungle Breakfast": "https://www.thrillophilia.com/tours/singapore-zoo-attraction-ticket",
                "Skyline Luge": "https://www.thrillophilia.com/tours/luge-skyride-singapore-attraction-ticket",
                "Royal Albatross Sunset Sail": "https://www.thrillophilia.com/tours/the-royal-albatross-sunset-cruise",
                "Wings of Time": "https://www.thrillophilia.com/tours/wings-of-time-musical-fountain-and-laser-show-attraction-tickets",
                "Little India": "https://www.thrillophilia.com/attractions/little-india",
                "SEA Aquarium": "https://www.thrillophilia.com/tours/s-e-a-aquarium",
                "Infinity Pool at Marina Bay Sands": "https://www.thrillophilia.com/tours/nightout-at-marina-bay-in-singapore"
                }

        singaporechoice.setStyleSheet("color: #878280; margin-left:200px; border:0px solid black;")
        singaporechoice1.clicked.connect(lambda: webbrowser.open(maps[most_looked]))
        singaporechoice1.setCursor(QCursor(Qt.PointingHandCursor))
        singaporechoice1.setFixedHeight(50)
        singaporechoice1.setStyleSheet(
            "color: #545454; border:0px solid black;margin-right:400px; margin-left:120px; text-align:left; font-weight:bold;text-decoration: underline;")
        # stylechoice.setAlignment(Qt.AlignHCenter)
        singaporechoice.setFont(QFont('Times', 11))
        singaporechoice1.setFont(QFont("Times", 12))
        singaporechoice2 = QLabel("(Click to Find Out More!)")
        singaporechoice2.setAlignment(Qt.AlignHCenter)
        singaporechoice2.setFixedHeight(60)
        singaporechoice2.setStyleSheet(
            "color: #9D8978; border:0px solid black; background-color: none;padding-bottom: 15px; margin-right:10px;")

        # stylechoice.setAlignment(Qt.AlignHCenter)
        singaporechoice.setFont(QFont('Times', 12))
        singaporechoice2.setFont(QFont('Arial', 11))
        layoutGrid.addWidget(singaporechoice, 1, 1, 1, 2)
        layoutGrid.addWidget(singaporechoice1, 1, 2, 1, 3)
        layoutGrid.addWidget(singaporechoice2, 2, 0, 1, 0, )
        # layoutGrid.addWidget(stylechoice1,1,0,1,0)
        # layoutGrid.addWidget(stylechoice1,1,0,1,1)

        a = positions[15:]

        for a, value in zip(a, singapore):

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
            singaporename = QLabel(value)
            singaporename.setAlignment(Qt.AlignHCenter)
            singaporename.setWordWrap(True)
            singaporename.setFixedHeight(10)
            # stylename.setStyleSheet("background-color: blue;")
            singaporename.setFont(QFont('Times', 10))
            singaporename.setStyleSheet("color: #545454;  padding :15px; font-weight: Semi Bold;")
            singaporename.setToolTip('<font color="red" >Click on the <b>Image</b> to view the info of the place</font>')

            # stylename.setStyleSheet("font-size: 24px;")

            singaporename.setMaximumHeight(50)
            vbox.addWidget(singaporename)
            vbox.setSpacing(0)

            images = QPushButton()
            # pixmap = QPixmap('images/Bak Kut Teh.png')
            # pixmap.scaledToHeight(images)

            # adding image to label
            # images.setPixmap(pixmap)
            images.setGeometry(100, 150, 100, 40)
            if value == "Singapore Zoo":
                images.setStyleSheet("border-image : url(sgimages/Singapore Zoo.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/singapore-zoo-attraction-ticket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 80 Mandai Lake Rd, Singapore, 729826")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Universal Studios Singapore":
                images.setStyleSheet("border-image : url(sgimages/Universal Studios Singapore.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/universal-studios-singapore-attraction-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 8 Sentosa Gateway, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Singapore Flyer":
                images.setStyleSheet("border-image : url(sgimages/Singapore Flyer.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/singapore-flyer-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 30 Raffles Ave, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Sentosa Merlion Tower":
                images.setStyleSheet("border-image : url(sgimages/Sentosa Merlion Tower.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/sentosa-merlion-e-ticket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 30 Imbiah Road, Sentosa, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Singapore Botanic Gardens":
                images.setStyleSheet("border-image : url(sgimages/Singapore Botanic Gardens.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/botanic-garden-singapore-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 1 Cluny Rd, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Buddha Tooth Relic Temple and Museum":
                images.setStyleSheet("border-image : url(sgimages/Buddha Tooth Relic Temple and Museum.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/buddha-tooth-relic-temple-and-museum'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 288 South Bridge Rd, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Asian Civilisations Museum":
                images.setStyleSheet("border-image : url(sgimages/Asian Civilisations Museum.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/asian-civilisations-museum-singapore-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 1 Empress Plaza, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Palawan Beach":
                images.setStyleSheet("border-image : url(sgimages/Palawan Beach.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/palawan-beach'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Palawan Beach, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Night Safari Nocturnal Wildlife Park":
                images.setStyleSheet("border-image : url(sgimages/Night Safari Nocturnal Wildlife Park.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/night-safari'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 80 Mandai Lake Rd, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Megazip":
                images.setStyleSheet("border-image : url(sgimages/Megazip.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/singapore-ziplining-and-megajump'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 10A Siloso Beach Walk, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Singapore Airzone":
                images.setStyleSheet("border-image : url(sgimages/Singapore Airzone.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/airzone-singapore-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 108 Kitchener Road, City Square Mall, Singapore 208539")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Marina Bay Singapore":
                images.setStyleSheet("border-image : url(sgimages/Marina Bay Singapore.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/nightout-at-marina-bay-in-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 10 Bayfront Avenue")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Tree-top Walk at MacRitchie Reservoir":
                images.setStyleSheet("border-image : url(sgimages/Tree-top Walk at MacRitchie Reservoir.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/macritchie-reservoir'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Macritchie Reservoir")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Bugis Street":
                images.setStyleSheet("border-image : url(sgimages/Bugis Street.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/bugis-street'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 3 New Bugis Street, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "1-Altitude Sightseeing Experience":
                images.setStyleSheet("border-image : url(sgimages/1-Altitude Sightseeing Experience.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/1-altitude-gallery-bar-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: One Raffles Place, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Tanjong Beach":
                images.setStyleSheet("border-image : url(sgimages/Tanjong Beach.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.tanjongbeachclub.com/'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 20 Tanjong Beach Walk, Sentosa, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Jurong Bird Park":
                images.setStyleSheet("border-image : url(sgimages/Jurong Bird Park.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/wings-of-colour-jurong-bird-park'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 2 Jurong Hill, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Driving on the F1 Track":
                images.setStyleSheet("border-image : url(sgimages/Driving on the F1 Track.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.viator.com/en-SG/tours/Singapore/F1-Street-Circuit-Driving-Experience-in-Singapore/d18-46827P5'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Marina Bay Sands (10 Bayfront Avenue, Singapore 018956)")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Singapore Cable Car":
                images.setStyleSheet("border-image : url(sgimages/Singapore Cable Car.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/sentosa-cable-car-2-way-att'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 1 Harbourfront Ave, tower 2 Keppel Bay Tower, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Gardens By The Bay":
                images.setStyleSheet("border-image : url(sgimages/Gardens By The Bay.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/gardens-by-the-bay-tickets-includes-both-domes-singapore-attraction-ticket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 18 Marina Gardens Dr, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Mount Faber Park":
                images.setStyleSheet("border-image : url(sgimages/Mount Faber Park.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/mount-faber-park'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 109 Faber road, Faber Peak, Singapore 099203, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "China Town":
                images.setStyleSheet("border-image : url(sgimages/China Town.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/china-town'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 158 Telok Ayer Street, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Adventure Cove Waterpark":
                images.setStyleSheet("border-image : url(sgimages/Adventure Cove Waterpark.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/adventure-cove-waterpark'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Resorts World Sentosa, 8 Sentosa Gateway, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)

            elif value == "Siloso Beach":
                images.setStyleSheet("border-image : url(sgimages/Siloso Beach.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.sentosa.com.sg/en/things-to-do/attractions/siloso-beach/'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 21 km from Singapore City")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Dolphin Island Interaction Program":
                images.setStyleSheet("border-image : url(sgimages/Dolphin Island Interaction Program.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/dolphin-island-interaction-program-attraction-ticket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Dolphin Island, Sentosa Island, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "IFly Singapore":
                images.setStyleSheet("border-image : url(sgimages/IFly Singapore.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/ifly-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: iFly Singapore, 43 Siloso Beach Walk #01-01 Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Singapore River Cruise":
                images.setStyleSheet("border-image : url(sgimages/Singapore River Cruise.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/singapore-river-cruise'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Clarke Quay, Singapore River, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Sentosa Island":
                images.setStyleSheet("border-image : url(sgimages/Sentosa Island.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/sentosa-tourist-pack'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: South of Singapore CBD, a 12-minute cable car ride away from Vivo City.")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "National Orchid Garden":
                images.setStyleSheet("border-image : url(sgimages/National Orchid Garden.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/national-orchid-garden'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 1 Cluny Road, Singapore Botanic Garden")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Marina Bay Sands Casino":
                images.setStyleSheet("border-image : url(sgimages/Marina Bay Sands Casino.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/marina-bay-sands-casino'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Marina Bay Sands, 10 Bayfront Avenue, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Tiger Brewery":
                images.setStyleSheet("border-image : url(sgimages/Tiger Brewery.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/tiger-brewery-tour'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 459 JIn Ahmad Ibrahim Singapore 639934")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Pulau Ubin":
                images.setStyleSheet("border-image : url(sgimages/Pulau Ubin.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/pulau-ubin-kayaking-singapore-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: The thrilling adventure starts on a bumboat that leaves from the Changi Village")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "River Wonders Singapore":
                images.setStyleSheet("border-image : url(sgimages/River Wonders Singapore.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/river-safari'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: The River Safari is situated just next to the famous Zoo, 80 Mandai Lake Road, Singapore, 729826")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Indoor Surfing Wave House Sentosa":
                images.setStyleSheet("border-image : url(sgimages/Indoor Surfing Wave House Sentosa.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/wave-house-sentosa'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 36 Siloso Beach Walk, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Kidzania Singapore":
                images.setStyleSheet("border-image : url(sgimages/Kidzania Singapore.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/ticket-to-kidzania-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 31 Beach View, #01-01/02, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Merlion Park":
                images.setStyleSheet("border-image : url(sgimages/Merlion Park.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.tripadvisor.com.sg/Attraction_Review-g294265-d644919-Reviews-Merlion_Park-Singapore.html'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 1 Fullerton Rd, Singapore 049213")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Butterfly Park And Insect Kingdom":
                images.setStyleSheet("border-image : url(sgimages/Butterfly Park And Insect Kingdom.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/buttertly-park-insect-kingdom-singapore-attraction-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 51 Imbiah Road, Sentosa 099702")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Clarke Quay":
                images.setStyleSheet("border-image : url(sgimages/Clarke Quay.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/clarke-quay'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Clarke Quay, Riverside, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Trick Eye Museum":
                images.setStyleSheet("border-image : url(sgimages/Trick Eye Museum.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/trick-eye-museum-attraction-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 26 Sentosa Gateway #01-43/44, Singapore 098138")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Kusu Island":
                images.setStyleSheet("border-image : url(sgimages/Kusu Island.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/kusu-islandhttps://www.thrillophilia.com/attractions/kusu-island'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Kusu Island, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Lunch with Parrots":
                images.setStyleSheet("border-image : url(sgimages/Lunch with Parrots.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/lunch-with-parrots-in-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Jurong Bird Park, 2 Jurong Hill, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "AJ Hackett Sentosa Bungy Jump":
                images.setStyleSheet("border-image : url(sgimages/AJ Hackett Sentosa Bungy Jump.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/aj-hackett-sentosa-bungy-jump'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 30 Siloso Beach Walk, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "The Original Duck Tours Sentosa":
                images.setStyleSheet("border-image : url(sgimages/The Original Duck Tours Sentosa.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/the-original-ducktours-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Suntec City, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "The Helix Bridge":
                images.setStyleSheet("border-image : url(sgimages/The Helix Bridge.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/helix-bridge'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Downtown Core")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Bukit Timah Nature Reserve":
                images.setStyleSheet("border-image : url(sgimages/Bukit Timah Nature Reserve.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/bukit-timah-nature-reserve'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Hindhede Drive, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Sri Mariamman Temple":
                images.setStyleSheet("border-image : url(sgimages/Sri Mariamman Temple.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/sri-mariamman-temple-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 244 South Bridge Road, Chinatown, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Madame Tussauds Wax Museum":
                images.setStyleSheet("border-image : url(sgimages/Madame Tussauds Wax Museum.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/madame-tussauds-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 40 Imbiah Road, Sentosa Island, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Lazarus Island":
                images.setStyleSheet("border-image : url(sgimages/Lazarus Island.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/lazarus-island'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Southern Islands, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Singapore Zoo Jungle Breakfast":
                images.setStyleSheet("border-image : url(sgimages/Singapore Zoo Jungle Breakfast.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/singapore-zoo-attraction-ticket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Ah Meng Restaurant (Terrace), Singapore Zoo, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Skyline Luge":
                images.setStyleSheet("border-image : url(sgimages/Skyline Luge.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/luge-skyride-singapore-attraction-ticket'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Skyline Luge Sentosa, Imbiah Road, Sentosa, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Royal Albatross Sunset Sail":
                images.setStyleSheet("border-image : url(sgimages/Royal Albatross Sunset Sail.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/the-royal-albatross-sunset-cruise'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 8 Sentosa Gateway, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Wings of Time":
                images.setStyleSheet("border-image : url(sgimages/Wings of Time.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/wings-of-time-musical-fountain-and-laser-show-attraction-tickets'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 50 Beach View, Sentosa Island, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Little India":
                images.setStyleSheet("border-image : url(sgimages/Little India.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/attractions/little-india'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Mini India is situated in the Serangoon ")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "SEA Aquarium":
                images.setStyleSheet("border-image : url(sgimages/SEA Aquarium.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/s-e-a-aquarium'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: 8 Sentosa Gateway, Sentosa Island, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value == "Infinity Pool at Marina Bay Sands":
                images.setStyleSheet("border-image : url(sgimages/Infinity Pool at Marina Bay Sands.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.thrillophilia.com/tours/nightout-at-marina-bay-in-singapore'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0, 0, 0, 0)
                location = QLabel("Location: Bayfront Road 10, Singapore")
                location.setWordWrap(True)
                vbox.addWidget(location)


            images.setFixedHeight(250)
            location.setFixedHeight(55)
            location.setAlignment(Qt.AlignHCenter)
            location.setStyleSheet("color: #6C756F;background-color: #F6F6F6 ; padding: 10px; opacity: 0.3;")

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
        border-image: url("SingaporeMain.png");
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
