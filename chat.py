# Function for simulating a conversation between two users
def chatbox(user1_name, user2_name):
    # print(f"{user1_name}: Hello!")
    # print(f"{user2_name}: Hi there!")

    while True:
        user1_input = input(f"{user1_name}: ")
        if user1_input.lower() in ['exit', 'quit']:
            break

        user2_input = input(f"{user2_name}: ")
        if user2_input.lower() in ['exit', 'quit']:
            break

        # print(f"{user1_name}: {user1_input}")
        # print(f"{user2_name}: {user2_input}")

# Main code
if __name__ == "__main__":
    user1_name = input("Enter User 1's name: ")
    user2_name = input("Enter User 2's name: ")

    print("Chatbox: Welcome to the chatbox!")

    chatbox(user1_name, user2_name)

    print("Chatbox: Goodbye! Chat session ended.")
