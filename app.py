# import libraries we will be working with
import tkinter as tk
from PIL import Image, ImageTk
import random

# launch gui window
root = tk.Tk()
# give gui window it's size
root.geometry("450x600")
# give gui window it's title
root.title("Where to GO?")

# add definition to add images to the background of our gui window
def add_image(root, file_path):

    # with the global we make sure our variables can be used properly
    global pic,f1

    # create the frame for the gui window
    f1 = tk.Frame(root)
    # read the image you want to use in the background of your frame
    img = Image.open(file_path)
    # resize the image so it fits the frame of the gui window
    img = img.resize((445, 600), Image.LANCZOS)
    # with this code the image is viewed as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # place the image with this code
    Lab.pack()
    f1.pack()

# add a definition to create the home page that asks user for name and password
def home_page():

    # choose first image as a background
    add_image(root, file_path="pictures/background.jpg")
    # this picture is the same as "essen-gehen.jpg", only I editit it so that it's slightly faded

    global first_title
    global shopkeeper_button
    global customer_button

    # create a title that shows name of the app: "Where to GO?"
    first_title = tk.Label(root,
                           text="Where to GO?",
                           font="Rockwell 28",
                           fg="green"
                           )
    first_title.place(x=122, y=50)
    # create a button that brings the user to the shopkeeper homepage
    shopkeeper_button = tk.Button(root,
                                  text="Shopkeeper",
                                  command=shopkeeper_home_page,
                                  font="Helvetica 25 bold",
                                  fg="green"
                                  )
    shopkeeper_button.place(x=127, y=200)
    # create a button that brings the user to the customer's homepage
    customer_button = tk.Button(root,
                                text="Customer",
                                command=customers_welcoming,
                                font="Helvetica 25 bold",
                                fg="green"
                                )
    customer_button.place(x=133, y=330)

# add definition for the customer's first page
def customers_welcoming():

    # use this code to cinfigure the size
    root.geometry('450x600')

    # destroy everything created on the home page in order to clear the screen
    f1.destroy()
    first_title.destroy()
    shopkeeper_button.destroy()
    customer_button.destroy()

    # add a new image to the background
    add_image(root, file_path="pictures/background.jpg")

    global title
    global title_2
    global search_button
    global back_button_1

    # add the first part of the title: this part is going to be a bit smaller
    title = tk.Label(root,
                     text="Don't know",
                     font="Helvetica 15 bold",
                     fg="black"
                     )
    title.place(x=180, y=175)
    # add the second part of the title:
    # this part is going to be bigger since it's the name of the app and we want it to stick out
    title_2 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 36",
                       fg="green"
                       )
    title_2.place(x=95, y=200)
    # create a search button, so that the user can get to the next page by clicking on it
    search_button = tk.Button(root,
                              text="SEARCH HERE!",
                              command=customers_first_choice,
                              font="Geneva 20 bold",
                              fg="green"
                              )
    search_button.place(x=135, y=370)
    # create a back button, so that the user can get back to the homepage
    back_button_1 = tk.Button(root,
                              text="Back",
                              command=back_1,
                              font="Helvetica 16 bold",
                              fg="black"
                              )
    back_button_1.place(x=188, y=565)

# create a definition that gets executed by the first back button
def back_1():
    # destroy everything we build on the customer's first page
    f1.destroy()
    title.destroy()
    title_2.destroy()
    search_button.destroy()
    back_button_1.destroy()

    # go back to the homepage
    home_page()

# create a definition for the customers second page
def customers_first_choice():

    root.geometry('450x600')

    # destroy everything we built on the page before in order to clear the screen
    f1.destroy()
    search_button.destroy()
    title.destroy()
    title_2.destroy()

    # choose an image as the background
    add_image(root, file_path="pictures/background.jpg")
    # this image was designed by me

    global title_3
    global people_label
    global people_entry
    global next_button
    global back_button_2

    # create the same title as on the homepage
    title_3 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_3.place(x=122, y=30)
    # create a label that asks the user for the number of people they're with
    people_label = tk.Label(root,
                            text="For how many people are you searching for?",
                            font="Helvetica 18 bold",
                            fg="green"
                            )
    people_label.place(x=45, y=240)
    # create a variable that stores the number of people the user is searching for
    number_of_people = tk.StringVar()
    # create an entry box where the user can enter the number
    people_entry = tk.Entry(root,
                            textvar=number_of_people,
                            font="Helvetica 26",
                            fg="black",
                            bg="white"
                            )
    people_entry.place(x=75, y=280)
    # create a button which leads the user to the next page
    next_button = tk.Button(root,
                            text="Next",
                            command=customers_second_choice,
                            font="Helvetica 28 bold",
                            fg="green"
                            )
    next_button.place(x=175, y=350)
    # create a back button that leads the user back to the welcoming page
    back_button_2 = tk.Button(root,
                              text="Back",
                              command=back_2,
                              font="Helvetica 16 bold",
                              fg="black"
                              )
    back_button_2.place(x=188, y=565)

# create a definition that gets executed by the second back button
def back_2():
    # destroy everything we built on the customers_first_choice page
    title_3.destroy()
    people_label.destroy()
    people_entry.destroy()
    next_button.destroy()
    back_button_2.destroy()

    # go back to the customers welcoming
    customers_welcoming()

def customers_second_choice():

    root.geometry('450x600')
    # destroy everything we build on the customers_first_choice page
    f1.destroy()
    title_3.destroy()
    people_label.destroy()
    people_entry.destroy()
    next_button.destroy()
    back_button_2.destroy()

    # choose an image as the background
    add_image(root, file_path="pictures/background.jpg")

    global title_4
    global instruction_label
    global vegetarian_button
    global vegan_button
    global all_button
    global back_button_3

    title_4 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_4.place(x=122, y=30)
    # create a new label that gives the user instructions
    instruction_label = tk.Label(root,
                                 text="What are you searching for?",
                                 font="Helvetica 23",
                                 fg="green"
                                 )
    instruction_label.place(x=80, y=120)
    # create a button that shows the user all vegetarian options
    vegetarian_button = tk.Button(root,
                                  text="Vegaterian",
                                  command=customers_home_page,
                                  font="Helvetica 28",
                                  fg="green"
                                  )
    vegetarian_button.place(x=140, y=210)
    # create a button that shows the user all vegan options
    vegan_button = tk.Button(root,
                             text="Vegan",
                             command=customers_home_page,
                             font="Helvetica 28",
                             fg="green"
                             )
    vegan_button.place(x=165, y=300)
    # create a button that shows the user all options
    all_button = tk.Button(root,
                           text="All",
                           command=customers_home_page,
                           font="Helvetica 28",
                           fg="green"
                           )
    all_button.place(x=190, y=390)
    # create a button that leads the user back to the customers_first_choice page
    back_button_3 = tk.Button(root,
                              text="Back",
                              command=back_3,
                              font="Helvetica 16 bold",
                              fg="black"
                              )
    back_button_3.place(x=188, y=565)

# create a definition that gets executed by the third back button
def back_3():
    # destroy everything we built on the customers_second_choice page
    f1.destroy()
    title_4.destroy()
    instruction_label.destroy()
    vegetarian_button.destroy()
    vegan_button.destroy()
    all_button.destroy()
    back_button_3.destroy()

    # go back to customers_first_choice
    customers_first_choice()
