class Receita:
    def __init__(self, nome, ingredientes):
        """
        Inicializa uma nova receita com um nome e uma lista de ingredientes.
        
        Parâmetros:
        - nome: Nome da receita.
        - ingredientes: Lista de ingredientes, onde cada ingrediente é um dicionário com
                        'grupo', 'descricao', 'unidade', 'quantidade', 'valor_unit' e 'custo'.
        """
        self.nome = nome
        self.ingredientes = ingredientes

    def calcular_custo_total(self):
        """
        Calcula o custo total da receita com base nos ingredientes.
        
        Retorna:
        - Custo total da receita.
        """
        return sum(ingrediente['custo'] for ingrediente in self.ingredientes)

    def exibir_detalhes(self):
        """
        Exibe os detalhes da receita, incluindo o custo total e a lista de ingredientes.
        """
        print(f"Receita: {self.nome}")
        print("Ingredientes:")
        for ingr in self.ingredientes:
            print(f" - {ingr['descricao']} ({ingr['quantidade']} {ingr['unidade']}): R${ingr['custo']:.2f}")
        print(f"Custo Total: R${self.calcular_custo_total():.2f}\n")


def carregar_receitas(excel_data):
    """
    Carrega todas as receitas de uma planilha Excel.
    
    Parâmetros:
    - excel_data: Objeto ExcelFile com os dados da planilha.
    
    Retorna:
    - Lista de objetos Receita.
    """
    receitas = []

    for sheet_name in excel_data.sheet_names:
        # Carregar dados da aba
        sheet = excel_data.parse(sheet_name)
        
        # Ignorar abas que não seguem a estrutura padrão
        if sheet.shape[0] < 5 or 'ITEM' not in sheet.columns:
            continue
        
        # Extrair dados dos ingredientes
        ingredientes = []
        for _, row in sheet.iterrows():
            if pd.notna(row.get("ITEM")):  # Verifica se há um item válido na linha
                ingrediente = {
                    'grupo': row.get("GRUPO"),
                    'descricao': row.get("Descrição"),
                    'unidade': row.get("UM"),
                    'quantidade': row.get("QUANTIDADE"),
                    'valor_unit': row.get("VALOR UNIT"),
                    'custo': row.get("CUSTO", 0)
                }
                ingredientes.append(ingrediente)
        
        # Criar objeto Receita
        receita = Receita(nome=sheet_name, ingredientes=ingredientes)
        receitas.append(receita)
    
    return receitas


# Carregar todas as receitas e exibir detalhes
receitas = carregar_receitas(excel_data)

# Exibir detalhes das receitas carregadas
for receita in receitas[:3]:  # Exibir apenas as 3 primeiras para não sobrecarregar a saída
    receita.exibir_detalhes()
