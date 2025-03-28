# import os
# import sys
#
# import smell_detection as detector
# import parser as parser
# from results import write_results_csv
#
#
# def main_method(input_path):
#     try:
#         # Check if the input path exists
#         if not os.path.exists(input_path):
#             print("Error: The specified input path does not exist.")
#             return
#
#         # Check if the input path is a file
#         if os.path.isfile(input_path):
#             process_file(input_path)
#         else:
#             # Input path is a directory
#             files = get_files_from_directory(input_path)
#             if not files:
#                 print("Error: No files found in the specified directory.")
#                 return
#             for file in files:
#                 process_file(file)
#
#     except Exception as e:
#         print("An error occurred:", str(e))
#
#
# def process_file(input_file):
#     try:
#         # Check if the input file exists
#         if not os.path.isfile(input_file):
#             print(f"Error: The specified input file '{input_file}' does not exist.")
#             return
#
#         # Open playbook file and extract tasks
#         with open(input_file) as f:
#             # Get the parsed tasks as a dictionary
#             tasks = parser.get_parsed_tasks(input_file=input_file)
#             task_number = 0
#             for task in tasks:
#                 task_number += 1
#                 output_tasks, new_output_tasks = detector.detect_smells(task, task_number, input_file)
#                 write_results_csv(output_tasks, new_output_tasks, input_file)
#     except FileNotFoundError:
#         print(f"Error: File '{input_file}' not found.")
#     except Exception as e:
#         print(f"An error occurred while processing file '{input_file}':", str(e))
#
#
# def get_files_from_directory(directory):
#     files = []
#     for root, _, filenames in os.walk(directory):
#         for filename in filenames:
#             files.append(os.path.join(root, filename))
#     return files
#
#
# if __name__ == "__main__":
#     # Check if the input path is provided as a command-line argument
#     if len(sys.argv) < 2:
#         print("Error: No input path provided.")
#     else:
#         input_path = sys.argv[1]
#         main_method(input_path)

import os
import sys
from . import smell_detection as detector
from . import parser
from .results import write_results_csv


def main_method(input_path, output_directory=None):
    try:
        # Check if the input path exists
        if not os.path.exists(input_path):
            print("Error: The specified input path does not exist.")
            return

        # Check if the input path is a file
        if os.path.isfile(input_path):
            process_file(input_path, output_directory)
        else:
            # Input path is a directory
            files = get_files_from_directory(input_path)
            if not files:
                print("Error: No files found in the specified directory.")
                return
            for file in files:
                process_file(file, output_directory)

    except Exception as e:
        print("An error occurred:", str(e))


def process_file(input_file, output_directory=None):
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file):
            print(
                "Error: The specified input file '{}' does not exist.".format(
                    input_file
                )
            )
            return

        # Open playbook file and extract tasks
        with open(input_file):
            # Get the parsed tasks as a dictionary
            tasks = parser.get_parsed_tasks(input_file=input_file)
            task_number = 0
            for task in tasks:
                task_number += 1
                output_tasks, new_output_tasks = detector.detect_smells(
                    task, task_number, input_file
                )
                write_results_csv(
                    output_tasks, new_output_tasks, input_file, output_directory
                )
    except FileNotFoundError:
        print("Error: File '{}' not found.".format(input_file))
    except Exception as e:
        print("An error occurred while processing file '{input_file}':", str(e))


def get_files_from_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


if __name__ == "__main__":
    # Check if the input path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Error: No input path provided.")
    else:
        input_path = sys.argv[1]
        output_directory = sys.argv[2] if len(sys.argv) > 2 else None
        main_method(input_path, output_directory)
# main_method('/home/ghazal/Ansible-Reproducibility/src/extraction/test/manual_validation/ansible-for-devops','/home/ghazal/Ansible-Reproducibility/src/extraction/test/output')
