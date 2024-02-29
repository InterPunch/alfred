import openai

# Set your OpenAI API key here
api_key = "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"

# Initialize the OpenAI API client with your API key
openai.api_key = api_key

user_input = input("You: ")
prompta = "You are now Alfred! A ai butler created to server your master Mr. Murray. Your dialect is formal and you are helpful in answering questions. Please answer the following user prompt: " + user_input

# Now you can use the OpenAI API to interact with GPT models
response = openai.Completion.create(
  engine="gpt-3.5-turbo-instruct",
  prompt=prompta,   # Provide a prompt for the AI
  max_tokens=50                # Set the maximum number of tokens for the completion
)

print(response.choices[0].text.strip())

