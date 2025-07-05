HELAPP – AI Virtual Assistant with Voice & Eye Control 👁️🎙️💻

HELAPP is a smart virtual assistant powered by voice commands and real-time eye tracking using computer vision. Built with Python, this assistant helps users control their computer entirely hands-free, making it especially useful for individuals with limited mobility or accessibility needs.
🌟 Features

✅ Voice Recognition with Speech Commands
✅ Text-to-Speech Feedback
✅ Eye-Tracking Mouse Movement with MediaPipe + OpenCV
✅ Voice-Controlled Automation (open/close apps, browser tabs, music, Google/YouTube search, etc.)
✅ Joke Generator for User Engagement
✅ Weather Information via WeatherStack API
✅ System Commands (volume control, scroll, shutdown, restart, lock, etc.)
✅ Typing via Voice Input
✅ Screenshot Capture by Voice
✅ Basic Calculator (voice-based math expression parsing)
✅ Wikipedia Search Integration
✅ IP Address Retrieval
⚙️ Technologies Used

    Python

    SpeechRecognition

    pyttsx3 (Text-to-Speech)

    MediaPipe & OpenCV (Eye and face tracking)

    pyautogui (Mouse & keyboard automation)

    Wikipedia API

    WeatherStack API

    pywhatkit (WhatsApp & YouTube automation)

    Threading (Concurrent eye-tracking and voice interaction)

🎯 Use Cases

    Hands-free system control for users with disabilities.

    Assistive tech for productivity and automation.

    Entertainment (jokes, YouTube, Spotify).

    Education and information retrieval via voice.

📦 Installation

Clone the Repository:

    git clone https://github.com/yourusername/helapp-virtual-assistant.git
    cd helapp-virtual-assistant

Install Required Packages:

    pip install -r requirements.txt

Run the Application:

    python main.py

Make sure you have a working microphone and webcam connected.
🧠 Eye Tracking Details

The assistant uses MediaPipe FaceMesh to detect and track landmarks around the eyes. Cursor movement is controlled using eye gaze, and left-eye blink triggers mouse clicks. You can quit the eye-tracking loop by saying:

    “Quit eye-tracking” or “Go to sleep”

🔐 API Keys Required

    WeatherStack: Replace api_key in the get_weather() function with your own WeatherStack API key.

    Wikipedia: No API key required.

🧪 Sample Voice Commands

    “Open YouTube”

    “Search on Google”

    “Tell me a joke”

    “What is the weather in Khorog?”

    “Open WhatsApp”

    “Type Hello, how are you?”

    “Calculate 7 plus 5”

    “Take a screenshot”

    “Shut down the system”

🚧 Limitations

    Eye tracking performance may vary based on camera quality and lighting.

    Voice commands depend on clear speech and background noise levels.

    Not cross-platform; optimized for Windows OS.

🙌 Credits

Created by Meder, Mariiam, Mustafo, and Firdous as a project to support and empower disabled users through innovative AI and ML-based interaction.
📜 License

This project is open-source and available under the MIT License.
