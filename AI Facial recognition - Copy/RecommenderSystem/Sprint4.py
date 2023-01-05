import threading
import webbrowser
import random

from PyQt5.QtGui import QPixmap, QFont, QCursor

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QGroupBox, QLabel, \
    QFormLayout, QLineEdit, QVBoxLayout, QRadioButton, QMainWindow, QHBoxLayout

import tobii_research as tr

from past.builtins import execfile

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtWidgets import *


from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QGroupBox, QLabel, \
    QFormLayout, QLineEdit, QVBoxLayout, QRadioButton
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import Qt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sb

most_looked = ''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        #buttonstyle
        self.pushButton1.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : #0E4557;"
                                       "color: white;"
                            
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
        lay.setContentsMargins(550,50,550,0)
        lay.addWidget(self.pushButton1)
        lay.addWidget(self.pushButton2)
        lay.setSpacing(30)

    def show_new_window(self, checked):
        execfile("face_gender.py")
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



 # food pics
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)
        # self.layoutGrid.setVerticalSpacing(50)
        # self.layoutGrid.setHorizontalSpacing(50)
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

        imagechooser = "imagechooser%d" % (random.randint(1, 6))
        # imagechooser = "imagechooser1"
        print(imagechooser)
        with open('courseimagechooser.txt','w') as out:
            line1 = imagechooser
            out.write(line1)
        if imagechooser =="imagechooser1":
            print("1")
            self.image.setStyleSheet("border-image: url(catalogue1.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser2":
            print("2")
            self.image.setStyleSheet("border-image: url(catalogue2.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser3":
            print("3")
            self.image.setStyleSheet("border-image: url(catalogue3.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser4":
            print("4")
            self.image.setStyleSheet("border-image: url(catalogue4.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser5":
            print("5")
            self.image.setStyleSheet("border-image: url(catalogue5.png);")
            self.layoutGrid.addWidget(self.image)
        elif imagechooser=="imagechooser6":
            print("6")
            self.image.setStyleSheet("border-image: url(catalogue6.png);")
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
            with open('coursetarget.txt','w') as out:
                line1 = self.xCord
                line2 = self.yCord
                out.write('{}\n{}'.format(line1,line2))

            if imagechooser == 'imagechooser1':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                informationtechnology = 0
                foodnbeveragebusiness = 0
                motiongraphicsdesign = 0
                foodsciencennutrition = 0
                experientialproductninteriordesign = 0
                appliedchemistry = 0
                businessmanagement = 0
                infocommnsecurity = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.13 <= i[1] <= 0.525:
                        informationtechnology += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.13 <= i[1] <= 0.525:
                        foodnbeveragebusiness += 1

                    elif 0.515<= i[0] <= 0.74 and 0.13 <= i[1] <= 0.525:
                        motiongraphicsdesign += 1

                    elif 0.74 <= i[0] <= 1 and 0.13 <= i[1] <= 0.525:
                        foodsciencennutrition += 1

                    elif 0 <= i[0] <= 0.28 and 0.575 <= i[1] <= 1:
                        experientialproductninteriordesign += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.575 <= i[1] <= 1:
                        appliedchemistry += 1

                    elif 0.515<= i[0] <= 0.74 and 0.575 <= i[1] <= 1:
                        businessmanagement += 1

                    elif 0.74 <= i[0] <= 1 and 0.575 <= i[1] <= 1:
                        infocommnsecurity += 1

                rank.append(informationtechnology)
                rank.append(foodnbeveragebusiness)
                rank.append(motiongraphicsdesign)
                rank.append(foodsciencennutrition)
                rank.append(experientialproductninteriordesign)
                rank.append(appliedchemistry)
                rank.append(businessmanagement)
                rank.append(infocommnsecurity)

                if max(rank) == rank[0]:
                    most_looked = 'Information Technology (SIT)'
                elif max(rank) == rank[1]:
                    most_looked = 'Food & Beverage Business (SBM)'
                elif max(rank) == rank[2]:
                    most_looked = 'Motion Graphics Design (SDM)'
                elif max(rank) == rank[3]:
                    most_looked = 'Food Science & Nutrition (SAS)'
                elif max(rank) == rank[4]:
                    most_looked = 'Experiential Product & Interior Design (SDM)'
                elif max(rank) == rank[5]:
                    most_looked = 'Applied Chemistry (SAS)'
                elif max(rank) == rank[6]:
                    most_looked = 'Business Management (SBM)'
                elif max(rank) == rank[7]:
                    most_looked = 'Infocomm & Security (SIT)'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser2':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                digitalgameartndesign = 0
                biomedicalengineering = 0
                massmediamanagement = 0
                socialwork = 0
                aindataengineering = 0
                accountancynfinance = 0
                pharmaceuticalscience = 0
                commonictprogramme = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.13 <= i[1] <= 0.525:
                        digitalgameartndesign += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.13 <= i[1] <= 0.525:
                        biomedicalengineering += 1

                    elif 0.515<= i[0] <= 0.74 and 0.13 <= i[1] <= 0.525:
                        massmediamanagement += 1

                    elif 0.74 <= i[0] <= 1 and 0.13 <= i[1] <= 0.525:
                        socialwork += 1

                    elif 0 <= i[0] <= 0.28 and 0.575 <= i[1] <= 1:
                        aindataengineering += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.575 <= i[1] <= 1:
                        accountancynfinance += 1

                    elif 0.515<= i[0] <= 0.74 and 0.575 <= i[1] <= 1:
                        pharmaceuticalscience += 1

                    elif 0.74 <= i[0] <= 1 and 0.575 <= i[1] <= 1:
                        commonictprogramme += 1

                rank.append(digitalgameartndesign)
                rank.append(biomedicalengineering)
                rank.append(massmediamanagement)
                rank.append(socialwork)
                rank.append(aindataengineering)
                rank.append(accountancynfinance)
                rank.append(pharmaceuticalscience)
                rank.append(commonictprogramme)

                if max(rank) == rank[0]:
                    most_looked = 'Digital Game Art & Design (SDM)'
                elif max(rank) == rank[1]:
                    most_looked = 'Biomedical Engineering (SEG)'
                elif max(rank) == rank[2]:
                    most_looked = 'Mass Media Management (SBM)'
                elif max(rank) == rank[3]:
                    most_looked = 'Social Work (SHSS)'
                elif max(rank) == rank[4]:
                    most_looked = 'AI & Data Engineering (SEG)'
                elif max(rank) == rank[5]:
                    most_looked = 'Accountancy & Finance (SBM)'
                elif max(rank) == rank[6]:
                    most_looked = 'Pharmaceutical Science (SAS)'
                elif max(rank) == rank[7]:
                    most_looked = 'Common ICT Programme (SIT)'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser3':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                oralhealththerapy = 0
                animationnvisualeffects = 0
                commonbusinessprogramme = 0
                cybersecurityndigitalforensics = 0
                biologicsnprocesstechnology = 0
                businessintelligencenanalytics = 0
                aeronauticalnaerospacetechnology = 0
                gamedevelopmentntechnology = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.13 <= i[1] <= 0.525:
                        oralhealththerapy += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.13 <= i[1] <= 0.525:
                        animationnvisualeffects += 1

                    elif 0.515<= i[0] <= 0.74 and 0.13 <= i[1] <= 0.525:
                        commonbusinessprogramme += 1

                    elif 0.74 <= i[0] <= 1 and 0.13 <= i[1] <= 0.525:
                        cybersecurityndigitalforensics += 1

                    elif 0 <= i[0] <= 0.28 and 0.575 <= i[1] <= 1:
                        biologicsnprocesstechnology += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.575 <= i[1] <= 1:
                        businessintelligencenanalytics += 1

                    elif 0.515<= i[0] <= 0.74 and 0.575 <= i[1] <= 1:
                        aeronauticalnaerospacetechnology += 1

                    elif 0.74 <= i[0] <= 1 and 0.575 <= i[1] <= 1:
                        gamedevelopmentntechnology += 1

                rank.append(oralhealththerapy)
                rank.append(animationnvisualeffects)
                rank.append(commonbusinessprogramme)
                rank.append(cybersecurityndigitalforensics)
                rank.append(biologicsnprocesstechnology)
                rank.append(businessintelligencenanalytics)
                rank.append(aeronauticalnaerospacetechnology)
                rank.append(gamedevelopmentntechnology)

                if max(rank) == rank[0]:
                    most_looked = 'Oral Health Therapy (SHSS)'
                elif max(rank) == rank[1]:
                    most_looked = 'Animation & Visual Effects (SDM)'
                elif max(rank) == rank[2]:
                    most_looked = 'Common Business Programme (SBM)'
                elif max(rank) == rank[3]:
                    most_looked = 'Cybersecurity  & Digital Forensics (SIT)'
                elif max(rank) == rank[4]:
                    most_looked = 'Biologics & Process Technology (SAS)'
                elif max(rank) == rank[5]:
                    most_looked = 'Business Intelligence & Analytics (SIT)'
                elif max(rank) == rank[6]:
                    most_looked = 'Aeronautical & Aerospace Technology (SEG)'
                elif max(rank) == rank[7]:
                    most_looked = 'Game Development & Technology (SDM)'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser4':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                bankingnfinance = 0
                visualcommunication = 0
                nursing = 0
                commonengineeringprogramme = 0
                businessnfinancialtechnology = 0
                chemicalnpharmaceuticaltechnology = 0
                nantotechnologynmaterialsscience = 0
                aerospacesystemsnmanagement = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.13 <= i[1] <= 0.525:
                        bankingnfinance += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.13 <= i[1] <= 0.525:
                        visualcommunication += 1

                    elif 0.515<= i[0] <= 0.74 and 0.13 <= i[1] <= 0.525:
                        nursing += 1

                    elif 0.74 <= i[0] <= 1 and 0.13 <= i[1] <= 0.525:
                        commonengineeringprogramme += 1

                    elif 0 <= i[0] <= 0.28 and 0.575 <= i[1] <= 1:
                        businessnfinancialtechnology += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.575 <= i[1] <= 1:
                        chemicalnpharmaceuticaltechnology += 1

                    elif 0.515<= i[0] <= 0.74 and 0.575 <= i[1] <= 1:
                        nantotechnologynmaterialsscience += 1

                    elif 0.74 <= i[0] <= 1 and 0.575 <= i[1] <= 1:
                        aerospacesystemsnmanagement += 1

                rank.append(bankingnfinance)
                rank.append(visualcommunication)
                rank.append(nursing)
                rank.append(commonengineeringprogramme)
                rank.append(businessnfinancialtechnology)
                rank.append(chemicalnpharmaceuticaltechnology)
                rank.append(nantotechnologynmaterialsscience)
                rank.append(aerospacesystemsnmanagement)

                if max(rank) == rank[0]:
                    most_looked = 'Banking & Finance (SBM)'
                elif max(rank) == rank[1]:
                    most_looked = 'Visual Communication (SDM)'
                elif max(rank) == rank[2]:
                    most_looked = 'Nursing (SHSS)'
                elif max(rank) == rank[3]:
                    most_looked = 'Common Engineering Programme (SEG)'
                elif max(rank) == rank[4]:
                    most_looked = 'Business & Financial Technology (SIT)'
                elif max(rank) == rank[5]:
                    most_looked = 'Chemical & Pharmaceutical Technology (SAS)'
                elif max(rank) == rank[6]:
                    most_looked = 'Nanotechnology & Materials Science (SEG)'
                elif max(rank) == rank[7]:
                    most_looked = 'Aerospace Systems & Management (SEG)'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser5':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                sportsnwellness = 0
                architecture = 0
                interactiondesign = 0
                engineeringwithbusiness = 0
                hospitalityntoursimmanagement = 0
                infocommnmediaengineering = 0
                electronicncomputerengineering = 0
                advancedndigtialmanufacturing = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.13 <= i[1] <= 0.525:
                        sportsnwellness += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.13 <= i[1] <= 0.525:
                        architecture += 1

                    elif 0.515<= i[0] <= 0.74 and 0.13 <= i[1] <= 0.525:
                        interactiondesign += 1

                    elif 0.74 <= i[0] <= 1 and 0.13 <= i[1] <= 0.525:
                        engineeringwithbusiness += 1

                    elif 0 <= i[0] <= 0.28 and 0.575 <= i[1] <= 1:
                        hospitalityntoursimmanagement += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.575 <= i[1] <= 1:
                        infocommnmediaengineering += 1

                    elif 0.515<= i[0] <= 0.74 and 0.575 <= i[1] <= 1:
                        electronicncomputerengineering += 1

                    elif 0.74 <= i[0] <= 1 and 0.575 <= i[1] <= 1:
                        advancedndigtialmanufacturing += 1

                rank.append(sportsnwellness)
                rank.append(architecture)
                rank.append(interactiondesign)
                rank.append(engineeringwithbusiness)
                rank.append(hospitalityntoursimmanagement)
                rank.append(infocommnmediaengineering)
                rank.append(electronicncomputerengineering)
                rank.append(advancedndigtialmanufacturing)

                if max(rank) == rank[0]:
                    most_looked = 'Sport & Wellness Management (SBM)'
                elif max(rank) == rank[1]:
                    most_looked = 'Architecture  (SDM)'
                elif max(rank) == rank[2]:
                    most_looked = 'Interaction Design (SDM)'
                elif max(rank) == rank[3]:
                    most_looked = 'Engineering with Business (SEG)'
                elif max(rank) == rank[4]:
                    most_looked = 'Hospitality & Tourism Management (SBM)'
                elif max(rank) == rank[5]:
                    most_looked = 'Infocomm & Media Engineering (SEG)'
                elif max(rank) == rank[6]:
                    most_looked = 'Electronic & Computer Engineering (SEG)'
                elif max(rank) == rank[7]:
                    most_looked = 'Advanced & Digital Manufacturing (SEG)'
                else:
                    print("Smth went very wrong")
            if imagechooser == 'imagechooser6':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                sportsnwellness = 0
                architecture = 0
                interactiondesign = 0
                robotics = 0
                hospitalityntoursimmanagement = 0
                infocommnmediaengineering = 0
                electronicncomputerengineering = 0
                advancedndigtialmanufacturing = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.28 and 0.13 <= i[1] <= 0.525:
                        sportsnwellness += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.13 <= i[1] <= 0.525:
                        architecture += 1

                    elif 0.515<= i[0] <= 0.74 and 0.13 <= i[1] <= 0.525:
                        interactiondesign += 1

                    elif 0.74 <= i[0] <= 1 and 0.13 <= i[1] <= 0.525:
                        robotics += 1

                    elif 0 <= i[0] <= 0.28 and 0.575 <= i[1] <= 1:
                        hospitalityntoursimmanagement += 1

                    elif 0.28 <= i[0] <= 0.515 and 0.575 <= i[1] <= 1:
                        infocommnmediaengineering += 1

                    elif 0.515<= i[0] <= 0.74 and 0.575 <= i[1] <= 1:
                        electronicncomputerengineering += 1

                    elif 0.74 <= i[0] <= 1 and 0.575 <= i[1] <= 1:
                        advancedndigtialmanufacturing += 1

                rank.append(sportsnwellness)
                rank.append(architecture)
                rank.append(interactiondesign)
                rank.append(robotics)
                rank.append(hospitalityntoursimmanagement)
                rank.append(infocommnmediaengineering)
                rank.append(electronicncomputerengineering)
                rank.append(advancedndigtialmanufacturing)

                if max(rank) == rank[0]:
                    most_looked = 'Sport & Wellness Management (SBM)'
                elif max(rank) == rank[1]:
                    most_looked = 'Architecture  (SDM)'
                elif max(rank) == rank[2]:
                    most_looked = 'Interaction Design (SDM)'
                elif max(rank) == rank[3]:
                    most_looked = 'Robotics & Mechatronics (SEG)'
                elif max(rank) == rank[4]:
                    most_looked = 'Hospitality & Tourism Management (SBM)'
                elif max(rank) == rank[5]:
                    most_looked = 'Infocomm & Media Engineering (SEG)'
                elif max(rank) == rank[6]:
                    most_looked = 'Electronic & Computer Engineering (SEG)'
                elif max(rank) == rank[7]:
                    most_looked = 'Advanced & Digital Manufacturing (SEG)'
                else:
                    print("Smth went very wrong")

            print("Most looked : ", most_looked)
            print("mostlooked type:", type(most_looked))
            with open('mostlookedcourses.txt','w') as out:
                line1 = most_looked
                out.write(line1)






class okk(QWidget):
    def __init__(self):
        super().__init__()
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
            with open('coursetarget.txt', 'r') as f:
                content_list = [line.rstrip('\n') for line in f]
                ok1= content_list[0]
                print(type(ok1))
                ok2=eval(ok1)
                x=list(ok2)
                print(type(x))
            return x
        def ycord():
            with open('coursetarget.txt', 'r') as f:
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
            with open('courseimagechooser.txt', 'r') as f:
                last_line = f.readlines()[-1]
            return last_line
        image=getimagechooser()
        if image=="imagechooser1":
            mp_img = mpimg.imread("catalogue1.png")
        elif image=="imagechooser2":
            mp_img = mpimg.imread("catalogue2.png")
        elif image=="imagechooser3":
            mp_img = mpimg.imread("catalogue3.png")
        elif image=="imagechooser4":
            mp_img = mpimg.imread("catalogue4.png")
        elif image=="imagechooser5":
            mp_img = mpimg.imread("catalogue5.png")
        elif image=="imagechooser6":
            mp_img = mpimg.imread("catalogue6.png")

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

import cfmodel_mahanttan as recommender

class foodwindow(QWidget):
    def __init__(self):
        super().__init__()
        global most_looked
        # self.setStyleSheet()
        self.setStyleSheet("background-color: #197796;")

        self.horizontalGroupBox = QGroupBox("Grid")



        def get_gender():
            with open('coursegender.txt', 'r') as f:
                last_line = f.readlines()[-1]
                q=last_line.strip('\n')
            return q

        def get_mostlooked():
            with open('mostlookedcourses.txt', 'r') as f:
                last_line = f.readlines()[-1]
                q=last_line.strip('\n')

            return q

        most_looked=get_mostlooked()
        gender=get_gender()
        print(gender)
        print(get_mostlooked())
        print("gender: ",get_gender())
        recommendations = recommender.recommend(get_gender(), most_looked,recommender.sim_mat_dic_m5, 5)
        print("here is the recommendations: " ,recommendations)
        values = recommendations

        food=[]
        for i in values:
            food.append(i)
        imgList = []
        print(food)

        print("Image List = ", imgList)

        positions = [(r, c) for r in range(3) for c in range(5)]
        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)
        layoutGrid.setVerticalSpacing(20)
        layoutGrid.setHorizontalSpacing(50)
        # layoutGrid.setColumnMinimumWidth(80,50)
        layoutGrid.setContentsMargins(50, 50, 50, 50)
        self.setFixedHeight(680)
        self.setMinimumWidth(1800)
        tittle=QLabel("Your Recommendations")
        tittle.setFont(QFont('Times New Roman', 25))
        tittle.setFixedHeight(60)
        tittle.setAlignment(Qt.AlignHCenter)
        tittle.setStyleSheet("color: white;")
        # tittle.setFont(QFont('Times', 11))
        layoutGrid.addWidget(tittle,0,0,1,0)
        foodchoice=QLabel("You've picked {}" .format(most_looked))
        foodchoice.setFixedHeight(50)

        foodchoice.setStyleSheet("color: white; border-top: 1px solid white; padding-top:10px; border-top-width: 10px; ")
        foodchoice.setAlignment(Qt.AlignHCenter)
        foodchoice.setFont(QFont('Times', 11))
        layoutGrid.addWidget(foodchoice,1,0,1,0)
        a=positions[10:]
        for a, value in zip(a, food):
            print(value)
            button = QGroupBox()
            button.setStyleSheet("border:none;")
            button.setFixedHeight(380)
            # button.setTitle("Hello")
            # button.setAlignment(Qt.AlignHCenter)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layoutGrid.addWidget(button, *a)
            vbox = QVBoxLayout()
            button.setLayout(vbox)
            foodname=QLabel(value)
            foodname.setWordWrap(True)
            foodname.setFixedHeight(30)
            # foodname.setStyleSheet(" border-radius: 15px 50px 0px 0px;")
            foodname.setAlignment(Qt.AlignCenter)

            # foodname.setStyleSheet("background-color: blue;")
            foodname.setFont(QFont('Arial', 10))
            foodname.setStyleSheet("background-color: lightblue; padding :10px;")
            foodname.setToolTip('<font color="red" >Click on the <b>Image</b> to learn more details about this course</font>')

            # foodname.setStyleSheet("font-size: 24px;")

            foodname.setMaximumHeight(80)
            vbox.addWidget(foodname)

            vbox.setSpacing(0)

            images=QPushButton()

            if value =="Business & Financial Technology (SIT)":
                images.setStyleSheet("border-image : url(nypcoursesimage/BusinessnFinancialTechnology.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SIT%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Information Technology (SIT)":
                images.setStyleSheet("border-image : url(nypcoursesimage/InformationTechnology.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SIT%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Infocomm & Security (SIT)":
                images.setStyleSheet("border-image : url(nypcoursesimage/InfocommnSecurity.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SIT%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Cybersecurity  & Digital Forensics (SIT)":
                images.setStyleSheet("border-image : url(nypcoursesimage/CybersecuritynDigitalForensics.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SIT%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Business Intelligence & Analytics (SIT)":
                images.setStyleSheet("border-image : url(nypcoursesimage/BusinessIntelligencenAnalytics.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SIT%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Common ICT Programme (SIT)":
                images.setStyleSheet("border-image : url(nypcoursesimage/CommonICTProgramme.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SIT%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)


            elif value=="Experiential Product & Interior Design (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/ExperientialProductnInteriorDesign.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Animation & Visual Effects (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AnimationnVisualEffects.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Architecture  (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/Architecture.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Interaction Design (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/InteractionDesign.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Digital Game Art & Design (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/DigitalGameArtnDesign.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Visual Communication (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/VisualCommunication.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Motion Graphics Design (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/MotionGraphicsDesign.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Game Development & Technology (SDM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/GameDevelopment nTechnology.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SDM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)


            elif value=="Applied Chemistry (SAS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AppliedChemistry.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SAS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Biologics & Process Technology (SAS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/BiologicsnProcessTechnology.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SAS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Chemical & Pharmaceutical Technology (SAS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/ChemicalnPharmaceuticalTechnology.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SAS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Food Science & Nutrition (SAS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/FoodSciencenNutrition.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SAS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Pharmaceutical Science (SAS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/PharmaceuticalScience.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SAS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)

            elif value=="Accountancy & Finance (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AccountancynFinance.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Banking & Finance (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/BankingnFinance.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Business Management (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/BusinessManagement.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Food & Beverage Business (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/FoodnBeverageBusiness.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Hospitality & Tourism Management (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/HospitalitynTourism Management.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Mass Media Management (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/MassMediaManagement.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Sport & Wellness Management (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/SportnWellnessManagement.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Common Business Programme (SBM)":
                images.setStyleSheet("border-image : url(nypcoursesimage/CommonBusinessProgramme.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SBM%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)


            elif value=="Advanced & Digital Manufacturing (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AdvancednDigitalManufacturing.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Aeronautical & Aerospace Technology (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AeronauticalAerospaceTechnology.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Aerospace Systems & Management (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AerospaceSystemsnManagement.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="AI & Data Engineering (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/AInDataEngineering.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Biomedical Engineering (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/BiomedicalEngineering.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Electronic & Computer Engineering (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/ElectronicnComputerEngineering.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Engineering with Business (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/EngineeringwithBusiness.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Infocomm & Media Engineering (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/InfocommnMediaEngineering.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Nanotechnology & Materials Science (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/NanotechnologynMaterialsScience.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Robotics & Mechatronics (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/RoboticsnMechatronics.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Common Engineering Programme (SEG)":
                images.setStyleSheet("border-image : url(nypcoursesimage/CommonEngineeringProgramme.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SEG%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)

            elif value=="Nursing (SHSS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/Nursing.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SHSS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Oral Health Therapy (SHSS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/OralHealthTherapy.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SHSS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            elif value=="Social Work (SHSS)":
                images.setStyleSheet("border-image : url(nypcoursesimage/SocialWork.png);")
                images.clicked.connect(lambda: webbrowser.open('https://www.nyp.edu.sg/content/dam/nyp/about-nyp/nyp-overview/media-room/publications/course-booklets/SHSS%20Course%20Booklet.pdf'))
                images.setCursor(QCursor(Qt.PointingHandCursor))
                images.setFixedHeight(300)
                vbox.addWidget(images)
                vbox.setContentsMargins(0,0,0,0)
            vbox.setSpacing(0)





        backbutton=QPushButton("Quit" )
        backbutton.clicked.connect(self.comeout)
        backbutton.setStyleSheet("background-color: white")
        # backbutton.setStyleSheet("QPushButton::hover" "{"  "background-color : orange;" "}")

        layoutGrid.addWidget(backbutton,3, 2, 1, 1)

        # foodchoice1=QLabel(most_looked)
        # foodchoice1.setAlignment(Qt.AlignLeft)
        # foodchoice1.setFont(QFont('Times', 11))
        # foodchoice.setAlignment(Qt.AlignHCenter)
        # layoutGrid.addWidget(foodchoice1)

    def comeout(self, checked):
         button = QMessageBox.critical(
            self,
            "Exiting Confirmation",
            "<font color =white>Are you sure you want to exit?</font>",
            buttons=QMessageBox.No | QMessageBox.Yes ,

            defaultButton=QMessageBox.No,)

         if button == QMessageBox.No:
            print("Rejected exit confirmation")
         elif button == QMessageBox.Yes:
            print("Back")
            self.close()



    # def main_menu(self, checked):
    #     self.a = MainWindow()
    #     self.a.show()
    #     self.close()


#main window stylesheet
stylesheet = """
    MainWindow {
        border-image: url("12.png");
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



#this is the sprint 4 working one
