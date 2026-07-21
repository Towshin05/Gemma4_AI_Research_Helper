class IntentDetector:
    def __init__(self):
        self.intents = {
    "comparison": [
        "compare",
        "comparison",
        "difference",
        "different",
        "better",
        "contrast"
    ],

    "limitations": [
        "limitation",
        "limitations",
        "drawback",
        "weakness",
        "disadvantage"
    ],

    "future_work": [
        "future work",
        "future research",
        "next step",
        "research direction"
    ],

    "research_gap": [
        "research gap",
        "gap",
        "missing",
        "unexplored",
        "not addressed"
    ],

    "summary": [
        "summary",
        "summarize",
        "overview",
        "brief"
    ],

    "methodology": [
        "method",
        "methodology",
        "approach",
        "framework",
        "architecture"
    ],

    "general": []
}
    def detect_intent(self, query):
        query=query.lower()
            
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in query:
                    return intent
                
        return "general"