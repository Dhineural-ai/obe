import json

def suggest_pedagogy(bloom_results):
    with open("knowledge_base/pedagogy_matrix.json") as f:
        pedagogy_data = json.load(f)

    recommendations = []

    for item in bloom_results:
        level = item["level"]

        if level in pedagogy_data:
            recommendations.append({
                "bloom_level": level,
                "pedagogy": pedagogy_data[level]
            })

    return recommendations
