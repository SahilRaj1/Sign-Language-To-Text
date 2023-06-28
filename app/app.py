from keras.models import model_from_json
import tensorflow as tf
from PIL import Image, ImageTk
from fileinput import filename
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import numpy as np
import cv2
import sys

sys.path.append("../")
from utils.apply_filter import apply_filter

root = Tk()
root.title("Sign Language to Text convertor")
root.geometry("1022x594")
root.iconbitmap("assets/my_icon.ico")
background_image = PhotoImage(file="assets/bg.png")
my_label = Label(root, image=background_image).place(relwidth=1, relheight=1)


def upload_file():
    # types of files to be shown and selecting the file
    f_types = [("Jpg files", "*.jpg"), ("PNG files", "*.png"), ("Jpeg files", "*.jpeg")]
    filename = filedialog.askopenfilename(filetypes=f_types)
    display_img = ImageTk.PhotoImage(file=filename)
    e1 = Label(root, image=display_img).place(x=457, y=230)
    file = str(filename)
    frame = cv2.imread(file)

    # Applying filter
    apply_filter(file)

    # loading the image
    fil_img = tf.keras.utils.load_img(
        file, target_size=(128, 128), color_mode="grayscale"
    )
    test_image = tf.keras.utils.img_to_array(fil_img)
    test_image = np.expand_dims(test_image, axis=0)

    # loading the saved model
    json_file = open("model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")

    # predicting the output
    result = loaded_model.predict(test_image)
    lis = [i for i in range(9)]
    prediction = {}
    prediction["blank"] = result[0][0]
    inde = 0
    sum = 0
    for i in lis:
        prediction[i] = result[0][inde]
        inde += 1
    max = 0
    output = 0
    for key, value in prediction.items():
        if key == "blank":
            continue
        sum += value
        if value > max:
            max = value
            output = key

    # print(output + 1)
    l3 = Label(
        root,
        text=str(output + 1),
        font="arial 24 bold",
        fg="black",
        width=3,
        height=1,
        bg="white",
    ).place(x=640, y=455)
    e1["image"] = display_img


def myIns():
    messagebox.showinfo(
        "Instructions",
        "1.Select folder Upload the test image.\n2.Please wait till the image is processed.\n3.You will now get the desired output below.",
    )


def myAbout():
    messagebox.showinfo("About", f"Sign Language to text {chr(169)}\nSahil")


btn_about = Button(
    padx=3,
    pady=3,
    bd=1,
    fg="black",
    activeforeground="hotpink",
    activebackground="grey",
    font=("verdana", 10, "bold"),
    text="About",
    command=myAbout,
    borderwidth=0,
).place(y=0, x=967)

btn_ins = Button(
    padx=3,
    pady=3,
    bd=1,
    fg="black",
    activeforeground="hotpink",
    activebackground="grey",
    font=("verdana", 10, "bold"),
    text="Instruction",
    command=myIns,
    borderwidth=0,
).place(y=0, x=0)

f1 = Frame(root, bg="white", bd=5, relief=SUNKEN).place(
    x=457, y=230, height=128, width=128
)

button1 = Button(
    root,
    text="Choose File",
    fg="black",
    activeforeground="hotpink",
    activebackground="grey",
    font=("verdana", 10, "bold"),
    width=13,
    height=1,
    command=lambda: upload_file(),
).place(x=460, y=380)

root.mainloop()
