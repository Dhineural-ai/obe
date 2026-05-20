import streamlit as st

try:

    with st.spinner("Reading PDFs..."):

        vision_text = extract_text_from_pdf(vision_file)
        peo_text = extract_text_from_pdf(peo_file)
        course_text = extract_text_from_pdf(course_file)

    with st.spinner("Analyzing Vision-Mission Alignment..."):

        alignment_report = analyze_alignment(
            vision_text,
            peo_text,
            course_text
        )

    with st.spinner("Generating CO-PO Mapping Analysis..."):

        mapping_report = generate_mapping_analysis(
            course_text,
            peo_text
        )

    with st.spinner("Refining Course File..."):

        refined_course = refine_course_document(
            vision_text,
            peo_text,
            course_text
        )

    with st.spinner("Preparing Final Report..."):

        final_report = generate_final_report(
            alignment_report,
            mapping_report,
            refined_course
        )

    st.success("OBE Refinement Completed")

    st.subheader("Vision-Mission Alignment")
    st.text_area(
        "Alignment Analysis",
        alignment_report,
        height=300
    )

    st.subheader("CO-PO Mapping Analysis")
    st.text_area(
        "Mapping Analysis",
        mapping_report,
        height=300
    )

    st.subheader("Refined Course File")
    st.text_area(
        "Refined Course Document",
        refined_course,
        height=700
    )

    st.subheader("Complete OBE Report")
    st.download_button(
        label="Download Final Report",
        data=final_report,
        file_name="obe_refined_report.txt",
        mime="text/plain"
    )

except Exception as e:
    st.error(f"Error: {e}")
