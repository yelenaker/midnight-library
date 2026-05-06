import tkinter as tk
from tkinter import messagebox
import webbrowser

# main window
window = tk.Tk()
window.title("Midnight Library")
window.geometry("980x780")
window.config(bg="#070b14")
window.resizable(False, False)

# starter books
books = [
    "The Great Gatsby",
    "Harry Potter",
    "Atomic Habits",
    "The Hobbit",
    "1984",
    "The Alchemist",
    "Pride and Prejudice",
    "Dune",
    "Sherlock Holmes",
    "Dracula",
    "The Little Prince"
]

# borrowed books list
borrowed_books = []

# updates library list
def refresh_books():

    library_list.delete(0, tk.END)

    for book in books:

        # check if borrowed
        if book in borrowed_books:

            library_list.insert(
                tk.END,
                f"  {book}        • Borrowed"
            )

        else:

            library_list.insert(
                tk.END,
                f"  {book}        • Available"
            )

# add new book
def add_book():

    new_book = book_entry.get()

    # if empty
    if new_book == "":

        messagebox.showerror(
            "Error",
            "Please enter a book name."
        )

        return

    books.append(new_book)

    refresh_books()

    # clear input after adding
    book_entry.delete(0, tk.END)

# borrow selected book
def borrow_book():

    selected = library_list.curselection()

    if selected == ():

        messagebox.showerror(
            "Error",
            "Please select a book."
        )

        return

    index = selected[0]

    selected_book = books[index]

    # already borrowed
    if selected_book in borrowed_books:

        messagebox.showerror(
            "Error",
            "This book is already borrowed."
        )

        return

    borrowed_books.append(selected_book)

    refresh_books()

# return book
def return_book():

    selected = library_list.curselection()

    if selected == ():

        messagebox.showerror(
            "Error",
            "Please select a book."
        )

        return

    index = selected[0]

    selected_book = books[index]

    # if already available
    if selected_book not in borrowed_books:

        messagebox.showerror(
            "Error",
            "This book is already available."
        )

        return

    borrowed_books.remove(selected_book)

    refresh_books()

# remove book completely
def remove_book():

    selected = library_list.curselection()

    if selected == ():

        messagebox.showerror(
            "Error",
            "Please select a book."
        )

        return

    index = selected[0]

    selected_book = books[index]

    books.remove(selected_book)

    # remove from borrowed too
    if selected_book in borrowed_books:
        borrowed_books.remove(selected_book)

    refresh_books()

# hidden links
def open_resume(event):

    webbrowser.open(
        "https://drive.google.com/drive/folders/1eShxIMHOdOhKEXf9QxqOmlBZDvNCY52p"
    )

# funny music
def open_music(event):

    webbrowser.open(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    )

# spotify playlist
def open_secret(event):

    webbrowser.open(
        "https://open.spotify.com/playlist/37i9dQZF1E8MXlpjbZoKhi"
    )

# title area
header_frame = tk.Frame(
    window,
    bg="#070b14"
)

header_frame.pack(pady=(30, 10))

title = tk.Label(
    header_frame,
    text="MIDNIGHT LIBRARY",
    font=("Georgia", 36, "bold"),
    bg="#070b14",
    fg="#f8fafc"
)

title.pack()

subtitle = tk.Label(
    header_frame,
    text="Personal desktop reading manager",
    font=("Segoe UI", 11),
    bg="#070b14",
    fg="#64748b"
)

subtitle.pack(pady=5)

# hidden dots
secret_frame = tk.Frame(
    window,
    bg="#070b14"
)

secret_frame.pack(pady=(0, 20))

# resume dot
dot1 = tk.Label(
    secret_frame,
    text="•",
    font=("Arial", 12),
    fg="#334155",
    bg="#070b14",
    cursor="hand2"
)

dot1.grid(row=0, column=0, padx=8)

dot1.bind("<Button-1>", open_resume)

# music dot
dot2 = tk.Label(
    secret_frame,
    text="•",
    font=("Arial", 12),
    fg="#334155",
    bg="#070b14",
    cursor="hand2"
)

dot2.grid(row=0, column=1, padx=8)

dot2.bind("<Button-1>", open_music)

# spotify dot
dot3 = tk.Label(
    secret_frame,
    text="•",
    font=("Arial", 12),
    fg="#334155",
    bg="#070b14",
    cursor="hand2"
)

