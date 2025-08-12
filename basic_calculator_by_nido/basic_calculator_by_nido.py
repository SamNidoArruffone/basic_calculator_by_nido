"""
basic_calculator_by_nido.py
A simple multilingual calculator program
Un semplice programma di calcolatrice multilingue
"""

def get_language():
    print("\n" + "="*40)
    print("BASIC CALCULATOR BY NIDO / CALCOLATRICE DI NIDO")
    print("="*40)
    print("\nPlease select a language / Seleziona una lingua:")
    print("1. English")
    print("2. Italiano")
    while True:
        choice = input("\nEnter your choice (1-2) / Inserisci la tua scelta (1-2): ")
        if choice in ('1', '2'):
            return int(choice)
        print("Invalid choice / Scelta non valida")

# Language dictionaries
messages = {
    1: {  # English
        "title": "BASIC CALCULATOR BY NIDO",
        "operations": "Operations:",
        "add": "1. Addition (+)",
        "sub": "2. Subtraction (-)",
        "mul": "3. Multiplication (*)",
        "div": "4. Division (/)",
        "exit": "5. Exit",
        "select_op": "Select operation (1/2/3/4/5): ",
        "first_num": "Enter first number: ",
        "second_num": "Enter second number: ",
        "result": "Result: {} {} {} = {}",
        "div_zero": "Error! Division by zero.",
        "invalid_num": "Invalid input. Please enter numbers only.",
        "invalid_op": "Invalid input. Please try again.",
        "goodbye": "Thank you for using BASIC CALCULATOR BY NIDO!",
        "error": "An error occurred: {}"
    },
    2: {  # Italian
        "title": "CALCOLATRICE DI NIDO",
        "operations": "Operazioni:",
        "add": "1. Addizione (+)",
        "sub": "2. Sottrazione (-)",
        "mul": "3. Moltiplicazione (*)",
        "div": "4. Divisione (/)",
        "exit": "5. Uscita",
        "select_op": "Seleziona operazione (1/2/3/4/5): ",
        "first_num": "Inserisci il primo numero: ",
        "second_num": "Inserisci il secondo numero: ",
        "result": "Risultato: {} {} {} = {}",
        "div_zero": "Errore! Divisione per zero.",
        "invalid_num": "Input non valido. Inserisci solo numeri.",
        "invalid_op": "Input non valido. Riprova.",
        "goodbye": "Grazie per aver usato CALCOLATRICE DI NIDO!",
        "error": "Si è verificato un errore: {}"
    }
}

def calculator(lang):
    msg = messages[lang]
    
    print("\n" + "="*40)
    print(msg["title"])
    print("="*40)
    print("\n" + msg["operations"])
    print(msg["add"])
    print(msg["sub"])
    print(msg["mul"])
    print(msg["div"])
    print(msg["exit"])

    while True:
        try:
            # Get user input
            choice = input("\n" + msg["select_op"])
            
            # Check if user wants to exit
            if choice == '5':
                print("\n" + "="*40)
                print(msg["goodbye"])
                print("="*40 + "\n")
                break
                
            # Validate input
            if choice not in ('1', '2', '3', '4'):
                print(msg["invalid_op"])
                continue
                
            num1 = float(input(msg["first_num"]))
            num2 = float(input(msg["second_num"]))
            
            # Perform calculation
            if choice == '1':
                print(msg["result"].format(num1, '+', num2, num1 + num2))
            elif choice == '2':
                print(msg["result"].format(num1, '-', num2, num1 - num2))
            elif choice == '3':
                print(msg["result"].format(num1, '*', num2, num1 * num2))
            elif choice == '4':
                if num2 == 0:
                    print(msg["div_zero"])
                else:
                    print(msg["result"].format(num1, '/', num2, num1 / num2))
                    
        except ValueError:
            print(msg["invalid_num"])
        except Exception as e:
            print(msg["error"].format(e))

# Main program
if __name__ == "__main__":
    language = get_language()
    calculator(language)