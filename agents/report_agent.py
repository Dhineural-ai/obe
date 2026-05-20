def generate_final_report(
    alignment_report,
    mapping_report,
    refined_course
):

    report = f"""
==============================
ADVANCED OBE AI REPORT
==============================


VISION-MISSION ALIGNMENT

{alignment_report}


====================================
CO-PO-PSO MAPPING ANALYSIS
====================================

{mapping_report}


====================================
REFINED COURSE DOCUMENT
====================================

{refined_course}

"""

    return report
