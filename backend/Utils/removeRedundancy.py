"""
Remove any Repeated words
Example: "very very good" -> "very good"
"""
import re


def remove_redundancy(text):
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)
    return text
