from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch

import findAcc
import createAcc
import createDatabase
import loadAcc
from kivymd.uix.selectioncontrol import MDCheckbox

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item'''
    icon = StringProperty()

    def __init__(self, pk=None, **kwargs):
            super().__init__(**kwargs)
            # state a pk which we shall use link the list items with the database primary keys
            self.pk = pk

class FirstWindow(Screen):

    Builder.load_file('firstwindow.kv')

    def login(self):
        
        self.manager.current = "third"
        self.manager.transition.direction = "left"

class SecondWindow(Screen):

    Builder.load_file('secondwindow.kv')

    def signUp(self):
        name = self.ids.create_name.text
        employee_id = self.ids.employee_id.text

        # If input(s) are incomplete
        if (name or employee_id) and name:
            # If username exists
            if findAcc.locateUsername(employee_id) is False:
                createAcc.storeAcc(name, employee_id)
                self.ids.create_name.text = ''
                self.ids.employee_id.text = ''
                self.manager.current = "first"
                self.manager.transition.direction = "right"
            else:
                self.error_dialog(message="The Employee ID you entered is already in used.")
                self.ids.employee_id.text = ''
        else:
            self.error_dialog(message="Make sure to fill up all the required information to proceed.")

    def clear(self):
        self.ids.create_username.text = ''
        self.ids.create_password.create_passw.text = ''
        self.ids.confirm_password.confirm_passw.text = ''

    def error_dialog(self, message):

        close_button = MDFlatButton(
            text='CLOSE',
            text_color=[0, 0, 0, 1],
            on_release=self.close_dialog,
        )
        self.dialog = MDDialog(
            title='[color=#FF0000]Ooops![/color]',
            text=message,
            buttons=[close_button],
        )
        self.dialog.open()

    # Close Dialog
    def close_dialog(self, obj):
        self.dialog.dismiss()

class ThirdWindow(Screen):

    Builder.load_file('thirdwindow.kv')

    def on_enter(self):

        employees_accs = loadAcc.allAcc()

        try:

            if employees_accs != []:
                
                for acc in employees_accs:
                    print(acc[0], acc[1], acc[2])
                    employee = ListItemWithCheckbox(pk=acc[0],text=acc[1], secondary_text=str(acc[2]), divider=None)

                    self.ids.employees.add_widget(employee)
                   # self.ids.timeout.add_widget(employee)
        except Exception as e:
            print(e)
            pass

class WindowManager(ScreenManager):
    pass

class rawApp(MDApp):

    def build(self):

        # Creating Database
        createDatabase.database()

        return WindowManager()

if __name__ == '__main__':
    rawApp().run()
