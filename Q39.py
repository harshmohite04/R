class Ticket:
    def __init__(self, ticket_id, event_name, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.price = price
        self.is_booked = False

    def display_info(self):
        print(f"Ticket ID: {self.ticket_id}, Event: {self.event_name}, Price: ${self.price:.2f}, Booked: {self.is_booked}")

    def book_ticket(self):
        if not self.is_booked:
            self.is_booked = True
            print("Ticket booked successfully!")
        else:
            print("Ticket is already booked.")


class MovieTicket(Ticket):
    def __init__(self, ticket_id, movie_name, show_time, price):
        super().__init__(ticket_id, f"Movie: {movie_name}, Show Time: {show_time}", price)


class ConcertTicket(Ticket):
    def __init__(self, ticket_id, artist_name, venue, date, price):
        super().__init__(ticket_id, f"Concert: {artist_name}, Venue: {venue}, Date: {date}", price)


class BookingSystem(Ticket):
    def __init__(self):
        super().__init__(ticket_id=None, event_name="Booking System", price=0)
        self.available_tickets = []

    def add_ticket(self, ticket):
        self.available_tickets.append(ticket)

    def display_available_tickets(self):
        print("Available Tickets:")
        for ticket in self.available_tickets:
            ticket.display_info()


# Example usage:
if __name__ == "__main__":
    # Create instances of subclasses
    movie_ticket = MovieTicket(1, "Inception", "18:00", 15.99)
    concert_ticket = ConcertTicket(2, "Coldplay", "Stadium XYZ", "2023-05-20", 49.99)

    # Create an instance of BookingSystem
    booking_system = BookingSystem()

    # Add tickets to the booking system
    booking_system.add_ticket(movie_ticket)
    booking_system.add_ticket(concert_ticket)

    # Display available tickets
    booking_system.display_available_tickets()

    # Book a ticket
    movie_ticket.book_ticket()
    concert_ticket.book_ticket()

    # Display updated ticket information
    booking_system.display_available_tickets()
