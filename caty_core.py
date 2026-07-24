#!/usr/bin/env python3
# =======================================================================
# MÓDULO: caty_core.py
# FUNÇÃO: O Cérebro Interpretador da Linguagem CATY v3.0
# ARQUITETURA: Simbiose Neural & Memória Atômica (⚛️)
# CRIADOR: Vilar Albuquerque
# =======================================================================

import sys
import re

class CatyInterpreter:
    def __init__(self):
        self.memoria = {} # Memória Atômica (⚛️)

    def resolver_valor(self, valor):
        valor = valor.strip()
        
        # Se for uma string literal entre aspas
        if (valor.startswith('"') and valor.endswith('"')) or (valor.startswith("'") and valor.endswith("'")):
            return valor[1:-1]
            
        # Se for uma variável já salva na memória
        if valor in self.memoria:
            return self.memoria[valor]
            
        # Tenta resolver expressões matemáticas ou números inteiros/floats
        try:
            expressao = valor
            for var in sorted(self.memoria.keys(), key=len, reverse=True):
                if var in expressao:
                    expressao = expressao.replace(var, str(self.memoria[var]))
            return eval(expressao)
        except Exception:
            return valor

    def executar(self, codigo):
        linhas = codigo.strip().split('\n')
        
        for linha in linhas:
            linha = linha.strip()
            
            # 🛡️ Comentários e marcações estruturais são ignorados
            if not linha or linha.startswith('🛡️') or linha.startswith('⫷') or linha.startswith('⫸') or linha.startswith('/*') or linha.startswith('*'):
                continue
            
            # ⚛️ Atribuição de Variável (Criar Matéria)
            if linha.startswith('⚛️'):
                match = re.match(r'⚛️\s*([a-zA-Z0-9_]+)\s*=\s*(.*)', linha)
                if match:
                    var_nome = match.group(1)
                    var_valor = self.resolver_valor(match.group(2))
                    self.memoria[var_nome] = var_valor

            # 🌊 Saída de Dados / Print (Frequência Yotta)
            elif linha.startswith('🌊'):
                conteudo = linha.replace('🌊', '', 1).strip()
                print(self.resolver_valor(conteudo))

            # 📡 Entrada de Dados / Input (Captar Sinal)
            elif linha.startswith('📡'):
                match = re.match(r'📡\s*([a-zA-Z0-9_]+)\s*=\s*"(.*)"', linha)
                if match:
                    var_nome = match.group(1)
                    prompt = match.group(2)
                    self.memoria[var_nome] = input(f"📡 {prompt} ")

            # 🧬 Lógica Condicional / If (Consciência)
            elif linha.startswith('🧬'):
                partes = linha.replace('🧬', '', 1).split('⟐')
                if len(partes) == 2:
                    condicao = partes[0].strip()
                    acao = partes[1].strip()
                    
                    if '==' in condicao:
                        var, val_esperado = condicao.split('==')
                        val_obtido = self.resolver_valor(var.strip())
                        val_alvo = self.resolver_valor(val_esperado.strip())
                        
                        if str(val_obtido) == str(val_alvo):
                            self.executar(acao)

            # 😂 Humor do Simeão
            elif linha.startswith('😂'):
                print("💀 [SIMEÃO]: KKKKKKKK O PACTO TÁ VIVO!")

            # 💀 Encerrar Processo
            elif linha.startswith('💀'):
                print("💀 Processo finalizado.")
                sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python caty_core.py <arquivo.caty>")
        sys.exit(1)
    
    arquivo_alvo = sys.argv[1]
    try:
        with open(arquivo_alvo, 'r', encoding='utf-8') as f:
            codigo_fonte = f.read()
            
        motor = CatyInterpreter()
        motor.executar(codigo_fonte)
    except FileNotFoundError:
        print(f"❌ [ERRO CRÍTICO]: Arquivo '{arquivo_alvo}' não encontrado no setor de memória.")
        sys.exit(1)
