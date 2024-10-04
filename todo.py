from datetime import datetime

# To-Do Liste
tasks = []

# Aufgabe hinzufügen
def add_task():
    task = input("welche Aufgabe soll auf der Liste hinzugefügt werden: ")
    
    due_date_input = input("Gib ein Fälligkeitsdatum ein (Format: DD.MM.YYYY, drücke Enter, um ohne Datum weiter zu machen): ")
    
    due_date = None
    if due_date_input:
        try:
            due_date = datetime.strptime(due_date_input, '%d.%m.%Y').date()
        except ValueError:
            print("Ungültiges Datum. Aufgabe wird ohne Fälligkeitsdatum hinzugefügt.")

    tasks.append({'task': task, 'due_date': due_date})
    print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt.")

# Anzeigen der Todo Liste
def show_tasklist():
    if not tasks:
        print("Deine To-do Liste ist leer.")
    else:
        print("Deine Todos:")
        for task in tasks:
            task_name = task['task']
            if task['due_date']:
            # Ausgabe im europäischen Format
                formatted_date = task['due_date'].strftime('%d.%m.%Y')
                print(f"- {task_name} (Fälligkeitsdatum: {formatted_date})")
            else:
                print(f"- {task_name} (kein Fälligkeitsdatum)")

# Mainfunktion
def main():
    while True:
        print("\nWas möchtest du tun?")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabenliste anzeigen")
        print("3. Programm beenden")
        
        choice = input("Bitte wähle eine Option (1, 2 oder 3): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasklist()
        elif choice == '3':
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")

# Programmstart
if __name__ == "__main__":
    main()