dot3.grid(row=0, column=2, padx=8)

dot3.bind("<Button-1>", open_secret)

# input area
entry_frame = tk.Frame(
    window,
    bg="#070b14"
)

entry_frame.pack(pady=10)

book_entry = tk.Entry(
    entry_frame,
    font=("Segoe UI", 15),
    width=38,
    justify="center",
    bg="#111827",
    fg="white",
    insertbackground="white",
    relief="flat",
    bd=0
)

book_entry.pack(
    ipady=14
)

# buttons area
button_frame = tk.Frame(
    window,
    bg="#070b14"
)

button_frame.pack(pady=20)

# common button style
button_style = {
    "font": ("Segoe UI", 10, "bold"),
    "fg": "white",
    "padx": 20,
    "pady": 11,
    "bd": 0,
    "cursor": "hand2",
    "width": 10,
    "relief": "flat"
}

# add button
add_button = tk.Button(
    button_frame,
    text="Add",
    bg="#4338ca",
    activebackground="#4f46e5",
    command=add_book,
    **button_style
)

add_button.grid(row=0, column=0, padx=8)

# borrow button
borrow_button = tk.Button(
    button_frame,
    text="Borrow",
    bg="#d97706",
    activebackground="#f59e0b",
    command=borrow_book,
    **button_style
)

borrow_button.grid(row=0, column=1, padx=8)

# return button
return_button = tk.Button(
    button_frame,
    text="Return",
    bg="#059669",
    activebackground="#10b981",
    command=return_book,
    **button_style
)

return_button.grid(row=0, column=2, padx=8)

# remove button
remove_button = tk.Button(
    button_frame,
    text="Remove",
    bg="#dc2626",
    activebackground="#ef4444",
    command=remove_book,
    **button_style
)

remove_button.grid(row=0, column=3, padx=8)

# books section
library_frame = tk.Frame(
    window,
    bg="#0f172a",
    highlightbackground="#1e293b",
    highlightthickness=1
)

library_frame.pack(
    pady=(10, 20)
)

library_title = tk.Label(
    library_frame,
    text="BOOK COLLECTION",
    font=("Segoe UI", 12, "bold"),
    bg="#0f172a",
    fg="#f8fafc"
)

library_title.pack(
    pady=(15, 5)
)

# list + scrollbar
list_container = tk.Frame(
    library_frame,
    bg="#0f172a"
)

list_container.pack(
    padx=20,
    pady=(10, 20)
)

scrollbar = tk.Scrollbar(
    list_container
)

scrollbar.pack(
    side="right",
    fill="y"
)

library_list = tk.Listbox(
    list_container,
    width=58,
    height=9,
    font=("Segoe UI", 13),
    bg="#111827",
    fg="#e2e8f0",
    selectbackground="#4338ca",
    selectforeground="white",
    activestyle="none",
    bd=0,
    highlightthickness=0,
    yscrollcommand=scrollbar.set
)

library_list.pack(
    side="left"
)

scrollbar.config(
    command=library_list.yview
)

# quick guide
help_frame = tk.Frame(
    window,
    bg="#070b14"
)

help_frame.pack(
    pady=(0, 20)
)

help_box = tk.Frame(
    help_frame,
    bg="#111827",
    highlightbackground="#1e293b",
    highlightthickness=1
)

help_box.pack()

help_title = tk.Label(
    help_box,
    text="QUICK GUIDE",
    font=("Segoe UI", 10, "bold"),
    bg="#111827",
    fg="#f8fafc"
)

help_title.pack(
    pady=(12, 5)
)

# small instructions
help_text = tk.Label(
    help_box,
    text=
    "• Add books using the text field above\n"
    "• Select books directly from the collection\n"
    "• Borrow and Return books anytime\n"
    "• Try clicking the hidden dots near the title",
    font=("Segoe UI", 10),
    bg="#111827",
    fg="#cbd5e1",
    justify="left"
)

help_text.pack(
    padx=20,
    pady=(0, 14)
)

# footer
footer = tk.Label(
    window,
    text="Python Tkinter Desktop Application",
    font=("Segoe UI", 9),
    bg="#070b14",
    fg="#475569"
)

footer.pack(
    side="bottom",
    pady=15
)

# start app
refresh_books()

window.mainloop()