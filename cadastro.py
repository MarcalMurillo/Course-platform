import tkinter as tk
from tkinter import messagebox, font
import login

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro")
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
        self.frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=320)

        # Título
        self.label_titulo = tk.Label(self.frame, text="Cadastro", fg="white", bg="#34495e", font=self.font_title)
        self.label_titulo.pack(pady=(20, 20))

        # Usuário
        self.label_usuario = tk.Label(self.frame, text="Usuário", fg="white", bg="#34495e", font=self.font_label)
        self.label_usuario.pack(anchor='w', padx=20)
        self.entry_usuario = tk.Entry(self.frame, font=self.font_entry, bd=0, highlightthickness=2,
                                      highlightbackground="#2980b9", highlightcolor="#3498db")
        self.entry_usuario.pack(padx=20, pady=(0, 10), fill='x')

        # Senha
        self.label_senha = tk.Label(self.frame, text="Senha", fg="white", bg="#34495e", font=self.font_label)
        self.label_senha.pack(anchor='w', padx=20)
        self.entry_senha = tk.Entry(self.frame, font=self.font_entry, bd=0, show="*", highlightthickness=2,
                                    highlightbackground="#2980b9", highlightcolor="#3498db")
        self.entry_senha.pack(padx=20, pady=(0, 10), fill='x')

        # Confirmar Senha
        self.label_confirmarsenha = tk.Label(self.frame, text="Confirmar Senha", fg="white", bg="#34495e", font=self.font_label)
        self.label_confirmarsenha.pack(anchor='w', padx=20)
        self.entry_confirmarsenha = tk.Entry(self.frame, font=self.font_entry, bd=0, show="*", highlightthickness=2,
                                             highlightbackground="#2980b9", highlightcolor="#3498db")
        self.entry_confirmarsenha.pack(padx=20, pady=(0, 20), fill='x')

        # Frame container para botões lado a lado
        self.botao_frame = tk.Frame(self.frame, bg="#34495e")
        self.botao_frame.pack(padx=20, fill='x')

        # Botão Cadastrar - maior largura
        self.botao_cadastro = tk.Button(self.botao_frame, text="Cadastrar", fg="white", bg="#2980b9", activebackground="#3498db",
                                       font=self.font_button, bd=0, cursor="hand2", command=self.verificar_cadastro)
        self.botao_cadastro.pack(side='left', fill='x', expand=True, pady=(0, 10))

        # Espaço entre botões
        self.botao_frame_spacer = tk.Frame(self.botao_frame, width=10, bg="#34495e")
        self.botao_frame_spacer.pack(side='left')

        # Botão Limpar - largura fixa menor
        self.botao_limpar = tk.Button(self.botao_frame, text="Limpar", fg="white", bg="#e74c3c", activebackground="#c0392b",
                                     font=self.font_button, bd=0, cursor="hand2", command=self.limpar_campos, width=10)
        self.botao_limpar.pack(side='left', pady=(0, 10))

        # Efeito hover nos botões
        self.botao_cadastro.bind("<Enter>", lambda e: self.botao_cadastro.configure(bg="#3498db"))
        self.botao_cadastro.bind("<Leave>", lambda e: self.botao_cadastro.configure(bg="#2980b9"))
        self.botao_limpar.bind("<Enter>", lambda e: self.botao_limpar.configure(bg="#c0392b"))
        self.botao_limpar.bind("<Leave>", lambda e: self.botao_limpar.configure(bg="#e74c3c"))

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def verificar_cadastro(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get()
        confirmarsenha = self.entry_confirmarsenha.get()

        if not usuario:
            messagebox.showerror("Erro", "Por favor, insira o nome do usuário.")
            return

        if not senha or not confirmarsenha:
            messagebox.showerror("Erro", "Por favor, insira e confirme a senha.")
            return

        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter no mínimo 6 caracteres.")
            return

        if senha != confirmarsenha:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        # Cadastro bem-sucedido
        messagebox.showinfo("Sucesso", f"Usuário '{usuario}' cadastrado com sucesso!")
        self.root.destroy()
        self.abrir_tela_login()

    def abrir_tela_login(self):
        root_login = tk.Tk()
        app_login = login.LoginApp(root_login)
        root_login.mainloop()

    def limpar_campos(self):
        self.entry_usuario.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_confirmarsenha.delete(0, tk.END)
        self.entry_usuario.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
