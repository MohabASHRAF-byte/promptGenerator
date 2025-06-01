from typing import List

from backend.Ai_Model.LLMProvider import LlmProvider
from backend.Utils.ReplaceAbbreviations import replace_abbreviations
from backend.Utils.cleanSentence import cleanSentence
from backend.Utils.removeRedundancy import remove_redundancy


class ChatGPT(LlmProvider):
    def __init__(self):
        super().__init__("ChatGpt")

    def clean(self, text: str) -> str:
        return text.strip()

    def init_query(self) -> dict:
        return {"messages": []}

    def _preProcessInstructions(self, instructions: List[str]) -> List[str]:
        instructions = [replace_abbreviations(instr) for instr in instructions]
        instructions = cleanSentence(instructions)
        instructions = [instr.strip() for instr in instructions]
        instructions = [remove_redundancy(instr) for instr in instructions]
        return instructions

    def add_instructions(self, instructions: List[str], prompt: dict) -> dict:
        cleaned_instructions = self._preProcessInstructions(instructions)
        cleaned_instructions.append("Follow this instructions.")
        prompt['messages'].append({
            "role": "system",
            "content": ", ".join(cleaned_instructions)
        })
        return prompt

    def add_query(self, query: str, prompt: dict) -> dict:
        prompt['messages'].append({
            "role": "user",
            "content": query.strip()
        })
        return prompt

    def add_scheme(self, answer_scheme: bool, prompt: dict) -> dict:
        if answer_scheme:
            prompt['output'] = "output only the code"
        return prompt

    def generate_prompt(self, instructions: List[str], prompt_query_text: str, output_only_code: bool = False) -> dict:
        prompt = self.init_query()
        prompt_query_text = self.clean(prompt_query_text)
        prompt = self.add_instructions(instructions, prompt)
        prompt = self.add_query(prompt_query_text, prompt)
        prompt = self.add_scheme(output_only_code, prompt)
        return prompt
