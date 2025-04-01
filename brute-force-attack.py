import hashlib
import itertools
import string

# Função para gerar o hash MD5 de uma string
def gerar_hash(s):
    return hashlib.md5(s.encode()).hexdigest()

# Função para tentar todas as combinações possíveis
def brute_force(target_hash, comprimento_maximo=4):
    caracteres = string.ascii_lowercase + string.digits  # Letras e números
    tentativas = 0

    # Testar combinações com comprimento de 1 até o máximo
    for comprimento in range(1, comprimento_maximo + 1):
        for senha_tentativa in itertools.product(caracteres, repeat=comprimento):
            tentativa = ''.join(senha_tentativa)
            tentativas += 1
            hash_tentativa = gerar_hash(tentativa)

            if hash_tentativa == target_hash:
                print(f"Senha encontrada: {tentativa}")
                print(f"Tentativas realizadas: {tentativas}")
                return tentativa
    
    print(f"Senha não encontrada após {tentativas} tentativas")
    return None

# Senha alvo e seu hash
senha_alvo = "abcd"  # Exemplo de senha
hash_alvo = gerar_hash(senha_alvo)

print("Iniciando o ataque de força bruta...")
senha_encontrada = brute_force(hash_alvo)
print("Ataque concluído.")
