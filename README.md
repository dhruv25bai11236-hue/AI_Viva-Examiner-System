                                           
**AI Viva Examiner System**
                                           
• **Overview of the Project**: The “**AI Viva Examiner system**” is a Python-based AI system designed to simulate real-world viva(oral) exams for students. It provides a hands-on platform for students to practice their explanations, giving real-time feedback and performance analysis to bridge the gap between theoretical knowledge and verbal communication.



•**Features**: This project consists of the following features:

•**Voice-First Interaction**: Uses advanced speech recognition to capture student responses via microphone, simulating a natural face-to-face exam environment.

•**Live Content Sourcing**: Integrates with the Wikipedia API to fetch detailed, up-to-date technical definitions and explanations for every topic.

•	**Threaded UI Animation**: Features a real-time ASCII wave animation that runs on a background thread to indicate when the system is actively listening.

•	**Comprehensive Syllabus**: Includes pre-defined question banks for Class 10th and 12th across Physics, Chemistry, Biology, Science, Social Science, and English.

•	**Automated Scoring Engine**: A "Pro-Analysis" system that calculates marks based on keyword accuracy, technical depth, and response length.

•	**Performance Reporting**: Generates a final grade (Expert/Good/Needs Work) and provides a "Reference Answer" for comparison.

•	**Smart Preparation Timer**: Includes a built-in 30-second countdown to allow students to organize their thoughts before the microphone activates.



• **Technologies/Tools Used**: Programming Language: Python 3.11.0 


•	**speech_recognition**: For capturing and converting audio input into text.

•	**Wikipedia**: For real-time retrieval of academic summaries and reference data.

•**threading**:AI Viva Examiner System.

•	**re (Regex)**: Used for sophisticated keyword matching and accuracy analysis.

•	**math & time**: For the wave trigonometry and exam countdowns.



• **Steps to install and run the project**: * Prerequisites: Ensure Python is installed. You will also need a working microphone and an internet connection.


•	**Install Libraries**: Open your terminal and run pip install speech_recognition, wikipedia & PyAudio.

•	**Download**: Save the script as viva_examiner.py.

•	**Run**: Navigate to the folder in your terminal and type: python viva_examiner.py.



• **Instructions for testing**:


•	**Select Class**: When prompted, enter "10th" or "12th" to load the relevant subjects.

•	**Choose Subject**: Select a subject number (e.g., 1 for Physics).

•	**Prepare Answer**: Once the question appears, use the 30-second timer to prepare your answer.

•	**Speak Clearly**: When the "SPEAK NOW" message and wave animation appear, answer the question into your microphone.

•	**Review Report**: Analyze your Accuracy %, Grade, and Final Score. Compare your answer with the provided "Reference Answer" to see what technical keywords you missed.




