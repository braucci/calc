## 1. Introduzione
L'applicazione Calcolatrice Interattiva è un tool basato su Python che permette all'utente di eseguire calcoli matematici sia in modo interattivo che tramite l'input da linea di comando. Utilizza la libreria SymPy per gestire le operazioni matematiche.

## 2. Requisiti
- Python 3.x
- Libreria SymPy

## 3. Installazione
Per installare la libreria SymPy, esegui il seguente comando:
```bash
pip install sympy
```

## 4. Utilizzo
### 4.1 Modalità da linea di comando
Per eseguire un calcolo dalla linea di comando, utilizzare l'opzione `-e` o `--expression` seguita dall'espressione da valutare:
```bash
python calcolatrice.py -e "espressione"
```

### 4.2 Modalità interattiva
Per avviare la modalità interattiva, basta eseguire lo script senza argomenti:
```bash
python calcolatrice.py
```
Nella modalità interattiva, inserire le espressioni al prompt `>`. Digitare `exit` per uscire.

## 5. Funzionalità
### 5.1 Funzioni Matematiche Supportate
- Radice quadrata: `sqrt`
- Logaritmo: `log`
- Logaritmo naturale: `ln`
- Funzioni trigonometriche: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- Fattoriale: `fact`

### 5.2 Variabili
È possibile assegnare valori alle variabili usando l'operatore `=`. Una volta assegnato un valore, la variabile può essere utilizzata in espressioni successive.

### 5.3 Risultato Precedente
Il risultato dell'ultimo calcolo può essere richiamato utilizzando un punto (.) nelle espressioni successive.

## 6. Gestione degli Errori
Gli errori durante il calcolo delle espressioni vengono catturati e visualizzati all'utente.

## 7. Struttura del Codice
- `main()`: punto di ingresso dell'applicazione.
- `interactive_mode(variables)`: gestisce la modalità interattiva.
- `print_complex(result)`: stampa il risultato.
- `replace_dot_with_last_result(expression, last_result)`: sostituisce il punto con l'ultimo risultato.
- `evaluate_expression(expression, last_result, variables)`: valuta le espressioni matematiche.
