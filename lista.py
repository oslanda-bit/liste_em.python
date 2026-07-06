import tkinter as tk
from tkinter import ttk, menssagebox
import os 

# =============================================
# LISTA DE COMPRAS - Aplicativo em Tkinter 
# =============================================

ARQUIVO = "Lista_compras.txt"

class ListaComprasApp:
       def __init__(self, root):
          self.root = root
          self.root.title("🛒 Lista de compras")
          self.root.geometry("750x550")
          self.root.comfigure(bg="#f0f4f8")

          #Dados em memória
          self.itens = []
          self.item_selecionado = None
         
          self.criar_widgets()
          self.carregar_do_arquivo()
          self.atualizar_lista()
    
       def criar_wedgets(self):
            # ========= TíTULO =========
         lbl_título = tk.Label(  
            self.root,
            text="🛒 LISTA DE COMPRAS",
            front=("Arial", 20, "bold"),
            bg= "#fafafb"
            fg=  "#1a5276"
        )  
         lbl_título.pack(pady=10)

         # ========= FRAME DE ENTRADA ========
         frame_entrada = tk.frame(self.root, "#f0f4f8")
         frame_entrada.pack(pady=10, padx=20, fill="x")

         # Descrição
         tk.Label(frame_entrada, text="Descrição:", font=("Arial", 11),bg= "#f0f4f8",fg= "#2c3e50").grid(row=0, column=0, padx=5, sticky="e")
         self.txt_descricao = tk.Entry(frame_entrada, front=("Arial", 11), width=30,relief="solid", bd=1 )
         self.txt_descricao.grid(row=0, column=1)

                    
                 

         