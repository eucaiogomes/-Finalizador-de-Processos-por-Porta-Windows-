import os
import subprocess

def matar_processo_por_porta(porta):
    try:
        # Encontra o PID do processo que está usando a porta
        resultado = subprocess.check_output(f'netstat -ano | findstr :{porta}', shell=True, text=True)
        
        # Extrai os PIDs das linhas de saída
        linhas = resultado.strip().split('\n')
        pids = set()
        for linha in linhas:
            partes = linha.split()
            if len(partes) >= 5:
                pid = partes[-1]
                pids.add(pid)
        
        # Mata os processos encontrados
        for pid in pids:
            print(f"Matando PID {pid}...")
            os.system(f"taskkill /PID {pid} /F")
        
        if not pids:
            print(f"Nenhum processo encontrado na porta {porta}.")
    except subprocess.CalledProcessError:
        print(f"Nenhum processo está usando a porta {porta}.")

# Exemplo de uso
porta_desejada = input("Digite o número da porta: ")
matar_processo_por_porta(porta_desejada)
