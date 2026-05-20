def generate_report(
    bloom_results,
    pedagogy_results,
    ict_results,
    assignments
):

    report = ""

    report += "\n===== BLOOM ANALYSIS =====\n"

    for item in bloom_results:
        report += f"Verb: {item['verb']} | Level: {item['level']}\n"

    report += "\n===== PEDAGOGY SUGGESTIONS =====\n"

    for item in pedagogy_results:
        report += f"{item['bloom_level']} -> {item['pedagogy']}\n"

    report += "\n===== ICT TOOL SUGGESTIONS =====\n"

    for tool in ict_results:
        report += f"- {tool}\n"

    report += "\n===== ASSIGNMENT SUGGESTIONS =====\n"

    report += assignments

    return report
