from prompt_agent import PromptEnhancementAgent
from ollama_provider import OllamaProvider


def main():

    print("=" * 60)
    print("🤖 PROMPT ENHANCEMENT AGENT")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    provider = OllamaProvider()

    agent = PromptEnhancementAgent(provider)

    while True:

        raw_prompt = input("Enter your raw prompt: ").strip()

        if raw_prompt.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Goodbye!")
            break

        if not raw_prompt:
            print("Please enter a prompt.\n")
            continue

        try:
            agent.enhance_prompt(raw_prompt)

        except Exception as error:
            print(f"\n❌ Error: {error}")

        print()


if __name__ == "__main__":
    main()