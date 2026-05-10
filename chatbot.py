rooms = {
    "standard": {"price": 2000, "beds": 1, "view": "Garden View"},
    "deluxe":   {"price": 4000, "beds": 2, "view": "City View"},
    "suite":    {"price": 7000, "beds": 3, "view": "Sea View"}
}

bookings = []

customer_name = input("Enter your name: ").title()

print("\n" + "=" * 60)
print(f"      WELCOME {customer_name} TO GRAND PALACE HOTEL")
print("=" * 60)
print("Type 'menu' to see available services")
print("Type 'bye' to exit")
print("=" * 60)


def show_menu():
    print("\n" + "=" * 50)
    print("           AVAILABLE SERVICES")
    print("=" * 50)
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
    print("my bookings")
    print("feedback")
    print("bye")
    print("=" * 50)


def show_rooms():
    print("Bot: We have the following rooms available:")
    print("-" * 40)
    for room, details in rooms.items():
        print(f"     {room.title()} Room")
        print(f"       Price : ₹{details['price']}/night")
        print(f"       Beds  : {details['beds']}")
        print(f"       View  : {details['view']}")
    print("-" * 40)


def handle_booking(customer_name):
    room_type = input("Bot: Which room would you like? (standard / deluxe / suite): ").strip().lower()

    if room_type not in rooms:
        print("Bot: Invalid room type. Please choose standard, deluxe, or suite.")
        return

    try:
        days = int(input("Bot: How many days will you stay? ").strip())
        if days <= 0:
            print("Bot: Please enter a valid number of days (must be 1 or more).")
            return
    except ValueError:
        print("Bot: Invalid input. Please enter a number for days.")
        return
   
    total = rooms[room_type]["price"] * days
    print(f"The total amount of {room_type} for {days}day is:{total}")
    ans=input("Do you want to confirm booking:")
    if ans=="yes" or ans=="Yes":
        booking = {
            "room": room_type.title(),
            "days": days,
            "total": total
        }
        bookings.append(booking)
    
        print("\n" + "=" * 50)
        print("         BOOKING CONFIRMATION")
        print("=" * 50)
        print(f"  Guest Name     : {customer_name}")
        print(f"  Room Type      : {room_type.title()}")
        print(f"  Beds           : {rooms[room_type]['beds']}")
        print(f"  View           : {rooms[room_type]['view']}")
        print(f"  Stay Duration  : {days} night(s)")
        print(f"  Total Amount   : ₹{total}")
        print(f"  Booking Status : Confirmed")
        print("=" * 50)
    else:
        print("for more information contact hotel!")


def show_bookings(customer_name):
    if not bookings:
        print(f"Bot: No bookings found for {customer_name} yet.")
        return
    print(f"\nBot: Bookings for {customer_name}:")
    print("-" * 40)
    for i, b in enumerate(bookings, 1):
        print(f"  {i}. {b['room']} Room | {b['days']} night(s) | ₹{b['total']}")
    print("-" * 40)


def handle_feedback(customer_name):
    while True:
        rating = input("Bot: Please rate our hotel service (1-5): ").strip()
        if rating in ["1", "2", "3", "4", "5"]:
            print(f"Bot: Thank you for rating us {rating}/5, {customer_name}! We appreciate your feedback.")
            break
        else:
            print("Bot: Please enter a number between 1 and 5.")


while True:
    user_input = input(f"\n{customer_name}: ").strip().lower()

    if not user_input:
        print("Bot: Please type something. Type 'menu' to see available services.")
        continue

    if "hello" in user_input or "hi" in user_input:
        print(f"Bot: Hello {customer_name}! How may I assist you today?")

    elif "room" in user_input and ("available" in user_input or "rooms" in user_input or "types" in user_input):
        show_rooms()

    elif "price" in user_input or "cost" in user_input or "charges" in user_input or "rate" in user_input:
        print("Bot: Here are our room prices:")
        for room, details in rooms.items():
            print(f"     {room.title()} Room = ₹{details['price']}/night")

    elif "check in" in user_input or "checkin" in user_input:
        print("Bot: Check-in time is 12:00 PM.")

    elif "check out" in user_input or "checkout" in user_input:
        print("Bot: Check-out time is 11:00 AM.")

    elif "wifi" in user_input or "internet" in user_input:
        print("Bot: Yes, free high-speed WiFi is available in all rooms and common areas.")

    elif "parking" in user_input:
        print("Bot: Free parking facility is available for all guests.")

    elif "food" in user_input or "restaurant" in user_input or "dining" in user_input:
        print("Bot: We offer breakfast (7-10 AM), lunch (12-3 PM), dinner (7-10 PM), and 24x7 room service.")

    elif "gym" in user_input or "fitness" in user_input:
        print("Bot: Yes, our fully equipped gym is open from 6 AM to 10 PM.")

    elif "pool" in user_input or "swimming" in user_input:
        print("Bot: Yes, we have a swimming pool open from 7 AM to 9 PM.")

    elif "location" in user_input or "address" in user_input or "where" in user_input:
        print("Bot: We are located near City Centre, Mumbai.")
        print("     Landmark: Opposite Central Mall, MG Road.")

    elif "contact" in user_input or "phone" in user_input or "number" in user_input:
        print("Bot: You can reach us at:")
        print("     Phone   : +91-9876543210")
        print("     Email   : info@grandpalace.com")

    elif "book" in user_input or "reservation" in user_input or "reserve" in user_input:
        handle_booking(customer_name)

    elif "my booking" in user_input or "my reservation" in user_input:
        show_bookings(customer_name)

    elif "feedback" in user_input or "rating" in user_input or "review" in user_input:
        handle_feedback(customer_name)

    elif "menu" in user_input or "help" in user_input or "services" in user_input:
        show_menu()
        print(f"Hi {customer_name} how i can help you!")

    elif "bye" in user_input or "exit" in user_input or "goodbye" in user_input:
        print(f"\nBot: Thank you for visiting Grand Palace Hotel, {customer_name}.")
        print("Bot: We hope to see you again soon. Have a wonderful day!")
        break

    else:
        print("Bot: Sorry, I could not understand that.")
        print("Bot: Type 'menu' to see all available services.")
