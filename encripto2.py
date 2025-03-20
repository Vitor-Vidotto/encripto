import hashlib
import base64
import hmac
import tkinter as tk
from tkinter import simpledialog
import pyperclip

# Função para gerar a senha com HMAC (SHA-256)
def generate_password_hmac(site, secret_key, checkbox_selection):
    combined = f"{site}{checkbox_selection}".encode()
    key = secret_key.encode()
    hmac_hash = hmac.new(key, combined, hashlib.sha256).digest()
    password = base64.urlsafe_b64encode(hmac_hash[:12]).decode()
    return password

# Função para exibir a tela de checkboxes (opcional)
def show_checkbox_screen():
    checkbox_selection = []  # Lista para armazenar valores selecionados
    checkbox_window = tk.Toplevel()  # Cria uma nova janela
    checkbox_window.title("Seleção de Checkboxes")

    # Tamanho da janela
    window_width = 300
    window_height = 250
    screen_width = checkbox_window.winfo_screenwidth()
    screen_height = checkbox_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    checkbox_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    # Variáveis para os checkboxes
    checkbox_vars = []

    for i in range(3):
        for j in range(3):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(checkbox_window, variable=var, width=5, height=2, font=("Arial", 14))
            checkbox.grid(row=i, column=j)
            checkbox_vars.append(var)
    
    # Função para confirmar a seleção
    def on_checkbox_select():
        nonlocal checkbox_selection
        checkbox_selection = [str(var.get()) for var in checkbox_vars]
        checkbox_window.destroy()  # Fecha a janela de checkboxes após confirmação

    # Botão de confirmação
    confirm_button = tk.Button(checkbox_window, text="Confirmar", command=on_checkbox_select, font=("Arial", 14))
    confirm_button.grid(row=3, column=1)

    # Faz o `wait_window` para não bloquear o fluxo principal
    checkbox_window.wait_window()  # Aguarda até que a janela seja destruída

    return ''.join(checkbox_selection)  # Retorna os v
# Função para exibir a interface e gerar a senha
def generate_password_gui():
    root = tk.Tk()
    root.withdraw()

    while True:
        # Janela de digitação do site
        site_window = tk.Toplevel()
        site_window.title("Digite o Site")
        
        screen_width = site_window.winfo_screenwidth()
        screen_height = site_window.winfo_screenheight()

        window_width = 400
        window_height = 200
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        site_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        site_label = tk.Label(site_window, text="Digite o nome do site (ex: google.com):", font=("Arial", 12))
        site_label.pack(pady=10)

        site_entry = tk.Entry(site_window, font=("Arial", 12), width=30)
        site_entry.pack(pady=5)

        use_checkboxes_var = tk.BooleanVar()
        use_checkboxes_checkbox = tk.Checkbutton(site_window, text="Usar Checkboxes", variable=use_checkboxes_var, font=("Arial", 12))
        use_checkboxes_checkbox.pack(pady=10)

        def on_confirm_site():
            site = site_entry.get()
            site_window.destroy()  # Fecha a janela de digitação do site
            generate_password(site, use_checkboxes_var.get())

        confirm_button = tk.Button(site_window, text="Confirmar", command=on_confirm_site, font=("Arial", 12))
        confirm_button.pack(pady=20)

        site_window.mainloop()

    root.quit()

# Função para gerar a senha com base no site e na senha de criptografia
def generate_password(site, use_checkboxes):
    secret_key = simpledialog.askstring("Senha de Criptografia", "Digite a senha de criptografia:")

    if secret_key:
        checkbox_selection = ""

        if use_checkboxes:
            checkbox_selection = show_checkbox_screen()  # Exibe a tela de checkboxes

        password = generate_password_hmac(site, secret_key, checkbox_selection)

        pyperclip.copy(password)

        # Exibe a tela com a senha gerada
        show_generated_password_screen(site, password)

    else:
        messagebox.showwarning("Aviso", "A senha de criptografia não pode estar vazia!")

# Função para exibir a tela com a senha gerada e opções "Gerar Outra" ou "Sair"
def show_generated_password_screen(site, password):
    generated_password_window = tk.Toplevel()
    generated_password_window.title("Senha Gerada")

    # Tamanho da janela
    window_width = 400
    window_height = 200
    screen_width = generated_password_window.winfo_screenwidth()
    screen_height = generated_password_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    generated_password_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Exibe a senha gerada
    password_label = tk.Label(
    generated_password_window,
    text=f"A senha para {site} é:\n{password}\nJá foi copiada para seu clipboard!",
    font=("Arial", 14)
)

    password_label.pack(pady=20)

    # Botões "Gerar Outra" e "Sair"
    def generate_another_password():
        generated_password_window.destroy()  # Fecha a janela atual
        generate_password_gui()  # Inicia a geração de uma nova senha

    def exit_program():
        generated_password_window.destroy()  # Fecha a janela e sai
        exit()

    generate_another_button = tk.Button(generated_password_window, text="Gerar Outra", command=generate_another_password, font=("Arial", 14))
    generate_another_button.pack(side=tk.LEFT, padx=20)

    exit_button = tk.Button(generated_password_window, text="Sair", command=exit_program, font=("Arial", 14))
    exit_button.pack(side=tk.RIGHT, padx=20)

    generated_password_window.mainloop()

# Chama a função para rodar o script
if __name__ == "__main__":
    generate_password_gui()

