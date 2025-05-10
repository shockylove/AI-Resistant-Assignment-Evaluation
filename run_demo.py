#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Run full AI-Resistant Assignment demo")
    parser.add_argument("assignment", help="Path to assignment text file")
    parser.add_argument("-o", "--output", default="report.md", help="Path to final report")
    args = parser.parse_args()

    assignment = args.assignment
    answer     = "ai_answer.md"
    evaluation = "evaluation.json"
    suggestions= "suggestions.md"
    report     = args.output

    # 1) Simulate AI student → writes ai_answer.md
    subprocess.run([sys.executable, "simulate.py", assignment, "-o", answer], check=True)

    # 2) Assess assignment + AI answer → writes evaluation.json
    subprocess.run([sys.executable, "assess.py", assignment, answer, "-o", evaluation], check=True)

    # 3) Generate redesign suggestions → writes suggestions.md
    subprocess.run([sys.executable, "redesign.py", assignment, evaluation, "-o", suggestions], check=True)

    # 4) Assemble final report → writes report (e.g. report.md)
    subprocess.run([
        sys.executable, "report.py",
        "--assignment",  assignment,
        "--answer",      answer,
        "--evaluation",  evaluation,
        "--suggestions", suggestions,
        "-o",            report
    ], check=True)

    print(f"Demo complete! Final report generated at: {report}")

if __name__ == "__main__":
    main()