def customers_home_page():

    root.geometry('450x600')
    # destroy everything we build on the customers_second_choice page in order to clear the screen
    f1.destroy()
    title_4.destroy()
    instruction_label.destroy()
    vegetarian_button.destroy()
    vegan_button.destroy()
    all_button.destroy()
    back_button_3.destroy()

    # add an image for the background
    add_image(root, file_path="pictures/background.jpg")

    global headline
    global search_button
    global search_box
    global restaurant_button
    global bar_button
    global cafe_button
    global breakfast_button
    global dinner_button
    global dessert_button
    global back_button_4

    # create a headline so that the title can still be seen
    headline = tk.Label(root,
                        text="Where to GO?",
                        font="Rockwell 28",
                        fg="green"
                        )
    headline.place(x=122, y=10)

    search = tk.StringVar()
    # create a search box so that the user can search for places/food/etc.
    search_box = tk.Entry(root,
                          textvar=search,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    search_box.place(x=150, y=65)

    # create a definition that executes the search
    def search_place():

        # create an option for "Italian" food
        if search.get() == "Italian":
            italian()
        # create a message that is displayed when something other than the above is typed in
        else:
            message = tk.Label(root,
                               text="No places found",
                               font="Helvetica 28 bold",
                               fg="white",
                               bg="green"
                               )
            message.place(x=95, y=280)

    # create a button that executes the definition above
    search_button = tk.Button(root,
                              text="search",
                              command=search_place,
                              font="Helvetica 17",
                              fg="black"
                              )
    search_button.place(x=60, y=62)
    # create a restaurant button that will show all the restaurants if the user clicks on it
    restaurant_button = tk.Button(root,
                                  text="Restaurants",
                                  command=places,
                                  font="Helvetica 15",
                                  fg="black"
                                  )
    restaurant_button.place(x=70, y=150)
    # create a bar button that will show all the bars if the user clicks on it
    bar_button = tk.Button(root,
                           text="Bars",
                           command=places,
                           font="Helvetica 15",
                           fg="black"
                           )
    bar_button.place(x=275, y=150)
    # create a cafe button that will show all the cafes if the user clicks on it
    cafe_button = tk.Button(root,
                            text="Cafes",
                            command=places,
                            font="Helvetica 15",
                            fg="black"
                            )
    cafe_button.place(x=85, y=280)
    # create a breakfast button that will show all the places serving breakfast when the user clicks on it
    breakfast_button = tk.Button(root,
                                 text="Breakfast",
                                 command=places,
                                 font="Helvetica 15",
                                 fg="black"
                                 )
    breakfast_button.place(x=255, y=280)
    # create a dinner button that will show all the places serving dinner when the user clicks on it
    dinner_button = tk.Button(root,
                              text="Dinner",
                              command=places,
                              font="Helvetica 15",
                              fg="black"
                              )
    dinner_button.place(x=83, y=410)
    # crete a dessert button that will show all the places serving dinner when the user clicks on it
    dessert_button = tk.Button(root,
                               text="Dessert",
                               command=places,
                               font="Helvetica 15",
                               fg="black"
                               )
    dessert_button.place(x=260, y=410)
    # create a back button that will go back to the customers_second_choice page
    back_button_4 = tk.Button(root,
                              text="Back",
                              command=back_4,
                              font="Helvetica 16 bold",
                              fg="black",
                              )
    back_button_4.place(x=188, y=565)

# create a definition that gets executed by the fourth back button
def back_4():
    # destroy everything we build on the customers_homepage
    f1.destroy()
    headline.destroy()
    search_button.destroy()
    search_box.destroy()
    restaurant_button.destroy()
    bar_button.destroy()
    cafe_button.destroy()
    breakfast_button.destroy()
    dinner_button.destroy()
    dessert_button.destroy()
    back_button_2.destroy()

    # go back to the customers_second_choice
    customers_second_choice()

# create a page that pops up if the user types in "Italian" into the search_box
def italian():

    global places_label
    global vita_button
    global vita_label
    global allround_button
    global allround_label
    global ice_button
    global ice_label
    global coffee_button
    global coffee_label
    global back_button_10

    root.geometry('450x600')

    # destroy everything we build on the customers_homepage to clear the screen
    f1.destroy()
    headline.destroy()
    search_button.destroy()
    search_box.destroy()
    restaurant_button.destroy()
    bar_button.destroy()
    cafe_button.destroy()
    breakfast_button.destroy()
    dinner_button.destroy()
    dessert_button.destroy()
    back_button_4.destroy()

    # add a new image as a background:
    add_image(root, file_path="pictures/background.jpg")
    # add a headline to the new page
    places_label = tk.Label(root,
                            text="Places",
                            font="Helvetica 25",
                            fg="green"
                            )
    places_label.place(x=175, y=35)
    # add a button for the first restaurant
    vita_button = tk.Button(root,
                            text="La Dolce Vita",
                            command=options_italian,
                            font="Helvetica 20",
                            fg="black"
                            )
    vita_button.place(x=120, y=110)
    # add a label to give a short description of the first restaurant
    vita_label = tk.Label(root,
                          text="an Italien restaurant",
                          font="Helvetica 17",
                          fg="black"
                          )
    vita_label.place(x=120, y=150)
    # add more buttons and labels to give the customer the option between different places
    allround_button = tk.Button(root,
                                text="AllRound",
                                command=options_italian,
                                font="Helvetica 20",
                                fg="black"
                                )
    allround_button.place(x=120, y=200)

    allround_label = tk.Label(root,
                              text="a Pizzaria",
                              font="Helvetica 17",
                              fg="black"
                              )
    allround_label.place(x=120, y=240)

    ice_button = tk.Button(root,
                           text="Cafè de Lulu",
                           command=options_italian,
                           font="Helvetica 20",
                           fg="black"
                           )
    ice_button.place(x=120, y=290)

    ice_label = tk.Label(root,
                         text="Ice cafe",
                         font="Helvetica 17",
                         fg="black"
                         )
    ice_label.place(x=120, y=330)

    coffee_button = tk.Button(root,
                              text="Espresso for two",
                              command=options_italian,
                              font="Helvetica 20",
                              fg="black"
                              )
    coffee_button.place(x=120, y=380)

    coffee_label = tk.Label(root,
                            text="cafe specialized in coffee",
                            font="Helvetica 17",
                            fg="black"
                            )
    coffee_label.place(x=120, y=420)
    # add a back button to go back to the customers_home_page
    back_button_10 = tk.Button(root,
                               text="Back",
                               command=back_10,
                               font="Helvetica 16 bold",
                               fg="black",
                               )
    back_button_10.place(x=188, y=565)

# create a definition that gets executed by the tenth back button
def back_10():

    f1.destroy()
    places_label.destroy()
    vita_button.destroy()
    vita_label.destroy()
    allround_button.destroy()
    allround_label.destroy()
    ice_button.destroy()
    ice_label.destroy()
    coffee_button.destroy()
    coffee_label.destroy()
    back_button_10.destroy()

    # go back to the customers_home_page
    customers_home_page()

# create another page to give the customer more otipns
def options_italian():

    global title_5
    global menu_button
    global reservation_button
    global review_button
    global back_button_11

    root.geometry('450x600')

    f1.destroy()
    places_label.destroy()
    vita_button.destroy()
    vita_label.destroy()
    allround_button.destroy()
    allround_label.destroy()
    ice_button.destroy()
    ice_label.destroy()
    coffee_button.destroy()
    coffee_label.destroy()
    back_button_10.destroy()

    add_image(root, file_path="pictures/options.jpg")

    title_5 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_5.place(x=122, y=30)
    # create a button that leads the customer to the menu of the restaurant
    menu_button = tk.Button(root,
                            text="Menu",
                            command=menu_italian,
                            font="Helvetica 20",
                            fg="black"
                            )
    menu_button.place(x=170, y=165)
    # create a button that leads the customer to a knew page where they can place a reservation
    reservation_button = tk.Button(root,
                                   text="Place a reservation",
                                   command=reservation_italian,
                                   font="Helvetica 20",
                                   fg="black"
                                   )
    reservation_button.place(x=170, y=253)
    # create a butten which leads the customer to the review page
    review_button = tk.Button(root,
                              text="Leave a review",
                              command=review_italian,
                              font="Helvetica 20",
                              fg="black"
                              )
    review_button.place(x=170, y=343)

    back_button_11 = tk.Button(root,
                               text="Back",
                               command=back_11,
                               font="Helvetica 16 bold",
                               fg="black",
                               )
    back_button_11.place(x=188, y=565)

def back_11():

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()
    back_button_11.destroy()

    italian()

# create a page that shows the menu of the restaurant
def menu_italian():

    global back_button_12

    root.geometry('450x600')

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()
    back_button_11.destroy()

    # add the menu as an image
    add_image(root, file_path="pictures/menu.jpg")

    back_button_12 = tk.Button(root,
                               text="Back",
                               command=back_12,
                               font="Helvetica 16 bold",
                               fg="black",
                               )
    back_button_12.place(x=188, y=565)

def back_12():

    f1.destroy()
    back_button_12.destroy()

    options_italian()

# create a page where the user can place a reservation
def reservation_italian():

    global title_11
    global back_button_15
    global place_reservation_label
    global date_label
    global date_entry
    global time_label
    global time_entry
    global person_label
    global person_entry
    global name_label
    global name_entry
    global submit_button

    root.geometry('450x600')

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()
    back_button_11.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    title_11 = tk.Label(root,
                        text="Where to GO?",
                        font="Rockwell 28",
                        fg="green"
                        )
    title_11.place(x=122, y=30)

    place_reservation_label = tk.Label(root,
                                       text="Place a reservation here",
                                       font="Helvetica 15",
                                       fg="green"
                                       )
    place_reservation_label.place(x=140, y=77)
    # create a label for the Date of the reservation
    date_label = tk.Label(root,
                          text="Date:",
                          font="Helvetica 20",
                          fg="black"
                          )
    date_label.place(x=130, y=120)

    date = tk.StringVar()
    # create an entry box where the user can enter the date of the reservation
    date_entry = tk.Entry(root,
                          textvar=date,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    date_entry.place(x=130, y=160)
    # create a label for the time of the reservation
    time_label = tk.Label(root,
                          text="Time:",
                          font="Helvetica 20",
                          fg="black"
                          )
    time_label.place(x=130, y=210)

    time = tk.StringVar()
    # create an entry box where the user can enter the time of the reservation
    time_entry = tk.Entry(root,
                          textvar=time,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    time_entry.place(x=130, y=250)
    # create a label for the number of people
    person_label = tk.Label(root,
                            text="Number of people:",
                            font="Helvetica 20",
                            fg="black"
                            )
    person_label.place(x=130, y=300)

    person = tk.StringVar()
    # create an entry box where the user can enter the number of people
    person_entry = tk.Entry(root,
                            textvar=person,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    person_entry.place(x=130, y=340)
    # create a label for the name in which the revervation is placed in
    name_label = tk.Label(root,
                          text="Name:",
                          font="Helvetica 20",
                          fg="black"
                          )
    name_label.place(x=130, y=390)

    name = tk.StringVar()
    # create an entry box where the user can enter the name in which the reservation is placed in
    name_entry = tk.Entry(root,
                          textvar=name,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    name_entry.place(x=130, y=430)

    # create a button that submits the reservation
    submit_button = tk.Button(root,
                              text="SUBMIT",
                              command=submit_reservation,
                              font="Helvetica 17",
                              fg="black"
                              )
    submit_button.place(x=175, y=530)

    back_button_15 = tk.Button(root,
                               text="Back",
                               command=back_15,
                               font="Helvetica 16 bold",
                               fg="black",
                               )
    back_button_15.place(x=188, y=565)

def back_15():
    # destroy everything we build on the customers_homepage
    f1.destroy()
    title_11.destroy()
    place_reservation_label.destroy()
    submit_button.destroy()
    back_button_15.destroy()
    date_label.destroy()
    date_entry.destroy()
    time_label.destroy()
    time_entry.destroy()
    person_label.destroy()
    person_entry.destroy()
    name_label.destroy()
    name_entry.destroy()

    # go back to the customers_second_choice
    options_italian()

# create a definition that lets the user know that his reservation has been submitted
def submit_reservation():

    # create a message that pops up if the reservation is submitted
    message = tk.Label(root,
                       text="Your reservation has been successful",
                       font="Helvetica 17 bold",
                       fg="white",
                       bg="green"
                       )
    message.place(x=70, y=280)

# create a review page
def review_italian():

    global title_8
    global back_button_16
    global review_label
    global review_entry
    global customers_review_button

    root.geometry('450x600')

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()

    add_image(root, file_path="pictures/review.jpg")

    title_8 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_8.place(x=122, y=30)

    review_label = tk.Label(root,
                            text="Leave a review here",
                            font="Helvetica 15",
                            fg="green"
                            )
    review_label.place(x=140, y=77)

    customers_review = tk.StringVar()
    # create an entry box where the user can enter their review
    review_entry = tk.Entry(root,
                            textvar=customers_review,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    review_entry.place(x=130, y=260)
    # create a button that submits the customer's review
    customers_review_button = tk.Button(root,
                                        text="SUBMIT",
                                        command=submit_review,
                                        font="Helvetica 17",
                                        fg="black"
                                        )
    customers_review_button.place(x=175, y=530)

    back_button_16 = tk.Button(root,
                               text="Back",
                               command=back_16,
                               font="Helvetica 16 bold",
                               fg="black",
                               )
    back_button_16.place(x=188, y=565)

def back_16():

    f1.destroy()
    title_8.destroy()
    back_button_16.destroy()
    review_label.destroy()
    review_entry.destroy()
    customers_review_button.destroy()

    options_italian()

# create a definition that let's the user know that his review has been submitted
def submit_review():

    # create a message that pops up if a review is submitted
    message = tk.Label(root,
                       text="We have recieved your review",
                       font="Helvetica 17 bold",
                       fg="white",
                       bg="green"
                       )
    message.place(x=100, y=280)

# create a page that show all the restaurants if the user clicks on a categorie on the customers_home_page
def places():

    global places_label_2
    global vita_button
    global vita_label
    global allround_button
    global allround_label
    global dumplings_button
    global dumplings_label
    global cosa_button
    global cosa_label
    global back_button_5

    root.geometry('450x600')

    f1.destroy()
    headline.destroy()
    search_button.destroy()
    search_box.destroy()
    restaurant_button.destroy()
    bar_button.destroy()
    cafe_button.destroy()
    breakfast_button.destroy()
    dinner_button.destroy()
    dessert_button.destroy()
    back_button_4.destroy()

    add_image(root, file_path="pictures/background.jpg")

    places_label_2 = tk.Label(root,
                              text="Places",
                              font="Helvetica 25",
                              fg="green"
                              )
    places_label_2.place(x=175, y=35)
    # create labels and buttons for the differnet places
    vita_button = tk.Button(root,
                            text="La Dolce Vita",
                            command=options,
                            font="Helvetica 20",
                            fg="black"
                            )
    vita_button.place(x=120, y=110)

    vita_label = tk.Label(root,
                          text="an Italien restaurant",
                          font="Helvetica 17",
                          fg="black"
                          )
    vita_label.place(x=120, y=150)

    allround_button = tk.Button(root,
                                text="AllRound",
                                command=options,
                                font="Helvetica 20",
                                fg="black"
                                )
    allround_button.place(x=120, y=200)

    allround_label = tk.Label(root,
                              text="a Pizzaria",
                              font="Helvetica 17",
                              fg="black"
                              )
    allround_label.place(x=120, y=240)

    dumplings_button = tk.Button(root,
                                 text="Dumplings",
                                 command=options,
                                 font="Helvetica 20",
                                 fg="black"
                                 )
    dumplings_button.place(x=120, y=290)

    dumplings_label = tk.Label(root,
                               text="a Chinese restaurant",
                               font="Helvetica 17",
                               fg="black"
                               )
    dumplings_label.place(x=120, y=330)

    cosa_button = tk.Button(root,
                            text="pequeña cosa",
                            command=options,
                            font="Helvetica 20",
                            fg="black"
                            )
    cosa_button.place(x=120, y=380)

    cosa_label = tk.Label(root,
                          text="a Tapas restaurant",
                          font="Helvetica 17",
                          fg="black"
                          )
    cosa_label.place(x=120, y=420)

    back_button_5 = tk.Button(root,
                              text="Back",
                              command=back_5,
                              font="Helvetica 16 bold",
                              fg="black",
                              )
    back_button_5.place(x=188, y=565)

def back_5():

    f1.destroy()
    places_label_2.destroy()
    vita_button.destroy()
    vita_label.destroy()
    allround_button.destroy()
    allround_label.destroy()
    dumplings_button.destroy()
    dumplings_label.destroy()
    cosa_button.destroy()
    cosa_label.destroy()
    back_button_5.destroy()

    customers_home_page()

# create another page that leads the user to the differnt options
def options():

    global title_5
    global menu_button
    global reservation_button
    global review_button
    global back_button_6

    root.geometry('450x600')

    f1.destroy()
    places_label_2.destroy()
    vita_button.destroy()
    vita_label.destroy()
    allround_button.destroy()
    allround_label.destroy()
    dumplings_button.destroy()
    dumplings_label.destroy()
    cosa_button.destroy()
    cosa_label.destroy()
    back_button_5.destroy()

    add_image(root, file_path="pictures/options.jpg")

    title_5 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_5.place(x=122, y=30)

    menu_button = tk.Button(root,
                            text="Menu",
                            command=menu,
                            font="Helvetica 20",
                            fg="black"
                            )
    menu_button.place(x=170, y=165)

    reservation_button = tk.Button(root,
                                   text="Place a reservation",
                                   command=reservation,
                                   font="Helvetica 20",
                                   fg="black"
                                   )
    reservation_button.place(x=170, y=253)

    review_button = tk.Button(root,
                              text="Leave a review",
                              command=review,
                              font="Helvetica 20",
                              fg="black"
                              )
    review_button.place(x=170, y=343)

    back_button_6 = tk.Button(root,
                              text="Back",
                              command=back_6,
                              font="Helvetica 16 bold",
                              fg="black",
                              )
    back_button_6.place(x=188, y=565)

def back_6():

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()
    back_button_6.destroy()

    places()

# create a menu page
def menu():

    global back_button_7

    root.geometry('450x600')

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()

    add_image(root, file_path="pictures/menu.jpg")

    back_button_7 = tk.Button(root,
                              text="Back",
                              command=back_7,
                              font="Helvetica 16 bold",
                              fg="black",
                              )
    back_button_7.place(x=188, y=565)

def back_7():

    f1.destroy()
    back_button_7.destroy()

    options()

# create another reservation page
def reservation():

    global title_7
    global back_button_8
    global submit_button
    global place_reservation_label
    global date_label
    global date_entry
    global time_label
    global time_entry
    global person_label
    global person_entry
    global name_label
    global name_entry

    root.geometry('450x600')

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    title_7 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_7.place(x=122, y=30)

    place_reservation_label = tk.Label(root,
                                       text="Place a reservation here",
                                       font="Helvetica 15",
                                       fg="green"
                                       )
    place_reservation_label.place(x=140, y=77)

    date_label = tk.Label(root,
                          text="Date:",
                          font="Helvetica 20",
                          fg="black"
                          )
    date_label.place(x=130, y=120)

    date = tk.StringVar()

    date_entry = tk.Entry(root,
                          textvar=date,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    date_entry.place(x=130, y=160)

    time_label = tk.Label(root,
                          text="Time:",
                          font="Helvetica 20",
                          fg="black"
                          )
    time_label.place(x=130, y=210)

    time = tk.StringVar()

    time_entry = tk.Entry(root,
                          textvar=time,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    time_entry.place(x=130, y=250)

    person_label = tk.Label(root,
                            text="Number of people:",
                            font="Helvetica 20",
                            fg="black"
                            )
    person_label.place(x=130, y=300)

    person = tk.StringVar()

    person_entry = tk.Entry(root,
                            textvar=person,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    person_entry.place(x=130, y=340)

    name_label = tk.Label(root,
                          text="Name:",
                          font="Helvetica 20",
                          fg="black"
                          )
    name_label.place(x=130, y=390)

    name = tk.StringVar()

    name_entry = tk.Entry(root,
                          textvar=name,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    name_entry.place(x=130, y=430)

    submit_button = tk.Button(root,
                              text="SUBMIT",
                              command=submit_reservation,
                              font="Helvetica 17",
                              fg="black"
                              )
    submit_button.place(x=175, y=530)

    back_button_8 = tk.Button(root,
                              text="Back",
                              command=back_8,
                              font="Helvetica 16 bold",
                              fg="black",
                              )
    back_button_8.place(x=188, y=565)

def back_8():

    f1.destroy()
    title_7.destroy()
    submit_button.destroy()
    place_reservation_label.destroy()
    back_button_8.destroy()
    date_label.destroy()
    date_entry.destroy()
    time_label.destroy()
    time_entry.destroy()
    person_label.destroy()
    person_entry.destroy()
    name_label.destroy()
    name_entry.destroy()

    options()

# create another review page
def review():

    global title_8
    global back_button_9
    global review_label
    global review_entry
    global customers_review_button

    root.geometry('450x600')

    f1.destroy()
    title_5.destroy()
    menu_button.destroy()
    reservation_button.destroy()
    review_button.destroy()

    add_image(root, file_path="pictures/review.jpg")

    title_8 = tk.Label(root,
                       text="Where to GO?",
                       font="Rockwell 28",
                       fg="green"
                       )
    title_8.place(x=122, y=30)

    review_label = tk.Label(root,
                            text="Leave a review here",
                            font="Helvetica 15",
                            fg="green"
                            )
    review_label.place(x=140, y=77)

    customers_review = tk.StringVar()

    review_entry = tk.Entry(root,
                            textvar=customers_review,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    review_entry.place(x=130, y=260)

    customers_review_button = tk.Button(root,
                                        text="SUBMIT",
                                        command=submit_review,
                                        font="Helvetica 17",
                                        fg="black"
                                        )
    customers_review_button.place(x=175, y=530)

    back_button_9 = tk.Button(root,
                              text="Back",
                              command=back_9,
                              font="Helvetica 16 bold",
                              fg="black",
                              )
    back_button_9.place(x=188, y=565)

def back_9():

    f1.destroy()
    title_8.destroy()
    back_button_9.destroy()
    review_entry.destroy()
    customers_review_button.destroy()
    review_label.destroy()

    options()

# create a definition for the shopkeepers first page
def shopkeeper_home_page():

    # destroy everything we build on the homepage in order to clear the screen
    f1.destroy()
    first_title.destroy()
    shopkeeper_button.destroy()
    customer_button.destroy()

    global cafe_label
    global table_one_button
    global table_two_button
    global table_three_button
    global table_four_button
    global table_five_button
    global table_six_button
    global back_button_13

    root.geometry('450x600')

    # add a new image for the background
    add_image(root, file_path="pictures/layout-cafe.jpg")
    # this is a prototype of what a restaurants/cafes/bars layout could look like (designed by me)

    # add a label that shows the name of the shopkeeper's place
    cafe_label = tk.Label(root,
                          text="Café de Lulu",
                          font="Papyrus 20",
                          fg="green"
                          )
    cafe_label.place(x=145, y=10)

    # add as many buttons as the place has tables
    table_one_button = tk.Button(root,
                                 text="Table 1",
                                 command=reservations,
                                 font="Helvetica 15",
                                 fg="black"
                                 )
    table_one_button.place(x=55,y=95)

    table_two_button = tk.Button(root,
                                 text="Table 2",
                                 command=reservations,
                                 font="Helvetica 15",
                                 fg="black"
                                 )
    table_two_button.place(x=165, y=95)

    table_three_button = tk.Button(root,
                                   text="Table 3",
                                   command=reservations,
                                   font="Helvetica 15",
                                   fg="black"
                                   )
    table_three_button.place(x=310, y=95)

    table_four_button = tk.Button(root,
                                  text="Table 4",
                                  command=reservations,
                                  font="Helvetica 15",
                                  fg="black"
                                  )
    table_four_button.place(x=250, y=290)

    table_five_button = tk.Button(root,
                                  text="Table 5",
                                  command=reservations,
                                  font="Helvetica 15",
                                  fg="black"
                                  )
    table_five_button.place(x=345, y=290)

    table_six_button = tk.Button(root,
                                 text="Table 6",
                                 command=reservations,
                                 font="Helvetica 15",
                                 fg="black"
                                 )
    table_six_button.place(x=300, y=500)

    # create a back button that goes back to the home page
    back_button_13 = tk.Button(root,
                               text="Back",
                               command=back_13,
                               font="Helvetica 16 bold",
                               fg="black"
                               )
    back_button_13.place(x=180, y=565)

def back_13():
    # destroy everything we build on the shopkeepers first page
    f1.destroy()
    cafe_label.destroy()
    table_one_button.destroy()
    table_two_button.destroy()
    table_three_button.destroy()
    table_four_button.destroy()
    table_five_button.destroy()
    table_six_button.destroy()
    back_button_13.destroy()

    # go back to the home page
    home_page()

# create a definition for the shopkeepers second page that shows the reservations of each table
def reservations():

        global reservation_label
        global back_button_14
        global sunday_label
        global left_button
        global right_button
        global nine_label
        global nine_entry
        global ten_label
        global ten_entry
        global eleven_label
        global eleven_entry
        global twelve_label
        global twelve_entry
        global thirteen_label
        global thirteen_entry
        global fourteen_label
        global fourteen_entry
        global fifteen_label
        global fifteen_entry
        global sixteen_label
        global sixteen_entry
        global seventeen_label
        global seventeen_entry
        global eighteen_label
        global eighteen_entry

        root.geometry('450x600')

        # destroy everything we build on the shopkeepers first page to clear the screen
        f1.destroy()
        cafe_label.destroy()
        table_one_button.destroy()
        table_two_button.destroy()
        table_three_button.destroy()
        table_four_button.destroy()
        table_five_button.destroy()
        table_six_button.destroy()
        back_button_13.destroy()

        # add a new image as a background:
        add_image(root, file_path="pictures/reservations.jpg")

        # create a headline for this page
        reservation_label = tk.Label(root,
                                     text="Reservations for this table:",
                                     font="Rockwell 12",
                                     fg="green"
                                     )
        reservation_label.place(x=140, y=10)
        # create a label for a day of the week
        sunday_label = tk.Label(root,
                                text="Sunday",
                                font="Helvetica 25",
                                fg="green"
                                )
        sunday_label.place(x=175, y=35)
        # create a button that leads to the day before
        left_button = tk.Button(root,
                                text="<<",
                                command=saturday,
                                font="Helvetica 15",
                                fg="black"
                                )
        left_button.place(x=115, y=37)
        # create a button that leads to the day after
        right_button = tk.Button(root,
                                 text=">>",
                                 command=monday,
                                 font="Helvetica 15",
                                 fg="black"
                                 )
        right_button.place(x=270, y=37)
        # create a label for each hour that the place is open
        nine_label = tk.Label(root,
                              text="09:00",
                              font="Helvetica 15",
                              fg="black"
                              )
        nine_label.place(x=40, y=90)

        nine_reservations = tk.StringVar()
        # create an entry box where the user can enter a reservation or other notes
        nine_entry = tk.Entry(root,
                              textvar=nine_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
        nine_entry.place(x=120, y=87)
        # repeat that process
        ten_label = tk.Label(root,
                             text="10:00",
                             font="Helvetica 15",
                             fg="black"
                             )
        ten_label.place(x=40, y= 130)

        ten_reservations = tk.StringVar()

        ten_entry = tk.Entry(root,
                             textvar=ten_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
        ten_entry.place(x=120, y=127)

        eleven_label = tk.Label(root,
                                text="11:00",
                                font="Helvetica 15",
                                fg="black"
                                )
        eleven_label.place(x=40, y=170)

        eleven_reservations = tk.StringVar()

        eleven_entry = tk.Entry(root,
                                textvar=eleven_reservations,
                                font="Helvetica 15",
                                fg="black",
                                bg="white"
                                )
        eleven_entry.place(x=120, y=167)

        twelve_label = tk.Label(root,
                                text="12:00",
                                font="Helvetica 15",
                                fg="black"
                                )
        twelve_label.place(x=40, y=210)

        twelve_reservations = tk.StringVar()

        twelve_entry = tk.Entry(root,
                                textvar=twelve_reservations,
                                font="Helvetica 15",
                                fg="black",
                                bg="white"
                                )
        twelve_entry.place(x=120, y=207)

        thirteen_label = tk.Label(root,
                                  text="13:00",
                                  font="Helvetica 15",
                                  fg="black"
                                  )
        thirteen_label.place(x=40, y=250)

        thirteen_reservations = tk.StringVar()

        thirteen_entry = tk.Entry(root,
                                  textvar=thirteen_reservations,
                                  font="Helvetica 15",
                                  fg="black",
                                  bg="white"
                                  )
        thirteen_entry.place(x=120, y=247)

        fourteen_label = tk.Label(root,
                                  text="14:00",
                                  font="Helvetica 15",
                                  fg="black"
                                  )
        fourteen_label.place(x=40, y=290)

        fourteen_reservations = tk.StringVar()

        fourteen_entry = tk.Entry(root,
                                  textvar=fourteen_reservations,
                                  font="Helvetica 15",
                                  fg="black",
                                  bg="white"
                                  )
        fourteen_entry.place(x=120, y=287)

        fifteen_label = tk.Label(root,
                                 text="15:00",
                                 font="Helvetica 15",
                                 fg="black"
                                 )
        fifteen_label.place(x=40, y=330)

        fifteen_reservations = tk.StringVar()

        fifteen_entry = tk.Entry(root,
                                 textvar=fifteen_reservations,
                                 font="Helvetica 15",
                                 fg="black",
                                 bg="white"
                                 )
        fifteen_entry.place(x=120, y=327)

        sixteen_label = tk.Label(root,
                                 text="16:00",
                                 font="Helvetica 15",
                                 fg="black"
                                 )
        sixteen_label.place(x=40, y=370)

        sixteen_reservations = tk.StringVar()

        sixteen_entry = tk.Entry(root,
                                 textvar=sixteen_reservations,
                                 font="Helvetica 15",
                                 fg="black",
                                 bg="white"
                                 )
        sixteen_entry.place(x=120, y=367)

        seventeen_label = tk.Label(root,
                                   text="17:00",
                                   font="Helvetica 15",
                                   fg="black"
                                   )
        seventeen_label.place(x=40, y=410)

        seventeen_reservations = tk.StringVar()

        seventeen_entry = tk.Entry(root,
                                   textvar=seventeen_reservations,
                                   font="Helvetica 15",
                                   fg="black",
                                   bg="white"
                                   )
        seventeen_entry.place(x=120, y=407)

        eighteen_label = tk.Label(root,
                                  text="18:00",
                                  font="Helvetica 15",
                                  fg="black"
                                  )
        eighteen_label.place(x=40, y=450)

        eighteen_reservations = tk.StringVar()

        eighteen_entry = tk.Entry(root,
                                  textvar=eighteen_reservations,
                                  font="Helvetica 15",
                                  fg="black",
                                  bg="white"
                                  )
        eighteen_entry.place(x=120, y=447)


        back_button_14 = tk.Button(root,
                                   text="Back",
                                   command=back_14,
                                   font="Helvetica 16 bold",
                                   fg="black"
                                   )
        back_button_14.place(x=180, y=565)

def back_14():

    f1.destroy()
    reservation_label.destroy()
    back_button_14.destroy()

    shopkeeper_home_page()

# create a page for every day of the week with the same attributes as above
def monday():

    global reservation_label
    global monday_label
    global left_button
    global right_button
    global nine_label
    global nine_entry
    global ten_label
    global ten_entry
    global eleven_label
    global eleven_entry
    global twelve_label
    global twelve_entry
    global thirteen_label
    global thirteen_entry
    global fourteen_label
    global fourteen_entry
    global fifteen_label
    global fifteen_entry
    global sixteen_label
    global sixteen_entry
    global seventeen_label
    global seventeen_entry
    global eighteen_label
    global eighteen_entry
    global back_button_14

    root.geometry('450x600')

    f1.destroy()
    reservation_label.destroy()
    back_button_14.destroy()
    sunday_label.destroy()
    left_button.destroy()
    right_button.destroy()
    nine_label.destroy()
    nine_entry.destroy()
    ten_label.destroy()
    ten_entry.destroy()
    eleven_label.destroy()
    eleven_entry.destroy()
    twelve_label.destroy()
    twelve_entry.destroy()
    thirteen_label.destroy()
    thirteen_entry.destroy()
    fourteen_label.destroy()
    fourteen_entry.destroy()
    fifteen_label.destroy()
    fifteen_entry.destroy()
    sixteen_label.destroy()
    sixteen_entry.destroy()
    seventeen_label.destroy()
    seventeen_entry.destroy()
    eighteen_label.destroy()
    eighteen_entry.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    reservation_label = tk.Label(root,
                                 text="Reservations for this table:",
                                 font="Rockwell 12",
                                 fg="green"
                                 )
    reservation_label.place(x=140, y=10)

    monday_label = tk.Label(root,
                            text="Monday",
                            font="Helvetica 25",
                            fg="green"
                            )
    monday_label.place(x=172, y=35)

    left_button = tk.Button(root,
                            text="<<",
                            command=reservations,
                            font="Helvetica 15",
                            fg="black"
                            )
    left_button.place(x=116, y=37)

    right_button = tk.Button(root,
                             text=">>",
                             command=tuesday,
                             font="Helvetica 15",
                             fg="black"
                             )
    right_button.place(x=270, y=37)

    nine_label = tk.Label(root,
                          text="09:00",
                          font="Helvetica 15",
                          fg="black"
                          )
    nine_label.place(x=40, y=90)

    nine_reservations = tk.StringVar()

    nine_entry = tk.Entry(root,
                          textvar=nine_reservations,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    nine_entry.place(x=120, y=87)

    ten_label = tk.Label(root,
                         text="10:00",
                         font="Helvetica 15",
                         fg="black"
                         )
    ten_label.place(x=40, y=130)

    ten_reservations = tk.StringVar()

    ten_entry = tk.Entry(root,
                         textvar=ten_reservations,
                         font="Helvetica 15",
                         fg="black",
                         bg="white"
                         )
    ten_entry.place(x=120, y=127)

    eleven_label = tk.Label(root,
                            text="11:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    eleven_label.place(x=40, y=170)

    eleven_reservations = tk.StringVar()

    eleven_entry = tk.Entry(root,
                            textvar=eleven_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    eleven_entry.place(x=120, y=167)

    twelve_label = tk.Label(root,
                            text="12:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    twelve_label.place(x=40, y=210)

    twelve_reservations = tk.StringVar()

    twelve_entry = tk.Entry(root,
                            textvar=twelve_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    twelve_entry.place(x=120, y=207)

    thirteen_label = tk.Label(root,
                              text="13:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    thirteen_label.place(x=40, y=250)

    thirteen_reservations = tk.StringVar()

    thirteen_entry = tk.Entry(root,
                              textvar=thirteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    thirteen_entry.place(x=120, y=247)

    fourteen_label = tk.Label(root,
                              text="14:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    fourteen_label.place(x=40, y=290)

    fourteen_reservations = tk.StringVar()

    fourteen_entry = tk.Entry(root,
                              textvar=fourteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    fourteen_entry.place(x=120, y=287)

    fifteen_label = tk.Label(root,
                             text="15:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    fifteen_label.place(x=40, y=330)

    fifteen_reservations = tk.StringVar()

    fifteen_entry = tk.Entry(root,
                             textvar=fifteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    fifteen_entry.place(x=120, y=327)

    sixteen_label = tk.Label(root,
                             text="16:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    sixteen_label.place(x=40, y=370)

    sixteen_reservations = tk.StringVar()

    sixteen_entry = tk.Entry(root,
                             textvar=sixteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    sixteen_entry.place(x=120, y=367)

    seventeen_label = tk.Label(root,
                               text="17:00",
                               font="Helvetica 15",
                               fg="black"
                               )
    seventeen_label.place(x=40, y=410)

    seventeen_reservations = tk.StringVar()

    seventeen_entry = tk.Entry(root,
                               textvar=seventeen_reservations,
                               font="Helvetica 15",
                               fg="black",
                               bg="white"
                               )
    seventeen_entry.place(x=120, y=407)

    eighteen_label = tk.Label(root,
                              text="18:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    eighteen_label.place(x=40, y=450)

    eighteen_reservations = tk.StringVar()

    eighteen_entry = tk.Entry(root,
                              textvar=eighteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    eighteen_entry.place(x=120, y=447)

    back_button_14 = tk.Button(root,
                               text="Back",
                               command=back_14,
                               font="Helvetica 16 bold",
                               fg="black"
                               )
    back_button_14.place(x=180, y=565)

def tuesday():
    global reservation_label
    global back_button_14
    global tuesday_label
    global left_button
    global right_button
    global nine_label
    global nine_entry
    global ten_label
    global ten_entry
    global eleven_label
    global eleven_entry
    global twelve_label
    global twelve_entry
    global thirteen_label
    global thirteen_entry
    global fourteen_label
    global fourteen_entry
    global fifteen_label
    global fifteen_entry
    global sixteen_label
    global sixteen_entry
    global seventeen_label
    global seventeen_entry
    global eighteen_label
    global eighteen_entry

    root.geometry('450x600')

    f1.destroy()
    reservation_label.destroy()
    back_button_14.destroy()
    monday_label.destroy()
    left_button.destroy()
    right_button.destroy()
    nine_label.destroy()
    nine_entry.destroy()
    ten_label.destroy()
    ten_entry.destroy()
    eleven_label.destroy()
    eleven_entry.destroy()
    twelve_label.destroy()
    twelve_entry.destroy()
    thirteen_label.destroy()
    thirteen_entry.destroy()
    fourteen_label.destroy()
    fourteen_entry.destroy()
    fifteen_label.destroy()
    fifteen_entry.destroy()
    sixteen_label.destroy()
    sixteen_entry.destroy()
    seventeen_label.destroy()
    seventeen_entry.destroy()
    eighteen_label.destroy()
    eighteen_entry.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    reservation_label = tk.Label(root,
                                 text="Reservations for this table:",
                                 font="Rockwell 12",
                                 fg="green"
                                 )
    reservation_label.place(x=140, y=10)

    tuesday_label = tk.Label(root,
                             text="Tuesday",
                             font="Helvetica 25",
                             fg="green"
                             )
    tuesday_label.place(x=170, y=35)

    left_button = tk.Button(root,
                            text="<<",
                            command=monday,
                            font="Helvetica 15",
                            fg="black"
                            )
    left_button.place(x=113, y=37)

    right_button = tk.Button(root,
                             text=">>",
                             command=wednesday,
                             font="Helvetica 15",
                             fg="black"
                             )
    right_button.place(x=275, y=37)

    nine_label = tk.Label(root,
                          text="09:00",
                          font="Helvetica 15",
                          fg="black"
                          )
    nine_label.place(x=40, y=90)

    nine_reservations = tk.StringVar()

    nine_entry = tk.Entry(root,
                          textvar=nine_reservations,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    nine_entry.place(x=120, y=87)

    ten_label = tk.Label(root,
                         text="10:00",
                         font="Helvetica 15",
                         fg="black"
                         )
    ten_label.place(x=40, y=130)

    ten_reservations = tk.StringVar()

    ten_entry = tk.Entry(root,
                         textvar=ten_reservations,
                         font="Helvetica 15",
                         fg="black",
                         bg="white"
                         )
    ten_entry.place(x=120, y=127)

    eleven_label = tk.Label(root,
                            text="11:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    eleven_label.place(x=40, y=170)

    eleven_reservations = tk.StringVar()

    eleven_entry = tk.Entry(root,
                            textvar=eleven_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    eleven_entry.place(x=120, y=167)

    twelve_label = tk.Label(root,
                            text="12:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    twelve_label.place(x=40, y=210)

    twelve_reservations = tk.StringVar()

    twelve_entry = tk.Entry(root,
                            textvar=twelve_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    twelve_entry.place(x=120, y=207)

    thirteen_label = tk.Label(root,
                              text="13:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    thirteen_label.place(x=40, y=250)

    thirteen_reservations = tk.StringVar()

    thirteen_entry = tk.Entry(root,
                              textvar=thirteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    thirteen_entry.place(x=120, y=247)

    fourteen_label = tk.Label(root,
                              text="14:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    fourteen_label.place(x=40, y=290)

    fourteen_reservations = tk.StringVar()

    fourteen_entry = tk.Entry(root,
                              textvar=fourteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    fourteen_entry.place(x=120, y=287)

    fifteen_label = tk.Label(root,
                             text="15:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    fifteen_label.place(x=40, y=330)

    fifteen_reservations = tk.StringVar()

    fifteen_entry = tk.Entry(root,
                             textvar=fifteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    fifteen_entry.place(x=120, y=327)

    sixteen_label = tk.Label(root,
                             text="16:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    sixteen_label.place(x=40, y=370)

    sixteen_reservations = tk.StringVar()

    sixteen_entry = tk.Entry(root,
                             textvar=sixteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    sixteen_entry.place(x=120, y=367)

    seventeen_label = tk.Label(root,
                               text="17:00",
                               font="Helvetica 15",
                               fg="black"
                               )
    seventeen_label.place(x=40, y=410)

    seventeen_reservations = tk.StringVar()

    seventeen_entry = tk.Entry(root,
                               textvar=seventeen_reservations,
                               font="Helvetica 15",
                               fg="black",
                               bg="white"
                               )
    seventeen_entry.place(x=120, y=407)

    eighteen_label = tk.Label(root,
                              text="18:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    eighteen_label.place(x=40, y=450)

    eighteen_reservations = tk.StringVar()

    eighteen_entry = tk.Entry(root,
                              textvar=eighteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    eighteen_entry.place(x=120, y=447)

    back_button_14 = tk.Button(root,
                               text="Back",
                               command=back_14,
                               font="Helvetica 16 bold",
                               fg="black"
                               )
    back_button_14.place(x=180, y=565)

def wednesday():
    global reservation_label
    global back_button_14
    global wednesday_label
    global left_button
    global right_button
    global nine_label
    global nine_entry
    global ten_label
    global ten_entry
    global eleven_label
    global eleven_entry
    global twelve_label
    global twelve_entry
    global thirteen_label
    global thirteen_entry
    global fourteen_label
    global fourteen_entry
    global fifteen_label
    global fifteen_entry
    global sixteen_label
    global sixteen_entry
    global seventeen_label
    global seventeen_entry
    global eighteen_label
    global eighteen_entry

    root.geometry('450x600')

    f1.destroy()
    reservation_label.destroy()
    tuesday_label.destroy()
    left_button.destroy()
    right_button.destroy()
    nine_label.destroy()
    nine_entry.destroy()
    ten_label.destroy()
    ten_entry.destroy()
    eleven_label.destroy()
    eleven_entry.destroy()
    twelve_label.destroy()
    twelve_entry.destroy()
    thirteen_label.destroy()
    thirteen_entry.destroy()
    fourteen_label.destroy()
    fourteen_entry.destroy()
    fifteen_label.destroy()
    fifteen_entry.destroy()
    sixteen_label.destroy()
    sixteen_entry.destroy()
    seventeen_label.destroy()
    seventeen_entry.destroy()
    eighteen_label.destroy()
    eighteen_entry.destroy()
    back_button_14.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    reservation_label = tk.Label(root,
                                 text="Reservations for this table:",
                                 font="Rockwell 12",
                                 fg="green"
                                 )
    reservation_label.place(x=140, y=10)

    wednesday_label = tk.Label(root,
                               text="Wednesday",
                               font="Helvetica 25",
                               fg="green"
                               )
    wednesday_label.place(x=150, y=35)

    left_button = tk.Button(root,
                            text="<<",
                            command=tuesday,
                            font="Helvetica 15",
                            fg="black"
                            )
    left_button.place(x=91, y=37)

    right_button = tk.Button(root,
                             text=">>",
                             command=thursday,
                             font="Helvetica 15",
                             fg="black"
                             )
    right_button.place(x=293, y=37)

    nine_label = tk.Label(root,
                          text="09:00",
                          font="Helvetica 15",
                          fg="black"
                          )
    nine_label.place(x=40, y=90)

    nine_reservations = tk.StringVar()

    nine_entry = tk.Entry(root,
                          textvar=nine_reservations,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    nine_entry.place(x=120, y=87)

    ten_label = tk.Label(root,
                         text="10:00",
                         font="Helvetica 15",
                         fg="black"
                         )
    ten_label.place(x=40, y=130)

    ten_reservations = tk.StringVar()

    ten_entry = tk.Entry(root,
                         textvar=ten_reservations,
                         font="Helvetica 15",
                         fg="black",
                         bg="white"
                         )
    ten_entry.place(x=120, y=127)

    eleven_label = tk.Label(root,
                            text="11:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    eleven_label.place(x=40, y=170)

    eleven_reservations = tk.StringVar()

    eleven_entry = tk.Entry(root,
                            textvar=eleven_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    eleven_entry.place(x=120, y=167)

    twelve_label = tk.Label(root,
                            text="12:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    twelve_label.place(x=40, y=210)

    twelve_reservations = tk.StringVar()

    twelve_entry = tk.Entry(root,
                            textvar=twelve_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    twelve_entry.place(x=120, y=207)

    thirteen_label = tk.Label(root,
                              text="13:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    thirteen_label.place(x=40, y=250)

    thirteen_reservations = tk.StringVar()

    thirteen_entry = tk.Entry(root,
                              textvar=thirteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    thirteen_entry.place(x=120, y=247)

    fourteen_label = tk.Label(root,
                              text="14:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    fourteen_label.place(x=40, y=290)

    fourteen_reservations = tk.StringVar()

    fourteen_entry = tk.Entry(root,
                              textvar=fourteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    fourteen_entry.place(x=120, y=287)

    fifteen_label = tk.Label(root,
                             text="15:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    fifteen_label.place(x=40, y=330)

    fifteen_reservations = tk.StringVar()

    fifteen_entry = tk.Entry(root,
                             textvar=fifteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    fifteen_entry.place(x=120, y=327)

    sixteen_label = tk.Label(root,
                             text="16:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    sixteen_label.place(x=40, y=370)

    sixteen_reservations = tk.StringVar()

    sixteen_entry = tk.Entry(root,
                             textvar=sixteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    sixteen_entry.place(x=120, y=367)

    seventeen_label = tk.Label(root,
                               text="17:00",
                               font="Helvetica 15",
                               fg="black"
                               )
    seventeen_label.place(x=40, y=410)

    seventeen_reservations = tk.StringVar()

    seventeen_entry = tk.Entry(root,
                               textvar=seventeen_reservations,
                               font="Helvetica 15",
                               fg="black",
                               bg="white"
                               )
    seventeen_entry.place(x=120, y=407)

    eighteen_label = tk.Label(root,
                              text="18:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    eighteen_label.place(x=40, y=450)

    eighteen_reservations = tk.StringVar()

    eighteen_entry = tk.Entry(root,
                              textvar=eighteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    eighteen_entry.place(x=120, y=447)

    back_button_14 = tk.Button(root,
                               text="Back",
                               command=back_14,
                               font="Helvetica 16 bold",
                               fg="black"
                               )
    back_button_14.place(x=180, y=565)

def thursday():
    global reservation_label
    global back_button_14
    global thursday_label
    global left_button
    global right_button
    global nine_label
    global nine_entry
    global ten_label
    global ten_entry
    global eleven_label
    global eleven_entry
    global twelve_label
    global twelve_entry
    global thirteen_label
    global thirteen_entry
    global fourteen_label
    global fourteen_entry
    global fifteen_label
    global fifteen_entry
    global sixteen_label
    global sixteen_entry
    global seventeen_label
    global seventeen_entry
    global eighteen_label
    global eighteen_entry

    root.geometry('450x600')

    f1.destroy()
    reservation_label.destroy()
    back_button_14.destroy()
    wednesday_label.destroy()
    left_button.destroy()
    right_button.destroy()
    nine_label.destroy()
    nine_entry.destroy()
    ten_label.destroy()
    ten_entry.destroy()
    eleven_label.destroy()
    eleven_entry.destroy()
    twelve_label.destroy()
    twelve_entry.destroy()
    thirteen_label.destroy()
    thirteen_entry.destroy()
    fourteen_label.destroy()
    fourteen_entry.destroy()
    fifteen_label.destroy()
    fifteen_entry.destroy()
    sixteen_label.destroy()
    sixteen_entry.destroy()
    seventeen_label.destroy()
    seventeen_entry.destroy()
    eighteen_label.destroy()
    eighteen_entry.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    reservation_label = tk.Label(root,
                                 text="Reservations for this table:",
                                 font="Rockwell 12",
                                 fg="green"
                                 )
    reservation_label.place(x=140, y=10)

    thursday_label = tk.Label(root,
                              text="Thursday",
                              font="Helvetica 25",
                              fg="green"
                              )
    thursday_label.place(x=165, y=35)

    left_button = tk.Button(root,
                            text="<<",
                            command=wednesday,
                            font="Helvetica 15",
                            fg="black"
                            )
    left_button.place(x=107, y=37)

    right_button = tk.Button(root,
                             text=">>",
                             command=friday,
                             font="Helvetica 15",
                             fg="black"
                             )
    right_button.place(x=279, y=37)

    nine_label = tk.Label(root,
                          text="09:00",
                          font="Helvetica 15",
                          fg="black"
                          )
    nine_label.place(x=40, y=90)

    nine_reservations = tk.StringVar()

    nine_entry = tk.Entry(root,
                          textvar=nine_reservations,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    nine_entry.place(x=120, y=87)

    ten_label = tk.Label(root,
                         text="10:00",
                         font="Helvetica 15",
                         fg="black"
                         )
    ten_label.place(x=40, y=130)

    ten_reservations = tk.StringVar()

    ten_entry = tk.Entry(root,
                         textvar=ten_reservations,
                         font="Helvetica 15",
                         fg="black",
                         bg="white"
                         )
    ten_entry.place(x=120, y=127)

    eleven_label = tk.Label(root,
                            text="11:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    eleven_label.place(x=40, y=170)

    eleven_reservations = tk.StringVar()

    eleven_entry = tk.Entry(root,
                            textvar=eleven_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    eleven_entry.place(x=120, y=167)

    twelve_label = tk.Label(root,
                            text="12:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    twelve_label.place(x=40, y=210)

    twelve_reservations = tk.StringVar()

    twelve_entry = tk.Entry(root,
                            textvar=twelve_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    twelve_entry.place(x=120, y=207)

    thirteen_label = tk.Label(root,
                              text="13:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    thirteen_label.place(x=40, y=250)

    thirteen_reservations = tk.StringVar()

    thirteen_entry = tk.Entry(root,
                              textvar=thirteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    thirteen_entry.place(x=120, y=247)

    fourteen_label = tk.Label(root,
                              text="14:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    fourteen_label.place(x=40, y=290)

    fourteen_reservations = tk.StringVar()

    fourteen_entry = tk.Entry(root,
                              textvar=fourteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    fourteen_entry.place(x=120, y=287)

    fifteen_label = tk.Label(root,
                             text="15:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    fifteen_label.place(x=40, y=330)

    fifteen_reservations = tk.StringVar()

    fifteen_entry = tk.Entry(root,
                             textvar=fifteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    fifteen_entry.place(x=120, y=327)

    sixteen_label = tk.Label(root,
                             text="16:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    sixteen_label.place(x=40, y=370)

    sixteen_reservations = tk.StringVar()

    sixteen_entry = tk.Entry(root,
                             textvar=sixteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    sixteen_entry.place(x=120, y=367)

    seventeen_label = tk.Label(root,
                               text="17:00",
                               font="Helvetica 15",
                               fg="black"
                               )
    seventeen_label.place(x=40, y=410)

    seventeen_reservations = tk.StringVar()

    seventeen_entry = tk.Entry(root,
                               textvar=seventeen_reservations,
                               font="Helvetica 15",
                               fg="black",
                               bg="white"
                               )
    seventeen_entry.place(x=120, y=407)

    eighteen_label = tk.Label(root,
                              text="18:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    eighteen_label.place(x=40, y=450)

    eighteen_reservations = tk.StringVar()

    eighteen_entry = tk.Entry(root,
                              textvar=eighteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    eighteen_entry.place(x=120, y=447)

    back_button_14 = tk.Button(root,
                              text="Back",
                              command=back_14,
                              font="Helvetica 16 bold",
                              fg="black"
                              )
    back_button_14.place(x=180, y=565)

def friday():
    global reservation_label
    global back_button_14
    global friday_label
    global left_button
    global right_button
    global nine_label
    global nine_entry
    global ten_label
    global ten_entry
    global eleven_label
    global eleven_entry
    global twelve_label
    global twelve_entry
    global thirteen_label
    global thirteen_entry
    global fourteen_label
    global fourteen_entry
    global fifteen_label
    global fifteen_entry
    global sixteen_label
    global sixteen_entry
    global seventeen_label
    global seventeen_entry
    global eighteen_label
    global eighteen_entry

    root.geometry('450x600')

    f1.destroy()
    reservation_label.destroy()
    back_button_14.destroy()
    thursday_label.destroy()
    left_button.destroy()
    right_button.destroy()
    nine_label.destroy()
    nine_entry.destroy()
    ten_label.destroy()
    ten_entry.destroy()
    eleven_label.destroy()
    eleven_entry.destroy()
    twelve_label.destroy()
    twelve_entry.destroy()
    thirteen_label.destroy()
    thirteen_entry.destroy()
    fourteen_label.destroy()
    fourteen_entry.destroy()
    fifteen_label.destroy()
    fifteen_entry.destroy()
    sixteen_label.destroy()
    sixteen_entry.destroy()
    seventeen_label.destroy()
    seventeen_entry.destroy()
    eighteen_label.destroy()
    eighteen_entry.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    reservation_label = tk.Label(root,
                                 text="Reservations for this table:",
                                 font="Rockwell 12",
                                 fg="green"
                                 )
    reservation_label.place(x=140, y=10)

    friday_label = tk.Label(root,
                            text="Friday",
                            font="Helvetica 25",
                            fg="green"
                            )
    friday_label.place(x=182, y=35)

    left_button = tk.Button(root,
                            text="<<",
                            command=thursday,
                            font="Helvetica 15",
                            fg="black"
                            )
    left_button.place(x=115, y=37)

    right_button = tk.Button(root,
                             text=">>",
                             command=saturday,
                             font="Helvetica 15",
                             fg="black"
                             )
    right_button.place(x=270, y=37)

    nine_label = tk.Label(root,
                          text="09:00",
                          font="Helvetica 15",
                          fg="black"
                          )
    nine_label.place(x=40, y=90)

    nine_reservations = tk.StringVar()

    nine_entry = tk.Entry(root,
                          textvar=nine_reservations,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    nine_entry.place(x=120, y=87)

    ten_label = tk.Label(root,
                         text="10:00",
                         font="Helvetica 15",
                         fg="black"
                         )
    ten_label.place(x=40, y=130)

    ten_reservations = tk.StringVar()

    ten_entry = tk.Entry(root,
                         textvar=ten_reservations,
                         font="Helvetica 15",
                         fg="black",
                         bg="white"
                         )
    ten_entry.place(x=120, y=127)

    eleven_label = tk.Label(root,
                            text="11:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    eleven_label.place(x=40, y=170)

    eleven_reservations = tk.StringVar()

    eleven_entry = tk.Entry(root,
                            textvar=eleven_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    eleven_entry.place(x=120, y=167)

    twelve_label = tk.Label(root,
                            text="12:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    twelve_label.place(x=40, y=210)

    twelve_reservations = tk.StringVar()

    twelve_entry = tk.Entry(root,
                            textvar=twelve_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    twelve_entry.place(x=120, y=207)

    thirteen_label = tk.Label(root,
                              text="13:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    thirteen_label.place(x=40, y=250)

    thirteen_reservations = tk.StringVar()

    thirteen_entry = tk.Entry(root,
                              textvar=thirteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    thirteen_entry.place(x=120, y=247)

    fourteen_label = tk.Label(root,
                              text="14:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    fourteen_label.place(x=40, y=290)

    fourteen_reservations = tk.StringVar()

    fourteen_entry = tk.Entry(root,
                              textvar=fourteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    fourteen_entry.place(x=120, y=287)

    fifteen_label = tk.Label(root,
                             text="15:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    fifteen_label.place(x=40, y=330)

    fifteen_reservations = tk.StringVar()

    fifteen_entry = tk.Entry(root,
                             textvar=fifteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    fifteen_entry.place(x=120, y=327)

    sixteen_label = tk.Label(root,
                             text="16:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    sixteen_label.place(x=40, y=370)

    sixteen_reservations = tk.StringVar()

    sixteen_entry = tk.Entry(root,
                             textvar=sixteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    sixteen_entry.place(x=120, y=367)

    seventeen_label = tk.Label(root,
                               text="17:00",
                               font="Helvetica 15",
                               fg="black"
                               )
    seventeen_label.place(x=40, y=410)

    seventeen_reservations = tk.StringVar()

    seventeen_entry = tk.Entry(root,
                               textvar=seventeen_reservations,
                               font="Helvetica 15",
                               fg="black",
                               bg="white"
                               )
    seventeen_entry.place(x=120, y=407)

    eighteen_label = tk.Label(root,
                              text="18:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    eighteen_label.place(x=40, y=450)

    eighteen_reservations = tk.StringVar()

    eighteen_entry = tk.Entry(root,
                              textvar=eighteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    eighteen_entry.place(x=120, y=447)

    back_button_14 = tk.Button(root,
                              text="Back",
                              command=back_14,
                              font="Helvetica 16 bold",
                              fg="black"
                              )
    back_button_14.place(x=180, y=565)

def saturday():
    global reservation_label
    global back_button_14
    global saturday_label
    global left_button
    global right_button
    global nine_label
    global nine_entry
    global ten_label
    global ten_entry
    global eleven_label
    global eleven_entry
    global twelve_label
    global twelve_entry
    global thirteen_label
    global thirteen_entry
    global fourteen_label
    global fourteen_entry
    global fifteen_label
    global fifteen_entry
    global sixteen_label
    global sixteen_entry
    global seventeen_label
    global seventeen_entry
    global eighteen_label
    global eighteen_entry

    root.geometry('450x600')

    f1.destroy()
    reservation_label.destroy()
    back_button_14.destroy()
    friday_label.destroy()
    left_button.destroy()
    right_button.destroy()
    nine_label.destroy()
    nine_entry.destroy()
    ten_label.destroy()
    ten_entry.destroy()
    eleven_label.destroy()
    eleven_entry.destroy()
    twelve_label.destroy()
    twelve_entry.destroy()
    thirteen_label.destroy()
    thirteen_entry.destroy()
    fourteen_label.destroy()
    fourteen_entry.destroy()
    fifteen_label.destroy()
    fifteen_entry.destroy()
    sixteen_label.destroy()
    sixteen_entry.destroy()
    seventeen_label.destroy()
    seventeen_entry.destroy()
    eighteen_label.destroy()
    eighteen_entry.destroy()

    add_image(root, file_path="pictures/reservations.jpg")

    reservation_label = tk.Label(root,
                                 text="Reservations for this table:",
                                 font="Rockwell 12",
                                 fg="green"
                                 )
    reservation_label.place(x=140, y=10)

    saturday_label = tk.Label(root,
                              text="Saturday",
                              font="Helvetica 25",
                              fg="green"
                              )
    saturday_label.place(x=165, y=35)

    left_button = tk.Button(root,
                            text="<<",
                            command=friday,
                            font="Helvetica 15",
                            fg="black"
                            )
    left_button.place(x=110, y=37)

    right_button = tk.Button(root,
                             text=">>",
                             command=reservations,
                             font="Helvetica 15",
                             fg="black"
                             )
    right_button.place(x=275, y=37)

    nine_label = tk.Label(root,
                          text="09:00",
                          font="Helvetica 15",
                          fg="black"
                          )
    nine_label.place(x=40, y=90)

    nine_reservations = tk.StringVar()

    nine_entry = tk.Entry(root,
                          textvar=nine_reservations,
                          font="Helvetica 15",
                          fg="black",
                          bg="white"
                          )
    nine_entry.place(x=120, y=87)

    ten_label = tk.Label(root,
                         text="10:00",
                         font="Helvetica 15",
                         fg="black"
                         )
    ten_label.place(x=40, y=130)

    ten_reservations = tk.StringVar()

    ten_entry = tk.Entry(root,
                         textvar=ten_reservations,
                         font="Helvetica 15",
                         fg="black",
                         bg="white"
                         )
    ten_entry.place(x=120, y=127)

    eleven_label = tk.Label(root,
                            text="11:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    eleven_label.place(x=40, y=170)

    eleven_reservations = tk.StringVar()

    eleven_entry = tk.Entry(root,
                            textvar=eleven_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    eleven_entry.place(x=120, y=167)

    twelve_label = tk.Label(root,
                            text="12:00",
                            font="Helvetica 15",
                            fg="black"
                            )
    twelve_label.place(x=40, y=210)

    twelve_reservations = tk.StringVar()

    twelve_entry = tk.Entry(root,
                            textvar=twelve_reservations,
                            font="Helvetica 15",
                            fg="black",
                            bg="white"
                            )
    twelve_entry.place(x=120, y=207)

    thirteen_label = tk.Label(root,
                              text="13:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    thirteen_label.place(x=40, y=250)

    thirteen_reservations = tk.StringVar()

    thirteen_entry = tk.Entry(root,
                              textvar=thirteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    thirteen_entry.place(x=120, y=247)

    fourteen_label = tk.Label(root,
                              text="14:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    fourteen_label.place(x=40, y=290)

    fourteen_reservations = tk.StringVar()

    fourteen_entry = tk.Entry(root,
                              textvar=fourteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    fourteen_entry.place(x=120, y=287)

    fifteen_label = tk.Label(root,
                             text="15:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    fifteen_label.place(x=40, y=330)

    fifteen_reservations = tk.StringVar()

    fifteen_entry = tk.Entry(root,
                             textvar=fifteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    fifteen_entry.place(x=120, y=327)

    sixteen_label = tk.Label(root,
                             text="16:00",
                             font="Helvetica 15",
                             fg="black"
                             )
    sixteen_label.place(x=40, y=370)

    sixteen_reservations = tk.StringVar()

    sixteen_entry = tk.Entry(root,
                             textvar=sixteen_reservations,
                             font="Helvetica 15",
                             fg="black",
                             bg="white"
                             )
    sixteen_entry.place(x=120, y=367)

    seventeen_label = tk.Label(root,
                               text="17:00",
                               font="Helvetica 15",
                               fg="black"
                               )
    seventeen_label.place(x=40, y=410)

    seventeen_reservations = tk.StringVar()

    seventeen_entry = tk.Entry(root,
                               textvar=seventeen_reservations,
                               font="Helvetica 15",
                               fg="black",
                               bg="white"
                               )
    seventeen_entry.place(x=120, y=407)

    eighteen_label = tk.Label(root,
                              text="18:00",
                              font="Helvetica 15",
                              fg="black"
                              )
    eighteen_label.place(x=40, y=450)

    eighteen_reservations = tk.StringVar()

    eighteen_entry = tk.Entry(root,
                              textvar=eighteen_reservations,
                              font="Helvetica 15",
                              fg="black",
                              bg="white"
                              )
    eighteen_entry.place(x=120, y=447)

    back_button_14 = tk.Button(root,
                               text="Back",
                               command=back_14,
                               font="Helvetica 16 bold",
                               fg="black"
                               )
    back_button_14.place(x=180, y=565)

# start with executing the homepage
home_page()

# this code executes the entire code
root.mainloop()