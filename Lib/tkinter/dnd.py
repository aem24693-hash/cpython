import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

OUTPUT_FOLDER = "outputs"
ALLOWED_EXTENSIONS = {'.pdf', '.doc', '.docx'}

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_EXTENSIONS

def convert_to_tns(input_path):
    filename = os.path.basename(input_path)
    name, _ = os.path.splitext(filename)
    output_path = os.path.join(OUTPUT_FOLDER, name + ".tns")
    shutil.copyfile(input_path, output_path)
    return output_path

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Documents", "*.pdf *.doc *.docx")]
    )

    if not file_path:
        return

    if not allowed_file(file_path):
        messagebox.showerror("Erro", "Formato inválido")
        return

    try:
        output = convert_to_tns(file_path)
        messagebox.showinfo("Sucesso", f"Ficheiro criado:\n{output}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

app = tk.Tk()
app.title("PDF/Word → TNS Converter")
app.geometry("300x150")

label = tk.Label(app, text="Seleciona um ficheiro")
label.pack(pady=10)

btn = tk.Button(app, text="Escolher ficheiro", command=select_file)
btn.pack(pady=10)

app.mainloop()
