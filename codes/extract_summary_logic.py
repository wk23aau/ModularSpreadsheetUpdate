def extract_summary(heading, summary_text):
    heading_part = heading if heading else ""
    summary_part = summary_text if summary_text else ""
    combined_summary = f"{heading_part}. {summary_part}".strip()
    return combined_summary if combined_summary else "No summary available"