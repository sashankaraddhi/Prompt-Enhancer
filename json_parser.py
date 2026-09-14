import json


def parse_json_response(response_text: str) -> dict | None:
    """
    Convert the model's JSON response into a Python dictionary.
    """

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        print("\n❌ The model returned invalid JSON.")
        print("Raw response:")
        print(response_text)

        return None