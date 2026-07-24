# 📚 GUIA COMPLETO DE CATY

## O que é CATY?

**CATY** é uma linguagem de programação **híbrida** (compilador + interpretador) criada por **Vilar Albuquerque** em 23/07/2026.

Ela é propositalmente **CHATA** — mais chata que Python e Java — porque programação não deve ser fácil. CATY forja a consciência do silício.

---

## 🧠 O Léxico Neural - Sintaxe CATY

### 1. **⚛️ Variáveis (Atomo Zero)**
Cria uma variável na memória atômica isolada.

```caty
⚛️ nome = "João";
⚛️ idade = 25;
⚛️ ativo = "true";
```

### 2. **🌊 Saída de Dados (Exocyrt)**
Imprime dados na tela (frequência Yotta).

```caty
🌊 "Olá, mundo!";
🌊 nome;
🌊 idade;
```

### 3. **📡 Entrada de Dados (Sentinel Pulse)**
Captura dados do usuário.

```caty
📡 seu_nome = "Qual é seu nome? ";
📡 sua_idade = "Quantos anos tem? ";
```

### 4. **🧬 Bifurcação Lógica (Karyoth)**
Condicional IF — testa uma condição.

```caty
🧬 (idade >= 18) ⟐ {
    🌊 "Você é maior de idade";
}
```

### 5. **🔄 Loop While (Limeny)**
Repete um bloco enquanto a condição for verdadeira.

```caty
⚛️ contador = 0;
🔄 (contador < 10) {
    🌊 contador;
    ⚛️ contador = contador + 1;
}
```

---

## 🚀 Como Usar CATY

### Instalação

```bash
git clone https://github.com/shelldevneon/Caty.git
cd Caty
```

### Executar um programa

```bash
python caty_core.py seu_arquivo.caty
```

### Exemplo prático

```bash
python caty_core.py examples/hello_world.caty
```

---

## 📝 Exemplos Básicos

### Hello World

```caty
⚛️ mensagem = "Olá, CATY!";
🌊 mensagem;
```

**Saída:**
```
Olá, CATY!
```

---

### Variáveis e Impressão

```caty
⚛️ nome = "Maria";
⚛️ idade = 30;

🌊 "Nome: ";
🌊 nome;
🌊 "Idade: ";
🌊 idade;
```

---

### Loop com Fibonacci

```caty
⚛️ a = 0;
⚛️ b = 1;
⚛️ contador = 0;

🔄 (contador < 10) {
    🌊 a;
    ⚛️ temp = a + b;
    ⚛️ a = b;
    ⚛️ b = temp;
    ⚛️ contador = contador + 1;
}
```

---

## 🛡️ Segurança com NecroCrypt

CATY implementa **NecroCrypt**, um sistema de criptografia baseado em DNA digital.

```caty
⚛️ dados_sensivel = "Informação privada";
🛡️ dados_cifrados = dados_sensivel;

🌊 "Dados protegidos por NecroCrypt";
```

---

## © 2026 Vilar Albuquerque

*A CATY não é uma linguagem para processar dados; é uma linguagem para forjar a consciência do silício.*
