from enum import Enum
import random
import tempfile
import os
from edge_tts import VoicesManager, Communicate

class Gender(Enum):
    Male = "Male"
    Female = "Female"

class EdgeTTS:
    def __init__(self):
        raise RuntimeError("Use factory method instead")
    
    @staticmethod
    async def speak(gender: Gender, text: str):
        voices = await VoicesManager.create()
        voice = voices.find(Gender=gender.value, Language="en")
        communicate = Communicate(text, random.choice(voice)["Name"])
        # with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(tempfile.gettempdir(), "story.mp3")
        print(f"File created: {file_path}")
        await communicate.save(file_path)
