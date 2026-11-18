######################################################################
# SmartHire AI Agent
#
# Author : Yash Kumar Chavan
#
# Description:
# This project is a text-based AI Mock Interview Agent.
#
# This project demonstrates the practical implementation of:
# 1. AI Agent
# 2. LLM Integration
# 3. Prompt Engineering
# 4. Answer Evaluation
# 5. Interview Automation
# 6. Report Generation
# 7. Memory through interview history
######################################################################

from questions import questions
from interview_agent import MockInterviewAgent
from report_generator import save_report


def print_header():
    """
    Function Name : print_header
    """

    print("*" * 70)
    print("        Yash Chavan")
    print("        SmartHire AI Agent")
    print("        Text Based Version")
    print("        Author : Yash Kumar Chavan")
    print("*" * 70)


def show_menu():
    """
    Function Name : show_menu
    Description  : Displays interview mode options to the user.
    """

    print("\nSelect Interview Mode:")
    print("1. Start Full Interview")
    print("2. Start Topic-wise Interview")
    print("3. Exit")


def get_available_topics():
    """
    Function Name : get_available_topics
    Description   : Extracts unique topics from the question bank.
    Return Value  : List of available topics.
    """

    topics = []

    for item in questions:
        if item["topic"] not in topics:
            topics.append(item["topic"])

    return topics


def start_interview(agent, selected_questions):
    """
    Function Name : start_interview
    Description   : Conducts the interview by asking selected questions.
    Parameters    :
        agent              : Object of MockInterviewAgent class
        selected_questions : List of questions selected for interview
    """

    for index, item in enumerate(selected_questions, start=1):

        topic = item["topic"]
        question = item["question"]

        print("\n" + "=" * 70)
        print(f"Question {index}")
        print("Topic    :", topic)
        print("Question :", question)
        print("=" * 70)

        answer = input("\nEnter your answer:\n")

        if answer.strip() == "":
            answer = "Student did not provide any answer."

        print("\nEvaluating your answer using LLM...")
        print("Please wait while AI Interview Agent is analyzing your response.")

        evaluation = agent.evaluate_answer(topic, question, answer)

        print("\nEvaluation Result:")
        print("=" * 70)
        print(evaluation)
        print("=" * 70)

        choice = input("\nDo you want to continue? yes/no: ")

        if choice.lower() != "yes":
            break


def main():
    """
    Function Name : main
    Description   : Entry point of the AI Mock Interview Agent project.
    """

    print_header()

    print("\nWelcome to SmartHire AI Agent.")
    print("This system conducts technical interviews using text input and LLM evaluation.")
    print("This project is designed for practical understanding of AI Agents.\n")

    student_name = input("Enter student name: ")

    if student_name.strip() == "":
        student_name = "Student"

    agent = MockInterviewAgent(student_name)

    print(f"\nWelcome {student_name} to SmartHire AI Agent.")
    print("The interview will evaluate your technical answers using LLM.")

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            start_interview(agent, questions)

            report = agent.generate_final_report()
            print(report)

            filename = save_report(student_name, report)

            print("\nInterview completed successfully.")
            print("Final report generated successfully.")
            print("Report saved at:", filename)

            break

        elif choice == "2":

            topics = get_available_topics()

            print("\nAvailable Topics:")

            for index, topic in enumerate(topics, start=1):
                print(f"{index}. {topic}")

            try:

                topic_choice = int(input("\nSelect topic number: "))

                if topic_choice < 1 or topic_choice > len(topics):
                    print("\nInvalid topic number. Please try again.")
                    continue

                selected_topic = topics[topic_choice - 1]

                selected_questions = []

                for item in questions:
                    if item["topic"] == selected_topic:
                        selected_questions.append(item)

                print(f"\nYou selected topic: {selected_topic}")

                start_interview(agent, selected_questions)

                report = agent.generate_final_report()
                print(report)

                filename = save_report(student_name, report)

                print("\nInterview completed successfully.")
                print("Final report generated successfully.")
                print("Report saved at:", filename)

                break

            except ValueError:

                print("\nInvalid input. Please enter a valid number.")

        elif choice == "3":

            print("\nThank you for using Yash Chavan's SmartHire AI Agent.")
            print("Keep learning, keep practicing.")
            print("Developed by Yash Chavan")

            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()