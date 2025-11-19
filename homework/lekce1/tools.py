"""
Matematické nástroje pro AI agenta
"""
import json


def calculate(operation: str, a: float, b: float) -> float:
    """
    Provede matematickou operaci se dvěma čísly.
    
    Args:
        operation: Typ operace ('add', 'subtract', 'multiply', 'divide')
        a: První číslo
        b: Druhé číslo
    
    Returns:
        Výsledek operace
    """
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else None
    }
    
    if operation not in operations:
        raise ValueError(f"Neznámá operace: {operation}")
    
    result = operations[operation](a, b)
    if result is None:
        raise ValueError("Nelze dělit nulou")
    
    return result


def get_tool_definition():
    """
    Vrátí definici nástroje pro LLM API (OpenAI format)
    """
    return {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Provede matematickou operaci se dvěma čísly (sčítání, odčítání, násobení, dělení)",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "Typ operace: 'add' (sčítání), 'subtract' (odčítání), 'multiply' (násobení), 'divide' (dělení)"
                    },
                    "a": {
                        "type": "number",
                        "description": "První číslo"
                    },
                    "b": {
                        "type": "number",
                        "description": "Druhé číslo"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        }
    }


def execute_tool(tool_name: str, arguments: dict) -> str:
    """
    Spustí nástroj podle názvu a argumentů
    
    Args:
        tool_name: Název nástroje
        arguments: Argumenty pro nástroj
    
    Returns:
        Výsledek jako string
    """
    if tool_name == "calculate":
        result = calculate(
            operation=arguments["operation"],
            a=arguments["a"],
            b=arguments["b"]
        )
        return json.dumps({"result": result})
    else:
        raise ValueError(f"Neznámý nástroj: {tool_name}")
