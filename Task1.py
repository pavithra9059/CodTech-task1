import tkinter as tk
from tkinter import messagebox

# ---------------- Window ----------------
root = tk.Tk()
root.title("🌫️ Glassmorphism To-Do List")
root.geometry("650x800")
root.configure(bg="#B3D9FF")   

tasks = []

# ---------------- Animated Title ----------------
colors = ["#00B4D8", "#FF6EC7", "#FFD166", "#06D6A0", "#8338EC"]
i = 0

def animate_title():
    global i
    title.config(fg=colors[i])
    i = (i + 1) % len(colors)
    root.after(400, animate_title)


# ---------------- Add Task ----------------
def add_task():
    task = entry.get()

    if task.strip() == "":
        messagebox.showwarning("Warning", "Enter a task!")
        return

    tasks.append(task)
    listbox.insert(tk.END, "✨ " + task)
    entry.delete(0, tk.END)


# ---------------- Delete ----------------
def delete_task():
    try:
        i = listbox.curselection()[0]
        listbox.delete(i)
        tasks.pop(i)
    except:
        messagebox.showwarning("Warning", "Select a task")


# ---------------- Complete ----------------
def complete():
    try:
        i = listbox.curselection()[0]
        item = listbox.get(i)

        if not item.startswith("✅"):
            listbox.delete(i)
            listbox.insert(i, "✅ " + item)
    except:
        messagebox.showwarning("Warning", "Select a task")


# ---------------- Hover ----------------
def hover(btn, enter, leave):
    btn.bind("<Enter>", lambda e: btn.config(bg=enter))
    btn.bind("<Leave>", lambda e: btn.config(bg=leave))


# ---------------- TITLE CARD ----------------
title_frame = tk.Frame(
    root,
    bg="#E6F2FF",   # light glass blue
    highlightbackground="#38BDF8",
    highlightthickness=2
)
title_frame.pack(pady=20, padx=20, fill="x")

title = tk.Label(
    title_frame,
    text="🌫️ GLASS TO-DO LIST",
    font=("Segoe UI", 24, "bold"),
    bg="#E6F2FF",
    fg="#0F172A"
)
title.pack(pady=10)


# ---------------- ENTRY CARD ----------------
entry_frame = tk.Frame(
    root,
    bg="#E6F2FF",
    highlightbackground="#60A5FA",
    highlightthickness=2
)
entry_frame.pack(pady=10, padx=20, fill="x")

entry = tk.Entry(
    entry_frame,
    font=("Arial", 16),
    justify="center",
    bg="#F0F9FF",
    fg="#0F172A",
    insertbackground="#0F172A",
    bd=0
)
entry.pack(padx=10, pady=10, ipady=6)


# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root, bg="#B3D9FF")
btn_frame.pack(pady=15)

btn_style = {
    "font": ("Arial", 13, "bold"),
    "fg": "white",
    "width": 18,
    "bd": 0,
    "cursor": "hand2"
}

add_btn = tk.Button(btn_frame, text="➕ Add Task", bg="#22C55E", command=add_task, **btn_style)
complete_btn = tk.Button(btn_frame, text="✅ Complete", bg="#3B82F6", command=complete, **btn_style)
delete_btn = tk.Button(btn_frame, text="🗑 Delete", bg="#EF4444", command=delete_task, **btn_style)

add_btn.pack(pady=5)
complete_btn.pack(pady=5)
delete_btn.pack(pady=5)

hover(add_btn, "#4ADE80", "#22C55E")
hover(complete_btn, "#60A5FA", "#3B82F6")
hover(delete_btn, "#F87171", "#EF4444")


# ---------------- LISTBOX GLASS PANEL ----------------
list_frame = tk.Frame(
    root,
    bg="#E6F2FF",
    highlightbackground="#38BDF8",
    highlightthickness=2
)
list_frame.pack(padx=20, pady=20, fill="both", expand=True)

listbox = tk.Listbox(
    list_frame,
    font=("Consolas", 14),
    bg="#F0F9FF",
    fg="#0F172A",
    selectbackground="#7DD3FC",
    bd=0,
    activestyle="none"
)
listbox.pack(fill="both", expand=True, padx=10, pady=10)


# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="✨ Stay Organized • Stay Productive ✨",
    font=("Arial", 11),
    bg="#B3D9FF",
    fg="#1E3A8A"
)
footer.pack(pady=10)


animate_title()
root.mainloop()
