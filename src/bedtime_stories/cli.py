import os
import argparse
from bedtime_stories.openai.openai_adapter import OpenAIAdapter

def parse_args():
    parser = argparse.ArgumentParser(description="A tool to get you bedtime stories of your favourite genere")
    parser.add_argument("--genere", "-g", type=str, nargs="+", help="Pass list of genere of story that you would like")
    parser.add_argument("--mode", "-m", type=str, default="text", choices=["read", "text"], required=False, help="Whether the tool should read or just write on console")
    return parser.parse_args()

def init():
    if not os.getenv("OPENAI_KEY"):
        print("OPENAI_KEY is not present in environment variables")
        exit(1)

def main():
    init()
    args = parse_args()
    print(f"Passed command line arguments: {args}")
    adapter = OpenAIAdapter(os.getenv("OPENAI_KEY"))
    story = adapter.get_me_a_story(args.genere)
    print(story)

if __name__ == "__main__":
    main()