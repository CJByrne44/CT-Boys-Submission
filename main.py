import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from database_functions import initDatabase
from database_functions import getID
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

session = initDatabase()

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Gender: "))
        self.gender = TextInput(multiline=False)
        self.inside.add_widget(self.gender)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="University: "))
        self.university = TextInput(multiline=False)
        self.inside.add_widget(self.university)

        self.inside.add_widget(Label(text="Major "))
        self.major = TextInput(multiline=False)
        self.inside.add_widget(self.major)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=25)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text
        gender = self.gender.text
        univ = self.university.text
        major = self.major.text
        # Comment test
        print("Name:\t\t\t\t\t |", name)
        print("Last Name:\t\t\t\t |", last)
        print("Gender\t\t\t\t\t |", gender)
        print("Major: \t\t\t\t\t |", major)
        print("University:\t\t\t\t |",univ)
        print("Email:\t\t\t\t\t |", email)
        self.name.text = ""
        self.lastName.text = ""
        self.gender.text = ""
        self.major.text = ""
        self.email.text = ""
        ##self.univ.text = ""

        id = getID(session)
        stmt = session.prepare("""
                        INSERT INTO users(id, first, last, university, major)
                        VALUES(?, ?, ?, ?, ?)
                        IF NOT EXISTS
                        """)
        results = session.execute(stmt, [id, name, last, univ, major])

        stmt2 = session.prepare("""
                                 SELECT (first, last, university, major) 
                                 FROM users WHERE university = ? 
                                 AND major = ? ALLOW FILTERING
                                """)
        users = session.execute(stmt2, [univ, major])
        for row in users:
            if row[0][0] != name and row[0][1] != last:
                print(row[0])

# class MyGrid(Widget):
#     firstname = ObjectProperty(None)
#     lastname =  ObjectProperty(None)
#     gender = ObjectProperty(None)
#     email = ObjectProperty(None)
#     university = ObjectProperty(None)
#     major = ObjectProperty(None)
#
#     def btn(self):
#         print("First Name:\t\t\t\t|", self.firstname.text)
#         print("Last Name:\t\t\t\t |", self.lastname.text)
#         print("Gender\t\t\t\t\t |", self.gender.text)
#         print("Major: \t\t\t\t\t |", self.major.text)
#         print("University:\t\t\t\t |", self.university.text)
#         print("Email:\t\t\t\t\t |", self.email.text)
#         id = getID(session)
#         stmt = session.prepare("""
#                         INSERT INTO users(id, first, last, university, major)
#                         VALUES(?, ?, ?, ?, ?)
#                         IF NOT EXISTS
#                         """)
#         results = session.execute(stmt, [id, name, last, univ, major])
#
#         stmt2 = session.prepare("""
#                                  SELECT (first, last, university, major)
#                                  FROM users WHERE university = ?
#                                  AND major = ? ALLOW FILTERING
#                                 """)
#         users = session.execute(stmt2, [univ, major])
#         for row in users:
#             print(row)
#
# class TestApp(App):
#     def build(self):
#
#         return MyGrid()


class TestApp(App):
    def build(self):

        return MyGrid()


if __name__ == '__main__':
    TestApp().run()