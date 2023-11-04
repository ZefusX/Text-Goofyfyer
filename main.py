import random
import emoji
import tkinter
import pyperclip  # Pour copier dans le presse-papiers

root = tkinter.Tk()
root.title("Goofyer")
root.geometry("500x250")

def load_emojis_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().splitlines()

ls_emoji = load_emojis_from_file("emoji.txt")

def random_emoji():
    return ls_emoji[random.randint(0, len(ls_emoji) - 1)]

def goofyfyer(event):
    text = to_goofy.get()
    result_goofyfied = "".join([emoji.emojize(random_emoji()) if c == " " else c for c in text])
    txt_result_goofyfy.config(text=result_goofyfied)

def copy_to_clipboard():
    result_text = txt_result_goofyfy.cget("text")
    pyperclip.copy(result_text)

txt_to_goofy = tkinter.Label(root, text="Put the text you want to goofyfy :")
txt_to_goofy.pack()

to_goofy = tkinter.Entry(root)
to_goofy.pack()
to_goofy.bind("<Return>", goofyfyer)

txt_result_goofyfy = tkinter.Label(root, text="")
txt_result_goofyfy.pack()

copy_button = tkinter.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()