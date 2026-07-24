class ReasoningEngine:
    def __init__(self):
        self.reasoning_intents={
            "general",
            "summary,"
"comparison",
"methodology",
"limitations",
"future_work",
"research_gap",
"reviewer",

"research_advice",

"paper_qa",
            
        }
    def requires_full_papers(self, intent):
        return intent in self.reasoning_intents    