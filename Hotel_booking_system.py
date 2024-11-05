from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_occupied = False
    
    def mark_as_occupied(self):
        self.is_occupied = True

    def mark_as_available(self):
        self.is_occupied = False
    

class Booking:
    def __init__(self, guest_name, room, check_in_date, check_out_date):
        self.guest_name = room
        self.room = room
        self.check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
        self.check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")


    def booking_duration(self):
        return (self.check_out_date  - self.check_in_date).days
    

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room_number, room_type):
        '''Add a new room to the hotels.'''
        new_room = Room(room_number, room_type)
        self.rooms.append(new_room)

    def check_room_availability(self, room_type, check_in_date, check_out_date):
        '''check if any room of the specified is available.'''
        available_rooms = [
            room for room in self.rooms if room.room_type == room_type and not room.is_occupied
        ]

        if available_rooms:
            return available_rooms[0] #Return the first available room
        return None
    
    def book_room(self, guest_name, room_type, check_in_date, check_out_date ):
        '''Book an available room for the guest.'''
        available_room = self.check_room_availability(room_type, check_in_date, check_out_date)
        if available_room:
            booking = Booking(guest_name, available_room, check_in_date, check_out_date)
            self.bookings.append(booking)
            available_room.mark_as_occupied()
            print(f"Room {available_room.room_number} Booked successfully for {guest_name}.")
        else:
            print(f"No Available {room_type} rooms for the selected dates")

    def cancel_booking(self, guest_name):
        '''Cancel an exiting booking.'''
        for booking in self.bookings:
            if booking.guest_name == guest_name:
                booking.room.mark_as_available()
                self.bookings.remove(booking)
                print(f"Booking for {guest_name} has been canceled.")
                return
        print(f"No bookings for {guest_name} found.")

    def check_out(self, guest_name):
        '''Check out the guest and mark the room as avaialble.'''
        for booking in self.bookings:
            if booking.guest_name == guest_name:
                booking.room.mark_as_available()
                print(f"{guest_name} has checked out of room {booking.room.room_number}.")
                self.bookings.remove(booking)
                return
        print(f"No booking found for {guest_name}.")
    
    
    def list_available_rooms(self):
        '''List all available rooms.'''
        available_rooms = [room.room_number for room in self.rooms if not room.is_occupied]
        print("Avaialble Rooms:", available_rooms)
hotel = Hotel("Sunshine Hotel")

# Adding rooms
hotel.add_room(101, "Single")
hotel.add_room(102, "Double")
hotel.add_room(201, "Single")
hotel.add_room(202, "Double")

# Booking a room
hotel.book_room("Alice", "Single", "2024-11-01", "2024-11-05")
hotel.book_room("Bob", "Double", "2024-11-01", "2024-11-07")

# List available rooms after bookings
hotel.list_available_rooms()

# Cancel a booking
hotel.cancel_booking("Alice")

# Check out a guest
hotel.check_out("Bob")

# List available rooms after check-out
hotel.list_available_rooms()

