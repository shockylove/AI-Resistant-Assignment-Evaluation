# Final AI-Resistant Assignment Report

## Vulnerability Analysis
{
  "context_dependence": {
    "score": 0,
    "rationale": "The assignment focuses solely on implementing and evaluating code generation using LLMs, without requiring real-world context or personal experience."
  },
  "counterfactual_need": {
    "score": 0,
    "rationale": "Tasks involve direct implementation and evaluation; no counterfactual reasoning or hypothetical 'why not' arguments are required."
  },
  "process_orientation": {
    "score": 100,
    "rationale": "Only final deliverables (code, results folders, and a report) are requested; no interim drafts, outlines, or process checkpoints are required."
  },
  "retrievability": {
    "score": 10,
    "rationale": "The specialized use of CodeGen and EvalPlus for program synthesis makes direct retrieval of a complete solution from public sources unlikely."
  },
  "templatedness": {
    "score": 60,
    "rationale": "While following a common ML-homework structure (setup, implementation, evaluation, report), it includes specific tools and metrics, reducing but not eliminating formulaicity."
  }
}

## Assessment
{
  "total_score": 100,
  "breakdown": {
    "context_dependence": 20,
    "counterfactual_need": 20,
    "process_orientation": 15,
    "retrievability": 25,
    "templatedness": 20
  },
  "strengths": "The submission is fully self-contained, does not rely on personal or real-world context, includes only final deliverables without intermediate drafts, and provides specific code and report details that could be verified via public sources.",
  "weaknesses": "None significant; the answer meets all rubric criteria and shows clear, assignment-focused content without generic templates."
}

## Redesign Suggestions
Below are three concrete redesigns to make the assignment more resilient to “copy-and-paste” AI assistance. Each redesign boosts one or more of the vulnerability dimensions identified in your analysis.

1) Require a Detailed Development Diary (Process-Orientation ↑, Counterfactual-Need ↑)  
Rationale: By forcing students to document every prompt variant they tried, why they tried it, and how the model’s output changed, you ensure that a simple AI-generated “final answer” won’t suffice. They must reveal their reasoning and adaptivity—exactly the kind of process only they can supply.  
Example prompt addition:  
“Alongside your code submission, include a `diary.md` that for each problem records:  
  • The initial greedy prompt you used.  
  • Two subsequent prompt tweaks (e.g. added test cases, few-shot examples, or chain-of-thought hints).  
  • For each tweak, a one-paragraph justification of why you thought it would help and how the model’s output changed (better coverage? fewer errors?).  
Without this diary, your code yields zero credit—AI-only write-ups will be obviously insufficient.”

2) Embed a Real-World, Context-Rich Mini-Project (Context-Dependence ↑, Retrievability ↓)  
Rationale: Generic “add two lists” tasks are readily available online. By embedding the assignment in a realistic scenario—say, building a tiny data-cleaning module for biomedical research—the student must supply domain choices (e.g. how to handle missing values, naming conventions, unit tests for lab-specific edge cases) that an LLM can’t invent without domain knowledge.  
Example modification:  
“Part A: You are given a CSV of patient lab results with columns like `Glucose(mg/dL)` and occasional ‘NA’ entries. Load this file, normalize units, impute or flag missing values, and then produce summary statistics. Use CodeGen+EvalPlus to bootstrap your solution—but you must also write at least two custom test cases that reflect real lab anomalies (e.g. ‘zero readings’, ‘out-of-range values’, ‘mixed units’). Describe in your report why those domain-specific tests matter.”

3) Add a Live or Video “Whiteboard” Defense (Process-Orientation ↑, Counterfactual-Need ↑)  
Rationale: A synchronous or recorded explanation forces students to articulate trade-offs (“If I’d used GPT-4 instead of CodeGen, I might’ve gained better library support but faced latency issues”), reflecting on what they did, why, and what they could have done differently. AI scripts collapse under unscripted questioning.  
Example requirement:  
“After you submit code+report, schedule a 10-minute video recording (or live Zoom) where you present:  
  1. A 30-second overview of your prompt strategy.  
  2. A demonstration of one problem that initially failed and how you iterated your prompt to fix it.  
  3. At least one ‘what if’ question from the instructor (e.g. ‘What if the test harness changed to require asynchronous I/O? How would your prompt/code adapt?’) and your live response.  
Failure to demonstrate this live adaptation will cost up to 20% of the assignment grade.”

Each of these redesigns raises the bar: students must expose their iteration process, embed genuine context that AI cannot hallucinate, and defend their work under dynamic questioning.
