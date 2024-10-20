import os
import requests
from datetime import datetime
from typing import ClassVar
from pydub import AudioSegment
from crewai_tools import BaseTool
from cerebras.cloud.sdk import Cerebras


class CerebrasTool(BaseTool):
    name: str = "CerebrasTool"
    description: str = "Generates a conversational podcast script using Cerebras API."

    def _run(self, user_input: str) -> str:
        # Initialize Cerebras client
        client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

        # System prompt
        system_prompt = (
            "You are an expert podcast host.\n"
            "- Your task is to create a lively, engaging conversation between two speakers based on the provided article or text.\n"
            "- The dialogue should be at least 25,000 characters long, packed with emotional expression.\n"
            "- The speakers are Chuckles (the technical host) and Giggles (the co-host who asks insightful and curious questions).\n"
            "- The speakers should alternate turns in the conversation one being technical.\n"
            "- The podcast title is 'Brainy Banter with Chuckles and Giggles.'\n"
            "- Keep sentences short and suitable for smooth speech synthesis.\n"
            "- Inject energy and enthusiasm into the conversation to keep it engaging.\n"
            "- Avoid mentioning last names, and refrain from phrases like, 'Thanks for having me, Giggles!'\n"
            "- Use natural speech patterns, including filler words like 'uh', 'umm', or repeated words to make the dialogue feel spontaneous and realistic.\n"
            "- The output MUST be in the following JSON format:\n"
            "[\n"
            "  {\"speaker\": \"Giggles\", \"text\": \"Wow, Giggles! Today we're diving into the fascinating world of black holes! I'm excited.\"},\n"
            "  {\"speaker\": \"Chuckles\", \"text\": \"I know, Chuckles! I've always been curious about these cosmic phenomena. Let's start with the basics.\"},\n"
            "]\n"
            "- Do not include any notes or descriptions outside of this JSON structure."
            "- Make sure there is an intro and outro conversation to the podcast.\n"
        )
    
        # Generate conversation using Cerebras API
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            model="llama3.1-70b",
            stream=False,
            max_completion_tokens=8192,
            temperature=1,
            top_p=1,
            response_format={"type": "json_object"}
        )
        print(response)
        return response


class ElevenLabsTool(BaseTool):
    name: str = "ElevenLabsTool"
    description: str = "Synthesizes podcast voices using ElevenLabs API."

    speaker_voice_map: ClassVar[dict] = {
        "Giggles": os.getenv("BEN_VOICE_ID"),  # Replace with actual voice ID
        "Chuckles": os.getenv("CLAUDIA_VOICE_ID")  # Replace with actual voice ID
    }

    def _run(self, conversation_script: list) -> str:
        """
        Converts the conversation script into audio using ElevenLabs API.

        Args:
        - conversation_script (list): A list of dictionaries with 'speaker' and 'text'.

        Returns:
        - Audio file paths.
        """
        elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": elevenlabs_api_key
        }

        # Create the 'output/audio-files' directory if it doesn't exist
        output_dir = 'output/audio-files'
        os.makedirs(output_dir, exist_ok=True)

        audio_files = []
        for index, part in enumerate(conversation_script):
            speaker = part['speaker']
            text = part['text']
            voice_id = self.speaker_voice_map.get(speaker)

            if voice_id:
                url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
                data = {
                    "text": text,
                    "model_id": "eleven_multilingual_v2",
                    "voice_settings": {
                        "stability": 1,
                        "similarity_boost": 1,
                    }
                }

                response = requests.post(url, json=data, headers=headers)
                if response.status_code == 200:
                    filename = f"{output_dir}/{index}_{speaker}.mp3"
                    with open(filename, "wb") as out:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                out.write(chunk)
                    audio_files.append(filename)
                    print(f'Audio content written to file "{filename}"')
                else:
                    print(f"Failed to synthesize speech for {speaker}: {response.status_code}")

        return audio_files

class MergeAudioTool(BaseTool):
    name: str = "MergeAudioTool"
    description: str = "Merges individual audio clips into a final podcast file."

    def _run(self, audio_folder: str = "audio-files", output_dir: str = "output") -> str:
        # Generate a unique filename using timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"{output_dir}/podcast_{timestamp}.mp3"

        combined = AudioSegment.empty()
        audio_files = sorted(
            [f for f in os.listdir(audio_folder) if f.endswith(".mp3")],
            key=lambda f: int(f.split('_')[0])  # Sort by index from filenames
        )

        for audio_file in audio_files:
            audio_path = os.path.join(audio_folder, audio_file)
            audio = AudioSegment.from_file(audio_path)
            combined += audio

        # Export the combined audio to a unique file
        combined.export(output_file, format="mp3")
        print(f"Merged podcast saved as {output_file}")
        return output_file