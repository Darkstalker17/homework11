def shutdown(user_input):
    if user_input.lower() == "yes":
        return "Shutting down"
    elif user_input.lower() == "no":
        return "Abort shut down"
    else:
        return "Sorry"


user_input = input("Do you want to shut down the system? (Yes/No): ")
print(shutdown(user_input))







