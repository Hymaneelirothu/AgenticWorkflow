import requests
import time

class ToolAgent:
    # Hugging Face API Key and URL for GPT-2
    HF_API_KEY = "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"
    HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    def solve_task(self, task, retries=3, delay=5):
        """Send the task to Hugging Face GPT-2 and get a solution."""
        payload = {"inputs": self.generate_prompt(task)}
        for attempt in range(retries):
            try:
                # Send request to Hugging Face
                response = requests.post(self.HF_API_URL, headers=self.headers, json=payload)
                response.raise_for_status()  # Check for errors
                result = response.json()
                
                # Get the generated text
                response_text = result[0].get("generated_text", "").strip()
                return self.clean_response(response_text)

            except requests.exceptions.RequestException as e:
                if response.status_code == 503:
                    print(f"Service unavailable. Retrying {attempt+1}/{retries}...")
                    time.sleep(delay)
                else:
                    print(f"Failed to solve task: {e}")
                    return f"Failed to solve task: {e}"

        return "Failed to solve task after multiple attempts."

    def generate_prompt(self, task):
        """Generate a prompt to send to the GPT-2 model."""
        return f"Provide detailed, step-by-step instructions to complete the following task: {task}"

    def clean_response(self, response_text):
        """Clean the response to make it more readable and remove unwanted content."""
        response_text = response_text.replace("Sub-task 1:", "").strip()
        return response_text
