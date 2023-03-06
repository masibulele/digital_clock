# import required libraries for gui creation and time

from tkinter import Tk, Label
import time

#create digital clock function


def main():
    
    #create main gui window
    app_window= Tk()
    #specify dimensions
    app_window.geometry('420x150')
    app_window.title('Digital clock')
    app_window.resizable(1,1)
    #create specifications for label
    text_font= ('boulder',68,'bold')
    background= "#f2e750"
    foreground= "#363529"
    border_width= 25
    #create label for watch
    label= Label(app_window,font=text_font,background=background,foreground=foreground,border=border_width)
    #position label on  main window
    label.grid(row=0,column=1)
    def digital_clock():
        '''gets current time and adds to label as text'''
        current_time= time.strftime('%H:%M:%S')
        label.config(text=current_time)
        label.after(200,digital_clock)
    #run function 
    digital_clock()
    #create main windowloop




    app_window.mainloop()


if __name__=='__main__':
   main()
  

