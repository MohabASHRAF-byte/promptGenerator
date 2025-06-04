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
        # instructions = cleanSentence(instructions)
        instructions = [instr.strip() for instr in instructions]
        instructions = [remove_redundancy(instr) for instr in instructions]
        return instructions

    def add_instructions(self, instructions: List[str], prompt: dict) -> dict:
        # cleaned_instructions = self._preProcessInstructions(instructions)
        cleaned_instructions = instructions
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

    def generate_prompt_message(self, instructions: List[str], prompt_query_text: str,
                                output_only_code: bool = False, ai_role=None, experience_level=None,
                                project_description=None,
                                ) -> str:
        """
        #Backendground
        ##your Role : {}
        ##Your experience level : {}
        #objective
          2 lines description of the project
        #instuctions
        -
        -
        #prompt
        lalalalalaalallalala
        #output
         output only code
        """
        message_template = ""
        if ai_role or experience_level:
            message_template += "#Backgroud\n"
            if ai_role:
                message_template += f"your Role : {ai_role}\n"
            if experience_level:
                message_template += f"Your experience level : {experience_level}\n"
        if project_description:
            message_template += "#project_description\n"
            message_template += f"{project_description}\n"
        if instructions:
            message_template += "#instructions\n"
            cleaned_instructions = self._preProcessInstructions(instructions)
            # cleaned_instructions = instructions
            cleaned_instructions.append("Follow this instructions.")
            for ins in cleaned_instructions:
                message_template += f"- {ins}\n"
        if prompt_query_text:
            message_template += "#prompt\n"
            message_template += f"-{prompt_query_text}\n"
        if output_only_code:
            message_template += f"#output\n"
            message_template += "output only the code"
        return message_template
