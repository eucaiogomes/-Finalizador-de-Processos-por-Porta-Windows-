````markdown
# 🔧 Finalizador de Processos por Porta (Windows)

Este script em Python permite localizar e finalizar processos que estejam utilizando uma porta específica no Windows. Ideal para desenvolvedores que precisam liberar rapidamente portas ocupadas, como a 8080.

## 🚀 Funcionalidades

- Localiza automaticamente o(s) processo(s) escutando uma porta específica.
- Finaliza o(s) processo(s) usando `taskkill /PID /F`.
- Funciona em sistemas operacionais Windows.

## 💻 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/eucaiogomes/-Finalizador-de-Processos-por-Porta-Windows-.git
````

2. Acesse a pasta do projeto:

   ```bash
   cd -Finalizador-de-Processos-por-Porta-Windows-
   ```
3. Execute o script com Python:

   ```bash
   python matar_porta.py
   ```
4. Digite o número da porta quando solicitado (ex: `8080`).

## 📌 Requisitos

* Python 3.x
* Sistema Operacional Windows

## ⚠️ Atenção

Use com responsabilidade! O script finaliza processos à força e pode encerrar serviços importantes se usada a porta incorreta.

## ⭐ Contribua

Se este projeto te ajudou, deixe uma estrela ⭐ no repositório e compartilhe com outros devs!

---

Desenvolvido por [Caio Gomes](https://github.com/eucaiogomes) 💻


