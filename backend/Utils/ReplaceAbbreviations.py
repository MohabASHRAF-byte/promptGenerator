"""
replace all the abbreviation to minimize the number of tokens
standard the same word
    example : chatGpt , chatGPT, CHATGPT --> chatGPT
              Python, PYTHON, PYthon --> PY
"""
# todo : refactor to be more dynamic
abbreviations = {
    "United States of America": "USA",
    "International Business Machines": "IBM",
    "Artificial Intelligence": "AI",
    "Machine Learning": "ML",
    "chatgpt": "chatGPT",
    "python": "Python",
    "cpp": "C++",
    "C plus plus": "C++",
    "c++": "C++"
}


def replace_abbreviations(text):
    text = text.lower()
    for full_text, short_text in abbreviations.items():
        text = text.replace(full_text.lower(), short_text)
    return text
