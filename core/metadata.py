import re


class MetadataEnricher:

    def enrich(self, record):

        instruction = record.get("instruction", "")
        output = record.get("output", "")

        language = record["metadata"].get("language", "unknown")

        text = instruction.lower()

        # Detect whether the output contains a code block
        has_code = "```" in output

        # Very simple topic detection (we'll improve this later)
        if "array" in text:
            topic = "Arrays"

        elif "tree" in text:
            topic = "Trees"

        elif "graph" in text:
            topic = "Graphs"

        elif "linked list" in text:
            topic = "Linked Lists"

        elif "sort" in text:
            topic = "Sorting"

        else:
            topic = "General Programming"

        # Estimate size
        estimated_tokens = (
            len(instruction.split())
            + len(output.split())
        )

        # Difficulty estimate
        if estimated_tokens < 250:
            difficulty = "Beginner"

        elif estimated_tokens < 700:
            difficulty = "Intermediate"

        else:
            difficulty = "Advanced"

        record["metadata"]["language"] = language
        record["metadata"]["topic"] = topic
        record["metadata"]["difficulty"] = difficulty
        record["metadata"]["estimated_tokens"] = estimated_tokens
        record["metadata"]["has_code"] = has_code

        return record