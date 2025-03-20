import asyncio
import os
import argparse

from dotenv import load_dotenv
from bedtime_stories.openai.openai_adapter import OpenAIAdapter
from bedtime_stories.tts.edge_tts import EdgeTTS, Gender

def parse_args():
    parser = argparse.ArgumentParser(description="A tool to get you bedtime stories of your favourite genere")
    parser.add_argument("--genere", "-g", type=str, nargs="+", help="Pass list of genere of story that you would like")
    parser.add_argument("--mode", "-m", type=str, default="text", choices=["read", "text"], required=False, help="Whether the tool should read or just write on console")
    return parser.parse_args()

def init():
    load_dotenv()
    if not os.getenv("OPENAI_KEY"):
        print("OPENAI_KEY is not present in environment variables")
        exit(1)

async def main():
    init()
    args = parse_args()
    print(f"Passed command line arguments: {args}")
    adapter = OpenAIAdapter(os.getenv("OPENAI_KEY"))
    story = adapter.get_me_a_story(args.genere)
    if args.mode == "read":
        print(story)
    elif args.mode == "text":
        await EdgeTTS.speak(Gender.Male, story)

def run_cli():
    asyncio.run(main())

if __name__ == "__main__":
    main()