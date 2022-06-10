import tkinter
from datetime import datetime


def get_actual_time():
    time = datetime.now()
    current_time = time.strftime("%H:%M:%S")

    return f'Current time: {current_time}'


window = tkinter.Tk()
window.geometry('500x500')

title = tkinter.Label(window, text='fui al baño :v', font=('Arial', 40))
title.pack()

current_time_label = tkinter.Label(
    window, text=get_actual_time(), font=('Arial', 20))

current_time_label.pack()


def update_actual_time():
    current_time_label.config(text=get_actual_time())

    window.after(1000, update_actual_time)


def init_window():
    update_actual_time()
    window.mainloop()


def main():
    init_window()


if __name__ == '__main__':
    main()
