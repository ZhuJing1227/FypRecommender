import random
import time
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
import tobii_research as tr
import seaborn as sb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import pandas as pd
import joblib
from past.builtins import execfile
import past.builtins

from sklearn.metrics.pairwise import linear_kernel
from ttkthemes import ThemedTk
from tkinter import ttk
import tkinter.font as tkFont
import age_gender_1food_recommender as collaborative_Recommender

count_runs = 0

if count_runs > 0:
    if fig != None:
        del fig
    if canva != None:
        del canva
    if canvaz != None:
        del canvaz

df = pd.read_csv('foodnew.csv', encoding='mac_roman')
fig = None
most_looked = ''
canvaz = None
canva = None
final_img = ""
final_page = ""


class SampleApp(ThemedTk):

    def __init__(self, *args, **kwargs):
        ThemedTk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.set_theme(theme_name="arc")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, bg="")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne_0, PageOne_1, PageOne_2, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, page_name):
        global most_looked
        global fig
        self.gaze = []
        self.Cord = []
        self.xCord = []
        self.yCord = []
        self.counter = 0

        def eyetracker_fig(self):
            global most_looked
            global fig
            global final_img
            global final_page
            poster = ['whatsfordinner1x.png', 'whatsfordinner2x.png', 'whatsfordinner3x.png']
            # img = Image.open(random.choice(poster))
            # img = random.choice(poster)
            print("This is the chosen page at the TOP -- > ", final_page)

            if final_page == "PageOne_0":
                img = 'whatsfordinner1x.png'
            elif final_page == "PageOne_1":
                img = 'whatsfordinner2x.png'
            elif final_page == "PageOne_2":
                img = 'whatsfordinner3x.png'

            print("This is the chosen image --> ", img)

            # function to detect eye tracker
            found_eyetrackers = tr.find_all_eyetrackers()
            my_eyetracker = found_eyetrackers[0]

            # callback function to subscribe to the gaze data as the eye tracker will output gaze data multiple times
            # every second
            def gaze_data_callback(i):
                self.gaze.append(i)

                for i in self.gaze:
                    self.Cord.append(self.gaze[self.counter]['left_gaze_point_on_display_area'])
                    self.counter += 1

            # tell the SDK to call the function everytime there is new gaze data
            my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

            # collecting eyetracker data for 10 seconds
            time.sleep(5)
            print("This is the count on the counter: ", self.Cord)
            """
            Tkinter codes
            """

            # separating the coordinates to fill "xCord" list with x-coordinates and "yCord" list with y-coordinates
            for x in self.Cord:
                self.xCord.append(x[0])
                self.yCord.append(x[1])

            # function to create heatmap
            def cplot():
                # background image for heatmap
                mp_img = mpimg.imread(img)

                # cleaning the list by removing null values generated when you blink
                self.xCord = [x for x in self.xCord if str(x) != 'nan']
                self.yCord = [x for x in self.yCord if str(x) != 'nan']

                # defining heatmap dimensions
                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                print("cord", self.Cord)
                print("x",self.xCord)
                print("y",self.yCord)
                # plotting heat map with x and y coordinates
                test = sb.kdeplot(self.xCord, self.yCord, shade=True, cmap="Reds", alpha=0.7)
                test.collections[0].set_alpha(0)
                plt.imshow(mp_img, zorder=0, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
                ax.invert_yaxis()
                plt.axis('off')

                return fig

            fig = cplot()
            print("fig print 1 -->", fig)

            """
            Display parts of poster that was looked at the most
            """
            if img == 'whatsfordinner1x.png':
                """
                Display parts of poster that was looked at the most
                """
                rank = []
                most_looked = ''
                laksa = 0
                chillicrab = 0
                charkwayteow = 0
                chickenrice = 0
                fishsoup = 0
                fishnchip = 0
                mixedrice = 0
                bento = 0

                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.25 and 0.3 <= i[1] <= 0.6:
                        chickenrice += 1

                    elif 0.25 <= i[0] <= 0.5 and 0.3 <= i[1] <= 0.6:
                        laksa += 1

                    elif 0.5 <= i[0] <= 0.75 and 0.3 <= i[1] <= 0.6:
                        charkwayteow += 1

                    elif 0.75 <= i[0] <= 1 and 0.3 <= i[1] <= 0.6:
                        chillicrab += 1

                    elif 0 <= i[0] <= 0.25 and 0.7 <= i[1] <= 1:
                        fishsoup += 1

                    elif 0.25 <= i[0] <= 0.5 and 0.7 <= i[1] <= 1:
                        fishnchip += 1

                    elif 0.5 <= i[0] <= 0.75 and 0.7 <= i[1] <= 1:
                        mixedrice += 1

                    elif 0.75 <= i[0] <= 1 and 0.7 <= i[1] <= 1:
                        bento += 1

                rank.append(laksa)
                rank.append(chillicrab)
                rank.append(charkwayteow)
                rank.append(chickenrice)
                rank.append(fishsoup)
                rank.append(fishnchip)
                rank.append(mixedrice)
                rank.append(bento)

                if max(rank) == rank[0]:
                    most_looked = 'laksa'
                elif max(rank) == rank[1]:
                    most_looked = 'Chili Crab'
                elif max(rank) == rank[2]:
                    most_looked = 'Char Kway Teow'
                elif max(rank) == rank[3]:
                    most_looked = 'hainanese chicken rice'
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

            if img == 'whatsfordinner2x.png':
                """

                """
                rank = []
                most_looked = ''
                currylaksa = 0
                yusheng = 0
                duckrice = 0
                fishheadcurry = 0
                bakkuhteh = 0
                hokkienmee = 0
                kwaychap = 0
                rotiprata = 0

                """

                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.25 and 0.3 <= i[1] <= 0.6:
                        currylaksa += 1

                    elif 0.25 <= i[0] <= 0.5 and 0.3 <= i[1] <= 0.6:
                        yusheng += 1

                    elif 0.5 <= i[0] <= 0.75 and 0.3 <= i[1] <= 0.6:
                        duckrice += 1

                    elif 0.75 <= i[0] <= 1 and 0.3 <= i[1] <= 0.6:
                        fishheadcurry += 1

                    elif 0 <= i[0] <= 0.25 and 0.7 <= i[1] <= 1:
                        bakkuhteh += 1

                    elif 0.25 <= i[0] <= 0.5 and 0.7 <= i[1] <= 1:
                        hokkienmee += 1

                    elif 0.5 <= i[0] <= 0.75 and 0.7 <= i[1] <= 1:
                        kwaychap += 1

                    elif 0.75 <= i[0] <= 1 and 0.7 <= i[1] <= 1:
                        rotiprata += 1

                rank.append(currylaksa)
                rank.append(yusheng)
                rank.append(duckrice)
                rank.append(fishheadcurry)
                rank.append(bakkuhteh)
                rank.append(hokkienmee)
                rank.append(kwaychap)
                rank.append(rotiprata)

                if max(rank) == rank[0]:
                    most_looked = 'Curry laksa'
                elif max(rank) == rank[1]:
                    most_looked = 'Yu Sheng'
                elif max(rank) == rank[2]:
                    most_looked = 'Duck Rice'
                elif max(rank) == rank[3]:
                    most_looked = 'Fish Head Curry'
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

            if img == 'whatsfordinner3x.png':
                """
                """
                rank = []
                most_looked = ''
                blackpeppercrab = 0
                rotijohn = 0
                cerealprawn = 0
                beefkwayteow = 0
                katonglaksa = 0
                sambalstingray = 0
                crabbeehoonsoup = 0
                satay = 0
                """
                Setup image map
                """
                for i in self.Cord:
                    if 0 <= i[0] <= 0.25 and 0.3 <= i[1] <= 0.6:
                        beefkwayteow += 1

                    elif 0.25 <= i[0] <= 0.5 and 0.3 <= i[1] <= 0.6:
                        blackpeppercrab += 1

                    elif 0.5 <= i[0] <= 0.75 and 0.3 <= i[1] <= 0.6:
                        cerealprawn += 1

                    elif 0.75 <= i[0] <= 1 and 0.3 <= i[1] <= 0.6:
                        rotijohn += 1

                    elif 0 <= i[0] <= 0.25 and 0.7 <= i[1] <= 1:
                        katonglaksa += 1

                    elif 0.25 <= i[0] <= 0.5 and 0.7 <= i[1] <= 1:
                        sambalstingray += 1

                    elif 0.5 <= i[0] <= 0.75 and 0.7 <= i[1] <= 1:
                        crabbeehoonsoup += 1
                    elif 0.75 <= i[0] <= 1 and 0.7 <= i[1] <= 1:
                        satay += 1

                rank.append(blackpeppercrab)
                rank.append(rotijohn)
                rank.append(cerealprawn)
                rank.append(beefkwayteow)
                rank.append(katonglaksa)
                rank.append(sambalstingray)
                rank.append(crabbeehoonsoup)
                rank.append(satay)

                if max(rank) == rank[0]:
                    most_looked = 'Black Pepper Crab'
                elif max(rank) == rank[1]:
                    most_looked = 'Roti John'
                elif max(rank) == rank[2]:
                    most_looked = 'Cereal Prawn'
                elif max(rank) == rank[3]:
                    most_looked = 'Beef Kway Teow'
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

        print("Most looked dish - global : ", most_looked)

        tfidf_matrix = joblib.load('tfidfVectorizer.pkl')

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        indices = pd.Series(df.index, index=df['name']).drop_duplicates()

        # Function that takes in movie title as input and gives recommendations
        def content_recommender(name, cosine_sim=cosine_sim, df=df, indices=indices):
            # Obtain the index of the movie that matches the title
            idx = indices[name]

            # Get the pairwise similarity scores of all movies with that movie
            # And convert it into a list of tuples as described above
            sim_scores = list(enumerate(cosine_sim[idx]))

            # Sort the movies based on the cosine similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the 10 most similar movies. Ignore the first movie.
            sim_scores = sim_scores[1:6]

            # Get the movie indices
            movie_indices = [i[0] for i in sim_scores]

            recomend_list = df['name'].iloc[movie_indices]
            recommend_string = ', '.join(recomend_list)
            return recommend_string

        """ Heatmap Display """

        def heatmap(self):
            global fig
            global most_looked
            global canvaz
            self.resImgList = []
            self.rating = []
            self.location = []
            self.fig = fig
            df1 = pd.read_csv('food_updated.csv', encoding='mac_roman')

            def get_age():
                with open('combined.txt', 'r') as f:
                    last_line = f.readlines()[-1]
                splitted= last_line.split(",")
                age=splitted[0]

                return age


            def get_gender():
                with open('combined.txt', 'r') as f:
                    last_line = f.readlines()[-1]
                splitted= last_line.split(",")
                gender=splitted[1]
                return gender


            age=get_age()
            print(age)
            gender=get_gender()
            print(gender)
            print("age: ",get_age())
            print("gender: ",get_gender())
            print("most looked: ",most_looked)
            recommendations = collaborative_Recommender.recommend(gender, age, most_looked,collaborative_Recommender.sim_mat_dic, 5)
            print("here is the recommendations: " ,recommendations)
            # recommendations_list=numpy.array_str(recommendations)

            # recoList = [x.strip() for x in recommendations_list.split(',')]
            # print(recoList)
            food=[]
            for i in recommendations:
                food.append(i)
            imgList = []

            # Storing img paths to match the recommendations, locations, and ratings
            for dish in food:
                for x in range(len(df1['name'])):
                    if df1['name'][x] == dish:
                        imgFile = "images/" + dish + ".png"
                        print('imgfile=',imgFile)

                        imgList.append("images/" + dish + ".png")
                        self.rating.append(df1['rating'][x])
                        self.location.append(df1['location'][x])


            print("Image List = ", imgList)

            popup = tk.Toplevel(self)
            popup.geometry("1900x600")
            popup.title("Recommended dishes")

            # labelTitle = tk.Label(popup, text="You picked " + most_looked + "\n\n" + "You might be interested in these dishes:", font="Helvetica 12 bold")
            labelTitle = tk.Label(popup, text="You picked " + most_looked, font="Helvetica 18 bold")
            labelTitle.pack(side=tk.TOP)
            labelTitle2 = tk.Label(popup, text="\n\nYou might be interested in these dishes: ", font="Helvetica 13 bold")
            labelTitle2.pack(side=tk.TOP)
            # labelTitle3 = tk.Label(popup, text="\n\nRecommened:" + food,
            #                        font="Helvetica 13 bold")
            # labelTitle3.pack(side=tk.TOP)


            # Storing resized images into a list
            for i in range(len(food)):
                img = Image.open(imgList[i])
                resized = img.resize((230, 230), Image.ANTIALIAS)
                newImg = ImageTk.PhotoImage(resized)
                self.resImgList.append(newImg)

            print("Reco Image List: ", self.resImgList)
            print("Ratings List: ", self.rating)
            print("Locations List: ", self.location)

            # Displaying recommendations with pictures
            for x in range(len(food)):
                label = tk.Label(popup, text=food[x], font="Helvetica 12 bold")
                lblImg = tk.Label(popup, image=self.resImgList[x], width=230, height=230)
                location = tk.Label(popup, text=self.location[x], bg='#fff', fg='#f00', font="Helvetica 10")
                rating = tk.Label(popup, text=self.rating[x], bg='#fff', fg='#f00', font="Helvetica 10")
                lblImg.pack(side=tk.LEFT, padx=70)
                label.place(
                    in_=lblImg,
                    bordermode="outside",
                    anchor="s",
                    relx=0.5,
                    rely=1.0,
                    y=30,
                    relwidth=1.3
                )
                location.place(
                    in_=lblImg,
                    bordermode="outside",
                    anchor="s",
                    relx=0.5,
                    rely=1.0,
                    y=70,
                    relwidth=1.4
                )
                rating.place(
                    in_=lblImg,
                    bordermode="outside",
                    anchor="s",
                    relx=0.5,
                    rely=1.0,
                    y=90,
                    relwidth=1.4
                )

        def test(self):
            global fig
            global canvaz
            self.fig = fig

            canvas = FigureCanvasTkAgg(self.fig, master=self.get_page(page_name))

            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

            canvaz = canvas

        def clear_image(self):
            global final_page
            # final_page = "PageOne_%d" % (random.randint(0, 2))
            final_page = "PageOne_0"
            # final_page = "PageOne_2"


            print("This is the chosen Image --> ", final_page)

        ''' Show a frame for the given page name '''
        frame = self.frames[page_name]
        frame.tkraise()

        global canvaz
        global canva

        if page_name == "StartPage":
            self.after(1, clear_image(self))


        if page_name == "PageOne_0" or page_name == "PageOne_1" or page_name == "PageOne_2":
            self.after(6000, lambda: self.show_frame("PageTwo"))
            self.after(1000, lambda: eyetracker_fig(self))
            # self.after(1, lambda: clear_image(self))

        if page_name == "PageTwo":
            self.after(500, lambda: heatmap(self))
            self.after(500, lambda: test(self))

def get_combined():
    sys.stdout = open("combined.txt", "w")
    execfile("face.py")
    sys.stdout.close()



class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        global final_img
        global final_page
        self.controller = controller
        self.final_img = final_img
        self.final_page = final_page

        img = ImageTk.PhotoImage(Image.open("FoodBG.png").resize((1925, 1080), Image.ANTIALIAS))
        self.img = img

        bg_img = tk.Label(self, image=self.img)
        bg_img.place(x=-5, y=-5)

        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=18)

        print("Page on Start --> ", final_page)



        # continueBtn = ttk.Button(self, text="Start", command=lambda: [controller.show_frame("PageOne_%d" % (random.randint(0, 2)))])
        continueBtn = ttk.Button(self, text="Start", command=lambda: [execfile("face.py"),controller.show_frame(final_page)])
        continueBtn.config(width=30)
        exitBtn = ttk.Button(self, text="Exit", command=lambda: sys.exit("Ended"))
        exitBtn.config(width=30)
        instructions = tk.Label(self, text="Instructions\n1. Click Start\n2. Stare at the dish you want for 5 seconds\n3. Your recommendations will be shown", bg='#fff')
        instructions.config(font=25, width=50, height=7)

        continueBtn.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-20)
        exitBtn.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=40)
        instructions.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=170)


def InitPageOneCanvas(self, filename):
    global canva
    img = Image.open(filename)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    plt.imshow(img, zorder=0, extent=[0, 1, 0, 1], origin='lower', aspect='auto')
    ax.invert_yaxis()
    plt.axis('off')
    img = fig
    canvas = FigureCanvasTkAgg(img, master=self)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)
    canva = canvas


class PageOne_0(tk.Frame): #classes btfo :troll:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global final_img
        self.controller = controller
        InitPageOneCanvas(self, "whatsfordinner1x.png")

        final_img = "whatsfordinner1x.png"
        # button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        # button.pack()


class PageOne_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global final_img
        self.controller = controller
        InitPageOneCanvas(self, "whatsfordinner2x.png")

        final_img = "whatsfordinner2x.png"


class PageOne_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global final_img
        self.controller = controller
        InitPageOneCanvas(self, "whatsfordinner3x.png")

        final_img = "whatsfordinner3x.png"


class PageTwo(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        global fig
        global canvaz
        global count_runs
        global final_img

        def addcount():
            count_runs += 1

        def error_catch():
            if canvaz is None:
                label = tk.Label(self, text="There was an error detecting your gaze! Please try again.")
                label.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Continue",
                           command=lambda: [controller.show_frame("StartPage"), canvaz.get_tk_widget().pack_forget(), addcount()], width=30)

        button.pack(pady=50)

        # if canvaz is None:
        # self.after(1000, lambda: error_catch())


if __name__ == "__main__":
    while True:
        try:
            app = SampleApp()
            app.title("Dish Recommender")
            app.state('zoomed')
            app.mainloop()

        except Exception as e:
            print("The error is --> ", e)
            app = SampleApp()
            app.title("Dish Recommender")
            app.state('zoomed')
            app.mainloop()
