import tkinter

def convert():
    run = time.get()
    h = int(run[0])
    m = int(run[2:4])
    s = int(run[5:7])
    ms = int(run[8:10])

    original = h * 3600 + m * 60 + s + (ms / 100)

    converted = original * (60 / 59.7275)
    converted = round(converted, 2)

    newtime = str(converted)

    newms = int(newtime[5:7])

    newseconds = int(newtime[0:4])
    news = newseconds % 60
    newseconds -= news

    newm = (newseconds % 3600) / 60
    newm = int(newm)

    newh = newseconds - (newm * 60)
    newh /= 3600
    newh = int(newh)

    newtime = str(newh) + ":" + str(newm) + ":" + str(news) + "." + str(newms)
    convertedtime.set(newtime)

w = tkinter.Tk()

time = tkinter.StringVar()
convertedtime = tkinter.StringVar()

w.title("Switch to GBA Time Converter")

timelabel = tkinter.Label(w, text='Initial Time', font=('arial', 16, 'normal'))
timeentry = tkinter.Entry(w, textvariable=time, font=('arial', 16, 'normal'))
convertedtimelabel = tkinter.Label(w, text='Converted Time', font=('arial', 16, 'normal'))
convertedtimeentry = tkinter.Entry(w, textvariable=convertedtime, font=('arial', 16, 'normal'))
button = tkinter.Button(w, text="Convert", width=16, command=convert)

timelabel.grid(row=0, column=0)
timeentry.grid(row=0, column=1)
button.grid(row=1, column=1)
convertedtimelabel.grid(row=2, column=0)
convertedtimeentry.grid(row=2, column=1)
w.mainloop()