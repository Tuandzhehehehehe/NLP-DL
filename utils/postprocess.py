def format_summary(summary):
    summary = summary.strip()

    if not summary.endswith("."):
        last_dot = summary.rfind(".")
        if last_dot != -1:
            summary = summary[:last_dot + 1]
        else:
            summary += "..."

    summary = summary.replace(" .", ".")
    return summary