import tkinter
import datetime


def init_window():
    window = tkinter.Tk()
    window.geometry('500x500')

    label = tkinter.Label(window, text='Python Alarm', bg='red')
    label.pack()

    window.mainloop()


def main():
    init_window()


if __name__ == '__main__':
    main()
