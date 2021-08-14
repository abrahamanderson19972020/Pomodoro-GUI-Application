from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#AA2EE6"
RED = "#e7305b"
GREEN = "#4AA96C"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
counter = 0
timer_maker = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer_maker)
    check.config(text="")
    timer.config(text="Timer", fg="#FF8303", font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    global counter
    counter = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global counter
    counter += 1
    if counter % 8 == 0:
        time = LONG_BREAK_MIN
        timer.config(text="Break",fg=RED,bg=YELLOW)
    elif counter % 2  == 0:
        time = SHORT_BREAK_MIN
        timer.config(text="Break",fg=PINK,bg=YELLOW)
    else:
        time = WORK_MIN
        timer.config(text="Work",fg=GREEN,bg=YELLOW)

    count_down(time * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    # if seconds == 0:
    #     seconds = "00"
    if int(seconds) < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count > 0:
        global timer_maker
        timer_maker = window.after(1000, count_down, count - 1)
    else:
        start_time()
        check_marker = ""
        work_session = counter // 2
        for i in range(work_session):
            check_marker += "✔"
        check.config(text= check_marker)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time Management")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)


timer = Label(text="Timer", fg="#FF8303", font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer.grid(row=0, column=1)

start = Button(text="Start", highlightthickness=0, command=start_time)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_time, highlightthickness=0)
reset.grid(row=2, column=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)
# checked_state = IntVar()
# checkbutton = Checkbutton(text="✔", variable=checked_state, command=checkbutton_used,fg=GREEN,bg=YELLOW)
# checkbutton.grid(row=3,column=1)






window.mainloop()