from tkinter import *


def addchar(event):
    button = event.widget
    char = button.cget("text")
    if char == "X":
        char = "*"
    current_view_text = calc_text_box.cget("text")
    result = current_view_text + str(char)
    if current_view_text == "0":
        calc_text_box.config(text = char)
    else:
        calc_text_box.config(text = result)
        print(result)


def clearScreen():
    calc_text_box.config(text = "")

def equalTo():
    main_result = calc_text_box.cget("text")
    try:
        main_result = eval(main_result)
    except:
        pass
    calc_text_box.config(text = main_result)

#getting the tk object
window = Tk()
window.title("Calculator")

#setting the main frame of the app
mainframe = Frame(window, bg = "cyan")

#creating the upper part of the layout that displays the calculator screen
sub_frame_top = Frame(mainframe, pady = 10, bg = "cyan")
calc_text_box = Label(sub_frame_top, text = "0", bg = "silver", fg = "blue", width = 35,
                      height = 5)
calc_text_box.pack()
#calc_text_box.config(font = ("Courier", 10))
sub_frame_top.pack(anchor = "n")


#creating the lower part that contains the button that perform various things
sub_frame_bottom = Frame(mainframe)
frame1 = Frame(sub_frame_bottom)
button6 = Button(frame1, text = "6", width = 5, height = 3, fg = "white", bg = "green")
button6.pack()
button6.bind("<Button-1>", addchar)
button3 = Button(frame1, text = "3", width = 5, height = 3, fg = "white", bg = "green")
button3.pack()
button3.bind("<Button-1>", addchar)
button0 = Button(frame1, text = "0", width = 5, height = 3, fg = "white", bg = "green")
button0.pack()
button0.bind("<Button-1>", addchar)
frame1.pack(side = LEFT)
frame2 = Frame(sub_frame_bottom)
button7 = Button(frame2, text = "7", width = 5, height = 3, fg = "white", bg = "green")
button7.pack()
button7.bind("<Button-1>", addchar)
button4 = Button(frame2, text = "4", width = 5, height = 3, fg = "white", bg = "green")
button4.pack()
button4.bind("<Button-1>", addchar)
button1 = Button(frame2, text = "1", width = 5, height = 3, fg = "white", bg = "green")
button1.pack()
button1.bind("<Button-1>", addchar)
frame2.pack(side = LEFT)
frame3 = Frame(sub_frame_bottom)
button8 = Button(frame3, text = "8", width = 5, height = 3, fg = "white", bg = "green")
button8.pack()
button8.bind("<Button-1>", addchar)
button5 = Button(frame3, text = "5", width = 5, height = 3, fg = "white", bg = "green")
button5.pack()
button5.bind("<Button-1>", addchar)
button2 = Button(frame3, text = "2", width = 5, height = 3, fg = "white", bg = "green")
button2.pack()
button2.bind("<Button-1>", addchar)
frame3.pack(side = LEFT)
frame4 = Frame(sub_frame_bottom)
button9 = Button(frame4, text = "9", width = 5, height = 3, fg = "white", bg = "green")
button9.pack()
button9.bind("<Button-1>", addchar)
button00 = Button(frame4, text = "00", width = 5, height = 3, fg = "white", bg = "green")
button00.pack()
button00.bind("<Button-1>", addchar)
button_p = Button(frame4, text = ".", width = 5, height = 3, fg = "white", bg = "green")
button_p.pack()
button_p.bind("<Button-1>", addchar)
frame4.pack(side = LEFT)
frame5 = Frame(sub_frame_bottom)
button_min = Button(frame5, text = "-", width = 5, height = 3, fg = "white", bg = "blue")
button_min.pack()
button_min.bind("<Button-1>", addchar)
button_div = Button(frame5, text = "/", width = 5, height = 3, fg = "white", bg = "blue")
button_div.pack()
button_div.bind("<Button-1>", addchar)
button_del = Button(frame5, text = "AC", width = 5, height = 3, fg = "red", bg = "purple", command = clearScreen)
button_del.pack()
frame5.pack(side = LEFT)
frame6 = Frame(sub_frame_bottom)
button_add = Button(frame6, text = "+", width = 5, height = 3, fg = "white", bg = "blue")
button_add.pack()
button_add.bind("<Button-1>", addchar)
button_multi = Button(frame6, text = "X", width = 5, height = 3, fg = "white", bg = "blue")
button_multi.pack()
button_multi.bind("<Button-1>", addchar)
button_eq = Button(frame6, text = "=", width = 5, height = 3, fg = "white", bg = "red", command = equalTo)
button_eq.pack()
frame6.pack(side = LEFT)
sub_frame_bottom.pack(side = LEFT)

mainframe.pack()

#it fixes the size of the window, it does not let the size of the widgrt determine it's size
#window.pack_propagate(0)

# it make the top level root widget which in thisn case is window unresizable
window.resizable(0, 0)

#using the event loop to run the app
window.mainloop()
