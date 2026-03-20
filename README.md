# 🔐 Port Scanner em Python

Este projeto é um **scanner de portas simples** desenvolvido em Python, com foco em aprendizado de redes e segurança ofensiva (reconhecimento).

A ferramenta permite verificar se portas estão abertas ou fechadas em um determinado host (IP ou domínio).

---

## 🚀 Funcionalidades

* 🌐 Entrada de alvo por:

  * IP
  * URL (domínio)

* 🔍 Tipos de varredura:

  * Porta específica
  * Intervalo de portas
  * Scan completo das portas comuns (1–1023)

* ⚡ Identificação de:

  * Portas abertas
  * Portas fechadas

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca nativa `socket`

---

## 📦 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/port-scanner.git
cd port-scanner
```

---

### 2. Execute o script

```bash
python scanner.py
```

---

## 🧠 Como funciona

O programa utiliza a função:

```python
socket.connect_ex((IP, porta))
```

* Retorno `0` → Porta aberta
* Retorno diferente de `0` → Porta fechada

---

## 💻 Exemplo de uso

```
///// ALVO /////

[1] Voce quer digitar um IP
[2] Voce quer Digitar um Url de um Site
```

Depois:

```
///// PORT SCANNER /////

[1] Scannear porta Especifica
[2] Scannear Um intervalo de portas
[3] Listar todas as portas
[4] Sair
```

---

## 📸 Exemplo de saída

```
A porta 80 esta aberta
A porta 22 esta aberta
A porta 443 esta aberta
A porta 21 esta fechada
```

---

## ⚠️ Aviso importante

Este projeto é destinado **exclusivamente para fins educacionais**.

⚠️ Não utilize este scanner em sistemas sem autorização.
A varredura de portas sem permissão pode ser considerada atividade ilegal.

---

## 💡 Melhorias futuras

* 🔥 Implementar multithreading (scan muito mais rápido)
* 📊 Exibir apenas portas abertas (modo silencioso)
* 🧠 Identificação de serviços (banner grabbing)
* 📝 Exportar resultados para arquivo `.txt` ou `.json`
* ⏱️ Adicionar timeout configurável

---

## 👨‍💻 Autor

Desenvolvido por **Davi** 🚀
Estudante de Sistemas de Informação com foco em back-end e cibersegurança.

---

## ⭐ Contribuição

Contribuições são bem-vindas!

* Abra uma issue
* Envie um pull request

---

## 📚 Observação

Você pode testar com segurança usando:

```
scanme.nmap.org
```

Servidor oficial para testes da ferramenta Nmap.

---
