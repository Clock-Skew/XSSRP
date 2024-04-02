def get_remediation_suggestion(vulnerability_type):
    suggestions = {
        "reflected_xss": "Implement proper input validation and sanitization. Use context-specific encoding when inserting user-controlled data into the page.",
        "stored_xss": "For stored data, ensure that input is sanitized upon saving and encoded upon retrieval before rendering to users.",
        # More types and suggestions can be added here
    }
    return suggestions.get(vulnerability_type, "No specific suggestion available.")
