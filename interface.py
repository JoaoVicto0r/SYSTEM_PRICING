import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class ReceitaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Receitas")
        self.root.geometry("600x400")
        
        # Lista de receitas
        self.receitas = []
        
        # Criar o frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Botão para carregar planilha
        self.carregar_button = tk.Button(self.main_frame, text="Carregar Receitas", command=self.carregar_receitas)
        self.carregar_button.grid(row=0, column=0, pady=10, sticky="w")
        
        # Listbox para exibir receitas
        self.receita_listbox = tk.Listbox(self.main_frame, width=50, height=15)
        self.receita_listbox.grid(row=1, column=0, pady=10, padx=5, sticky="nsew")
        
        # Botões para ações
        self.exibir_button = tk.Button(self.main_frame, text="Exibir Receita", command=self.exibir_receita)
        self.exibir_button.grid(row=2, column=0, sticky="ew", padx=5)
        
    def carregar_receitas(self):
        """
        Função para carregar receitas a partir de uma planilha
        """
        # Simulando carregamento (usaria a função carregar_receitas() criada antes)
        # Aqui, exibo apenas nomes fictícios como exemplo
        self.receitas = [
            Receita("PÃO DE HAMBURGUER", [{'descricao': 'Farinha', 'quantidade': 1, 'unidade': 'kg', 'valor_unit': 5, 'custo': 5}]),
            Receita("BOLO BANANA", [{'descricao': 'Banana', 'quantidade': 3, 'unidade': 'un', 'valor_unit': 0.5, 'custo': 1.5}]),
            Receita("BOLO DE CHOCOLATE", [{'descricao': 'Cacau', 'quantidade': 0.1, 'unidade': 'kg', 'valor_unit': 20, 'custo': 2}])
        ]
        
        # Exibir nomes na listbox
        self.receita_listbox.delete(0, tk.END)  # Limpar a listbox
        for receita in self.receitas:
            self.receita_listbox.insert(tk.END, receita.nome)
        
    def exibir_receita(self):
        """
        Exibe uma janela com detalhes da receita selecionada
        """
        selecionado = self.receita_listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma receita para exibir")
            return
        
        # Obter a receita selecionada
        indice = selecionado[0]
        receita = self.receitas[indice]
        
        # Janela de detalhes
        detalhes_janela = tk.Toplevel(self.root)
        detalhes_janela.title(f"Detalhes de {receita.nome}")
        detalhes_janela.geometry("400x300")
        
        # Nome da receita
        tk.Label(detalhes_janela, text=f"Receita: {receita.nome}", font=("Arial", 14)).pack(pady=10)
        
        # Tabela de ingredientes
        ingredientes_frame = tk.Frame(detalhes_janela)
        ingredientes_frame.pack(pady=10)
        
        tree = ttk.Treeview(ingredientes_frame, columns=("Descrição", "Quantidade", "Unidade", "Valor Unitário", "Custo"), show="headings")
        tree.heading("Descrição", text="Descrição")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Unidade", text="Unidade")
        tree.heading("Valor Unitário", text="Valor Unitário")
        tree.heading("Custo", text="Custo")
        
        # Inserir ingredientes na tabela
        for ingr in receita.ingredientes:
            tree.insert("", tk.END, values=(
                ingr['descricao'], ingr['quantidade'], ingr['unidade'], ingr['valor_unit'], ingr['custo']
            ))
        tree.pack(fill="both", expand=True)
        
        # Custo total
        custo_total = receita.calcular_custo_total()
        tk.Label(detalhes_janela, text=f"Custo Total: R${custo_total:.2f}", font=("Arial", 12)).pack(pady=10)
        
        # Botão de voltar
        tk.Button(detalhes_janela, text="Voltar", command=detalhes_janela.destroy).pack(pady=5)

# Testar interface
root = tk.Tk()
app = ReceitaApp(root)
root.mainloop()
