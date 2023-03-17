# Import necessary libraries
import openai
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        # Get user input and generate response using ChatGPT 3.5 API
        user_input = request.form["user_input"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{user_input}\n\nChatGPT:",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        chat_response = response.choices[0].text.strip()
        return render_template("index.html", chat_response=chat_response)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
