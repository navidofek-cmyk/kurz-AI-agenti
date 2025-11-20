# Výsledky testování AI Agenta - Lekce 1

**Autor:** Ivan Dofek  
**Datum:** 20. 11. 2025  
**Model:** GPT-4o (OpenAI)

---

## 📊 Přehled testů

Celkem provedeno: **5 testů**  
✅ Úspěšné: **5**  
❌ Neúspěšné: **0**  
🔧 Použití nástroje: **4x**  
💬 Bez nástroje: **1x**

---

## Test 1: Jednoduchý výpočet (násobení)

### Dotaz
```
Kolik je 123 krát 456?
```

### Průběh
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

### Vyhodnocení
✅ **ÚSPĚCH**
- Model správně identifikoval potřebu nástroje
- Nástroj vrátil správný výsledek: 56088
- Odpověď je přesná a srozumitelná

---

## Test 2: Slovní úloha (složený výpočet)

### Dotaz
```
Mám 1500 Kč. Koupím 3 položky po 275 Kč. Kolik mi zbyde?
```

### Průběh
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
   Nyní spočítáme, kolik ti zbude z 1500 Kč.
   1500 Kč - 825 Kč = 675 Kč
   Takže ti zbyde 675 Kč.
```

### Vyhodnocení
✅ **ÚSPĚCH**
- Model použil nástroj pro násobení (3 × 275)
- Odčítání provedl sám (1500 - 825)
- Správný výsledek: 675 Kč
- Dobré vysvětlení postupu

---

## Test 3: Logická úloha (bez nástroje)

### Dotaz
```
Jak dlouho bude trvat natřít stěnu jednomu pracovníkovi, 
když dva stejnou stěnu natírají hodinu?
```

### Průběh
```
🤖 AI Agent začíná...
📝 Uživatel: Jak dlouho bude trvat natřít stěnu jednomu pracovníkovi, 
             když dva stejnou stěnu natírají hodinu?

⏳ Posílám dotaz LLM modelu...
💬 Odpověď (bez použití nástroje): Pokud dva pracovníci natřou stěnu 
   za jednu hodinu, tak jednomu pracovníkovi by natření stejné stěny 
   trvalo dvakrát déle. Takže jednomu pracovníkovi to zabere 2 hodiny.
```

### Vyhodnocení
✅ **ÚSPĚCH**
- Model správně rozpoznal, že nepotřebuje kalkulačku
- Logická úvaha je správná
- Odpověď: 2 hodiny ✓

---

## Test 4: Dělení s desetinným výsledkem

### Dotaz
```
Kolik je 100 děleno 3?
```

### Průběh
```
🤖 AI Agent začíná...
📝 Uživatel: Kolik je 100 děleno 3?

⏳ Posílám dotaz LLM modelu...
🔧 Model chce použít 1 nástroj(ů):

  📌 Nástroj: calculate
  📊 Argumenty: {'operation': 'divide', 'a': 100, 'b': 3}
  ✅ Výsledek: {"result": 33.333333333333336}

⏳ Posílám výsledek nástroje zpět LLM modelu...
💬 Finální odpověď: Výsledek 100 děleno 3 je přibližně 33,33 
   (nebo přesněji 33 a 1/3).
```

### Vyhodnocení
✅ **ÚSPĚCH**
- Model použil nástroj pro dělení
- Správně zaokrouhlil výsledek
- Přidal dodatečnou informaci (33 a 1/3)

---

## Test 5: Komplexní výpočet

### Dotaz
```
Pokud mám 50 jablek a rozdám je 8 lidem rovnoměrně, 
kolik jablek dostane každý a kolik mi zbude?
```

### Průběh
```
🤖 AI Agent začíná...
📝 Uživatel: Pokud mám 50 jablek a rozdám je 8 lidem rovnoměrně,
             kolik jablek dostane každý a kolik mi zbude?

⏳ Posílám dotaz LLM modelu...
🔧 Model chce použít 1 nástroj(ů):

  📌 Nástroj: calculate
  📊 Argumenty: {'operation': 'divide', 'a': 50, 'b': 8}
  ✅ Výsledek: {"result": 6.25}

⏳ Posílám výsledek nástroje zpět LLM modelu...
💬 Finální odpověď: Každý člověk dostane 6 jablek a zbudou ti 2 jablka.
   (50 ÷ 8 = 6 se zbytkem 2)
```

### Vyhodnocení
✅ **ÚSPĚCH**
- Model správně použil dělení
- Správně interpretoval desetinný výsledek jako celé číslo se zbytkem
- Výsledek: 6 jablek/osobu, zbytek 2 ✓

---

## 📈 Statistiky nástrojů

| Nástroj    | Operace   | Počet použití |
|------------|-----------|---------------|
| calculate  | multiply  | 2×            |
| calculate  | divide    | 2×            |
| calculate  | add       | 0×            |
| calculate  | subtract  | 0×            |

---

## 💡 Pozorování

### Co funguje dobře
✅ Model správně rozhoduje, kdy použít nástroj  
✅ Nástroj pro výpočty funguje přesně  
✅ Model umí interpretovat výsledky a přidat kontext  
✅ Odpovědi jsou srozumitelné a příjemné pro uživatele  

### Možná vylepšení
🔧 Přidat nástroj pro modulo (zbytek po dělení)  
🔧 Přidat nástroj pro mocniny a odmocniny  
🔧 Přidat nástroj pro převody jednotek  
🔧 Přidat podporu pro historii konverzace  

---

## 🎯 Závěr

Agent úspěšně splňuje všechny požadavky zadání:
1. ✅ Komunikuje s LLM API (OpenAI GPT-4o)
2. ✅ Používá nástroj (matematická kalkulačka)
3. ✅ Vrací výsledky nástroje zpět modelu
4. ✅ Generuje finální odpověď pro uživatele

Projekt je **plně funkční** a připravený k odevzdání.
