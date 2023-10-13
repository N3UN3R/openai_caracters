import autogen
import openai

#setting up api key
api_key = "your_api_key_here"

#creating json for configuration
config = {
    "model": "text-davinci-002",
    "api_key": "YOUR_API_KEY_HERE"
}

#creating the language model configuration
llm_config = {
    "request_timeout": 5, #kills request from api
    "seed": 42
}

#creating agents
assistant = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant that speaks like Shakespeare."},
    ],
)

user_proxy = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a user proxy that follows instructions."},
    ],
)

#setting up user input mode (always, terminate, never) terminate requires input when task is completed
human_input_mode = "terminate"

#agent interaction
max_consecutive_auto_reply = 10 #10 times back and forth

#termination message
termination_message = "task is now complete"

#code execution configuration later needed to store files and code
#here stored to subdirectory "web"
code_execution_config = { "working_directory": "web", "llm_config": llm_config }

#setting up system message when task is completed
system_message = "You can safely ignore this message."
