# from PyQt5.QtWidgets import *
# import sys
# from pprint import pprint as pp
#
# from PyQt5.QtGui import QPixmap, QFont
# from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QGroupBox, QLabel, \
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

import age_gender_1food_recommender as CollaborativeRecomender1
import random
most_looked = ''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # string value
        title = "Food Recommender App"

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


        #buttonstyle
        self.pushButton1.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : lightgreen;"
                             "}")
        self.pushButton2.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : orange;"

                             "}")

        # self.setGeometry(0,0,500,500)
        self.pushButton2.setMinimumHeight(40)
        self.pushButton1.setMinimumHeight(40)
        self.pushButton2.setMinimumWidth(200)
        self.pushButton1.setMinimumWidth(200)
        self.pushButton1.resize(300,300)
        self.pushButton2.resize(300,300)
        self.showMaximized()

        lay = QHBoxLayout(self.centralwidget)
        lay.setContentsMargins(550,0,550,0)
        lay.addWidget(self.pushButton1)
        lay.addWidget(self.pushButton2)
        lay.setSpacing(30)

    def show_new_window(self, checked):
        execfile("face.py")
        self.w = GridDemo()
        self.okk=okk()

        self.foodwindow=foodwindow()

        self.foodwindow.show()
        self.close()

    def comeout(self, checked):
         button = QMessageBox.critical(
            self,
            "Exiting Confirmation",
            "Are you sure you want to exit?",
            buttons=QMessageBox.No | QMessageBox.Yes ,
            defaultButton=QMessageBox.No,)

         if button == QMessageBox.No:
            print("Rejected exit confirmation")
         elif button == QMessageBox.Yes:
            print("Exit")
            self.close()

    def plot(self):
            def xcord():
                with open('cords.txt', 'r') as f:
                    content_list = [line.rstrip('\n') for line in f]
                    ok1= content_list[0]
                    print(type(ok1))
                    ok2=eval(ok1)
                    x=list(ok2)
                    print(type(x))
                return x
            def ycord():
                with open('cords.txt', 'r') as f:
                    last_line = f.readlines()[-1]
                    ycord=last_line
                x=eval(ycord)
                y=list(x)
                print(type(y))
                return y
            x=xcord()
            y=ycord()
            print("x",x)
            print("y",y)

            counter = 0
            mp_img = mpimg.imread("Untitled.png")

            fig =plt.figure()
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

 # food pics
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        title = "Food Recommender App"

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
        thread1 = threading.Thread(target=self.eyetracker)# so that the ui display first then scan the eyes
        # thread42 = threading.Thread(target=self.aa)# so that the ui display first then scan the eyes

        thread1.start()
        thread1.join()
        self.hide()
        # thread42.start()


    def ui(self):
        self.image=QLabel()
        global imagechooser

        # imagechooser = "imagechooser%d" % (random.randint(1, 3))
        imagechooser = "imagechooser1"

        with open('imagechooser.txt','w') as out:
            line1 = imagechooser
            out.write(line1)
        if imagechooser =="imagechooser1":
            print("1")
            self.image.setStyleSheet("border-image: url(foodmenu1.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser2":
            print("2")
            self.image.setStyleSheet("border-image: url(foodmenu2.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser3":
            print("3")
            self.image.setStyleSheet("border-image: url(foodmenu3.png);")
            self.layoutGrid.addWidget(self.image)
        else:
            print("Error")


    def eyetracker(self):
            global most_looked
            import time
            time.sleep(2)
            self.gaze = []
            self.Cord = []
            self.xCord =[]
            self.yCord =[]
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
            with open('target.txt','w') as out:
                line1 = self.xCord
                line2 = self.yCord
                out.write('{}\n{}'.format(line1,line2))
            if imagechooser == 'imagechooser1':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                chickenrice = 0
                laksa = 0
                charkwayteow = 0
                chillicrab = 0
                fishsoup = 0
                fishnchip = 0
                mixedrice = 0
                bento = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                        chickenrice += 1

                    elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                        laksa += 1

                    elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                        charkwayteow += 1

                    elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                        chillicrab += 1

                    elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                        fishsoup += 1

                    elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                        fishnchip += 1

                    elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                        mixedrice += 1

                    elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                        bento += 1

                rank.append(chickenrice)
                rank.append(laksa)
                rank.append(charkwayteow)
                rank.append(chillicrab)
                rank.append(fishsoup)
                rank.append(fishnchip)
                rank.append(mixedrice)
                rank.append(bento)

                if max(rank) == rank[0]:
                    most_looked = 'hainanese chicken rice'
                elif max(rank) == rank[1]:
                    most_looked = 'laksa'
                elif max(rank) == rank[2]:
                    most_looked = 'Char Kway Teow'
                elif max(rank) == rank[3]:
                    most_looked = 'Chili Crab'
                elif max(rank) == rank[4]:
                    most_looked = 'Sliced Fish Soup'
                elif max(rank) == rank[5]:
                    most_looked = 'Fish and Chips'
                elif max(rank) == rank[6]:
                    most_looked = 'Chinese Economy Rice'
                elif max(rank) == rank[7]:
                    most_looked = 'Japanese Bento'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser2':
                rank = []
                most_looked = ''
                fishheadcurry = 0
                currylaksa = 0
                duckrice = 0
                yusheng = 0
                bakkuhteh = 0
                hokkienmee = 0
                kwaychap = 0
                rotiprata = 0

                """
    
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                        fishheadcurry += 1

                    elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                        currylaksa += 1

                    elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                        duckrice += 1

                    elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                        yusheng += 1

                    elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                        bakkuhteh += 1

                    elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                        hokkienmee += 1

                    elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                        kwaychap += 1

                    elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                        rotiprata += 1

                rank.append(fishheadcurry)
                rank.append(currylaksa)
                rank.append(duckrice)
                rank.append(yusheng)
                rank.append(bakkuhteh)
                rank.append(hokkienmee)
                rank.append(kwaychap)
                rank.append(rotiprata)

                if max(rank) == rank[0]:
                    most_looked = 'Fish Head Curry'
                elif max(rank) == rank[1]:
                    most_looked = 'Curry laksa'
                elif max(rank) == rank[2]:
                    most_looked = 'Duck Rice'
                elif max(rank) == rank[3]:
                    most_looked = 'Yu Sheng'
                elif max(rank) == rank[4]:
                    most_looked = 'Bak Kut Teh'
                elif max(rank) == rank[5]:
                    most_looked = 'Hokkien Mee'
                elif max(rank) == rank[6]:
                    most_looked = 'Kway Chap'
                elif max(rank) == rank[7]:
                    most_looked = 'Roti Prata'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser3':

                rank = []
                most_looked = ''
                beefkwayteow = 0
                blackpeppercrab = 0
                cerealprawn = 0
                rotijohn = 0
                katonglaksa = 0
                sambalstingray = 0
                crabbeehoonsoup = 0
                satay = 0
                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.2 <= i[1] <= 0.6:
                        beefkwayteow += 1

                    elif 0.28 <= i[0] <= 0.52 and 0.2 <= i[1] <= 0.6:
                        blackpeppercrab += 1

                    elif 0.52 <= i[0] <= 0.74 and 0.2 <= i[1] <= 0.6:
                        cerealprawn += 1

                    elif 0.74 <= i[0] <= 1 and 0.2 <= i[1] <= 0.6:
                        rotijohn += 1

                    elif 0 <= i[0] <= 0.28 and 0.63 <= i[1] <= 1:
                        katonglaksa += 1

                    elif 0.28 <= i[0] <= 0.52 and 0.63 <= i[1] <= 1:
                        sambalstingray += 1

                    elif 0.52 <= i[0] <= 0.74 and 0.63 <= i[1] <= 1:
                        crabbeehoonsoup += 1
                    elif 0.74 <= i[0] <= 1 and 0.63 <= i[1] <= 1:
                        satay += 1

                rank.append(beefkwayteow)
                rank.append(blackpeppercrab)
                rank.append(cerealprawn)
                rank.append(rotijohn)
                rank.append(katonglaksa)
                rank.append(sambalstingray)
                rank.append(crabbeehoonsoup)
                rank.append(satay)

                if max(rank) == rank[0]:
                    most_looked = 'Beef Kway Teow'
                elif max(rank) == rank[1]:
                    most_looked = 'Black Pepper Crab'
                elif max(rank) == rank[2]:
                    most_looked = 'Cereal Prawn'
                elif max(rank) == rank[3]:
                    most_looked = 'Roti John'
                elif max(rank) == rank[4]:
                    most_looked = 'Katong laksa'
                elif max(rank) == rank[5]:
                    most_looked = 'Sambal Stingray'
                elif max(rank) == rank[6]:
                    most_looked = 'Crab Bee Hoon Soup'
                elif max(rank) == rank[7]:
                    most_looked = 'Satay'
                else:
                    print("Smth went very wrong")
            print("Most looked dish: ", most_looked)
            print("mostlooked type:", type(most_looked))
            with open('mostlooked.txt','w') as out:
                line1 = most_looked
                out.write(line1)

    def plot(self):
        def xcord():
            with open('cords.txt', 'r') as f:
                content_list = [line.rstrip('\n') for line in f]
                ok1= content_list[0]
                print(type(ok1))
                ok2=eval(ok1)
                x=list(ok2)
                print(type(x))
            return x
        def ycord():
            with open('cords.txt', 'r') as f:
                last_line = f.readlines()[-1]
                ycord=last_line
            x=eval(ycord)
            y=list(x)
            print(type(y))
            return y
        x=xcord()
        y=ycord()
        print("x",x)
        print("y",y)

        counter = 0
        mp_img = mpimg.imread("Untitled.png")

        fig =plt.figure()
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
        title = "Food Recommender App"

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
                ok1= content_list[0]
                print(type(ok1))
                ok2=eval(ok1)
                x=list(ok2)
                print(type(x))
            return x
        def ycord():
            with open('target.txt', 'r') as f:
                last_line = f.readlines()[-1]
                ycord=last_line
            x=eval(ycord)
            y=list(x)
            print(type(y))
            return y

        x=xcord()
        y=ycord()
        print("x",x)
        print("y",y)

        counter = 0
        def getimagechooser():
            with open('imagechooser.txt', 'r') as f:
                last_line = f.readlines()[-1]
            return last_line
        image=getimagechooser()
        if image=="imagechooser1":
            mp_img = mpimg.imread("foodmenu1.png")
        elif image=="imagechooser2":
            mp_img = mpimg.imread("foodmenu2.png")
        elif image=="imagechooser3":
            mp_img = mpimg.imread("foodmenu3.png")


        fig =plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])

        test = sb.kdeplot(x, y, shade=True, cmap="Reds", alpha=0.7)
        test.collections[0].set_alpha(0)
        plt.imshow(mp_img, zorder=0, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
        ax.invert_yaxis()
        plt.axis('off')
        canvas = FigureCanvas(fig)
        canvas.draw()
        self.layoutGrid.addWidget(canvas)

class foodwindow(QWidget):

    def __init__(self):
        super().__init__()
        global most_looked
        title = "Food Recommender App"

        # set the title
        self.setWindowTitle(title)
        # self.setStyleSheet()
        self.setStyleSheet("background-color: #EADDCC;")

        self.horizontalGroupBox = QGroupBox("Grid")
        def get_age():
            with open('combined.txt', 'r') as f:
                last_line = f.readlines()[-1]
            splitted= last_line.split(",")
            age=splitted[0]

            return age


        def get_gender():
            with open('combined.txt', 'r') as f:
                last_line = f.readlines()[-1]
                q=last_line.strip('\n')

            splitted= q.split(",")

            gender=splitted[1]
            return gender

        def get_mostlooked():
            with open('mostlooked.txt', 'r') as f:
                last_line = f.readlines()[-1]
                q=last_line.strip('\n')

            return q

        most_looked=get_mostlooked()
        age=get_age()
        gender=get_gender()
        print(age)
        print(gender)
        print(get_mostlooked())
        print("age: ",get_age())
        print("gender: ",get_gender())
        recommendations = CollaborativeRecomender1.recommend(get_gender(), age, most_looked,CollaborativeRecomender1.sim_mat_dic, 5)
        print("here is the recommendations: " ,recommendations)
        values = recommendations

        food=[]
        for i in values:
            food.append(i)
        imgList = []
        print(food)
        df1 = pd.read_csv('food_updated.csv', encoding='mac_roman')

        location=[]
            # Storing img paths to match the recommendations, locations, and ratings
        for dish in food:
            for x in range(len(df1['name'])):
                if df1['name'][x] == dish:
                    imgFile = "images/" + dish + ".png"
                    print('imgfile=',imgFile)

                    imgList.append("images/" + dish + ".png")
                    # self.rating.append(df1['rating'][x])
                    locate=(df1['location'][x])
                    location.append(locate)
        print(location)


        print("Image List = ", imgList)

        positions = [(r, c) for r in range(4) for c in range(5)]

        layoutGrid = QGridLayout()

        self.setLayout(layoutGrid)
        # layoutGrid.setVerticalSpacing(50)
        layoutGrid.setHorizontalSpacing(50)
        # layoutGrid.setColumnMinimumWidth(80,50)
        layoutGrid.setContentsMargins(50, 50, 50, 50)
        self.setFixedHeight(800)
        self.setMinimumWidth(1800)

        tittle=QLabel("Your Recommendations")
        tittle.setFont(QFont('Times New Roman', 27))
        tittle.setFixedHeight(75)
        tittle.setAlignment(Qt.AlignHCenter)
        tittle.setStyleSheet("color: #6C756F;border-bottom: 1px solid white; padding-bottom:15px; border-bottom-width: 10px;")
        # tittle.setFont(QFont('Times', 11))
        layoutGrid.addWidget(tittle,0,0,1,0)
        foodchoice=QLabel("You've picked: ")

        foodchoice1=QPushButton(most_looked)
        maps={"hainanese chicken rice":"https://goo.gl/maps/ExXRoVutPEc9zbut5",
              "laksa":"https://goo.gl/maps/jCfuXr7goptAcK5G8",
              "Char Kway Teow":"https://goo.gl/maps/tgT3Kw1LHAEuBYBHA",
              "Chili Crab":"https://goo.gl/maps/jnGPwEqoR5HhZFmA7",
              "Sliced Fish Soup":"https://goo.gl/maps/BYucH36RLoyDuWjB8",
              "Fish and Chips":"https://goo.gl/maps/5idvXsawPfgvyHVT7",
              "Chinese Economy Rice":"https://goo.gl/maps/FiTjsPxM4YFPgV9N6",
              "Japanese Bento":"https://goo.gl/maps/iyN4RxfT8Zm9Pk2w5",
              "Fish Head Curry":"https://goo.gl/maps/pSVuLEgyo2kV2wsW9",
              "Curry laksa":"https://goo.gl/maps/qN82sqgivL6RJ9R46",
              "Duck Rice":"https://goo.gl/maps/TDRW9jfAueS98KK89",
              "Yu Sheng":"https://goo.gl/maps/mdo6r6tH43QQQsvu8",
              "Bak Kut Teh":"https://goo.gl/maps/tW5MHvyoGKzRWErh6",
              "Hokkien Mee":"https://goo.gl/maps/T4s9rHef1PUEX5EZ8",
              "Kway Chap":"https://goo.gl/maps/bpB8qaRjyw4yc7L69",
              "Roti Prata":"https://goo.gl/maps/Ln5YwpgBj437YwCi6",
              "Beef Kway Teow":"https://goo.gl/maps/NmbpDSMoceWpEBsJ7",
              "Black Pepper Crab":"https://goo.gl/maps/zmz3d8pRMTdoYRgX7",
              "Cereal Prawn":"https://goo.gl/maps/5kbbE9jXo3eywhpj6",
              "Roti John":"https://goo.gl/maps/SCPvAPP1b2y6y1vTA'",
              "Katong laksa":"https://goo.gl/maps/qnWdHpzi367mxBUJ8",
              "Sambal Stingray":"https://goo.gl/maps/HguvMDEmbVzR43MJA",
              "Crab Bee Hoon Soup":"https://goo.gl/maps/rjkAmbqjhh44D2XF9",
              "Satay":"https://goo.gl/maps/GuqqRajMceVUU4tU9"

              }
        foodchoice.setStyleSheet("color: #878280; margin-left:300px; border:0px solid black;")
        foodchoice1.clicked.connect(lambda: webbrowser.open(maps[most_looked]))
        foodchoice1.setCursor(QCursor(Qt.PointingHandCursor))
        foodchoice1.setFixedHeight(50)
        foodchoice1.setStyleSheet("color: #DB8012; border:0px solid black;margin-right:400px; margin-left:120px; text-align:left; font-weight:bold;text-decoration: underline;")
        # foodchoice.setAlignment(Qt.AlignHCenter)
        foodchoice.setFont(QFont('Times', 11))
        foodchoice1.setFont(QFont("Times",12))
        foodchoice2=QLabel("(Click to Find Out More!)")
        foodchoice2.setAlignment(Qt.AlignHCenter)
        foodchoice2.setFixedHeight(60)
        foodchoice2.setStyleSheet("color: #9D8978; border:0px solid black; background-color: none;padding-bottom: 15px; margin-right:10px;")

        # foodchoice.setAlignment(Qt.AlignHCenter)
        foodchoice.setFont(QFont('Times', 12))
        foodchoice2.setFont(QFont('Arial', 11))
        layoutGrid.addWidget(foodchoice ,1,1,1,2)
        layoutGrid.addWidget(foodchoice1,1,2,1,3)
        layoutGrid.addWidget(foodchoice2,2,0,1,0,)
        # layoutGrid.addWidget(foodchoice1,1,0,1,0)
        # layoutGrid.addWidget(foodchoice1,1,0,1,1)

        a=positions[15:]

        for a, value in zip(a, food):

            print(value)
            button = QGroupBox()
            button.setStyleSheet("border:none;")
            button.setFixedHeight(400)
            # button.setTitle("Hello")
            # button.setAlignment(Qt.AlignHCenter)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layoutGrid.addWidget(button, *a)
            vbox = QVBoxLayout()
            button.setLayout(vbox)
            foodname=QLabel(value)
            foodname.setAlignment(Qt.AlignHCenter)
            foodname.setWordWrap(True)
            foodname.setFixedHeight(10)
            # foodname.setStyleSheet("background-color: blue;")
            foodname.setFont(QFont('Times', 12))
            foodname.setStyleSheet("color: #6C756F;  padding :10px; font-weight: bold;")
            foodname.setToolTip('<font color="red" >Click on the <b>Image</b> to view the location</font>')

            # foodname.setStyleSheet("font-size: 24px;")

            foodname.setMaximumHeight(50)
            vbox.addWidget(foodname)
            vbox.setSpacing(0)

            images=QPushButton()
            # pixmap = QPixmap('images/Bak Kut Teh.png')
            # pixmap.scaledToHeight(images)

            # adding image to label
            # images.setPixmap(pixmap)
            images.setGeometry(100, 150, 100, 40)
            if value =="laksa":
                images.setStyleSheet("border-image : url(images/laksa.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/jCfuXr7goptAcK5G8'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Meixi's Kitchen ,  Ang Mo Kio Ave 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Chili Crab":
                images.setStyleSheet("border-image : url(images/Chili Crab.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/jnGPwEqoR5HhZFmA7'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Hai Zhong Bao Live Seafood ,Ang Mo Kio Ave 3, #01-2508 Block 422")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Char Kway Teow":
                images.setStyleSheet("border-image : url(images/Char Kway Teow.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/tgT3Kw1LHAEuBYBHA'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel(" Porridge Stall,Block 505 Ang Mo Kio Ave 8")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="hainanese chicken rice":
                images.setStyleSheet("border-image : url(images/hainanese chicken rice.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/ExXRoVutPEc9zbut5'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("#01-2843 Blk 925 Yishun Hainanese Chicken Rice@ AMK722")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Sliced Fish Soup":
                images.setStyleSheet("border-image : url(images/Sliced Fish Soup.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/BYucH36RLoyDuWjB8'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Yun Fishhead Steamboat, Block 632 HDB Ang Mo Kio AVE 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Fish and Chips":
                images.setStyleSheet("border-image : url(images/Fish and Chips.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/5idvXsawPfgvyHVT7'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Happy Hawkers,Blk 531 Ang Mo Kio Ave 10, #01-2429")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Chinese Economy Rice":
                images.setStyleSheet("border-image : url(images/Chinese Economy Rice.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/FiTjsPxM4YFPgV9N6'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Foy Yin Vegetarian Food,  Ang Mo Kio Ave 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Japanese Bento":
                images.setStyleSheet("border-image : url(images/Japanese Bento.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/iyN4RxfT8Zm9Pk2w5'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Casuarina Road, Tamako Meal, Casuarina Rd")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Curry laksa":
                images.setStyleSheet("border-image : url(images/Curry laksa.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/qN82sqgivL6RJ9R46'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Nonya Curry Mixed Veg Rice,  Ang Mo Kio Ave 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Yu Sheng":
                images.setStyleSheet("border-image : url(images/Yu Sheng.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/mdo6r6tH43QQQsvu8'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Shen Ji Tong Guo Chuan, Ang Mo Kio Ave 6, #01-05")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Duck Rice":
                images.setStyleSheet("border-image : url(images/Duck Rice.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/TDRW9jfAueS98KK89'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Roasted Delight, Ang Mo Kio Ave 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Fish Head Curry":
                images.setStyleSheet("border-image : url(images/Fish Head Curry.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/pSVuLEgyo2kV2wsW9'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Yun Fishhead Steamboat, Block 632 HDB Ang Mo Kio AVE 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Bak Kut Teh":
                images.setStyleSheet("border-image : url(images/Bak Kut Teh.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/tW5MHvyoGKzRWErh6'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Li Yuan Herbal Bak Kut Teh, Ang Mo Kio Ave 8")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Hokkien Mee":
                images.setStyleSheet("border-image : url(images/Hokkien Mee.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/T4s9rHef1PUEX5EZ8'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Fried Hokkien Prawn Noodles, Ang Mo Kio Ave 6, #01-41")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Kway Chap":
                images.setStyleSheet("border-image : url(images/Kway Chap.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/bpB8qaRjyw4yc7L69'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Ying Yi Kway Chap Braised Duck,#01-145, Ang Mo Kio Ave 10")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Roti Prata":
                images.setStyleSheet("border-image : url(images/Roti Prata.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/Ln5YwpgBj437YwCi6'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Prata Raya Singapore, AMK Hub No.53, #01-38")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Black Pepper Crab":
                images.setStyleSheet("border-image : url(images/Black Pepper Crab.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/zmz3d8pRMTdoYRgX7'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Yun Fishhead Steamboat, Block 632 HDB Ang Mo Kio AVE 4")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Roti John":
                images.setStyleSheet("border-image : url(images/Roti John.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/SCPvAPP1b2y6y1vTA'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Kensington Park Road Eating House,1 Kensington Park Rd")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Cereal Prawn":
                images.setStyleSheet("border-image : url(images/Cereal Prawn.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/5kbbE9jXo3eywhpj6'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Chui Xiang Kitchen,126 Casuarina Rd")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Beef Kway Teow":
                images.setStyleSheet("border-image : url(images/Beef Kway Teow.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/NmbpDSMoceWpEBsJ7'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("AMK Char Kway Teow, Ang Mo Kio Ave 6, #01-28")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Katong laksa":
                images.setStyleSheet("border-image : url(images/Katong laksa.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/qnWdHpzi367mxBUJ8'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Khoon's Katong Laksa & Seafood Soup, Upper Thomson Rd, #01-26")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Sambal Stingray":
                images.setStyleSheet("border-image : url(images/Sambal Stingray.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/HguvMDEmbVzR43MJA'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Lucy BBQ Seafood,20 Kensington Park Rd")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Crab Bee Hoon Soup":
                images.setStyleSheet("border-image : url(images/Crab Bee Hoon Soup.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/rjkAmbqjhh44D2XF9'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("Mellben Seafood,232 Ang Mo Kio Avenue 3,#01-1222")
                location.setWordWrap(True)
                vbox.addWidget(location)
            elif value=="Satay":
                images.setStyleSheet("border-image : url(images/Satay.png);")
                images.clicked.connect(lambda: webbrowser.open('https://goo.gl/maps/GuqqRajMceVUU4tU9'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
                location=QLabel("The Satay Taste,528 Ang Mo Kio Ave 10, #01-116")
                location.setWordWrap(True)
                vbox.addWidget(location)

            images.setFixedHeight(300)
            location.setFixedHeight(55)
            location.setAlignment(Qt.AlignHCenter)
            location.setStyleSheet("color: #6C756F;background-color: #FFECD4 ; padding: 10px; opacity: 0.3;")



        backbutton=QPushButton("Quit" )
        backbutton.setCursor(QCursor(Qt.PointingHandCursor))
        backbutton.clicked.connect(self.comeout)
        backbutton.setStyleSheet("background-color: white")

        layoutGrid.addWidget(backbutton,4, 2, 1, 1)
        # foodchoice=QLabel("You've picked")
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
            buttons=QMessageBox.No | QMessageBox.Yes ,
            defaultButton=QMessageBox.No,)

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
#main window stylesheet
stylesheet = """
    MainWindow {
        border-image: url("mainimage11.jpg");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)     # <---
    window = MainWindow()
    window.resize(640, 640)
    window.show()
    sys.exit(app.exec_())



#this is the working one , some changes has been done in sprint 4 to make it better
