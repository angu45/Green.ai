"""
Nova's optional PyScript helper.
This runs in the browser sandbox and does not call a remote AI API.
The JavaScript interface currently uses its own deterministic router so the
core UI remains functional even if the Python runtime is slow or unavailable.
"""
import re
from datetime import datetime

def classify_prompt(prompt):
    """Return an intent and simple confidence score using transparent rules."""
    text = (prompt or "").lower()
    rules = {
        "ebook": r"\b(ebook|e-book|chapters|manuscript|kdp|book outline)\b",
        "image": r"\b(image|illustration|wallpaper|cover art|logo|visual)\b",
        "code": r"\b(html|css|javascript|python|code|debug|website|app|program)\b",
        "write": r"\b(write|article|blog|email|rewrite|story|description)\b",
    }
    for intent, pattern in rules.items():
        if re.search(pattern, text):
            return {"intent": intent, "confidence": 0.72, "engine": "rule-based"}
    return {"intent": "chat", "confidence": 0.50, "engine": "rule-based"}

def make_plan(goal):
    """Create a short, deterministic task plan from a goal."""
    goal = (goal or "").strip()
    if not goal:
        return ["Describe the goal", "Choose an output format", "Review the result"]
    return [
        "Clarify success criteria for: " + goal[:120],
        "Break the task into small, verifiable steps",
        "Generate a first draft with the selected workspace",
        "Review accuracy, quality and edge cases",
        "Export the result and test it in its target environment",
    ]

def status():
    return {
        "runtime": "PyScript browser sandbox",
        "time": datetime.now().isoformat(timespec="minutes"),
        "remote_api": False,
    }
