import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QProgressBar, QLabel, QFrame, QMainWindow, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import os
import time


from PyQt5.QtCore import pyqtSignal, QThread
import threading

class Thread(QThread):
    progressChanged = pyqtSignal(int)
    def run(self):
        for i in range(100):
            QThread.msleep(100)
            self.progressChanged.emit(i)

# class Function:
#     def loading(self):
#         self.screen = SplashScreen()
#         self.screen.show()
#         self.thread = Thread()
#         self.thread.progressChanged.connect(
#             self.screen.progressBar.setValue)
#         self.thread.finished.connect(self.screen.close)
#         self.thread.start()
#
#     def facialrec2(self):
#         os.system('python Face_Gender_Latest_Travel.py')

class Function:
    def loading(self):
        self.screen = SplashScreen()
        self.screen.show()
        for i in range(80):
            self.screen.progressBar.setValue(i)
            QApplication.processEvents()
            time.sleep(0.05)
            # if i == 60:
            #     QApplication.processEvents()
            #     os.system('python Face_Gender_Latest_Travel.py')
            #     print("Running Facial Recognition here:")

            # print(self.screen.progressBar.value())
        self.screen.close()

    # def facialrec2(self):
    #     os.system('python Face_Gender_Latest_Travel.py')

    # ray.init()
    #
    # # Define functions you want to execute in parallel using
    # # the ray.remote decorator.
    # @ray.remote
    # def func1(self):
    #     # self.Function.loading()
    #     self.function = Function()
    #     self.function.loading()
    #
    # @ray.remote
    # def func2(self):
    #     self.function = Function()
    #     self.function.facialrec2()
    #
    # # Execute func1 and func2 in parallel.
    # ray.get([func1.remote(), func2.remote()])

# class Function:
#     def loading(self):
#         self.screen = SplashScreen()
#         self.screen.show()
#         time.sleep(10)
#         self.screen.close()

class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spash Screen Example')
        self.setFixedSize(1100, 500)
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
        self.labelDescription.setText('<strong>Working on loading facial recognition with camera</strong>')
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
        self.labelLoading.setText('loading...')

        self.setStyleSheet('''
                        #LabelTitle {
                            font-size: 60px;
                            color: #93deed;
                        }

                        #LabelDesc {
                            font-size: 30px;
                            color: #c2ced1;
                        }

                        #LabelLoading {
                            font-size: 30px;
                            color: #e8e8eb;
                        }

                        QFrame {
                            background-color: #2F4454;
                            color: rgb(220, 220, 220);
                        }

                        QProgressBar {
                            background-color: #DA7B93;
                            color: rgb(200, 200, 200);
                            border-style: none;
                            border-radius: 10px;
                            text-align: center;
                            font-size: 30px;
                        }

                        QProgressBar::chunk {
                            border-radius: 10px;
                            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
                        }
                    ''')

# class Window(QWidget):
#     def _init_(self):
#         super()._init_()
#         layout_window = QVBoxLayout()
#         self.setLayout(layout_window)
#         self.button = QPushButton("open", self)
#         layout_window.addWidget(self.button)
#         self.button.clicked.connect(self.splashscreen)
#
#     def splashscreen(self):
#         self.function = Function()
#         self.function.loading()
#         self.function.facialrec2()


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.button = QPushButton("Start", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.Splashscreenwindow)

    # def show_new_window(self):
    #
    #     self.window.show()
        # app.processEvents()
        # thread1 = threading.Thread(target=self.facialrec1)
        # thread1.start()
        # thread1.join()
        # self.hide()
        # os.system('python Face_Gender_Latest_Travel.py')
        # self.window = Window()


    # def facialrec1(self):
    #     os.system('python Face_Gender_Latest_Travel.py')

    def Splashscreenwindow(self):
        # os.system('python Face_Gender_Latest_Travel.py')
        # app.processEvents()
        # thread1 = threading.Thread(target=self.facialrec1)
        # thread1.start()
        # thread1.join()
        # self.hide()
        t1 = threading.Thread(target=self.Operation)
        # t1 = Thread(target=self.Operation)
        t1.start()
        self.function = Function()
        self.function.loading()

        # self.function.facialrec2()
        # app.processEvents()
        # thread1 = threading.Thread(target=self.facialrec1)
        # thread1.start()
        # thread1.join()
        # self.hide()
        # os.system('python Face_Gender_Latest_Travel.py')

    def Operation(self):
        os.system('python face_updated.py')
        print("starting latest facial recognition")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')