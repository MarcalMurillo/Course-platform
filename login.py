import tkinter as tk
from tkinter import messagebox, font

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela de Login")
        self.root.geometry("350x400")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        # Centralizar janela na tela
        self.center_window(350, 400)

        # Fontes
        self.font_title = font.Font(family="Segoe UI", size=20, weight="bold")
        self.font_label = font.Font(family="Segoe UI", size=10)
        self.font_entry = font.Font(family="Segoe UI", size=12)
        self.font_button = font.Font(family="Segoe UI", size=12, weight="bold")

        # Frame principal para centralizar conteúdo
        self.frame = tk.Frame(self.root, bg="#34495e", bd=0, relief=tk.RIDGE)
        self.frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=280)

        # Título
        self.label_titulo = tk.Label(self.frame, text="Login", fg="white", bg="#34495e", font=self.font_title)
        self.label_titulo.pack(pady=(20, 20))

        # Usuário
        self.label_usuario = tk.Label(self.frame, text="Usuário", fg="white", bg="#34495e", font=self.font_label)
        self.label_usuario.pack(anchor='w', padx=20)
        self.entry_usuario = tk.Entry(self.frame, font=self.font_entry, bd=0, highlightthickness=2, highlightbackground="#2980b9", highlightcolor="#3498db")
        self.entry_usuario.pack(padx=20, pady=(0, 20), fill='x')

        # Senha
        self.label_senha = tk.Label(self.frame, text="Senha", fg="white", bg="#34495e", font=self.font_label)
        self.label_senha.pack(anchor='w', padx=20)
        self.entry_senha = tk.Entry(self.frame, font=self.font_entry, bd=0, show="*", highlightthickness=2, highlightbackground="#2980b9", highlightcolor="#3498db")
        self.entry_senha.pack(padx=20, pady=(0, 30), fill='x')

        # Botão login
        self.botao_login = tk.Button(self.frame, text="Entrar", fg="white", bg="#2980b9", activebackground="#3498db",
                                    font=self.font_button, bd=0, cursor="hand2", command=self.verificar_login)
        self.botao_login.pack(padx=20, fill='x')

        # Efeito hover no botão
        self.botao_login.bind("<Enter>", lambda e: self.botao_login.configure(bg="#3498db"))
        self.botao_login.bind("<Leave>", lambda e: self.botao_login.configure(bg="#2980b9"))

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "admin" and senha == "senha123":
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
