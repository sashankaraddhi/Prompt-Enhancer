import json
import re


def parse_json_response(response_text: str) -> dict | None:
    """
    Convert the model's JSON response into a Python dictionary.
    Handles potential markdown code fences and cleans whitespace.
    """
    if not response_text or not response_text.strip():
        print("\n❌ The model returned an empty response.")
        return None

    cleaned_text = response_text.strip()

    # Strip markdown code blocks if present (e.g. ```json ... ``` or ``` ... ```)
    if cleaned_text.startswith("```"):
        cleaned_text = re.sub(r"^```(?:json)?\s*", "", cleaned_text)
        cleaned_text = re.sub(r"\s*```$", "", cleaned_text)

    try:
        return json.loads(cleaned_text)

    except json.JSONDecodeError:
        # Fallback: attempt to find JSON object substring enclosed in { ... }
        match = re.search(r"\{.*\}", cleaned_text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass

        print("\n❌ The model returned invalid JSON.")
        print("Raw response:")
        print(response_text)

        return None