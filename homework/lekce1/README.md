# AI Agent s nástroji - Lekce 1

Praktické cvičení z předmětu AI Agenti - implementace jednoduchého agenta s nástrojem.

## 📋 Zadání

Vytvořit Python skript, který:
1. ✅ Zavolá LLM API
2. ✅ Použije nějaký nástroj (matematická kalkulačka)
3. ✅ Vrátí výsledek nástroje zpět LLM modelu
4. ✅ Získá finální odpověď

## 🚀 Funkce

- **LLM Integrace**: Komunikace s OpenAI API (nebo lokální Ollama)
- **Matematické nástroje**: Sčítání, odčítání, násobení, dělení
- **Tool Calling**: Automatické rozhodování, kdy použít nástroj
- **Interaktivní režim**: Možnost zadat vlastní dotaz

## 📁 Struktura projektu

```
lekce1/
├── main.py              # Hlavní skript s AI agentem
├── tools.py             # Definice nástrojů (kalkulačka)
├── pyproject.toml       # Závislosti projektu
├── .env.example         # Příklad konfigurace
├── .env                 # Tvá konfigurace (nepřidávat do gitu!)
└── README.md            # Tento soubor
```

## 🛠️ Instalace

### 1. Naklonuj repozitář

```bash
git clone <tvuj-github-repo>
cd homework/lekce1
```

### 2. Vytvoř virtuální prostředí

```bash
python -m venv .venv
```

### 3. Aktivuj virtuální prostředí

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Nainstaluj závislosti

```bash
pip install openai python-dotenv
```

nebo pomocí pyproject.toml:

```bash
pip install -e .
```

### 5. Nastav API klíč

Edituj soubor `.env` a přidej svůj OpenAI API klíč:

```env
OPENAI_API_KEY=sk-proj-tvuj-api-key-zde
```

## ▶️ Spuštění

```bash
python main.py
```

## 📖 Jak to funguje

### 1. Uživatel položí otázku

```python
"Kolik je 123 krát 456?"
```

### 2. LLM model dostane dotaz + definici nástrojů

```python
tools = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Provede matematickou operaci...",
        "parameters": {...}
    }
}]
```

### 3. Model se rozhodne použít nástroj

```json
{
  "tool_call": {
    "function": "calculate",
    "arguments": {
      "operation": "multiply",
      "a": 123,
      "b": 456
    }
  }
}
```

### 4. Nástroj se spustí a vrátí výsledek

```python
result = calculate("multiply", 123, 456)  # 56088
```

### 5. Výsledek se pošle zpět LLM

Model dostane kontext:
- Původní dotaz
- Že použil nástroj
- Výsledek nástroje: `56088`

### 6. Model vytvoří finální odpověď

```
"Výsledek násobení 123 krát 456 je 56 088."
```

## 🎯 Ukázkový výstup

### Příklad 1: Jednoduchý výpočet
```
🤖 AI Agent začíná...
📝 Uživatel: Kolik je 123 krát 456?

⏳ Posílám dotaz LLM modelu...
🔧 Model chce použít 1 nástroj(ů):

  📌 Nástroj: calculate
  📊 Argumenty: {'operation': 'multiply', 'a': 123, 'b': 456}
  ✅ Výsledek: {"result": 56088}

⏳ Posílám výsledek nástroje zpět LLM modelu...
💬 Finální odpověď: Výsledek násobení 123 krát 456 je 56 088.
```

### Příklad 2: Slovní úloha
```
🤖 AI Agent začíná...
📝 Uživatel: Mám 1500 Kč. Koupím 3 položky po 275 Kč. Kolik mi zbyde?

⏳ Posílám dotaz LLM modelu...
🔧 Model chce použít 1 nástroj(ů):

  📌 Nástroj: calculate
  📊 Argumenty: {'operation': 'multiply', 'a': 3, 'b': 275}
  ✅ Výsledek: {"result": 825}

⏳ Posílám výsledek nástroje zpět LLM modelu...
💬 Finální odpověď: Celková cena za 3 položky po 275 Kč je 825 Kč. 
                   1500 Kč - 825 Kč = 675 Kč. Zbude ti 675 Kč.
```

### Příklad 3: Otázka bez použití nástroje
```
📝 Uživatel: Jak dlouho bude trvat natřít stěnu jednomu pracovníkovi, 
             když dva stejnou stěnu natírají hodinu?

⏳ Posílám dotaz LLM modelu...
💬 Odpověď (bez použití nástroje): Pokud dva pracovníci natřou stěnu 
   za jednu hodinu, tak jednomu pracovníkovi by natření stejné stěny 
   trvalo dvakrát déle. Takže jednomu pracovníkovi to zabere 2 hodiny.
```

## 🔧 Možná rozšíření

- Přidat více nástrojů (např. převody jednotek, získání aktuální doby, počasí)
- Implementovat history konverzace
- Přidat logování do souboru
- Vytvořit webové rozhraní (Flask/Streamlit)
- Přidat unit testy

## 📚 Závislosti

- `openai>=1.0.0` - OpenAI Python SDK (funguje i pro Ollama)
- `python-dotenv>=1.0.0` - Načítání proměnných prostředí

## 👤 Autor

Ivan Dofek  
AI Agenti - Lekce 1  
Datum: 18.11.2025

## 📝 Licence

Tento projekt je vytvořen pro vzdělávací účely.
