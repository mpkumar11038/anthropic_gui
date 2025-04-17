from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

def anthropic_loop(
    *,
    model: str,
    messages: list[dict],
    max_tokens: int = 4096,
    tool_version: str,
    thinking_budget: int | None = None,
    max_iterations: int = 10,
):
    """
    A simple agent loop for Claude computer use interactions.

    This function handles the back-and-forth between:
    1. Sending user messages to Claude
    2. Claude requesting to use tools
    3. Your app executing those tools
    4. Sending tool results back to Claude
    """

    beta_flag = "computer-use-2025-01-24" if "20250124" in tool_version else "computer-use-2024-10-22"

    tools = [
        {"type": f"computer_{tool_version}", "name": "computer", "display_width_px": 1024, "display_height_px": 768}
    ]

    iterations = 0
    while True and iterations < max_iterations:
        iterations += 1
        thinking = None
        if thinking_budget:
            thinking = {"type": "enabled", "budget_tokens": thinking_budget}

        response = client.beta.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            tools=tools,
            betas=[beta_flag],
            thinking=thinking
        )

        response_content = response.content
        print(response_content, end="\n\n")
        messages.append({"role": "assistant", "content": response_content})

        tool_results = []
        for block in response_content:
            if block.type == "tool_use":
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": f"Run tool: {block.input}"
                })

        if not tool_results:
            break

        messages.append({
            "role": "user",
            "content": tool_results
        })

messages=[
    {
        "role": "user", 
        "content": "Open a browser and go to http://localhost:5000/. Then, visually locate a button labeled 'YES'. Move the mouse to that button and click it. Wait for the message area below to update. Then, visually locate the 'NO' button. Move the mouse to it and click it as well. Again, observe the updated message. Interact only through the visible GUI. Simulate mouse movement and clicks just like a human would."
    }
]

anthropic_loop(
    model="claude-3-7-sonnet-20250219",
    messages=messages,
    max_tokens=2048,
    tool_version="20250124",
    thinking_budget=1024,
    max_iterations=30,
)