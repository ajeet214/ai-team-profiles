# utils/helpers.py

import base64
import os


def highlight_match(text, search_term):
    """Highlight search term in text (case-insensitive)."""
    if not search_term:
        return text
    lower_text = text.lower()
    index = lower_text.find(search_term)
    if index == -1:
        return text
    end = index + len(search_term)
    return (
        text[:index]
        + f"<mark style='background-color: #ffeb3b;'>{text[index:end]}</mark>"
        + text[end:]
    )


def encode_image_to_base64(image_path):
    """Convert image file to base64 string for embedding."""
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
