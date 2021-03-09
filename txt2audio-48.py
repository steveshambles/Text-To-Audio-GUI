"""
Text To Audio V0.48
Freeware March 2021
By Steve Shambles
https://stevepython.wordpress.com

pip3 install gtts
pip3 install Pillow
pip3 install pyperclip
pip3 install sounddevice

"""
from datetime import datetime
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser as web

from PIL import Image, ImageTk
import pyperclip
from gtts import gTTS
import sounddevice as sd
import soundfile as sf

root = tk.Tk()
root.title('Text To Audio V0.48')
root.resizable(False, False)

# Load and display logo.
logo_frame = tk.LabelFrame(root)
logo_frame.grid(padx=4, pady=4)

logo_image = Image.open('buttons/txt2audio_logov2.png')
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo_photo)
logo_label.logo_image = logo_photo
logo_label.grid(padx=2, pady=2, row=0, column=0)

scrtxtbx_frame = tk.LabelFrame(root)
scrtxtbx_frame.grid(padx=8, pady=8, row=2, column=0)

btn_frame = tk.Frame(root)
btn_frame.grid(padx=0, pady=4, row=3, column=0)


def play_sound(filename):
    """Play WAV file.Supply filename when calling this function."""
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    # Status = sd.wait()  # Wait until file is done playing.


def updt_status_bar(txt):
    """Displays current action in the status bar, message to be displayed
       must be supplied when calling this function."""
    stat_bar.config(text='STATUS: ' + txt)


def clear_txt():
    """Clear text from scr txt box."""
    play_sound('sounds/cool.wav')
    scr_txt_box.delete(1.0, tk.END)
    updt_status_bar('Text box cleared.')


def clear_clipbrd():
    """Clear the clipboard"""
    play_sound('sounds/cool2.wav')
    pyperclip.copy('')
    updt_status_bar('Clipboard cleared.')


def paste_txt():
    """Pastes text from clipboard to scr txt box."""
    pasted_txt = pyperclip.paste()
    if not pasted_txt:
        play_sound('sounds/donk.wav')
        updt_status_bar('Nothing on clipboard to paste!')
        return
    play_sound('sounds/cool2.wav')
    scr_txt_box.insert(tk.INSERT, pasted_txt)
    updt_status_bar('Clipboard pasted.')


def conv_to_audio():
    """This converts tthe text to mp3 using google translate."""
    pasted_txt = scr_txt_box.get('1.0', tk.END)
    if len(pasted_txt) < 2:
        play_sound('sounds/donk.wav')
        updt_status_bar('Nothing to convert! Type or paste some text dude.')
        return
    play_sound('sounds/click.wav')
    updt_status_bar('Converting, saving and then playing audio, '
                    'please be patient.')
    stat_bar.update()
    myobj = gTTS(text=pasted_txt, lang='en', slow=False)

    file_name = datetime.now().strftime(r'%y%m%d%H%M%S')+'.mp3'
    myobj.save('mp3s/' + file_name)
    cwd = os.getcwd()
    web.open(cwd + '/mp3s/' + file_name)
    updt_status_bar('')


def open_folder():
    """Get current dir and open systems file browser to view MP3 files."""
    cwd = os.getcwd()
    play_sound('sounds/splat.wav')
    web.open(cwd + '/mp3s/')
    updt_status_bar('Opened saved MP3s folder.')


def popup(event):
    """On right click, display popup menu at mouse position."""
    MENU.post(event.x_root, event.y_root)


def help_me():
    """Opens a help, using systems default text viewer."""
    web.open('tta_help.txt')
    updt_status_bar('Opened help text file.')


def about_menu():
    """About program."""
    messagebox.showinfo('About',
                        'Text To Audio V0.48\n'
                        'Freeware By\n'
                        'Steve Shambles.\n'
                        'Last updated March 2021.')


def visit_github():
    """View my source codes on GitHub."""
    web.open("https://github.com/steveshambles/")


def visit_blog():
    """Visit my blog."""
    web.open('https://stevepython.wordpress.com/')


def contact_me():
    """Go to the contact page on my blog."""
    web.open('https://stevepython.wordpress.com/contact/')


def donate_me():
    """User splashes the cash here donating via PayPal."""
    web.open("https:\\paypal.me/photocolourizer")


def exit_app():
    """Don't go.I love you and want to have your children, I'm rich too!."""
    ask_yn = messagebox.askyesno('Question', 'Confirm Quit?')
    if not ask_yn:
        return
    root.destroy()


def demo_text():
    """Always availabe for testing purpose.
       Selected from mouse right click menu."""
    play_sound('sounds/donk.wav')
    updt_status_bar('Pasted demo text.')
    demo_txt = """
My wife asked me if i'd seen the dog bowl,
i said i didn't know he could.\n
If you get attacked by a gang of clowns,
always go for the juggler first.\n
I ate a kids meal at McDonald’s today,
his mum got really angry.
"""
    scr_txt_box.insert(tk.INSERT, demo_txt)


