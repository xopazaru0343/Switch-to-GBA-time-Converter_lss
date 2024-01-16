import tkinter

def convert():
    conversion_constant = (60 / 59.7275)
    run = time.get()
    h = int(run.split(':')[0])
    m = int(run.split(':')[1])
    s = int(run.split(':')[2].split('.')[0])
    ms = int(run.split('.')[1])

    original = h * 3600 + m * 60 + s + (ms / 1000)

    converted = round(original * conversion_constant, 3)

    newtime = str(converted)

    newms = int(newtime.split('.')[1])

    newseconds = int(newtime.split('.')[0])
    news = newseconds % 60
    newseconds -= news

    newm = (newseconds % 3600) / 60
    newm = int(newm)

    newh = newseconds - (newm * 60)
    newh /= 3600
    newh = int(newh)

    newtime = f'{newh}:{newm:02d}:{news:02d}.{newms:03d}'
    convertedtime.set(newtime)

w = tkinter.Tk()

time = tkinter.StringVar()
convertedtime = tkinter.StringVar()

w.title("Switch to GBA Time Converter")

timelabel = tkinter.Label(w, text='Initial Time', font=('arial', 16, 'normal'))
timeentry = tkinter.Entry(w,textvariable=time,font=('arial', 16, 'normal'))
convertedtimelabel = tkinter.Label(w, text='Converted Time', font=('arial', 16, 'normal'))
convertedtimeentry = tkinter.Entry(w, textvariable=convertedtime, font=('arial', 16, 'normal'))
button = tkinter.Button(w, text="Convert", width=16, command=convert)

timelabel.grid(row=0, column=0)
timeentry.grid(row=0, column=1)
button.grid(row=1, column=1)
convertedtimelabel.grid(row=2, column=0)
convertedtimeentry.grid(row=2, column=1)
w.mainloop()
