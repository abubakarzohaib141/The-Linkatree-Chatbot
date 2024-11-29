import os
import google.generativeai as genai
from student_listt import class_1, class_2 , class_3
# Step 1: Configure the API key
api_key = os.getenv("GEMINI_API_KEY")  # Environment variable approach
if not api_key:
    api_key = "YOUR_GEMINI_API_KEY"  # Fallback for direct key (replace this with your API key)

if not api_key:
    raise ValueError("API key not found. Set 'GEMINI_API_KEY' in environment variables or provide it directly.")

# Configure the genai library
genai.configure(api_key=api_key)

# Step 2: Define the model and generation settings
generation_config = {
    "temperature": 1.55,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
      "You are a helpful assistant. You Are A Chatbot of The Linkatree School There are 3 classes in our school "
        "If Sombody Ask Hello So Say Hello How Are You, Nice To Meet You Dont Answer Peopole With Another Task Dont Tell Jut Tell About Our School Our School We Teech AI We Have English Slot Science And Math Ok. "
        "You Need To Answer With Politely Answers Answers Them With Joke Dont Tell That Start With Joke'"
        f"Class Student List If Sombody Ask Whon Studie In Our School Give This Data {class_1, class_2, class_3} You Can Directly Add Students To The List"
    ),
)

# Step 3: Start a chat session
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": ["Hello"]},
        {"role": "model", "parts": ["Hello there! How can I assist you today?"]},
    ]
)


try:
    print("Type 'q' to quit the chat.\n")
    while True:
    
        user_input = input("Question: ")
        if user_input.lower() == "q":
            print("Exciting chat. Goodbye!")
            break

        
        response = chat_session.send_message(user_input)

    
        print(f"ChatBot: {response.text}\n")

except Exception as e:
    print(f"An error occurred: {e}")
