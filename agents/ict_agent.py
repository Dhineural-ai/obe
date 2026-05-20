import json

def suggest_ict_tools(course_text):
    with open("knowledge_base/ict_tools.json") as f:
        ict_data = json.load(f)

    recommendations = []

    text = course_text.lower()

    if "python" in text:
        recommendations.extend(ict_data["programming"])

    recommendations.extend(ict_data["quiz"])
    recommendations.extend(ict_data["collaboration"])

    return list(set(recommendations))
