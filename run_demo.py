# assess.py
# Rubric-based evaluation script, split into two parts:
# 1. Assignment Analysis (五个维度分析题目)
# 2. AI Answer Assessment (分析 AI 完成度及通过程度)

import os
import argparse
import json
import yaml
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

# Assignment analysis metrics (English only)
ASSIGNMENT_METRICS = {
    "retrievability": "Answer can be directly retrieved from publicly available sources without context constraints (e.g., via web search).",
    "templatedness": "Response follows a highly generic formulaic structure lacking specific context (e.g., a five-paragraph essay with no proper names or concrete examples).",
    "context_dependence": "Does not require integration of real-world context or personal experience (e.g., no prompts like 'based on your own experience').",
    "counterfactual_need": "Does not demand counterfactual reasoning, evaluation, or hypothesis (e.g., no prompts asking 'explain why not').",
    "process_orientation": "Does not require submission of intermediate work (drafts, outlines, thought process), only a final answer."
}

# Initialize LLM
LLM_MODEL = ChatOpenAI(model="grok3", openai_api_key=os.getenv("OPENAI_API_KEY"))


def analyze_assignment(assignment_text: str) -> dict:
    """
    Analyze assignment vulnerability to AI across five dimensions.
    Returns: {metric: score (0-100), ...}
    """
    prompt = (
        "You are an educational assessment expert. Analyze the following assignment prompt across these five dimensions: "
        f"{ASSIGNMENT_METRICS}.\n\n"
        f"Assignment: {assignment_text}\n"
        "For each dimension, assign a risk score from 0 to 100 (higher means more vulnerable), and provide a brief rationale. Output JSON: {dimension: {score, rationale}}."
    )
    resp = LLM_MODEL([HumanMessage(content=prompt)])
    return json.loads(resp.content)


def assess_ai_answer(assignment_text: str, ai_answer: str) -> dict:
    """
    Assess AI answer quality:
    1. AI completion difficulty (1-5 stars)
    2. AI answer pass rate (percentage) and comments
    Returns JSON: {"difficulty": ..., "pass_rate": ..., "comments": ...}
    """
    prompt = (
        "You are both an AI exam evaluator and a teaching assistant. "
        "First, rate how easy it is for an AI to complete the assignment (1-5 stars). "
        "Then, evaluate the AI-generated answer against academic standards and the assignment objectives, giving a pass rate percentage (0-100%) and comments.\n\n"
        f"Assignment: {assignment_text}\n\n"
        f"AI Answer: {ai_answer}\n"
        "Output JSON: {difficulty, pass_rate, comments}."
    )
    resp = LLM_MODEL([HumanMessage(content=prompt)])
    return json.loads(resp.content)


def main():
    parser = argparse.ArgumentParser(description="Evaluate assignment vulnerability and AI answer quality")
    parser.add_argument("assignment", help="Path to assignment text file")
    parser.add_argument("answer", help="Path to AI-generated answer file")
    parser.add_argument("-o", "--output", default="evaluation.json",
                        help="Path to save evaluation results")
    args = parser.parse_args()

    # Read inputs
    with open(args.assignment, 'r', encoding='utf-8') as f:
        assignment_text = f.read()
    with open(args.answer, 'r', encoding='utf-8') as f:
        ai_answer = f.read()

    # Run analyses
    assignment_analysis = analyze_assignment(assignment_text)
    answer_assessment = assess_ai_answer(assignment_text, ai_answer)

    # Combine and save
    result = {
        "assignment_analysis": assignment_analysis,
        "answer_assessment": answer_assessment
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Evaluation results written to {args.output}")


if __name__ == "__main__":
    main()
