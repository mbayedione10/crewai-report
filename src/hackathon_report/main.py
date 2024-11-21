#!/usr/bin/env python
import sys
import sys
from pathlib import Path
from utils import save_report

# Utiliser save_report à la fin de final_report_task ou dans main.py


# Ajoutez le chemin vers le dossier src
sys.path.append(str(Path(__file__).resolve().parent.parent))
from hackathon_report.crew import HackathonReportCrew


def run():
    """
    Run the crew with specified inputs and save the report.
    """
    inputs = {
        'topic': 'Programme de mentorat du Hackathon #Innov4Democracy'
    }
    try:
        # Lance l'exécution de la crew et récupère le rapport généré
        crew = HackathonReportCrew().crew()
        report_content = crew.kickoff(inputs=inputs)
        
        # Sauvegarde du rapport
        save_report(report_content)  # Appel de save_report ici
        
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    Usage: `train <n_iterations> <filename>`
    """
    if len(sys.argv) < 3:
        print("Usage: train <n_iterations> <filename>")
        sys.exit(1)

    inputs = {
        "topic": "Programme de mentorat du Hackathon #Innov4Democracy"
    }
    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        HackathonReportCrew().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        print(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    Usage: `replay <task_id>`
    """
    if len(sys.argv) < 2:
        print("Usage: replay <task_id>")
        sys.exit(1)

    try:
        task_id = sys.argv[1]
        HackathonReportCrew().crew().replay(task_id=task_id)
    except Exception as e:
        print(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    Usage: `test <n_iterations> <openai_model_name>`
    """
    if len(sys.argv) < 3:
        print("Usage: test <n_iterations> <openai_model_name>")
        sys.exit(1)

    inputs = {
        "topic": "Programme de mentorat du Hackathon #Innov4Democracy"
    }
    try:
        n_iterations = int(sys.argv[1])
        openai_model_name = sys.argv[2]
        HackathonReportCrew().crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)
    except Exception as e:
        print(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [arguments]")
        print("Available commands: run, train, replay, test")
        sys.exit(1)

    command = sys.argv[1]
    sys.argv = sys.argv[2:]  # Redéfinir `sys.argv` pour ignorer le premier argument de commande

    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: run, train, replay, test")
        sys.exit(1)
