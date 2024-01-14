"""
This is the required file to play the beetle game: https://en.wikipedia.org/wiki/Beetle_(game)
Contains 5 classes:
  DiceRoll - rolls the dice to play the game
  DrawBeetle - draws the beetle parts
  Beetle - determines which parts of the beetle should be drawn
  BeetleGame - plays the game itself
"""

from random import randint
from turtle import *
from turtle import exitonclick
from turtle import textinput

import _tkinter


class DiceRoll:
    def __init__(self):
        self.dice_roll = 0
        self.dice_total = 0

    def clear_dice(self):
        self.dice_roll = 0
        self.dice_total = 0

    def roll_dice(self, num=1):
        for roll in range(num):
            self.dice_roll = randint(1, 6)
            self.dice_total += self.dice_roll
        x = self.dice_total
        self.clear_dice()
        return x


class DrawBeetle:
    def __init__(self, x_pos, y_pos, player_name):
        self.x_pos = x_pos
        self.y_pos = y_pos + 100
        self.player_name = player_name
        self.turtle_drawer = Turtle()
        self.turtle_writer = Turtle()
        self.turtle_writer.hideturtle()
        self.cursor = 0

    def print_player(self):
        self.teleport(0, -40)
        self.turtle_drawer.write(self.player_name, align="center", font=("Calibri", 20, "normal"))
        self.cursor -= 25

    def print_roll(self, roll, statement):
        if self.cursor < -380:
            self.turtle_writer.clear()
            self.cursor = -25
        self.teleport(0, -40 + self.cursor, True)
        self.turtle_writer.write(f"{self.player_name} rolled a {roll} - {statement}",
                                 align="center",
                                 font=("Calibri", 13, "normal"))
        self.cursor -= 18

    def teleport(self, x, y, writer=False):
        if not writer:
            self.turtle_drawer.penup()
            self.turtle_drawer.goto(x + self.x_pos, y + self.y_pos)
            self.turtle_drawer.pendown()
        else:
            self.turtle_writer.penup()
            self.turtle_writer.goto(x + self.x_pos, y + self.y_pos)
            self.turtle_writer.pendown()

    def draw_line(self, direction, length):
        self.turtle_drawer.showturtle()
        self.turtle_drawer.setheading(direction)
        self.turtle_drawer.forward(length)
        self.turtle_drawer.hideturtle()

    def draw_oval(self, rad1, rad2=None, deg=90):
        self.turtle_drawer.showturtle()
        if not rad2:
            rad2 = rad1
        self.turtle_drawer.setheading(0)
        for i in range(2):
            self.turtle_drawer.circle(rad1, deg / 2)
            self.turtle_drawer.circle(rad2, 180 - deg)
            self.turtle_drawer.circle(rad1, deg / 2)
        self.turtle_drawer.hideturtle()

    def draw_body(self):
        self.teleport(0, 0)
        self.draw_oval(40, 100)

    def draw_head(self):
        self.teleport(0, 165)
        self.draw_oval(35)

    def draw_left_wing(self):
        self.teleport(-80, 25)
        self.draw_oval(12, 125, 130)

    def draw_right_wing(self):
        self.teleport(80, 25)
        self.draw_oval(12, 125, 130)

    def draw_top_left_leg(self):
        self.teleport(-40, 138)
        self.draw_line(140, 70)

    def draw_middle_left_leg(self):
        self.teleport(-45, 30)
        self.draw_line(210, 70)

    def draw_bottom_left_leg(self):
        self.teleport(-30, 13)
        self.draw_line(220, 70)

    def draw_top_right_leg(self):
        self.teleport(40, 138)
        self.draw_line(40, 70)

    def draw_middle_right_leg(self):
        self.teleport(45, 30)
        self.draw_line(330, 70)

    def draw_bottom_right_leg(self):
        self.teleport(30, 13)
        self.draw_line(320, 70)

    def draw_left_antenna(self):
        self.teleport(-25, 225)
        self.draw_line(110, 40)

    def draw_right_antenna(self):
        self.teleport(25, 225)
        self.draw_line(70, 40)

    def draw_left_eye(self):
        self.teleport(-15, 200)
        self.turtle_drawer.begin_fill()
        self.draw_oval(5)
        self.turtle_drawer.end_fill()

    def draw_right_eye(self):
        self.teleport(15, 200)
        self.turtle_drawer.begin_fill()
        self.draw_oval(5)
        self.turtle_drawer.end_fill()