def chng_bg_col(colour):
    """Change scr txt box background colour, for eye strain purpose."""
    play_sound('sounds/splat.wav')
    updt_status_bar('Changed background colour.')
    scr_txt_box.config(bg=colour)


def copy_text():
    """Copy all the text from scr txt box widget to clipboard."""
    value = scr_txt_box.get("1.0", "end-1c")

    if not value:
        play_sound('sounds/donk.wav')
        updt_status_bar('No text to copy!')
        return
        
    play_sound('sounds/splat.wav')
    updt_status_bar('Copied all text from editor to clipboard.')
    pyperclip.copy(value)


# pre-load icons for drop-down menu.
help_icon = ImageTk.PhotoImage(file='icons/help-16x16.ico')
about_icon = ImageTk.PhotoImage(file='icons/about-16x16.ico')
blog_icon = ImageTk.PhotoImage(file='icons/blog-16x16.ico')
exit_icon = ImageTk.PhotoImage(file='icons/exit-16x16.ico')
donation_icon = ImageTk.PhotoImage(file='icons/donation-16x16.ico')
github_icon = ImageTk.PhotoImage(file='icons/github-16x16.ico')
contact_icon = ImageTk.PhotoImage(file='icons/contact-16x16.ico')
prg_fldr_icon = ImageTk.PhotoImage(file='icons/prg-fldr-16x16.ico')

# Drop-down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Menu', menu=file_menu)

file_menu.add_command(label='Help', compound='left',
                      image=help_icon, command=help_me)

file_menu.add_command(label='About', compound='left',
                      image=about_icon, command=about_menu)

file_menu.add_separator()

file_menu.add_command(label='Python source code on GitHub', compound='left',
                      image=github_icon, command=visit_github)

file_menu.add_command(label='Visit my Blog', compound='left',
                      image=blog_icon, command=visit_blog)

file_menu.add_separator()

file_menu.add_command(label='Contact Me', compound='left',
                      image=contact_icon, command=contact_me)

file_menu.add_command(label='Make a small donation via PayPal',
                      compound='left',
                      image=donation_icon, command=donate_me)

file_menu.add_separator()

file_menu.add_command(label='Exit', compound='left',
                      image=exit_icon, command=exit_app)

root.config(menu=menu_bar)


# Create buttons.
paste_btn = tk.Button(btn_frame, command=paste_txt)
paste_photo = tk.PhotoImage(file='buttons/paste_btn_140x52.png')
paste_btn.config(image=paste_photo, relief=tk.FLAT)
paste_btn.grid(row=1, column=0, pady=4, padx=4)

clear_btn = tk.Button(btn_frame, command=clear_txt)
clear_photo = tk.PhotoImage(file='buttons/clear_btn_140x52.png')
clear_btn.config(image=clear_photo, relief=tk.FLAT)
clear_btn.grid(row=1, column=1, pady=4, padx=4)

convert_btn = tk.Button(btn_frame, command=conv_to_audio)
conv_photo = tk.PhotoImage(file='buttons/convert_btn_140x52.png')
convert_btn.config(image=conv_photo, relief=tk.FLAT)
convert_btn.grid(row=1, column=2, pady=4, padx=4)

mp3s_btn = tk.Button(btn_frame, command=open_folder)
mp3s_photo = tk.PhotoImage(file='buttons/mp3s_btn_140x52.png')
mp3s_btn.config(image=mp3s_photo, relief=tk.FLAT)
mp3s_btn.grid(row=1, column=3, pady=4, padx=4)

# Create the scrolled text box.
scr_txt_box = scrolledtext.ScrolledText(scrtxtbx_frame, bg='gold',
                                        width=70, height=20)
scr_txt_box.grid()

# Create the status bar.
stat_frame = tk.Frame(root)
stat_frame.grid(padx=0, pady=4, row=4, column=0, sticky=tk.W + tk.E)

stat_bar = tk.Label(stat_frame, text='STATUS:  Use right mouse menu or'
                    ' buttons above to Paste or type in text.', bd=1,
                    relief=tk.SUNKEN, anchor=tk.W)
stat_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Bind mouse right click to scr text box.
scr_txt_box.bind('<Button-3>', popup)

# Create the mouse right click popup menu.
MENU = tk.Menu(root, tearoff=0)

MENU.add_command(label='Paste',
                 command=paste_txt)
MENU.add_command(label='Copy all',
                 command=copy_text)
MENU.add_command(label='Clear text',
                 command=clear_txt)
MENU.add_command(label='Clear clipboard',
                 command=clear_clipbrd)

MENU.add_separator()

MENU.add_command(label='Paste demo text',
                 command=demo_text)

MENU.add_separator()

MENU.add_command(label='white background',
                 command=lambda: chng_bg_col('white'))
MENU.add_command(label='Blue background',
                 command=lambda: chng_bg_col('powderblue'))
MENU.add_command(label='Yellow background',
                 command=lambda: chng_bg_col('gold'))
MENU.add_command(label='Green background',
                 command=lambda: chng_bg_col('limegreen'))

play_sound('sounds/startup.wav')

# Capture user trying to exit via x icon on window.
root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()
