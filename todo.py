# Todo-Liste
tasks = []

def add_task():
    # Was sollen für Aufgaben auf die Liste
    task = input("Hier die Aufgabe die auf die Liste soll: ")
    
    # Frage nach der Fälligkei (optiornal)
    due_date = input("Bis wann soll die Aufgabe erledigt sein? (drücke Enter ohne Datum): ")
    
    # Aufgaben zur Liste hinzufügen
    if due_date:
        tasks.append({'task': task, 'due_date': due_date})
        print(f"Aufgabe '{task}' mit Fälligkeitsdatum {due_date} wurde zur Liste hinzugefügt.")
    else:
        tasks.append({'task': task})
        print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt.")

# Test
add_task()
