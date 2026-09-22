import hashlib
import itertools
import time

def calcula_hash(texto: str) -> str:
    """Calcula o hash SHA-256 de um texto."""
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

# 1. BANCO DE DADOS SIMULADO (Senhas armazenadas apenas como HASH)
usuarios_cadastrados = {
    "alice": calcula_hash("abc"),
    "bob": calcula_hash("bca"),
    "charlie": calcula_hash("cab")
}

def sistema_de_login():
    print("\n--- [SISTEMA DE LOGIN SEGURO] ---")
    usuario = input("👤 Usuário: ").strip().lower()
    senha = input("🔒 Senha: ")
    
    if usuario in usuarios_cadastrados:
        # Verifica se o hash da senha digitada bate com o do banco
        if calcula_hash(senha) == usuarios_cadastrados[usuario]:
            print(f"🎉 Login realizado com sucesso! Bem-vindo, {usuario}.")
            return True
        print("❌ Senha incorreta!")
    else:
        print("❌ Usuário não encontrado!")
    return False

def ataque_forca_bruta():
    print("\n--- [SIMULADOR DE ATAQUE DE FORÇA BRUTA] ---")
    usuario_alvo = input("Alvo do ataque (ex: alice, bob, charlie): ").strip().lower()
    
    if usuario_alvo not in usuarios_cadastrados:
        print("❌ Usuário não existe no sistema.")
        return

    hash_alvo = usuarios_cadastrados[usuario_alvo]
    print(f"Buscando a senha que gera o hash: {hash_alvo}")
    
    # Configurações do ataque (senhas curtas para o teste ser rápido)
    caracteres = "abc"
    tamanho_maximo = 3
    tentativas = 0
    inicio = time.time()
    senha_descoberta = None

    print("\nIniciando quebra de hash por força bruta...")
    
    # Gera combinações de tamanho 1 até o tamanho máximo
    for tamanho in range(1, tamanho_maximo + 1):
        if senha_descoberta:
            break
            
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativas += 1
            senha_teste = "".join(combinacao)
            
            # Compara os hashes
            if calcula_hash(senha_teste) == hash_alvo:
                senha_descoberta = senha_teste
                break

    fim = time.time()
    tempo_total = fim - inicio

    print("-" * 50)
    if senha_descoberta:
        print(f"🔓 SUCESSO! Senha do usuário '{usuario_alvo}' foi quebrada!")
        print(f"🔑 Senha encontrada: '{senha_descoberta}'")
        print(f"📊 Total de tentativas: {tentativas}")
        print(f"⏱️ Tempo gasto: {tempo_total:.4f} segundos")
    else:
        print("❌ Falha! A senha não foi encontrada com as combinações testadas.")
    print("-" * 50)

# Menu principal do programa
if __name__ == "__main__":
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[1] Testar Sistema de Login")
        print("[2] Executar Ataque de Força Bruta")
        print("[3] Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            sistema_de_login()
        elif opcao == "2":
            ataque_forca_bruta()
        elif opcao == "3":
            print("Encerrando simulador. Até logo!")
            break
        else:
            print("Opção inválida!")
