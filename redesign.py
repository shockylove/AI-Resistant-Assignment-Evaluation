

# redesign.py
# Script to generate AI-resistant assignment redesign suggestions

import os
import argparse
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

def generate_redesign_suggestions(assignment_text: str, analysis: dict, assessment: dict) -> str:
    """
    Use the evaluation analysis and assessment weaknesses to propose redesign suggestions.
    Returns a markdown-formatted string with three suggestions, each with rationale and an example.
    """
    llm = ChatOpenAI(model="grok-3-mini-beta", openai_api_key=os.getenv("OPENAI_API_KEY"))
    prompt = (
        "You are an instructional designer. Given the original assignment prompt and the following analysis:\n\n"
        f"Assignment Prompt:\n{assignment_text}\n\n"
        f"Assignment Vulnerability Analysis (risk scores):\n{json.dumps(analysis, ensure_ascii=False, indent=2)}\n\n"
        f"AI Answer Assessment (weaknesses):\n{assessment.get('weaknesses', '')}\n\n"
        "Propose three concrete redesign suggestions to make the assignment more resistant to AI-generated responses, while preserving the learning objectives. "
        "For each suggestion, include a brief rationale and an example."
    )
    response = llm([HumanMessage(content=prompt)])
    return response.content

def main():
    parser = argparse.ArgumentParser(description="Generate AI-resistant assignment redesign suggestions")
    parser.add_argument("assignment", help="Path to assignment text file")
    parser.add_argument("evaluation", help="Path to evaluation JSON file (output from assess.py)")
    parser.add_argument("-o", "--output", default="suggestions.md", help="Path to save redesign suggestions")
    args = parser.parse_args()

    # Load inputs
    with open(args.assignment, 'r', encoding='utf-8') as f:
        assignment_text = f.read()
    with open(args.evaluation, 'r', encoding='utf-8') as f:
        evaluation = json.load(f)

    analysis = evaluation.get("assignment_analysis", {})
    assessment = evaluation.get("answer_assessment", {})

    # Generate suggestions
    suggestions_md = generate_redesign_suggestions(assignment_text, analysis, assessment)

    # Write to output file
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(suggestions_md)

    print(f"Redesign suggestions written to {args.output}")

if __name__ == "__main__":
    main()