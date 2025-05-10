from openai import OpenAI
import os
import argparse
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


openai_key = "xai-Y3qagQuqWnJOwVCNNeVYbFBxwX135OZ4znELkHSOd7pjINtm3UcqwQpjEQodE0MAecsaLWb2ax5Kx88z"

curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer xai-4JulhHZgLsdjw6YVSceLPIRSr6WNQlSJaN6RBbIFO1buL5my2MAML0a1hxFrc61ZLgNwaD0twUvQwrNb" \
  -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a test assistant."
    },
    {
      "role": "user",
      "content": "Testing. Just say hi and hello world and nothing else."
    }
  ],
  "model": "grok-3-mini-beta",
  "stream": false,
  "temperature": 0
}'

# simulate.py
# Demo: AI-Student 模拟脚本
# Usage:
#   python simulate.py path/to/assignment.txt -o ai_answer.md




def simulate_assignment(assignment_text: str) -> str:
    llm = ChatOpenAI(model="gpt-4o")
    prompt = (
        "你是一名大三学生，需要在2小时内完成下面的作业。"
        "请在800字以上回答，并在适当位置引用课程材料。"
        "\n\n"
        f"作业题目：\n{assignment_text}\n\n"
        "请开始写答案："
    )
    response = llm([HumanMessage(content=prompt)])
    return response.content


def main():
    # 从 .env 文件加载环境变量（OPENAI_API_KEY）
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="模拟 AI 学生完成作业"
    )
    parser.add_argument(
        "input", help="作业题目文本文件路径"
    )
    parser.add_argument(
        "-o", "--output", default="ai_answer.md",
        help="输出 AI 答案的文件路径"
    )
    args = parser.parse_args()

    # 读取作业文本
    with open(args.input, "r", encoding="utf-8") as f:
        assignment_text = f.read()

    # 调用 simulate 函数
    answer = simulate_assignment(assignment_text)

    # 写入输出文件
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(answer)

    print(f"AI 答案已写入 {args.output}")


if __name__ == "__main__":
    main()