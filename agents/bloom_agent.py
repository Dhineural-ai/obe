import json

def evaluate_bloom_levels(course_text):
    with open("knowledge_base/bloom_verbs.json") as f:
        bloom_data = json.load(f)

    results = []

    for level, verbs in bloom_data.items():
        for verb in verbs:
            if verb.lower() in course_text.lower():
                results.append({
                    "verb": verb,
                    "level": level
                })

    return results
