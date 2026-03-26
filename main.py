# AI Viva Examiner - A Python-based AI system to simulate viva exams for students, providing real-time feedback and performance analysis.

# libraries used:
import time
import sys
import random
import threading
import math
import speech_recognition as sr
import re
import wikipedia 

def welcome(): # welcome message and important instructions for students before starting the viva exam.
    print("="*60)
    print("AI VIVA EXAMINER".center(60))
    print("="*60)
    print("\nSystem: Ready for Examination.")
    print("Instructions: Answer clearly and technically for better marks. Best of Luck!\n")

def Wave(stop_event): # A simple animated wave to indicate that the system is listening for the student's response. It runs in a separate thread and stops when the main thread signals it.
    chars = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    t = 0
    while not stop_event.is_set():
        wave = ""
        for i in range(20):
            index = int((math.sin(t + i) + 1) * (len(chars)-1)/2)
            wave += chars[index]
        sys.stdout.write(f"\r[Listening] {wave}")
        sys.stdout.flush()
        time.sleep(0.1)
        t += 0.5
    sys.stdout.write("\r" + " "*50 + "\r")

def Voice(): # This function uses the SpeechRecognition library to capture audio from the microphone and convert it to text using Google's speech recognition API. It also handles timeouts and errors gracefully, ensuring that the system remains responsive even if no speech is detected.
    r = sr.Recognizer()
    stop_event = threading.Event()
    t = threading.Thread(target=Wave, args=(stop_event,))
    t.start()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=10, phrase_time_limit=20)
        stop_event.set()
        t.join()
        return r.recognize_google(audio)
    except:
        stop_event.set()
        if t.is_alive():
            t.join()
        return None

def subject(subs): # This function displays a list of subjects for the student to choose from and captures their selection. It ensures that the input is valid by prompting the user until a correct choice is made, allowing the system to proceed with generating questions based on the selected subject.
    print("\nSelect Subject:")
    for i, s in enumerate(subs, 1):
        print(f"{i}. {s}")

    while True:
        try:
            choice = input("Enter number: ")
            return subs[int(choice) - 1]
        except:
            print("Invalid choice.")

Questions = set()
Topics = {}

def get_random_topic(subject): # This function retrieves a random topic from the predefined syllabus for the given subject. It ensures that the same topic is not repeated until all topics have been covered, providing a diverse range of questions for the student.
    syllabus = {
        "Physics": ["Electric Charges and Fields","Electrostatic Potential and Capacitance","Current Electricity","Moving Charges and Magnetism", "Magnetism and Matter","Electromagnetic Induction", "Alternating Current","Electromagnetic Waves", "Ray Optics and Optical Instruments","Wave Optics", "Dual Nature of Radiation and Matter","Atoms","Nuclei","Semiconductor Electronics"],
        "Chemistry": ["Solutions","Electrochemistry","Chemical Kinetics","Surface Chemistry", "General Principles and Processes of Isolation of Elements", "p-Block Elements","d and f Block Elements", "Coordination Compounds","Haloalkanes and Haloarenes", "Alcohols Phenols and Ethers","Aldehydes Ketones and Carboxylic Acids", "Amines","Biomolecules","Polymers","Chemistry in Everyday Life"],
        "Biology": ["Reproduction","Sexual Reproduction in Flowering Plants","Human Reproduction","Reproductive Health","Genetics and Evolution","Molecular Basis of Inheritance", "Biology and Human Welfare","Human Health and Disease", "Microbes in Human Welfare","Biotechnology Principles and Processes", "Biotechnology and its Applications","Ecology and Environment", "Biodiversity and Conservation"],
        "Science": ["Chemical Reactions and Equations","Acids Bases and Salts","Metals and Non-metals","Carbon and its Compounds","Periodic Classification of Elements","Life Processes","Control and Coordination","How do Organisms Reproduce", "Heredity and Evolution","Light Reflection and Refraction", "Human Eye and Colourful World","Electricity","Magnetism","Sources of Energy","Our Environment","Management of Natural Resources"],
        "Social science": ["The Rise of Nationalism in Europe","Nationalism in India","Globalisation and the Indian Economy","Agriculture","Resources and Development","Water Resources", "Manufacturing Industries","Minerals and Energy Resources", "Political Parties","Federalism","Democracy and Diversity", "Gender Religion and Caste","Outcomes of Democracy", "Money and Credit","Development","Sectors of Indian Economy"],
        "English": [ "Reading Comprehension","Writing Skills","Letter Writing", "Article Writing","Story Writing","Tenses","Modals","Voice","Reported Speech","Determiners", "Literary Devices","Poetry Analysis","Prose Analysis" ] }

    topics = syllabus.get(subject, ["General Science"])

    if subject not in Topics:
        Topics[subject] = []

    remaining = list(set(topics) - set(Topics[subject]))

    if not remaining:
        Topics[subject].clear()
        remaining = topics

    topic = random.choice(remaining)
    Topics[subject].append(topic)
    return topic

