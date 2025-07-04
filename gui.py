import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from models.player import Player

class FootballManagerGUI:
    def __init__(self, team, coach):
        self.team = team
        self.coach = coach
        self.root = tk.Tk()
        self.root.title("Manchester United Team Manager")
        self.root.geometry("600x600")  # Ukuran jendela yang lebih besar
        self.root.configure(bg="#000000")
        
        # Header Section with Team Logo
        self.header_frame = tk.Frame(self.root, bg="#2c3e50")
        self.header_frame.pack(fill="x", padx=10, pady=10)

        # Gambar latar belakang
        self.background_image = Image.open("background_image.png")  # Ganti dengan gambar latar belakang
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Tampilkan gambar bola
        try:
            self.logo_image = Image.open("football_icon.png")
            self.logo_image = self.logo_image.resize((80, 80))
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(self.root, image=self.logo_photo)
            self.logo_label.pack()
        except Exception as e:
            print("Gagal memuat gambar:", e)

        # Tampilkan nama pelatih
        self.label_coach = tk.Label(
            self.root,
            text=self.coach.get_role_info(),  # ← Harus memanggil coach.get_role_info()
            font=("Helvetica", 12, "italic"),
            fg='black',
            bg='#8B0000'  # Sesuaikan dengan latar tema MU
        )
        self.label_coach.pack(pady=5)

        # Judul
        self.title_label = tk.Label(self.root, text="Manchester United Team Manager", font=("Helvetica", 20, "bold"), fg='white', bg="#000000")
        self.title_label.pack(pady=5)

        # Frame input
        self.form_frame = tk.Frame(self.root, bg="#920808")
        self.form_frame.pack(pady=5)
        self._create_form_input("Name:", "name", 0)
        self._create_form_input("Age:", "age", 1)
        self._create_form_input("Position:", "position", 2)

        # Tombol Tambah
        self.btn_add = tk.Button(self.root, text="➕ Add Player", command=self.add_player,
                                 bg="#000000", fg="white", font=("Helvetica", 10, "bold"))
        self.btn_add.pack(pady=6)

        # Listbox
        self.listbox = tk.Listbox(self.root, width=60, height=10, bg="white", font=("Courier", 10))
        self.listbox.pack(pady=10)

        # Tombol Simpan dan Load
        self.btn_save = tk.Button(self.root, text="💾 Save Players", command=self.save_players,
                                  bg="#c51616", fg="white", font=("Helvetica", 10, "bold"))
        self.btn_save.pack(pady=4)

        self.btn_load = tk.Button(self.root, text="📂 Load Players", command=self.load_players,
                                  bg="#ffffff", fg="black", font=("Helvetica", 10, "bold"))
        self.btn_load.pack(pady=4)

    def _create_form_input(self, label_text, attribute_name, row):
        label = tk.Label(self.form_frame, text=label_text, fg='white', bg="#000000", font=("Helvetica", 10, "bold"))
        label.grid(row=row, column=0, sticky='e', padx=5, pady=3)
        entry = tk.Entry(self.form_frame, width=30)
        entry.grid(row=row, column=1, pady=3)
        setattr(self, f"entry_{attribute_name}", entry)

    def add_player(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        position = self.entry_position.get()
        if name and age.isdigit() and position:
            player = Player(name, int(age), position)
            self.team.add_player(player)
            self.listbox.insert(tk.END, player.get_role_info())
            self.entry_name.delete(0, tk.END)
            self.entry_age.delete(0, tk.END)
            self.entry_position.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter valid player data.")

    def save_players(self):
        self.team.save_to_file("data/players.json")
        messagebox.showinfo("Saved", "Players saved to data/players.json.")

    def load_players(self):
        try:
            self.team.load_from_file("data/players.json")
            self.listbox.delete(0, tk.END)
            for player in self.team.players:
                self.listbox.insert(tk.END, player.get_role_info())
            messagebox.showinfo("Loaded", "Players loaded from data/players.json.")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "players.json not found.")
