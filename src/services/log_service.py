import os
import json
from typing import List
from .log_model import StockLog

# Caminho absoluto e seguro para o arquivo de log
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(CURRENT_DIR, '..', '..', 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'stock_log.json')

def save_log_entry(log: StockLog):
    """
    Salva uma nova entrada de log no arquivo JSON.
    """
    try:
        # Cria a pasta 'logs' se ela não existir
        os.makedirs(LOG_DIR, exist_ok=True)
        
        # Debug: vamos ver se a pasta foi criada
        print(f"[DEBUG] Tentando criar diretório: {LOG_DIR}")
        print(f"[DEBUG] Diretório existe? {os.path.exists(LOG_DIR)}")
        
        logs = load_logs()
        logs.append(log.__dict__)
        
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=4, default=str, ensure_ascii=False)
            
        print(f"[INFO] Log salvo com sucesso em: {LOG_FILE}")
        
    except Exception as e:
        print(f"[ERRO] Ao salvar log: {e}")
        print(f"[DEBUG] Caminho completo: {LOG_FILE}")

def load_logs() -> List[dict]:
    """
    Carrega todos os logs existentes do arquivo JSON.
    """
    if not os.path.exists(LOG_FILE):
        print(f"[DEBUG] Arquivo de log não existe ainda: {LOG_FILE}")
        return []
    
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[ERRO] JSON mal formatado. Retornando lista vazia.")
        return []
    except Exception as e:
        print(f"[ERRO] Ao carregar logs: {e}")
        return []

# Função auxiliar para testar se tudo está funcionando
def test_log_creation():
    """
    Testa se a criação de diretório está funcionando
    """
    print(f"Diretório atual: {CURRENT_DIR}")
    print(f"Diretório de logs: {LOG_DIR}")
    print(f"Arquivo de log: {LOG_FILE}")
    
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        print(f"✅ Diretório criado/verificado: {os.path.exists(LOG_DIR)}")
    except Exception as e:
        print(f"❌ Erro ao criar diretório: {e}")

if __name__ == "__main__":
    # TESTE DIRETO - adicionar no final do arquivo
    print("=== TESTE DIRETO ===")
    test_log_creation()
    
    # Criar um log de teste
    from datetime import datetime
    
    test_log = StockLog(
        timestamp=datetime.now(),
        color="Azul Teste",
        model="Modelo Teste", 
        movement="Saída",
        quantity=5
    )
    
    print("Chamando save_log_entry com log de teste...")
    save_log_entry(test_log)