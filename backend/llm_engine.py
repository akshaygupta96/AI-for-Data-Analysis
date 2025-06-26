import subprocess
import json

def generate_code_from_query(query, df_sample):
    prompt = f"""
You are a Python data analyst.

Given the dataset sample:
{df_sample.to_string(index=False)}

Question: "{query}"

Please provide a clear and concise explanation answering the question, then leave a few lines of space,
then provide Python code using pandas and matplotlib to demonstrate how you arrived at the answer.
Include comments in the code to explain each step. Comment with #
Return the full response in plain text without markdown formatting.
Do NOT include any header like "Generated Code:".
"""
    output = subprocess.run(
        ["ollama", "run", "codellama"],  # or the best available model for combined tasks
        input=prompt.encode(),
        capture_output=True
    )
    result = output.stdout.decode().strip()

    # Remove any markdown triple backticks that might be included in output
    #result = result.replace("```python", "").replace("```", "").strip()

    return result
