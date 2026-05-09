rooms = {
    "standard": 2000,
    "deluxe": 4000,
    "suite": 7000
}

customer_name = input("Enter your name: ").title()

print("\n" + "=" * 60)
print(f"      WELCOME {customer_name} TO GRAND PALACE HOTEL")
print("=" * 60)
print("Type 'menu' to see available services")
print("Type 'bye' to exit")
print("=" * 60)

while True:

    user_input = input(f"\n{customer_name}: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print(f"Bot: Hello {customer_name}! How may I help you today?")

    elif "room" in user_input and ("available" in user_input or "rooms" in user_input):
        print("Bot: We have the following rooms available:")
        print("     - Standard Room")
        print("     - Deluxe Room")
        print("     - Suite Room")

    elif "price" in user_input or "cost" in user_input or "charges" in user_input:
        print("Bot: Here are our room prices:")
        for room, price in rooms.items():
            print(f"     {room.title()} Room = ₹{price}/night")

    elif "check in" in user_input:
        print("Bot: Check-in time is 12:00 PM.")

    elif "check out" in user_input:
        print("Bot: Check-out time is 11:00 AM.")

    elif "wifi" in user_input:
        print("Bot: Yes, free WiFi is available in all rooms.")

    elif "parking" in user_input:
        print("Bot: Free parking facility is available.")

    elif "food" in user_input or "restaurant" in user_input:
        print("Bot: We provide breakfast, lunch, dinner, and 24x7 room service.")

    elif "gym" in user_input:
        print("Bot: Yes, our hotel has a fully equipped gym.")

    elif "pool" in user_input or "swimming" in user_input:
        print("Bot: Yes, we have a swimming pool open from 7 AM to 9 PM.")

    elif "location" in user_input or "address" in user_input:
        print("Bot: We are located near City Center, Mumbai.")

    elif "contact" in user_input or "phone" in user_input:
        print("Bot: You can contact us at +91-9876543210.")

    elif "book" in user_input or "reservation" in user_input:

        room_type = input("Bot: Which room would you like (standard/deluxe/suite)? ").lower()

        if room_type in rooms:

            days = int(input("Bot: How many days will you stay? "))

            total = rooms[room_type] * days

            print("\n" + "=" * 50)
            print("         BOOKING CONFIRMATION")
            print("=" * 50)
            print(f"Guest Name   : {customer_name}")
            print(f"Room Type    : {room_type.title()}")
            print(f"Stay Days    : {days}")
            print(f"Total Amount : ₹{total}")
            print("Booking Status : Confirmed")
            print("=" * 50)

        else:
            print("Bot: Invalid room type selected.")

    elif "feedback" in user_input or "rating" in user_input:

        rating = input("Bot: Please rate our hotel service (1-5): ")

        print(f"Bot: Thank you for your feedback, {customer_name}!")

    elif "menu" in user_input:

        print("\n" + "=" * 50)
        print("              AVAILABLE SERVICES")
        print("=" * 50)
        print("hello / hi")
        print("rooms available")
        print("room price")
        print("check in time")
        print("check out time")
        print("wifi")
        print("parking")
        print("food / restaurant")
        print("gym")
        print("swimming pool")
        print("hotel location")
        print("contact number")
        print("book room")
        print("feedback")
        print("bye")
        print("=" * 50)

    elif "bye" in user_input or "exit" in user_input:

        print("\nBot: Thank you for visiting Grand Palace Hotel.")
        print("Bot: We hope to see you again soon.")
        break

    else:

        print("Bot: Sorry, I could not understand your request.")
        print("Bot: Please type 'menu' to see available services.")