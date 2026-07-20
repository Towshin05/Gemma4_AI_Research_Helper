import re


class ContextExtractor:
    def __init__(self):
        self.sections = [
            "abstract",
            "keywords",
            "introduction",
            "background",
            "related work",
            "literature review",
            
            "methodology",
            "materials and methods",
            "experiments",
            "experimental setup",
            "results",
            "discussion",
            "limitations",
            "future work",
            "conclusion",
            "references",
        ]

    def detect_sections(self, text):
        found_sections = []

        text = text.lower()

        for section in self.sections:
            pattern = rf"\b{re.escape(section)}\b"

            if re.search(pattern, text):
                found_sections.append(section.title())

        return found_sections
