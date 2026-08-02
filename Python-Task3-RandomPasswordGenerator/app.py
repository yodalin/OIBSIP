import tkinter as tk
from tkinter import ttk, messagebox

from generator import generate_password
from strength import check_strength
from clipboard_utils import copy_to_clipboard

history = []


def generate():
    try:
        password = generate_password(
            length_var.get(),
            upper_var.get(),
            lower_var.get(),
            digit_var.get(),
            symbol_var.get(),
            ambiguous_var.get(),
        )

        password_var.set(password)

        strength_label.config(
            text=f"Strength: {check_strength(password)}"
        )

        history.insert(0, password)

        if len(history) > 5:
            history.pop()

        history_box.delete(0, tk.END)

        for item in history:
            history_box.insert(tk.END, item)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def copy():
    if password_var.get():
        copy_to_clipboard(password_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def clear_history():
    history.clear()
    history_box.delete(0, tk.END)
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("650x650")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

password_var = tk.StringVar()

length_var = tk.IntVar(value=16)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

ambiguous_var = tk.BooleanVar(value=False)

title = ttk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 18, "bold")
)

title.pack(pady=15)

ttk.Label(root, text="Password Length").pack()

length_spin = ttk.Spinbox(
    root,
    from_=8,
    to=64,
    textvariable=length_var,
    width=10,
)

length_spin.pack(pady=5)

ttk.Checkbutton(
    root,
    text="Uppercase",
    variable=upper_var
).pack(anchor="w", padx=40)

ttk.Checkbutton(
    root,
    text="Lowercase",
    variable=lower_var
).pack(anchor="w", padx=40)

ttk.Checkbutton(
    root,
    text="Numbers",
    variable=digit_var
).pack(anchor="w", padx=40)

ttk.Checkbutton(
    root,
    text="Symbols",
    variable=symbol_var
).pack(anchor="w", padx=40)

ttk.Checkbutton(
    root,
    text="Exclude Ambiguous Characters",
    variable=ambiguous_var
).pack(anchor="w", padx=40)

ttk.Button(
    root,
    text="Generate Password",
    command=generate,
).pack(pady=15)

password_entry = ttk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 12),
    width=40,
)
password_entry.config(state="readonly")
password_entry.pack()

ttk.Button(
    root,
    text="Copy to Clipboard",
    command=copy,
).pack(pady=10)

strength_label = ttk.Label(
    root,
    text="Strength:"
)

strength_label.pack()
strength_bar = ttk.Progressbar(
    root,
    length=300,
    mode="determinate"
)

strength_bar.pack(pady=5)
ttk.Label(
    root,
    text="Last 5 Passwords"
).pack(pady=10)

history_box = tk.Listbox(
    root,
    height=5,
    width=50,
)

history_box.pack()
ttk.Button(
    root,
    text="Clear History",
    command=clear_history
).pack(pady=5)

root.mainloop()