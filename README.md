                                           
**AI Viva Examiner System**
                                           
• **Overview of the Project**: The “**AI Viva Examiner system**” is a Python-based AI system designed to simulate real-world viva(oral) exams for students. It provides a hands-on platform for students to practice their explanations, giving real-time feedback and performance analysis to bridge the gap between theoretical knowledge and verbal communication.



•**Features**: This project consists of the following features:


1.**Voice-First Interaction**: Uses advanced speech recognition to capture student responses via microphone, simulating a natural face-to-face exam environment.

2.**Live Content Sourcing**: Integrates with the Wikipedia API to fetch detailed, up-to-date technical definitions and explanations for every topic.

3.**Threaded UI Animation**: Features a real-time ASCII wave animation that runs on a background thread to indicate when the system is actively listening.

4. **Comprehensive Syllabus**: Includes pre-defined question banks for Class 10th and 12th across Physics, Chemistry, Biology, Science, Social Science, and English.
   
5. **Automated Scoring Engine**: A "Pro-Analysis" system that calculates marks based on keyword accuracy, technical depth, and response length.
   
6. **Performance Reporting**: Generates a final grade (Expert/Good/Needs Work) and provides a "Reference Answer" for comparison.

7. **Smart Preparation Timer**: Includes a built-in 30-second countdown to allow students to organize their thoughts before the microphone activates.



• **Technologies/Tools Used**: Programming Language: Python 3.11.0 


1. **speech_recognition**: For capturing and converting audio input into text.
2. **Wikipedia**: For real-time retrieval of academic summaries and reference data.
3. **threading**:AI Viva Examiner System.
4. **re (Regex)**: Used for sophisticated keyword matching and accuracy analysis.
5. **math & time**: For the wave trigonometry and exam countdowns.



• **Steps to install and run the project**: * Prerequisites: Ensure Python is installed. You will also need a working microphone and an internet connection.


1. **Install Libraries**: Open your terminal and run pip install speech_recognition, wikipedia & PyAudio.
2. **Download**: Save the script as viva_examiner.py.
3. **Run**: Navigate to the folder in your terminal and type: python viva_examiner.py.



• **Instructions for testing**:


1. **Select Class**: When prompted, enter "10th" or "12th" to load the relevant subjects.
2. **Choose Subject**: Select a subject number (e.g., 1 for Physics).
3. **Prepare Answer**: Once the question appears, use the 30-second timer to prepare your answer.
4. **Speak Clearly**: When the "SPEAK NOW" message and wave animation appear, answer the question into your microphone.
5. **Review Report**: Analyze your Accuracy %, Grade, and Final Score. Compare your answer with the provided "Reference Answer" to see what technical keywords you missed.


**Screenshots & Result**:


<img width="1370" height="269" alt="1" src="https://github.com/user-attachments/assets/e7af7a5d-8fc8-48ea-81e8-4ed7e00b90d5" />

<img width="590" height="249" alt="2" src="https://github.com/user-attachments/assets/05bc576f-9922-426b-9be4-a9e8f00d4688" />


<img width="824" height="164" alt="3" src="https://github.com/user-attachments/assets/2d339a74-9156-468a-9af3-bd9c55868b49" />


<img width="464" height="99" alt="4" src="https://github.com/user-attachments/assets/4939de7e-fa0b-401a-9f8e-24abd2002ab0" />


<img width="826" height="83" alt="5" src="https://github.com/user-attachments/assets/3a67f5ca-deea-423c-8962-154b13245b26" />




<img width="1816" height="879" alt="6" src="https://github.com/user-attachments/assets/f2f751ad-0f6a-4ab4-941e-c351c4dd97dd" />















