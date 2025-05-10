# report.py
# Script to assemble final Markdown report from all phases

import os
import argparse
import json

def load_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def dict_to_markdown_table(d: dict) -> str:
    # Convert a flat dict of key: value to a markdown table
    header = "| Criterion | Score |\n|---|---|\n"
    rows = "".join(f"| {k} | {v} |\n" for k, v in d.items())
    return header + rows

def main():
    parser = argparse.ArgumentParser(description="Assemble final report")
    parser.add_argument("--assignment", default="assignment.txt", help="Path to original assignment text")
    parser.add_argument("--answer", default="ai_answer.md", help="Path to AI-generated answer")
    parser.add_argument("--evaluation", default="evaluation.json", help="Path to evaluation JSON")
    parser.add_argument("--suggestions", default="suggestions.md", help="Path to redesign suggestions")
    parser.add_argument("-o", "--output", default="report.md", help="Path to write final report")
    args = parser.parse_args()

    assignment_text = load_text(args.assignment)
    ai_answer = load_text(args.answer)
    evaluation = json.load(open(args.evaluation, 'r', encoding='utf-8'))
    suggestions = load_text(args.suggestions)

    analysis = evaluation.get("assignment_analysis", {})
    assessment = evaluation.get("answer_assessment", {})
    breakdown = assessment.get("breakdown", {})

    # Build Markdown
    md = []
    md.append("# AI-Resistant Assignment Evaluation Report\n")
    md.append("## 1. Assignment Prompt\n")
    md.append(f"{assignment_text}\n")
    md.append("## 2. AI-Generated Answer\n")
    md.append(f"{ai_answer}\n")
    md.append("## 3. Assignment Vulnerability Analysis\n")
    md.append("Risk scores (higher = more vulnerable):\n\n")
    md.append(dict_to_markdown_table(analysis))
    md.append("## 4. AI Answer Assessment\n")
    md.append("Scores per criterion:\n\n")
    md.append(dict_to_markdown_table(breakdown))
    md.append(f"**Strengths:** {assessment.get('strengths', '')}\n\n")
    md.append(f"**Weaknesses:** {assessment.get('weaknesses', '')}\n\n")
    md.append("## 5. Redesign Suggestions\n")
    md.append(f"{suggestions}\n")

    # Write to file
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("\n".join(md))

    print(f"Final report written to {args.output}")

if __name__ == "__main__":
    main()
