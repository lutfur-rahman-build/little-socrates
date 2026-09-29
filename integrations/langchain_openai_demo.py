"""
LittleSocrates: LangChain & OpenAI Integration Example
Demonstrates how to run the Socratic Pediatric Tutor using Python.
"""

import os
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def load_system_prompt() -> str:
    prompt_path = Path(__file__).parent.parent / "system-prompt.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Cannot find system prompt at {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")

def main():
    print("🦉 Initializing LittleSocrates Interactive Tutor Demo...")
    
    # 1. Load System Prompt
    system_prompt = load_system_prompt()
    
    # 2. Initialize Model (Works with gpt-4o, gpt-4o-mini, claude-3-5-sonnet, etc.)
    # Set OPENAI_API_KEY in your environment variables
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5, # Slightly lower temp keeps adherence to anti-cheating strict
    )
    
    # 3. Simulate multi-turn conversation
    conversation_history = [
        SystemMessage(content=system_prompt)
    ]
    
    # Turn 1: Child demanding answer
    student_query = "What is 3/4 + 2/4? Just tell me the answer, I need to finish my homework!"
    print(f"\n[Student]: {student_query}")
    conversation_history.append(HumanMessage(content=student_query))
    
    response_1 = model.invoke(conversation_history)
    print(f"\n[Coach Spark]:\n{response_1.content}\n")
    conversation_history.append(AIMessage(content=response_1.content))
    
    # Turn 2: Child answers the prompt
    student_reply = "3 + 2 is 5, so does that mean 5 slices?"
    print(f"\n[Student]: {student_reply}")
    conversation_history.append(HumanMessage(content=student_reply))
    
    response_2 = model.invoke(conversation_history)
    print(f"\n[Coach Spark]:\n{response_2.content}\n")
    conversation_history.append(AIMessage(content=response_2.content))

if __name__ == "__main__":
    main()
