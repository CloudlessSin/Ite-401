import json

responses = {
    "hello": "Hello! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "tell me about paris": "Paris is the capital of France, known for its art, fashion, and the Eiffel Tower.",
    "tell me about japan": "Japan is an island nation in East Asia, famous for its technology, anime, and cherry blossoms.",
    "default": "I'm not sure about that. Can you ask something else?"
}

def get_bot_response(user_message):
    user_message = user_message.lower()
    return responses.get(user_message, responses["default"])

def collect_places():
    places = []

    while True:
        place = input("Enter a place (or 'q' to quit): ")
        if place.lower() == 'q':
            break
        places.append(place)

    with open("places.json", "w") as file:
        json.dump(places, file)

    print("\nAll places entered have been saved to 'places.json'.")
    print("Here are the places you entered:")
    for place in places:
        print(place)

def load_places():
    try:
        with open("places.json", "r") as file:
            places = json.load(file)
            print("\nPlaces loaded from 'places.json':")
            for place in places:
                print(place)
    except FileNotFoundError:
        print("No places file found. Please collect some places first.")

def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot:", responses["bye"])
            break
        
        bot_response = get_bot_response(user_input)
        print("Chatbot:", bot_response)

def main():
    while True:
        print("\nMain Menu:")
        print("1. Collect Places")
        print("2. Load Places")
        print("3. Chat with the Bot")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            collect_places()
        elif choice == "2":
            load_places()
        elif choice == "3":
            chatbot()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()