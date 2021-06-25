# Importação da library pathlib, para lidar com diretórios e caminhos (paths).
from pathlib import Path


# Prompt para pedir o caminho absoluto, onde o arquivo se encontra,
# ao usuário. 
input_file_path = Path(input("Enter the file path (absolute): "))

# Prompt para pedir o nome do arquivo que deseja utilizar, ao usuário.
input_file_name = input("Enter file name: ")

# Arquivo e o seu caminho absoluto.
file_to_open = input_file_path / input_file_name


# Dicionário contendo o nome dos países, de acordo com seu código telefônico.
country = {
    "52": "Mexico",
    "55": "Brasil",
    "56": "Chile"
}

# Dicionário contendo o número total de usuários por país, de acordo com seu
# código telefônico.
users_per_country = {
    "52": 0,
    "55": 0,
    "56": 0
}

# Dicionário contendo o número de usuários ativos por país, de acordo com seu
# código telefônico.
active_users_per_country = {
    "52": 0,
    "55": 0,
    "56": 0
}


# With statement, usado para abrir e fechar o arquivo indicado pelo usuário
with open(file_to_open, "r") as file:
    # Itera pelas linhas do arquivo, uma por uma
    for line in file:
        
        # Seleciona a substring com o código telefônico do país.
        calling_code = line[0: 2]
        
        # Seleciona a substring com o status da assinatura do usuário.
        user_subscription_status = line[15: (len(line) - 1)]

        # Soma 1 (um) ao número total de usuários do país, indicado pelo seu
        # código telefônico.
        users_per_country[calling_code] += 1
        
        # Se o status da assinatura do usuário for "assinado", soma 1 (um) ao
        # número de usuários ativos do país.
        if user_subscription_status == "assinado":
            active_users_per_country[calling_code] += 1


# Função que recebe o código telefônico de um país, e cria uma string com seus
# dados.
# Dados do país: nome do país, número total de usuários e número de usuários
# ativos.
def country_data(code):
    return ("{}, {}, {}\n"
            .format(country[code],
                    users_per_country[code],
                    active_users_per_country[code]))


# Prompt para pedir ao usuário o caminho onde o arquivo deve ser salvo.
output_file_path = Path(input("Enter (the path) where you want the file to be saved: "))

# Prompt para pedir ao usuário o nome do arquivo a ser salvo.
output_file_name = input(
    "Enter the name of the file you wish to create: ")

# Arquivo a ser salvo.
file_to_save = output_file_path / output_file_name


# With statement, que cria o novo arquivo com os dados dos países.
with open(file_to_save, "w") as file:
    file.writelines([country_data("55"),
                     country_data("56"),
                     country_data("52")])
