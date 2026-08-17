from chatbot import get_response
def main():
    print( "chatbot : hhi how can i help you")
    while True:
        user_input = input("user:  ").lower()
        responses = get_response( user_input )
        print("chatbot",responses )
        if user_input ==" goodbye":
            break
