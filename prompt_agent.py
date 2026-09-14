from base import LLMProvider
from system_prompt import SYSTEM_PROMPT
from json_parser import parse_json_response


class PromptEnhancementAgent:

    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def _call_llm(self, messages: list[dict]) -> dict | None:
        """
        Send messages to the provider and parse the response.
        """

        response_text = self.provider.chat(messages)

        return parse_json_response(response_text)

    def enhance_prompt(self, raw_prompt: str) -> str | None:
        """
        Main prompt enhancement workflow.

        Workflow:
        1. Analyze raw prompt
        2. Ask clarification questions if needed
        3. Gather answers
        4. Confirm requirements
        5. Generate enhanced prompt
        """

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Here is the user's raw prompt:

{raw_prompt}

Analyze it and decide whether clarification is needed.
"""
            }
        ]

        while True:

            # ------------------------------------------
            # Step 1: Analyze prompt
            # ------------------------------------------

            result = self._call_llm(messages)

            if result is None:
                return None

            action = result.get("action")

            # ------------------------------------------
            # Step 2: Ask clarification questions
            # ------------------------------------------

            if action == "ask_questions":

                questions = result.get("questions", [])

                if not questions:
                    print("\n❌ The model returned no questions.")
                    return None

                print(
                    "\n🔍 I need a few details before "
                    "enhancing your prompt:\n"
                )

                for index, question in enumerate(questions, start=1):
                    print(f"{index}. {question}")

                answers = []

                print()

                for index, question in enumerate(questions, start=1):
                    answer = input(f"Your answer {index}: ")
                    answers.append(answer)

                clarification_text = "\n".join(
                    f"Question: {question}\nAnswer: {answer}"
                    for question, answer in zip(questions, answers)
                )

                messages.append(
                    {
                        "role": "assistant",
                        "content": self._last_response_as_json(result)
                    }
                )

                messages.append(
                    {
                        "role": "user",
                        "content": f"""
Here are the user's answers to your clarification questions:

{clarification_text}

Using the original prompt and these answers, decide whether
you need any additional clarification.

If the requirements are now clear, summarize them for confirmation.
If something important is still missing, ask additional questions.
"""
                    }
                )

            # ------------------------------------------
            # Step 3: Confirm requirements
            # ------------------------------------------

            elif action == "confirm_requirements":

                summary = result.get("summary", "")

                print(
                    "\n📋 Here is my understanding "
                    "of your requirements:\n"
                )
                print(summary)

                confirmation = input(
                    "\nDo you confirm these requirements? (yes/no): "
                ).strip().lower()

                messages.append(
                    {
                        "role": "assistant",
                        "content": self._last_response_as_json(result)
                    }
                )

                if confirmation in ["yes", "y"]:

                    messages.append(
                        {
                            "role": "user",
                            "content": """
The user confirmed the requirements.

Now generate the final enhanced prompt.

Return only JSON using this format:

{
    "action": "enhance_prompt",
    "enhanced_prompt": "..."
}
"""
                        }
                    )

                else:

                    correction = input(
                        "\nWhat would you like to change or correct? "
                    )

                    messages.append(
                        {
                            "role": "user",
                            "content": f"""
The user did not confirm the requirements.

Their correction is:

{correction}

Update the requirements and ask for confirmation again.
"""
                        }
                    )

            # ------------------------------------------
            # Step 4: Return enhanced prompt
            # ------------------------------------------

            elif action == "enhance_prompt":

                enhanced_prompt = result.get("enhanced_prompt", "")

                if not enhanced_prompt:
                    print("\n❌ The model returned an empty prompt.")
                    return None

                print("\n" + "=" * 60)
                print("✨ ENHANCED PROMPT")
                print("=" * 60)
                print(enhanced_prompt)
                print("=" * 60)

                return enhanced_prompt

            # ------------------------------------------
            # Unknown action
            # ------------------------------------------

            else:
                print("\n❌ Unknown action returned by the model.")
                print(result)

                return None

    @staticmethod
    def _last_response_as_json(result: dict) -> str:
        """
        Convert the assistant's structured response back into JSON
        so it can be included in the conversation history.
        """

        import json

        return json.dumps(result)