import instaloader
import tkinter as tk
import shutil
import os
from PIL import Image, ImageTk

def InitializeGUI():
    # Set basic things on window
    gui.title('Instagram downlader')
    gui.iconbitmap('pics/ig_icon.ico')
    gui.config(bg='#292929')

    width = 400  # Width
    height = 400  # Height

    screen_width = gui.winfo_screenwidth()  # Width of the screen
    screen_height = gui.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    gui.geometry('%dx%d+%d+%d' % (width, height, x - 100, y - 100))

def EnterInput():
    user = username.get(1.0, "end-1c") # Get input from text box
    DownloadProfilePic(user)

def DownloadProfilePic(username):
    ig = instaloader.Instaloader()
    ig.download_profile(username, profile_pic_only=True)
    LoadImage(username)

def LoadImage(username):
    for file in os.listdir(username):
        if file.endswith(".jpg"):
            image_ = Image.open(username + "\\" + file)
            n_image = image_.resize((200, 200))
            photo = ImageTk.PhotoImage(n_image)
            img_label = tk.Label(gui, image=photo)
            img_label.photo = photo  # <--
            img_label.place(x=100, y=100)
    RemoveImage(username)

def RemoveImage(username):
    shutil.rmtree(username)

if __name__ == '__main__':
    gui = tk.Tk()
    InitializeGUI()

    username = tk.Text(gui, height=2, width=15, bg="#1B1B1B", fg="#FFFFFF", highlightcolor="#2E2E2E",
                       insertbackground="#FFFFFF")
    username.place(x=120, y=30)

    enterButton = tk.Button(gui, text="Show", command=EnterInput, cursor="")
    enterButton.place(x=270, y=35)

    username_label = tk.Label(gui, text="Enter username:", fg="#FFFFFF", bg="#292929", padx=5, pady=15)
    username_label.place(x=10, y=20)

    gui.mainloop()