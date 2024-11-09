from rembg import remove
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import io

# Função para abrir a imagem e remover o fundo
def remove_background():
    # Abrir caixa de diálogo para escolher uma imagem
    filepath = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not filepath:
        return  # Sai da função se o usuário cancelar
    
    try:
        # Abrir e remover o fundo da imagem
        with open(filepath, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)
        
        # Carregar a imagem sem fundo
        output_image = Image.open(io.BytesIO(output_data))
        
        # Exibir a imagem na tela
        output_image.thumbnail((300, 300))  # Redimensiona para caber na tela
        output_image_tk = ImageTk.PhotoImage(output_image)
        
        result_label.config(image=output_image_tk)
        result_label.image = output_image_tk  # Armazena a imagem para evitar descarte
        
        # Salvar a imagem sem fundo
        output_image.save("imagem_sem_fundo.png")
        messagebox.showinfo("Sucesso", "Fundo removido e imagem salva como 'imagem_sem_fundo.png'")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Remover Fundo de Imagem")
root.geometry("400x400")

# Botão para remover o fundo
remove_bg_button = tk.Button(root, text="Selecionar Imagem e Remover Fundo", command=remove_background)
remove_bg_button.pack(pady=20)

# Label para exibir a imagem com fundo removido
result_label = tk.Label(root)
result_label.pack()

# Iniciar a aplicação
root.mainloop()
