"""
AI Agent s nástroji - Lekce 1

Tento skript demonstruje:
1. Volání LLM API (OpenAI)
2. Použití nástroje (matematická kalkulačka)
3. Vrácení výsledku zpět LLM modelu
4. Získání finální odpovědi
"""
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pprint import pprint
from tools import get_tool_definition, execute_tool

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def run_agent(user_message: str, model: str = "gpt-4o"):
    """
    Spustí AI agenta s nástrojem
    
    Args:
        user_message: Zpráva od uživatele
        model: Model k použití (gpt-4o, gpt-4o-mini)
    """
    # 1. Inicializace konverzace
    messages = [
        {"role": "system", "content": "Jsi užitečný asistent s přístupem k matematické kalkulačce. Když potřebuješ provést výpočet, použij nástroj 'calculate'."},
        {"role": "user", "content": user_message}
    ]
    
    # Definice dostupných nástrojů
    tools = [get_tool_definition()]
    
    print(f"🤖 AI Agent začíná...")
    print(f"📝 Uživatel: {user_message}\n")
    
    # 2. První volání LLM - model se může rozhodnout použít nástroj
    print("⏳ Posílám dotaz LLM modelu...")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    messages.append(response_message)
    
    # 3. Zpracování tool calls (pokud model chce použít nástroj)
    tool_calls = response_message.tool_calls
    
    if tool_calls:
        print(f"🔧 Model chce použít {len(tool_calls)} nástroj(ů):\n")
        
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"  📌 Nástroj: {function_name}")
            print(f"  📊 Argumenty: {function_args}")
            
            # Spuštění nástroje
            try:
                function_response = execute_tool(function_name, function_args)
                print(f"  ✅ Výsledek: {function_response}\n")
                
                # Přidání výsledku nástroje do konverzace
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                })
            except Exception as e:
                print(f"  ❌ Chyba: {e}\n")
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps({"error": str(e)}),
                })
        
        # 4. Druhé volání LLM - model dostane výsledek nástroje a vytvoří finální odpověď
        print("⏳ Posílám výsledek nástroje zpět LLM modelu...")
        second_response = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        
        final_message = second_response.choices[0].message.content
        print(f"💬 Finální odpověď: {final_message}\n")
        
        return final_message
    else:
        # Model nepotřeboval nástroj
        print(f"💬 Odpověď (bez použití nástroje): {response_message.content}\n")
        return response_message.content


def main():
    """
    Hlavní funkce s ukázkovými příklady
    """
    print("=" * 70)
    print("AI AGENT S NÁSTROJI - LEKCE 1")
    print("=" * 70)
    print()
    
    # Používáme model gpt-4o
    model = "gpt-4o"
    
    # Příklad 1: Jednoduchý výpočet
    print("📍 PŘÍKLAD 1: Jednoduchý výpočet")
    print("-" * 70)
    run_agent("Kolik je 123 krát 456?", model=model)
    
    print("\n")
    
    # Příklad 2: Složitější dotaz
    print("📍 PŘÍKLAD 2: Slovní úloha")
    print("-" * 70)
    run_agent("Mám 1500 Kč. Koupím 3 položky po 275 Kč. Kolik mi zbyde?", model=model)
    
    print("\n")
    
    # Příklad 3: Interaktivní režim (volitelné)
    print("📍 PŘÍKLAD 3: Tvůj vlastní dotaz")
    print("-" * 70)
    user_input = input("Zadej svůj dotaz (nebo Enter pro přeskočení): ")
    if user_input.strip():
        run_agent(user_input, model=model)
    else:
        print("⏭️  Přeskočeno\n")
    
    print("=" * 70)
    print("✅ Hotovo!")
    print("=" * 70)


if __name__ == "__main__":
    main()
