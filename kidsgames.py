"""
File: kidsgames.py
----------------
This Program creates three Educational games for kids
- Word Game
    shows a picture and gives the name of the picture with a letter missing in it
    it provides 3 options of missing letter and user needs to select the correct missing letter.
    This helps kids in learning words
- Alphabet Game
    Shows an Upper case Alphabet and gives 3 options with the Lower case Alphabets
    User has to select the correct Lower Case Alphabet.
    This helps kids in learning Upper case and Lower Case Alphabets.
- Counting Game
    User has to count the number of balls shown
    and select the correct number from the 3 options of numbers provided.
    This helps kids in learning counting numbers.
"""


import tkinter
import time
from PIL import ImageTk,Image
import random
import string
from playsound import playsound

CANVAS_WIDTH = 800      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels

WORD_GAME_IMAGE_SIZE = 300
WORD_GAME_IMAGE_POSITION = 15
WORD_GAME_BUTTON_BASE_WIDTH = 400
WORD_GAME_LABEL_WIDTH = 500
WORD_GAME_LABEL_HEIGHT = 250

ALPHABET_GAME_BUTTON_BASE_WIDTH = 250

COUNT_GAME_BUTTON_BASE_WIDTH = 400
BALL_SIZE = 50
BALL_DIST_APART = 20
BALL_SIZE_UPPER = 90
NUM_OF_COLS = 5
MAX_NUMBERS = 20

BUTTON_HEIGHT = 400
NUM_OF_BUTTONS = 3

FONT = "Calibri"

HOME_PAGE_COLOR = 'skyblue'
COUNTING_PAGE_COLOR = 'palegreen'
ALPHABET_PAGE_COLOR = 'turquoise'
WORD_PAGE_COLOR = 'white'

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Kids Educational Games')
    create_game_select_page(canvas)

def create_game_select_page(canvas):
    """
    This creates 3 Game buttons to be selected from.
    :param canvas: canvas to be used
    :return: None
    """
    change_canvas_color(canvas, HOME_PAGE_COLOR)
    buttons_text_list = ['Word Game', 'Alphabets', 'Counting']
    buttons_width = [200, 550, 380]
    buttons_height = [200, 200, 350]
    buttons = []
    for i in range(NUM_OF_BUTTONS):
        btn = tkinter.Button(canvas, text=buttons_text_list[i], fg='blue', font=(FONT, 50),
                         command=lambda j=i: select_game(canvas, buttons_text_list[j]))
        canvas.create_window(buttons_width[i], buttons_height[i] , window=btn)
        buttons.append(btn)
    canvas.mainloop()

def select_game(canvas, game_string):
    """
    This checks the game that is selected by button press and loads the
    canvas with that specific game page.
    :param canvas: canvas to be used
    :param game_string: string with name of game selected
    :return: None
    """
    canvas_sleep_delete(canvas, 1/50)
    if game_string == 'Word Game':
        create_word_game_page(canvas)
    elif game_string == 'Alphabets':
        create_alphabet_game_page(canvas)
    elif game_string == 'Counting':
        create_counting_page(canvas)

"""
Word Game APIs
"""
def create_word_game_page(canvas):
    """
    This Loads the word game page.
    page has an image for word, respective text label with a missing letter,
    3 buttons with answer options
    and a home button
    word is selected randomly
    :param canvas: canvas to be used
    :return: None
    """
    word_list = ['CAT', 'RAT', 'BAT', 'MAT', 'HAT', 'PIG', 'SUN', 'PEN', 'HEN', 'JAR', 'CAP', 'CAR', 'DOG',
                 'ANT', 'EGG', 'BEE', 'BUS', 'NUT', 'BED', 'FAN', 'TEN', 'MUG', 'NET', 'MAP', 'PAN', 'TUB',
                 'TREE', 'KITE', 'CAKE', 'BALL', 'FISH', 'HAND', 'DUCK', 'STAR', 'FROG', 'DRUM', 'FLAG']

    word_index = random.randint(0, len(word_list) - 1)
    word = word_list[word_index]

    change_canvas_color(canvas, WORD_PAGE_COLOR)
    img = get_image(word)
    canvas.create_image(WORD_GAME_IMAGE_POSITION, WORD_GAME_IMAGE_POSITION, anchor=tkinter.NW, image=img)

    create_home_button(canvas)

    test_text, missing_letter_idx = get_test_word_text(word)

    canvas.create_text(WORD_GAME_LABEL_WIDTH, WORD_GAME_LABEL_HEIGHT, anchor=tkinter.CENTER, font=(FONT, 100), fill='blue',
                       text=test_text)

    create_word_buttons(canvas, word, missing_letter_idx)
    canvas.mainloop()

