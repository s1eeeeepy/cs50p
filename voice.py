import cowsay
import pyttsx3


engine = pyttsx3.init()
ru_voice_id = (
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
)
engine.setProperty("voice", ru_voice_id)
this = input(">>> ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
