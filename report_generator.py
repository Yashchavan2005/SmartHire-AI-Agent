"""
File Name    : report_generator.py
Author       : Yash Kumar Chavan

Description  :
This file is responsible for generating and saving
final interview reports of students.

The generated report contains:
1. Student Information
2. Interview Evaluation
3. Technical Feedback
4. Score Analysis
5. Suggestions

The report is automatically stored inside the
'reports' folder with timestamp information.
"""

import os
import datetime


def save_report(student_name, report):
    """
    Function Name : save_report

    Description  :
    Saves the final interview report into a text file.

    Parameters   :
        student_name : Name of student
        report       : Final generated report

    Return Value :
        Returns generated filename
    """

    if not os.path.exists("reports"):
        os.mkdir("reports")

    timestamp = datetime.datetime.now().strftime(
        "%d_%m_%Y_%H_%M_%S"
    )

    safe_name = student_name.replace(" ", "_")

    filename = (
        f"reports/"
        f"SmartHire_AI_Agent_"
        f"{safe_name}_"
        f"Interview_Report_"
        f"{timestamp}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("              SmartHire AI Agent\n")
        file.write("           AI Mock Interview Agent\n")
        file.write("        Generated Interview Report\n")
        file.write("=" * 70 + "\n\n")

        file.write("=" * 70 + "\n")
        file.write("             STUDENT REPORT\n")
        file.write("=" * 70 + "\n\n")

        file.write(report)

        file.write("\n\n")
        file.write("=" * 70 + "\n")
        file.write("Project Name : SmartHire AI Agent\n")
        file.write("Creator      : Yash Chavan\n")
        file.write("=" * 70 + "\n")

    print("\n===================================================")
    print("Interview Report Generated Successfully")
    print("Report File :", filename)
    print("===================================================")

    return filename
