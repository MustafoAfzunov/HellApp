from __future__ import with_statement
import pyttsx3 # Text-to-speech library
import speech_recognition as sr # Speech recognition library
import datetime # Library for working with dates and times
import wikipedia # Library for interacting with Wikipedia
import webbrowser # Library for opening web browsers
import os # Library for interacting with the operating system
import pywhatkit as kit # Library for automating WhatsApp actions
import pyautogui# Library for GUI automation
import time # Library for working with time
import operator # Library for performing operations
import requests # Library for making HTTP requests
import random # Library for generating random numbers
import cv2 # OpenCV library for computer vision tasks
import mediapipe as mp # MediaPipe library for face and hand tracking
import threading # Library for multi-threading

# Initializing the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    '''Function to speak the provided text'''
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    """ Provides a greeting based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")
 
    speak("At your service. What can I do?")

def takeCommand():
    '''Function to recognize and process user commands using speech recognition'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        print("Say that again please...")
        # speak('could you repeat sir?') 
        return "None"
    return query.lower().strip()
def get_joke():
    '''Function to get a random joke from a predefined list'''
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! HA HA HA HA HA",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them! HA HA HA HA HA",
        "Why did the scarecrow win an award? Because he was outstanding in his field! HA HA HA HA HA",
        "What do you call fake spaghetti? An impasta! HA HA HA HA HA",
        "Why don't oysters donate to charity? Because they are shellfish! HA HA HA HA HA",
        "What do you call a fish with no eyes? Fsh! HA HA HA HA HA",
        "Why did the coffee file a police report? It got mugged! HA HA HA HA HA",
        "How do you organize a space party? You planet! HA HA HA HA HA",
        "Why did the bicycle fall over? Because it was two-tired! HA HA HA HA HA",
        "What's a vampire's favorite fruit? A blood orange! HA HA HA HA HA",
        "Why did the math book look sad? Because it had too many problems! HA HA HA HA HA",
        "What did one hat say to the other? Stay here, I'm going on ahead! HA HA HA HA HA",
        "How do you catch a squirrel? Climb a tree and act like a nut! HA HA HA HA HA",
        "Why did the scarecrow become a successful motivational speaker? Because he was outstanding in his field! HA HA HA HA HA"]
    return random.choice(jokes)

def get_weather(city):
    '''Function to get the weather information for a specified city using an API'''
    api_key = 'cde63da6094e0839bcd484b6c58c850a' 
    base_url = 'http://api.weatherstack.com/current'
    params = {'access_key': api_key, 'query': city}

    try:
        # Making a request to the weather API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        weather_data = response.json()
        # Handling possible errors in the API response
        if 'error' in weather_data:
            return f"Error: {weather_data['error']['info']}"
        temperature = weather_data['current']['temperature']
        description = weather_data['current']['weather_descriptions'][0]
        result = f'The weather in {city} is {description}. The temperature is {temperature} degrees Celsius.'
        return result
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def eye_track():
    '''Function for eye tracking using the computer's camera'''
    global eye_track
    eye_track = True
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while eye_track:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            # Detecting left eye closure and performing a click
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Project', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    # Main execution block
    wishMe()
    # Starting the thread for eye tracking
    face_thread = threading.Thread(target=eye_track)
    face_thread.start()
    while True:
        # Recognizing user command
        query = takeCommand()
        # Performing actions based on user commands
        if 'wikipedia' in query:        
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that topic.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are multiple possible matches. Please specify: {e.options}")
        elif any(keyword in query for keyword in ['who are you', 'what is your name', 'introduce yourself']):
            print('My Name Is HELAPP')
            speak('My Name Is HELAPP')
            print('I am a virtual assistant that can do whatever you would like me to do')
            speak('I am a virtual assistant that can do whatever you would like me to do. For example: telling the jokes, calculate, open different apps, scroll up and down, search on google, youtube and wikipedia, volume up and down, I can also type, tell the time and your ip address, also I can tell the weather')
        elif any(keyword in query for keyword in ['who is your creator', 'who created you', 'tell me about your creator']):
            print('I was created by the group members of the project to assist and help disabled people')
            speak('I was created by Meder, Mariiam, Mustafo, and Firdous to assist and help disabled and lazy people in controlling computers remotely with voice and eye-tracking system')
# -----------------------------------------------------------------------------------------------------------------            
        elif any(keyword in query for keyword in ['search on youtube','youtube search']):
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
# -----------------------------------------------------------------------------------------------------------------            
        elif 'open youtube' in query:
            speak("what we gonna watch sir?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")
        elif 'close youtube' in query:
            pyautogui.hotkey('ctrl', 'w')
# -----------------------------------------------------------------------------------------------------------------            
        elif any(keyword in query for keyword in ['open google']):
            speak("what should I search ?")
            qry = takeCommand().lower()
            speak('in process sir')
            webbrowser.open('https://www.google.com/search?q=' + qry)
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif any(keyword in query for keyword in ['open tab','open new tab']):
            pyautogui.hotkey('ctrl', 't')
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close google' in query:
            os.system("taskkill /f /im chrome.exe")
        elif any(keyword in query for keyword in ['play music','open spotify', 'open music']):
            music_dir = "D:\Новая папка\Spotify.lnk"
            os.startfile(music_dir)
        elif any(keyword in query for keyword in ['close music','stop music', 'close spotify']):
            os.system("taskkill /f /im spotify.exe")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:") 
            speak(f"Sir, the time is {strTime}")
# ----------------------------------------------------------------------------------------------------------------------------
        elif "open notepad" in query:
            npath = r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2310.13.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe"
            os.startfile(npath)
        elif "close notepad" in query:
            os.system('taskkill /f /im Notepad.exe')
        elif any(keyword in query for keyword in ['open telegram','telegram']):
            tpath = r"D:\Новая папка\Telegram Desktop.lnk"
            os.startfile(tpath)
        elif any(keyword in query for keyword in ['close Telegram']):
            os.system('taskkill /f /im Telegram Desktop.exe')
        elif any(keyword in query for keyword in ['open whatsapp','whatsapp']):
            wppath = r"D:\Новая папка\WhatsApp.lnk"
            os.startfile(wppath)
        elif any (keyword in query for keyword in ['close whatsapp']):
            os.system('taskkill /f /im WhatsApp.exe')
        elif any (keyword in query for keyword in ['open netflix',' netflix']):
            netflix_path = 'https://www.netflix.com/browse'
            webbrowser.open(netflix_path)
        elif "take a screenshot" in query:
            speak('tell me a name for the file to save')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot() 
            img.save(f"{name}.png") 
            speak("screenshot saved")
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    '/' : operator.__truediv__,}[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = float(op1), float(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        elif any(keyword in query for keyword in ['what is my ip address','tell me my ip address','ip address']):
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif any(keyword in query for keyword in['go to sleep', 'stop listening', 'you can rest', 'good bye', "you did a good job",'quit eye-tracking']):
            speak('alright then, I am switching off')
            eye_track = False
            break
        elif "refresh" in query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=556, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        elif "scroll down" in query:
            pyautogui.scroll(-800)
        elif "scroll up" in query:
            pyautogui.scroll(800)
        elif any(keyword in query for keyword in ['thank you','thank you very much','thanks']):
            speak('always at your service sir.')
            print('always at your service sir.')
        elif any(keyword in query for keyword in ['roll down all the windows','down all the windows']):
            pyautogui.hotkey('win', 'd')
        elif any(keyword in query for keyword in['roll up the last window', 'roll up the previous window']):
            pyautogui.hotkey('alt', 'tab')
        elif any(keyword in query for keyword in ['I am sad', 'tell me a joke', 'joke']):
            joke = get_joke()
            speak(joke)
        elif 'shut down the system' in query:
            confirmation = input("Are you sure you want to shut down the system? (yes/no): ").lower()
            if confirmation == 'yes':
                speak("Shutting down the system. Goodbye!")
                os.system("shutdown /s /t 5")
            else:
                speak("Shutdown canceled. Resuming normal operation.")

        elif "restart the system" in query:
            confirmation = input("Are you sure you want to shut down the system? (yes/no): ").lower()
            if confirmation == 'yes':
                speak("Shutting down the system. Goodbye!")
                os.system("shutdown /r /t 5")
            else:
                speak("Shutdown canceled. Resuming normal operation.")
        elif "lock the system" in query:
            time.sleep(5)
            speak('computer will go to sleep in 5 seconds')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif any(keyword in query for keyword in['change the layout', 'change the language']):
            pyautogui.hotkey('shift', 'alt')         
        elif any(keyword in query for keyword in ['open steam','turn on the gaming mod', 'game mod']):
            steam_dir = r"C:\Users\Public\Desktop\Steam.lnk"
            os.startfile(steam_dir)
        elif any(keyword in query for keyword in ['close steam','back to work', 'turn off the gaming mod']):
            os.system("taskkill /f /im Steam.exe")
        elif any(keyword in query for keyword in ['open teams','open microsoft teams']):
            team_dir = r"C:\Users\User\AppData\Local\Microsoft\Teams\current\Teams.exe"
            os.startfile(team_dir)
        elif any(keyword in query for keyword in ['close teams','close microsoft teams']):
            os.system("text_to_type")
        elif 'open microsoft word' in query:
            word_d = r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(word_d)
        elif 'close microsoft word' in query:
            os.system("taskkill /f /im WINWORD.EXE")
        elif 'type' in query:
            speak("What should I type?")
            text_to_type = takeCommand()
            pyautogui.write(text_to_type)
        elif any(keyword in query for keyword in ['erase','erase the text']):
            speak("Erasing")
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
        elif 'weather' in query:
            speak("Sure, which city's weather do you want to check?")
            city = takeCommand().lower()
            weather_result = get_weather(city)
            speak(weather_result)
            print(get_weather(city))
        elif 'are you there' in query:
            speak('Yes sir')


        
        



            




                    


        














