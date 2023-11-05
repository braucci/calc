#!/usr/bin/env python3
import argparse
import sympy
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

def main():
    parser = argparse.ArgumentParser(description="Calcolatrice interattiva")
    parser.add_argument("-e", "--expression", type=str, help="Esegui un singolo comando e esci")
    args = parser.parse_args()

    variables = {}

    if args.expression:
        try:
            result = evaluate_expression(args.expression, None, variables)
            print_complex(result)
        except Exception as e:
            print(f"Errore durante il calcolo dell'espressione: {e}")

    else:
        interactive_mode(variables)

def interactive_mode(variables):
    print("Benvenuto nella calcolatrice interattiva. Digita 'exit' per uscire.")
    last_result = None
    while True:
        try:
            expression = input("> ")
            if expression.lower() == "exit":
                break
            expression = replace_dot_with_last_result(expression, last_result)
            result = evaluate_expression(expression, last_result, variables)
            last_result = result
            print_complex(result)
        except Exception as e:
            print(f"Errore durante il calcolo dell'espressione: {e}")

def print_complex(result):
    if result.is_complex:
        print(f"{result.evalf()}")
    else:
        print(f"{result}")

def replace_dot_with_last_result(expression, last_result):
    if last_result is not None:
        expression = expression.replace('.', str(last_result))
    return expression

def evaluate_expression(expression, last_result, variables):
    # Creare un ambiente sicuro con funzioni personalizzate e funzioni di SymPy
    safe_env = {'sqrt': sympy.sqrt, 'log': sympy.log, 'ln': sympy.ln,
                'sin': sympy.sin, 'cos': sympy.cos, 'tan': sympy.tan,
                'asin': sympy.asin, 'acos': sympy.acos, 'atan': sympy.atan,
                'fact': sympy.factorial, 'I': sympy.I}

    if last_result is not None:
        safe_env['.'] = last_result

    # Aggiungere variabili all'ambiente
    safe_env.update(variables)

    # Utilizzare SymPy per analizzare e calcolare l'espressione
    transformations = (standard_transformations + (implicit_multiplication_application,))
    parsed_expr = parse_expr(expression, local_dict=safe_env, transformations=transformations)

    # Verificare se l'espressione è un'assegnazione di variabile
    if isinstance(parsed_expr, sympy.Equality):
        variable_name = parsed_expr.lhs
        if not isinstance(variable_name, sympy.Symbol):
            raise ValueError(f"Impossibile assegnare il valore a {variable_name}")
        value = sympy.N(parsed_expr.rhs)
        variables[variable_name.name] = value
        return f"{variable_name} = {value}"
    else:
        # Calcolare il risultato dell'espressione
        result = sympy.N(parsed_expr)
        return result

if __name__ == "__main__":
    main()