def get_image(word):
    """
    This gets the image to be loaded on the word game page for the word selected
    for the the game.
    :param word: Word to be used to get the specific image
    :return: image of specific word given
    """
    image_name = 'images/' + word + '.png'
    image = Image.open(image_name)
    image = image.resize((WORD_GAME_IMAGE_SIZE, WORD_GAME_IMAGE_SIZE), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    return img

def get_test_word_text(word):
    """
    This forms the Word string with a missing letter
    and also gives information on which letter index is made missing.
    missing letter index is chosen by random each time.
    :param word: word to be used for the game.
    :return: test_text : text to be displayed with a missing letter
             missing_letter_index: index of letter that is missing in the word
    """
    word_len = len(word)
    missing_letter_idx = random.randint(0, word_len - 1)
    test_text = ""
    for i in range(word_len):
        if i == missing_letter_idx:
            test_text = test_text + '_'
        else:
            test_text = test_text + word[i]
    return test_text, missing_letter_idx

def create_word_buttons(canvas, word, missing_letter_idx):
    """
    This creates 3 buttons from which the missing letter can be chosen.
    :param canvas: canvas to be used
    :param word: word to be used for the game.
    :param missing_letter_idx: index of letter that is missing in the word
    :return: None
    """
    btn_text_list = get_word_button_text_list(word, missing_letter_idx)
    buttons = []  # store the buttons created
    for i in range(NUM_OF_BUTTONS):
        btn = tkinter.Button(canvas, text=btn_text_list[i], fg='black', font=(FONT, 70), width=2,
                             command=lambda j = i: check_word(canvas, btn_text_list[j], word))
        canvas.create_window(WORD_GAME_BUTTON_BASE_WIDTH + i * 100, BUTTON_HEIGHT, window=btn)
        buttons.append(btn)

def get_word_button_text_list(word, missing_letter_idx):
    """
    This creates text to be put on 3 buttons
    with 1 button having the answer of missing letter as text on it.
    the button to have answer is chosen randomly.
    other 2 buttons will have a random letter as text on them.
    :param word: word to be used for the game.
    :param missing_letter_idx: index of letter that is missing in the word
    :return: list of texts to be displayed on buttons.
    """
    ans_btn_index = random.randint(0, NUM_OF_BUTTONS - 1)
    btn_text_list = []
    for i in range(NUM_OF_BUTTONS):
        if i == ans_btn_index:
            btn_text_list.append(word[missing_letter_idx])
        else:
            btn_letter = random.choice(string.ascii_uppercase)
            while (btn_letter in btn_text_list) or (btn_letter == word[missing_letter_idx]):
                btn_letter = random.choice(string.ascii_uppercase)
            btn_text_list.append(btn_letter)
    return btn_text_list

def check_word(canvas, pressed_letter, word):
    """
    This checks if the letter pressed is the correct answer.
    if it is correct it will print the complete word and
    loads the page with next word to be guessed
    :param canvas: canvas to be used
    :param pressed_letter: text on button that is pressed
    :param word: word used for the game.
    :return: None
    """
    if pressed_letter in word:
        canvas_sleep_delete(canvas, 1 / 50)
        img = get_image(word)
        canvas.create_image(WORD_GAME_IMAGE_POSITION, WORD_GAME_IMAGE_POSITION, anchor=tkinter.NW, image=img)
        canvas.create_text(WORD_GAME_LABEL_WIDTH, WORD_GAME_LABEL_HEIGHT, anchor=tkinter.CENTER, font=(FONT, 100),
                           fill='blue',
                           text=word)
        canvas.update()
        song = 'sounds/words/' + word + '.m4a'
        playsound(song)
       # pause
        canvas_sleep_delete(canvas, 1)
        create_word_game_page(canvas)

"""
Alphabet Game APIs
"""
def create_alphabet_game_page(canvas):
    """
    This Loads the Alphabet game page.
    page will have an upper case Alphabet displayed
    3 buttons with answer options
    and a home button
    Alphabet is selected randomly
    :param canvas: canvas to be used
    :return: None
    """
    change_canvas_color(canvas, 'turquoise')
    upper_case_letter = random.choice(string.ascii_uppercase)
    canvas.create_text(400, 200, anchor=tkinter.CENTER, font=(FONT, 150),
                       fill='black',
                       text=upper_case_letter)
    create_home_button(canvas)
    create_lower_alphabet_buttons(canvas, upper_case_letter)
    canvas.mainloop()

def create_lower_alphabet_buttons(canvas, upper_case_letter):
    """
    This creates 3 buttons from which the lower case alphabet can be chosen.
    :param canvas: canvas to be used
    :param upper_case_letter: Upper Case Alphabet displayed in Game
    :return: None
    """
    btn_text_list = get_alphabet_button_text_list(upper_case_letter)
    buttons = []  # store the buttons created
    for i in range(NUM_OF_BUTTONS):
        btn = tkinter.Button(canvas, text=btn_text_list[i], fg='black', font=(FONT, 100), width=2,
                             command=lambda j = i: check_alphabet(canvas, btn_text_list[j], upper_case_letter))
        canvas.create_window(ALPHABET_GAME_BUTTON_BASE_WIDTH + i * 150, BUTTON_HEIGHT, window=btn)
        buttons.append(btn)

def get_alphabet_button_text_list(upper_case_letter):
    """
    This creates text to be put on 3 buttons
    with 1 button having the answer of lower case alphabet as text on it.
    the button to have answer is chosen randomly.
    other 2 buttons will have a random lower case alphabet as text on them.
    :param upper_case_letter: Upper Case Alphabet displayed in Game
    :return: list of texts to be displayed on buttons.
    """
    ans_btn_index = random.randint(0, NUM_OF_BUTTONS - 1)
    btn_text_list = []
    for i in range(NUM_OF_BUTTONS):
        if i == ans_btn_index:
            btn_text_list.append(upper_case_letter.lower())
        else:
            btn_letter = random.choice(string.ascii_lowercase)
            while (btn_letter in btn_text_list) or (btn_letter == upper_case_letter.lower()):
                btn_letter = random.choice(string.ascii_lowercase)
            btn_text_list.append(btn_letter)
    return btn_text_list

def check_alphabet(canvas, letter_pressed, upper_case_letter):
    """
    This checks if the letter pressed is the correct answer.
    if it is correct it will print both upper and lower case alphabets and
    loads the page with next upper case alphabet to be guessed
    :param canvas: canvas to be used
    :param letter_pressed: text on button that is pressed
    :param upper_case_letter: Upper Case Letter displayed in the game
    :return: None
    """
    if letter_pressed == upper_case_letter.lower():
        canvas_sleep_delete(canvas, 1/50)
        canvas.create_text(300, 250, anchor=tkinter.CENTER, font=(FONT, 250),
                           fill='black',
                           text=upper_case_letter)
        canvas.create_text(500, 250, anchor=tkinter.CENTER, font=(FONT, 200),
                           fill='blue',
                           text=upper_case_letter.lower())
        canvas.update()
        song = 'sounds/alphabets/' + upper_case_letter + '.m4a'
        playsound(song)
       # pause
        canvas_sleep_delete(canvas, 2)
        create_alphabet_game_page(canvas)

"""
Counting game APIs
"""

def create_counting_page(canvas):
    """
    This Loads the counting game page.
    page has an number of circles to be counted
    3 buttons with answer options
    and a home button
    number of circles is selected randomly
    :param canvas: canvas to be used
    :return: None
    """
    change_canvas_color(canvas, COUNTING_PAGE_COLOR)
    number = random.randint(1, MAX_NUMBERS)
    create_circles(canvas, number)
    create_number_buttons(canvas, number)
    create_home_button(canvas)
    canvas.mainloop()

def create_circles(canvas, number):
    """
    This creates the number of circles on canvas
    with maximum of 5 circles per row.
    :param canvas: canvas to be used
    :param number: number to be used to create number of circles
    :return: None
    """
    number_rows = number//NUM_OF_COLS + 1
    for i in range(number_rows):
        if number < NUM_OF_COLS:
            num_cols = number
        else:
            num_cols = NUM_OF_COLS
        for j in range(num_cols):
            number -= 1
            canvas.create_oval(BALL_SIZE_UPPER + BALL_SIZE * j + BALL_DIST_APART,
                               BALL_SIZE_UPPER + BALL_SIZE * i + BALL_DIST_APART * i,
                               BALL_SIZE + BALL_DIST_APART + BALL_SIZE * j,
                               BALL_SIZE + BALL_SIZE * i + BALL_DIST_APART * i, fill='red', outline='red')


def create_number_buttons(canvas, number):
    """
    This creates 3 buttons from which the answer for number of circles can be chosen.
    :param canvas: canvas to be used
    :param number: number of circles displayed in game
    :return: None
    """
    btn_num_list = get_count_button_list(number)
    buttons = []  # store the buttons created
    for i in range(NUM_OF_BUTTONS):
        btn = tkinter.Button(canvas, text=btn_num_list[i], fg='black', font=(FONT, 60), width=2,
                         command=lambda j=i: check_count(canvas, btn_num_list[j], number))
        canvas.create_window(COUNT_GAME_BUTTON_BASE_WIDTH + i * 100, BUTTON_HEIGHT, window=btn)
        buttons.append(btn)

def check_count(canvas, pressed_num, number):
    """
    This checks if the number pressed is the correct answer.
    if it is correct it will print the number of circles and
    loads the page with next set of number of circles to be counted
    :param canvas: canvas to be used
    :param pressed_num: number on pressed button
    :param number: number of circles displayed in game
    :return: None
    """
    if  pressed_num == number:
        canvas_sleep_delete(canvas, 1/50)
        create_circles(canvas, number)
        canvas.create_text(500, 275, anchor=tkinter.CENTER, font=(FONT, 200),
                           fill='black',
                           text=number)
        canvas.update()
        song = 'sounds/counting/' + str(number) + '.m4a'
        playsound(song)
       # pause
        canvas_sleep_delete(canvas, 2)
        create_counting_page(canvas)

def get_count_button_list(number):
    """
    This creates text to be put on 3 buttons
    with 1 button having the answer of number of circles as text on it.
    the button to have answer is chosen randomly.
    other 2 buttons will have a random numbers as text on them.
    :param number: number of circles displayed in game
    :return: list of numbers to be displayed on buttons
    """
    ans_btn_index = random.randint(0, NUM_OF_BUTTONS - 1)
    btn_num_list = []
    for i in range(NUM_OF_BUTTONS):
        if i == ans_btn_index:
            btn_num_list.append(number)
        else:
            btn_num = random.randint(0, MAX_NUMBERS)
            while (btn_num in btn_num_list) or (btn_num == number):
                btn_num = random.randint(0, MAX_NUMBERS)
            btn_num_list.append(btn_num)
    return btn_num_list

"""
Global APIs
"""
def create_home_button(canvas):
    """
    This creates a home button
    :param canvas: canvas to be used
    :return: None
    """
    btn_home = tkinter.Button(canvas, text="HOME", fg='black', font=(FONT, 30),
                              command=lambda: go_home(canvas))
    canvas.create_window(700, 40, window=btn_home)

def go_home(canvas):
    """
    this loads canvas with page to select the game to be played
    when home button is pressed
    :param canvas: canvas to be used
    :return: None
    """
    canvas_sleep_delete(canvas, 1/50)
    create_game_select_page(canvas)

def canvas_sleep_delete(canvas, time_to_sleep):
    """
    This adds delay of time requested for and thes cleans up the
    canvas for next page load.
    :param canvas: canvas to be used
    :param time_to_sleep: sleep time
    :return: None
    """
    time.sleep(time_to_sleep)
    canvas.delete("all")

def change_canvas_color(canvas, color_name):
    """
    This sets the canvas background color to the color name specified.
    :param canvas: canvas to be used
    :param color_name: name of the color
    :return: None
    """
    canvas.configure(bg=color_name)

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
