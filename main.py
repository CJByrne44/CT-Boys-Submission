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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

session = initDatabase()

Builder.load_string("""
<MainWindow>:
    name: "main"
    Button:
        text: "Sign Up"
        on_release:
            root.manager.current = "signup"

<SignUp>
    name: "signup"
    firstname: firstname
    lastname: lastname
    gender: gender
    email: email
    university: university
    major: major

    GridLayout:
        cols:1
        size: root.width, root.height

        GridLayout:
            cols:2

            Label:
                text:   "First Name: "
            TextInput:
                id: firstname
                multinline: False

            Label:
                text:   "Last Name: "
            TextInput:
                id: lastname
                multinline: False

            Label:
                text:   "Gender: "
            TextInput:
                id: gender
                multinline: False

            Label:
                text:   "Email: "
            TextInput:
                id: email
                multinline: False

            Label:
                text:   "University: "
            TextInput:
                id: university
                multinline: False

            Label:
                text:   "Major: "
            TextInput:
                id: major
                multinline: False

        Button:
            text: "Submit"
            on_press: root.btn()
            on_release:
                root.manager.current = "matches"

<Matches>:
    name: "matches"
    Label:
        text: "Result"
""")

class SignUp(Screen):
    firstname = ObjectProperty(None)
    lastname =  ObjectProperty(None)
    gender = ObjectProperty(None)
    email = ObjectProperty(None)
    university = ObjectProperty(None)
    major = ObjectProperty(None)

    def btn(self):
        firstname = self.firstname.text
        lastname = self.lastname.text
        gender = self.gender.text
        major = self.major.text
        university = self.university.text
        email = self.email.text

        print("First Name:\t\t\t\t|", firstname)
        print("Last Name:\t\t\t\t |", lastname)
        print("Gender\t\t\t\t\t |", gender)
        print("Major: \t\t\t\t\t |", major)
        print("University:\t\t\t\t |", university)
        print("Email:\t\t\t\t\t |", email)

        id = getID(session)
        stmt = session.prepare("""
                        INSERT INTO users(id, first, last, university, major)
                        VALUES(?, ?, ?, ?, ?)
                        IF NOT EXISTS
                        """)
        results = session.execute(stmt, [id, firstname, lastname, university, major])

        stmt2 = session.prepare("""
                                 SELECT (first, last, university, major) 
                                 FROM users WHERE university = ? 
                                 AND major = ? ALLOW FILTERING
                                """)
        users = session.execute(stmt2, [university, major])
        for row in users:
            if row[0][0] != firstname and row[0][1] != lastname:
                print(row[0])
        return

class MainWindow(Screen):
    pass

class Matches(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(SignUp(name='signup'))
sm.add_widget(Matches(name='matches'))

class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()