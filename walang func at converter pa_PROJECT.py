import tkinter

root = tkinter.Tk()
root.resizable(False, False)
root.title("Speed Calculator")
root.geometry("320x500")
root.configure(background="#006865")
root.iconbitmap(r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\AES.ico')

# Images
Img = tkinter.PhotoImage(name='Bor', file=r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\border.png')
Img2 = tkinter.PhotoImage(name='spd', file=r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\spd.png')
Img3 = tkinter.PhotoImage(name='brd2', file=r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\border2.png')
# Label 1
tkinter.Label(root, image=Img, bg="#006865").place(x=1, y=1)
tkinter.Label(root, image=Img2, bg="#006865").place(x=85, y=55)
tkinter.Label(root, image=Img3, bg="#006865").place(x=45, y=196)
# Label 2
tkinter.Label(root, text="DTS CALCULATOR", font=("Courier", 15, "bold"), fg="white",
              bg='#006865').place(x=83, y=165)


# Speed Window
def openspeed_window():
    speed_window = tkinter.Toplevel(root)
    speed_window.resizable(False, False)
    speed_window.title("Speed Calculator")
    speed_window.geometry("350x300")
    speed_window.configure(background="#006865")
    speed_window.iconbitmap(r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\AES.ico')

    # Image Section
    Img4 = tkinter.PhotoImage(name='wd2', file=r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\wd2.png')
    Img5 = tkinter.PhotoImage(name='mini_bor', file=r'C:\Users\SHINY PEARL D '
                                                    r'ABDULA\OneDrive\Desktop\tk.icon\mini_bor.png')
    # Label One
    tkinter.Label(speed_window, image=Img4, bg="#006865").place(x=0, y=1)
    tkinter.Label(speed_window, image=Img5, bg="#006865").place(x=50, y=40)
    # Label two
    tkinter.Label(speed_window, text="SPEED CALCULATOR", font=("Courier", 13, 'bold'),
                  bg="#006865", fg="#eccb5b").place(x=95, y=55)
    # CONTENT LaBel
    # Distance
    tkinter.Label(speed_window, text="Distance:", font=("Courier", 12, 'bold'), relief='ridge',
                  bg="#006865", fg="white", borderwidth=3).place(x=50, y=120)
    # Time
    tkinter.Label(speed_window, text="Time:", relief='ridge', font=("Courier", 12, 'bold'), bg="#006865",
                  fg="white", borderwidth=3).place(x=50, y=162)
    # Speed
    tkinter.Label(speed_window, text="Speed:", relief='ridge', font=("Courier", 12, 'bold'), bg="#006865",
                  fg="white", borderwidth=3).place(x=50, y=205)
    # Speed Variable
    speed_num1 = tkinter.IntVar()
    speed_num2 = tkinter.IntVar()
    speed_num3 = tkinter.IntVar()
    # CONTENT Entry
    # C.E_DISTANCE
    tkinter.Label(speed_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=153, y=104)
    tkinter.Entry(speed_window, textvariable=speed_num1, font=('Courier', 12), width=12).place(x=155, y=122)
    # C.E_TIME
    tkinter.Label(speed_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=153, y=145)
    tkinter.Entry(speed_window, textvariable=speed_num2, font=('Courier', 12), width=12).place(x=155, y=162)
    # C.E_SPEED
    tkinter.Label(speed_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=153, y=187)
    tkinter.Entry(speed_window, textvariable=speed_num3, font=('Courier', 12), width=12).place(x=155, y=205)
    # SPEED_BUTTON_SOLVE
    tkinter.Button(speed_window, text="Solve", font=("Courier", 10, 'bold'), activebackground="#00827e",
                   bg="#006865", fg='#eccb5b', bd=2, padx=20, pady=0, relief='raised',
                   overrelief='sunken').place(x=131, y=240)
    speed_window.mainloop()


# Distance Window
def open_distance_window():
    distance_window = tkinter.Toplevel(root)
    distance_window.resizable(False, False)
    distance_window.title("Speed Calculator")
    distance_window.geometry("350x300")
    distance_window.configure(background="#006865")
    distance_window.iconbitmap(r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\AES.ico')

    # Image Section
    Img4 = tkinter.PhotoImage(name='wd2', file=r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\wd2.png')
    Img5 = tkinter.PhotoImage(name='mini_bor', file=r'C:\Users\SHINY PEARL D '
                                                    r'ABDULA\OneDrive\Desktop\tk.icon\mini_bor.png')
    # Label One
    tkinter.Label(distance_window, image=Img4, bg="#006865").place(x=0, y=1)
    tkinter.Label(distance_window, image=Img5, bg="#006865").place(x=50, y=40)
    # Label two
    tkinter.Label(distance_window, text="DISTANCE CALCULATOR", font=("Courier", 13, 'bold'),
                  bg="#006865", fg="#eccb5b").place(x=77, y=55)
    # CONTENT LaBel
    # Speed
    tkinter.Label(distance_window, text="Speed:", font=("Courier", 12, 'bold'), relief='ridge',
                  bg="#006865", fg="white", borderwidth=3).place(x=50, y=120)
    # Time
    tkinter.Label(distance_window, text="Time:", relief='ridge', font=("Courier", 12, 'bold'), bg="#006865",
                  fg="white", borderwidth=3).place(x=50, y=162)
    # distance
    tkinter.Label(distance_window, text="Distance:", relief='ridge', font=("Courier", 12, 'bold'), bg="#006865",
                  fg="white", borderwidth=3).place(x=50, y=205)
    # Distance Variable
    speed_num4 = tkinter.IntVar()
    speed_num5 = tkinter.IntVar()
    speed_num6 = tkinter.IntVar()
    # CONTENT Entry
    # C.E_SPEED
    tkinter.Label(distance_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=155, y=104)
    tkinter.Entry(distance_window, textvariable=speed_num4, font=('Courier', 12), width=12).place(x=157, y=122)
    # C.E_TIME
    tkinter.Label(distance_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=155, y=145)
    tkinter.Entry(distance_window, textvariable=speed_num5, font=('Courier', 12), width=12).place(x=157, y=162)
    # C.E_DISTANCE
    tkinter.Label(distance_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=155, y=187)
    tkinter.Entry(distance_window, textvariable=speed_num6, font=('Courier', 12), width=12).place(x=157, y=205)
    # DISTANCE_BUTTON_SOLVE
    tkinter.Button(distance_window, text="Solve", font=("Courier", 10, 'bold'), activebackground="#00827e",
                   bg="#006865", fg='#eccb5b', bd=2, padx=20, pady=0, relief='raised',
                   overrelief='sunken').place(x=131, y=240)
    distance_window.mainloop()


# Time Window
def open_time_window():
    time_window = tkinter.Toplevel(root)
    time_window.resizable(False, False)
    time_window.title("Speed Calculator")
    time_window.geometry("350x300")
    time_window.configure(background="#006865")
    time_window.iconbitmap(r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\AES.ico')

    # Image Section
    Img4 = tkinter.PhotoImage(name='wd2', file=r'C:\Users\SHINY PEARL D ABDULA\OneDrive\Desktop\tk.icon\wd2.png')
    Img5 = tkinter.PhotoImage(name='mini_bor', file=r'C:\Users\SHINY PEARL D '
                                                    r'ABDULA\OneDrive\Desktop\tk.icon\mini_bor.png')
    # Label One
    tkinter.Label(time_window, image=Img4, bg="#006865").place(x=0, y=1)
    tkinter.Label(time_window, image=Img5, bg="#006865").place(x=50, y=40)
    # Label two
    tkinter.Label(time_window, text="TIME CALCULATOR", font=("Courier", 13, 'bold'),
                  bg="#006865", fg="#eccb5b").place(x=100, y=55)
    # CONTENT LaBel
    # Distance
    tkinter.Label(time_window, text="Distance:", font=("Courier", 12, 'bold'), relief='ridge',
                  bg="#006865", fg="white", borderwidth=3).place(x=50, y=120)
    # Speed
    tkinter.Label(time_window, text="Speed:", relief='ridge', font=("Courier", 12, 'bold'), bg="#006865",
                  fg="white", borderwidth=3).place(x=50, y=165)
    # Time
    tkinter.Label(time_window, text="Time:", relief='ridge', font=("Courier", 12, 'bold'), bg="#006865",
                  fg="white", borderwidth=3).place(x=50, y=205)
    # Distance Variable
    speed_num7 = tkinter.IntVar()
    speed_num8 = tkinter.IntVar()
    speed_num9 = tkinter.IntVar()
    # CONTENT Entry
    # C.E_DISTANCE
    tkinter.Label(time_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=155, y=104)
    tkinter.Entry(time_window, textvariable=speed_num7, font=('Courier', 12), width=12).place(x=157, y=125)
    # C.E_SPEED
    tkinter.Label(time_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=155, y=145)
    tkinter.Entry(time_window, textvariable=speed_num8, font=('Courier', 12), width=12).place(x=157, y=160)
    # C.E_TIME
    tkinter.Label(time_window, text='Enter a value:', font=('Verdana', 8), fg='#E6E6E6',
                  bg="#006865").place(x=155, y=187)
    tkinter.Entry(time_window, textvariable=speed_num9, font=('Courier', 12), width=12).place(x=157, y=205)
    # TIME_BUTTON_SOLVE
    tkinter.Button(time_window, text="Solve", font=("Courier", 10, 'bold'), activebackground="#00827e",
                   bg="#006865", fg='#eccb5b', bd=2, padx=20, pady=0, relief='raised',
                   overrelief='sunken').place(x=131, y=240)
    time_window.mainloop()


# Convert
tkinter.Button(root, text="Convert", font=("Courier", 12), activebackground="white", bg="silver", padx=33, pady=2,
               bd=4, relief='raised', overrelief='sunken').place(x=90, y=230)
# Speed
tkinter.Button(root, text="Speed", font=("Courier", 12), activebackground="white", bg="silver", padx=43, pady=2,
               bd=4, relief='raised', overrelief='sunken', command=openspeed_window).place(x=90, y=280)
# Distance
tkinter.Button(root, text="Distance", font=("Courier", 12), activebackground="white", bg="silver", padx=28, pady=2,
               bd=4, relief='raised', overrelief='sunken', command=open_distance_window).place(x=90, y=330)
# Time
tkinter.Button(root, text="Time", font=("Courier", 12), activebackground="white", bg="silver", padx=48, pady=3,
               bd=4, relief='raised', overrelief='sunken', command=open_time_window).place(x=90, y=380)
root.mainloop()
