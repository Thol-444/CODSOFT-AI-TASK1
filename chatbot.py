import re
import datetime

def get_response(user_input):
    user_input = user_input.lower().strip()

    #Greetings
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! I'm your AI assistant. How can I help you today?"
    
    #How are you
    elif re.search(r'how are you|how r u|how do you do', user_input):
        return "I'm doing great! Thanks for asking. How about you?"
    
    #Name
    elif re.search(r' your name|who are you|what are you', user_input):
        return "I'm an AI Chatbot built by Nihaarika using rule-based responses!"
    
    #Time
    elif re.search(r'time|what time' , user_input):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"Current time is {now}"
    
    #Date
    elif re.search(r'date|today|what day',user_input):
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}"
    
    #What is AI
    elif re.search(r'what is ai|artificial intelligence|define ai', user_input):
        return "AI (Artificial Intelligence) is the simulation of human intelligence by machines to perform tasks like learning, reasoning, and problem-solving!"
    
    #what is ML
    elif re.search(r'what is ml|What is Machine Learning|machine learning|define ml', user_input):
        return "Machine Learning is a subset of AI where machines learn from data to improve their performance without being explicitly programmed!"
    
    # What is Python
    elif re.search(r'what is python|python programming', user_input):
        return "Python is a high-level programming language known for its simplicity and is widely used in AI, ML, web development and data science!"
    
    # Weather
    elif re.search(r'weather|temperature|climate', user_input):
        return "I don't have access to real-time weather data. Please check weather.com for updates!"
    
    # Jokes
    elif re.search(r'joke|funny|make me laugh', user_input):
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😄"
    
    # Help
    elif re.search(r'\bhelp\b|what can you do|features', user_input):
        return """I can help you with:
  → Greetings and conversations
  → Current time and date
  → Questions about AI and ML
  → Python programming info
  → Tell jokes
  → General knowledge questions
  Just type your question!"""
    
    # Age
    elif re.search(r'your age|how old are you', user_input):
        return "I'm a brand new chatbot — just created! Age doesn't apply to me 😄"
    
    # Creator
    elif re.search(r'who made you|who created you|who built you', user_input):
        return "I was built by Nihaarika Tholu as part of CodSoft AI Internship Task 1!"
    
    # Bye
    elif re.search(r'\bbye\b|\bgoodbye\b|\bsee you\b|\bexit\b|\bquit\b', user_input):
        return "EXIT"
    
    # Thanks
    elif re.search(r'thank you|thanks|thank u', user_input):
        return "You're welcome! Happy to help 😊"
    
    # Default
    else:
        return "I'm not sure about that. Type 'help' to see what I can do!"


def main():
    print("=" * 45)
    print("     Welcome to Nihaarika's AI Chatbot!    ")
    print("=" * 45)
    print("  Type 'help' to see available commands  ")
    print("  Type 'quit' or 'bye' to exit           ")
    print("=" * 45)
    print()
    
    while True:
        user_input = input("You: ")
        
        if not user_input.strip():
            print("Bot: Please type something!\n")
            continue
        
        response = get_response(user_input)
        
        if response == "EXIT":
            print("Bot: Goodbye! Have a wonderful day! 👋")
            break
        
        print(f"Bot: {response}")
        print()


if __name__ == "__main__":
    main()