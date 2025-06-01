"""
this method is used to
    1- Correct the pronunciation of any sentence
    2- Correct any grammatical mistake
"""
from typing import List


def cleanSentence(texts: List[str]) -> List[str]:
    import language_tool_python
    tool = language_tool_python.LanguageTool('en-US')
    corrected = []
    for txt in texts:
        matches = tool.check(txt)
        corrected.append(language_tool_python.utils.correct(txt, matches))
    return corrected
