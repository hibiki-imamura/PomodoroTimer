import time
import tkinter as tk
import tkinter.font as font
import winsound

WORK_TIME = 0,25,0
REST_TIME = 0,5,0

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.label_font = tk.font.Font(family="Helvetica", size=20, weight="bold")
        self.timer_font = tk.font.Font(family="Helvetica", size=100, weight="bold")
        # Create a label
        self.label = tk.Label(root, text="Tomato Timer", font=self.label_font, bg="white")
        self.label.grid(row=0,column=0,columnspan=3,pady=20)
        # Create a timer label
        self.timer_label = tk.Label(root, text=f"{WORK_TIME[0]:02}:{WORK_TIME[1]:02}:{WORK_TIME[2]:02}", font=self.timer_font, bg="white")
        self.timer_label.grid(row=1,column=0,columnspan=3,pady=20)
        self.timer_label.place_forget()

        # Create a button to start the timer
        self.timer_start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.timer_start_button.grid(row=2,column=0,pady=20)
        # Create a button to stop the timer
        self.timer_stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer)
        self.timer_stop_button.grid(row=2,column=1,pady=20)

        # Create a button to close the application
        self.quit_button = tk.Button(root, text="Quit", command=self.destroy)
        self.quit_button.grid(row=2,column=2,pady=20)
        # Create a flag to indicate if the timer is active
        self.timer_active = False

    def start_timer(self):
        self.timer_active = True
        self.timer_label.place()
        period_count = 0
        while self.timer_active:
            if period_count % 2 == 0:
                time_limit = WORK_TIME[0] * 3600 + WORK_TIME[1] * 60 + WORK_TIME[2]
                self.label["text"] = "Work for 25 minutes"
            else:
                time_limit = REST_TIME[0] * 3600 + REST_TIME[1] * 60 + REST_TIME[2]
                self.label["text"] = "Rest for 5 minutes"
            self.label.update()
            start_time = time.time()
            end_time = start_time + time_limit
            remaining_time = time_limit
            while remaining_time >= 0 and self.timer_active:
                remaining_time = int(end_time - time.time())
                remaining_hours = max(remaining_time // 3600,0)
                remaining_minutes = (max(remaining_time,0) % 3600) // 60
                remaining_seconds = max(remaining_time,0) % 60
                self.timer_label["text"] = f"{remaining_hours:02}:{remaining_minutes:02}:{remaining_seconds:02}"
                time.sleep(1)
                self.root.update()
            period_count += 1
            winsound.Beep(1000, 4000)

    def stop_timer(self):
        self.timer_active = False
        print(self.root.geometry())

    def destroy(self):
        self.timer_active = False
        self.root.destroy()

if __name__ == "__main__":
    # Create a window
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry("540x360")
    root.resizable(False, False)
    root.config(bg="white")
    # Create the timer application
    app = TimerApp(root)
    # Run the window's main loop
    root.mainloop()