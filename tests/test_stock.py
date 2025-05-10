import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from services.stock_service import list_colors_by_model, update_quantity





def display_colors(id_models):
    colors = list_colors_by_model(id_models)
    print(f"\nCores do modelo {id_models}: ")
    for color in colors:
        id_colors, name, amount = color
        amount = amount if amount is not None else 0
        print(f"ID: {id_colors} | Nome: {name} | Quantidade: {amount}")
    
    return colors

def get_current_quantity(id_colors, colors):
    for color in colors:
        if color[0] == id_colors:
            return color[2] if color[2] is not None else 0
    
    return 0

def main():
    id_models = int(input("Digite o ID do modelo (1 a 4): "))

    colors = display_colors(id_models)

    id_colors = int(input("\nDigite o ID da cor que deseja movimentar: "))
    operation = input("Digite 'e' para entrada ou 's' para saída: ")

    value = int(input("Quantidade a movimentar: "))
    actualy = get_current_quantity(id_colors, colors)

    if operation == 'e':
        new = actualy + value
    elif operation == 's':
        if value > actualy:
            print("Erro: Não há estoque suficiente para essa saída.")
            return
        new = actualy - value
    else:
        print("Operação inválida.")
        return
    
    update_quantity(new, id_colors)
    print("\nEstoque atualizado com sucesso!")

    display_colors(id_models)

if __name__ == "__main__":
    main()

