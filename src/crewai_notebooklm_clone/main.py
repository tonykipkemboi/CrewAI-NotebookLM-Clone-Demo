#!/usr/bin/env python
import os
import sys
from crewai_notebooklm_clone.crew import CrewaiNotebooklmCloneCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the path to the file containing the content: ")

    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            user_input = file.read()

        inputs = {
            'content': user_input,
        }
        CrewaiNotebooklmCloneCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"Error reading the file: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the path to the file containing the content: ")

    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            user_input = file.read()

        inputs = {
            'content': user_input,
        }
        CrewaiNotebooklmCloneCrew().crew().train(n_iterations=2, filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