def answer(topic, sub_context=""): # This function generates a detailed answer for the given topic by fetching a summary from Wikipedia. It structures the answer into sections such as definition, explanation, key points, and application. If there is an error in fetching the data, it provides a fallback answer with general information about the topic.
    try:
        wikipedia.set_lang("en")

        summary = wikipedia.summary(f"{topic} {sub_context}", sentences=5)

        sentences = summary.split('. ')
        definition = sentences[0]
        explanation = '. '.join(sentences[1:])

        keywords = list(set(re.findall(r'\b\w{5,}\b', summary)))[:5]
        key_points = "\n- ".join(keywords)

        structured = f"""
DETAILED ANALYSIS: {topic.upper()}

Definition:
{definition}

Explanation:
{explanation}

Application:
Used in practical and theoretical understanding of {sub_context}.

[Source: Wikipedia]
"""
        return structured

    except Exception:
        return f"""
DETAILED ANALYSIS: {topic.upper()}

Definition:
{topic} is an important concept in {sub_context}.

Explanation:
It explains key principles and plays a major role in understanding the subject.

Key Points:
- Core concept of {sub_context}
- Important for exams
- Used in real-world applications

[Fallback Answer]
"""

def check_accuracy(user_ans, model_ans): # This function evaluates the accuracy of the student's answer by comparing it to the model answer. It extracts key technical terms from the model answer and checks how many of those terms are present in the student's response. The accuracy is calculated as a percentage of matched keywords, providing a quantitative measure of how closely the student's answer aligns with the expected content.
    keywords = set(re.findall(r'\b\w{5,}\b', model_ans.lower()))
    user_words = user_ans.lower()

    if not keywords:
        return 0

    matches = sum(1 for word in keywords if word in user_words)
    return round((matches / len(keywords)) * 100, 2)


def analyze_answer_pro(user_ans, model_ans):# This function analyzes the student's answer by calculating a final score based on both the accuracy of the content and the length of the response. It assigns marks for accuracy and word count, with a maximum score of 10. The function also categorizes the performance level as "Expert", "Good", or "Needs Work" based on the final score, providing a comprehensive evaluation of the student's answer.
    word_count = len(user_ans.split())
    accuracy = check_accuracy(user_ans, model_ans)

    base_marks = (accuracy * 0.07) + (min(word_count, 60) * 0.05)
    final_marks = min(round(base_marks, 1), 10.0)

    level = "Expert" if final_marks >= 8.5 else "Good" if final_marks >= 6.5 else "Needs Work"

    return final_marks, level, accuracy

def generate_question_and_answer(subject_input): # This function generates a random topic based on the selected subject and retrieves a detailed answer for that topic. It also creates a variety of question patterns related to the topic, from which it randomly selects one to present to the student. The function returns the generated question, the model answer for reference, and the topic for context.
    topic = get_random_topic(subject_input)
    summary_text = answer(topic, subject_input)
    question_patterns = [
        f"Explain {topic} in detail.",
        f"What do you understand by {topic}?",
        f"Define {topic} and explain its significance in {subject_input}.",
        f"Can you elaborate on {topic} with examples?",
        f"Discuss the concept of {topic} in {subject_input}.",
        f"What are the key principles of {topic}?",
        f"Why is {topic} important in {subject_input}?",
        f"Explain the applications of {topic} in real life.",
        f"Differentiate {topic} with related concepts in {subject_input}.",
        f"Give a detailed note on {topic}.",
        f"Explain {topic} as if teaching a beginner.",
        f"What are the advantages and limitations of {topic}?",
        f"How does {topic} work in practical scenarios?",
        f"Can you justify the importance of {topic} in modern studies?",
        f"Explain {topic} with a real-world example.",
        f"What are the main components or elements of {topic}?",
        f"Describe the process involved in {topic}.",
        f"How is {topic} used in industry or technology?",
        f"Provide a structured explanation of {topic}.",
        f"Explain {topic} step by step."]

    question = random.choice(question_patterns)
    return question, summary_text, topic


def guide(): # This is the main function that orchestrates the flow of the viva examination. It starts by welcoming the student and providing instructions, then prompts them to select their class and subject. It generates a relevant question based on the chosen subject and provides a preparation time before allowing the student to speak their answer. The function then analyzes the student's response, calculates their score, and provides a performance report along with a reference answer for comparison.
    welcome()

    cls = input("Enter Class (10th/12th): ")
    subs = ["Physics", "Chemistry", "Biology", "English"] if "12" in cls else ["Science", "Social science", "English"]
    chosen_sub = subject(subs)
    print(f"\n[System] Generating {chosen_sub} question for viva examination.......")
    question, raw_summary, topic = generate_question_and_answer(chosen_sub)

    print(f"QUESTION: {question}")

    print("\nPreparation: 30s")
    for i in range(30, 0, -1):
        sys.stdout.write(f"\rTimer: {i}s ")
        sys.stdout.flush()
        time.sleep(1)

    print("\n\n SPEAK NOW...")

    speak = Voice()

    if speak:
        print(f"\nYour Response: {speak}")

        marks, level, accuracy_pct = analyze_answer_pro(speak, raw_summary)

        print("\n--- PERFORMANCE REPORT ---")
        print(f"Subject: {chosen_sub} | Topic: {topic}")
        print(f"Accuracy: {accuracy_pct}% | Grade: {level}")
        print(f"Final Score: {marks}/10")
        print("-" * 35)

        print("\nReference Answer:")
        print(raw_summary)

    else:
        print("\n[!] Error: No speech detected.")

if __name__ == "__main__":
    guide()