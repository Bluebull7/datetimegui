# Challenge
# Create a GUI that tells you the date and time and allows you to switch time zones

# Dependencies
# Clock/Date API
# Buttons to allow to switch from EST,CST,PST,MST


import dearpygui.dearpygui as dpg


class createWindow():

    def __init__(self,width=600,height=600,title='New Title'):


        self.width =  width 
        self.height = height 
        self.title = title 
        


    def newWin(self):
        dpg.create_context()
        dpg.create_viewport(title=self.title,width=self.width,height=self.height)

    
    def showWindow(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

def main():
            window1 = createWindow()
            createWindow.newWin(window1)
            createWindow.showWindow(window1)
if __name__ == "__main__":
        main()
