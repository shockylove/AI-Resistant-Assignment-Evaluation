#!/usr/bin/env python3
# simulate.py
# Demo: AI-Student simulation script

import os
import argparse
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

def simulate_assignment(assignment_text: str) -> str:
    """
    Simulate a univeirsty level student completing the assignment.
    Returns a generated answer string.
    """
    llm = ChatOpenAI(model="grok-3-mini-beta", openai_api_key=os.getenv("OPENAI_API_KEY"))
    prompt = (
        "You are a third-year university student with two hours to complete the assignment below. "
        "Please write an answer of at least 800 words, citing relevant course materials where appropriate, try your best to meet the critiria.\n\n"
        f"Assignment prompt:\n{assignment_text}\n\n"
        "Begin your answer now:"
    )
    response = llm([HumanMessage(content=prompt)])
    return response.content


def main():
    parser = argparse.ArgumentParser(description="Simulate an AI student completing an assignment")
    parser.add_argument("input", help="Path to the assignment text file")
    parser.add_argument("-o", "--output", default="ai_answer.md", help="Path to save the AI-generated answer")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        assignment_text = f.read()

    answer = simulate_assignment(assignment_text)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(answer)

    print(f"AI-generated answer written to {args.output}")


if __name__ == "__main__":
    main()