class Beetle:
    def __init__(self, player_name, player_num):
        self.player_name = player_name
        if player_num == 1:
            self.x_pos = -250
            self.y_pos = 50
        elif player_num == 2:
            self.x_pos = 250
            self.y_pos = 50
        self.beetle = DrawBeetle(self.x_pos, self.y_pos, self.player_name)
        self.eyes = 0
        self.antenna = 0
        self.legs = 0
        self.wings = 0
        self.head = 0
        self.body = 0
        self.complete = False
        self.quit = False

    def complete_beetle(self):
        if (self.eyes == 2 and
                self.antenna == 2 and
                self.legs == 6 and
                self.wings == 2 and
                self.head == 1 and
                self.body == 1):
            self.complete = True

    def draw_part(self, die):
        if self.body == 0:
            if die != 6:
                self.beetle.print_roll(die, "nothing drawn")
            elif die == 6:
                self.beetle.print_roll(die, "body drawn")
                self.draw_body()
        else:
            if die in (1, 2):
                if self.head == 0:
                    self.beetle.print_roll(die, "nothing drawn")
                elif die == 1:
                    if self.eyes < 2:
                        self.beetle.print_roll(die, "eye drawn")
                        self.draw_eyes()
                    else:
                        self.beetle.print_roll(die, "nothing drawn")
                elif die == 2:
                    if self.antenna < 2:
                        self.beetle.print_roll(die, "antenna drawn")
                        self.draw_antenna()
                    else:
                        self.beetle.print_roll(die, "nothing drawn")
            elif die == 3:
                if self.legs < 6:
                    self.beetle.print_roll(die, "leg drawn")
                    self.draw_leg()
                else:
                    self.beetle.print_roll(die, "nothing drawn")
            elif die == 4:
                if self.wings < 2:
                    self.beetle.print_roll(die, "wing drawn")
                    self.draw_wing()
                else:
                    self.beetle.print_roll(die, "nothing drawn")
            elif die == 5:
                if self.head == 0:
                    self.beetle.print_roll(die, "head drawn")
                    self.draw_head()
                else:
                    self.beetle.print_roll(die, "nothing drawn")
            elif die == 6:
                self.beetle.print_roll(die, "nothing drawn")

    def draw_eyes(self):
        self.eyes += 1
        if self.eyes == 1:
            self.beetle.draw_left_eye()
        elif self.eyes == 2:
            self.beetle.draw_right_eye()
        return True

    def draw_antenna(self):
        self.antenna += 1
        if self.antenna == 1:
            self.beetle.draw_left_antenna()
        elif self.antenna == 2:
            self.beetle.draw_right_antenna()
        return True

    def draw_leg(self):
        self.legs += 1
        if self.legs == 1:
            self.beetle.draw_top_left_leg()
        elif self.legs == 2:
            self.beetle.draw_middle_left_leg()
        elif self.legs == 3:
            self.beetle.draw_bottom_left_leg()
        elif self.legs == 4:
            self.beetle.draw_top_right_leg()
        elif self.legs == 5:
            self.beetle.draw_middle_right_leg()
        elif self.legs == 6:
            self.beetle.draw_bottom_right_leg()
        return True

    def draw_wing(self):
        self.wings += 1
        if self.wings == 1:
            self.beetle.draw_left_wing()
        elif self.wings == 2:
            self.beetle.draw_right_wing()
        return True

    def draw_head(self):
        self.head += 1
        self.beetle.draw_head()
        return True

    def draw_body(self):
        self.body += 1
        self.beetle.draw_body()
        return True

    def quit_game(self):
        self.quit = True

    def roll(self, dice_roll):
        self.draw_part(dice_roll)
        self.complete_beetle()

    def game_over(self):
        if self.complete or self.quit:
            return True

    def print_beetle(self):
        print(f"body: {self.body}")
        print(f"head: {self.head}")
        print(f"wings: {self.wings}")
        print(f"legs: {self.legs}")
        print(f"antenna: {self.antenna}")
        print(f"eyes: {self.eyes}")


class BeetleGame:
    def __init__(self):
        self.players = {}
        self.beetle_screen = Turtle()
        self.beetle_screen.hideturtle()
        self.beetle_screen.penup()
        self.beetle_screen.write("Welcome to the Beetle game!", align="center", font=("Calibri", 40, "bold"))

    def initialise_game(self):
        while True:
            computer_or_2_player = textinput("Number of players?",
                                             "Type 1 to play against computer or 2 to play against another player")
            if computer_or_2_player in ("1", "2"):
                break
        player_names = []
        if computer_or_2_player == "1":
            player_names.append(textinput("Player name", f"Insert player name"))
            player_names.append("Computer")
        elif computer_or_2_player == "2":
            player_names.append(textinput("Player name", f"Insert player 1 name"))
            player_names.append(textinput("Player name", f"Insert player 2 name"))
        for index, player_name in enumerate(player_names):
            self.add_player(player_name, index+1)

    def add_player(self, player_name, player_num):
        if player_num == 1:
            self.beetle_screen.clear()
        self.players[player_name] = Beetle(player_name, player_num)
        self.players[player_name].beetle.turtle_drawer.hideturtle()
        self.players[player_name].beetle.print_player()

    def play_game(self):
        while not self.game_over():
            for player_name in self.players:
                self.roll_or_quit(player_name)
                if self.game_over():
                    break

    def roll_or_quit(self, player_name):
        if player_name == "Computer":
            user_input = "r"
        else:
            while True:
                try:
                    user_input = textinput(f"{player_name}", f"{player_name}, roll or quit:")
                except EOFError:
                    user_input = "q"
                if user_input in ("roll", "quit", "r", "q"):
                    break

        try:
            if user_input[0] == "r":
                dice = DiceRoll()
                dice_roll = dice.roll_dice()
                self.players[player_name].roll(dice_roll)
            elif user_input[0] == "q":
                self.players[player_name].quit_game()
        except ValueError:
            self.players[player_name].quit_game()

    def game_over(self):
        for player_name in self.players:
            if self.players[player_name].game_over():
                try:
                    self.beetle_screen.setposition(0, 300)
                except _tkinter.TclError:
                    pass
                else:
                    if self.players[player_name].quit:
                        self.beetle_screen.write(f"{player_name} quit game",
                                                 align="center",
                                                 font=("Calibri", 30, "bold"))
                    elif self.players[player_name].complete and player_name != "Computer":
                        self.beetle_screen.write(f"Congrats {player_name}, you drew a beetle!!!",
                                                 align="center",
                                                 font=("Calibri", 30, "bold"))
                    elif self.players[player_name].complete and player_name == "Computer":
                        self.beetle_screen.write(f"Computer won...", align="center", font=("Calibri", 30, "bold"))
                    exitonclick()
                return True
        return False
