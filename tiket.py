class TrainTicket:
    def __init__(self, origin, destination, price):
        self.origin = origin
        self.destination = destination
        self.price = price

class Station:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def add_ticket(self, origin, destination, price):
        self.tickets.append(TrainTicket(origin, destination, price))

    def get_available_tickets(self):
        available_tickets = []
        for ticket in self.tickets:
            if ticket.price > 0:
                available_tickets.append(ticket)
        return available_tickets

def main():
    # Initialize train stations with train tickets
    jakarta = Station("Jakarta")
    jakarta.add_ticket("Jakarta", "Bandung", 200000)
    jakarta.add_ticket("Jakarta", "Bali", 400000)
    jakarta.add_ticket("Jakarta", "Malang", 100000)

    bandung = Station("Bandung")
    bandung.add_ticket("Bandung", "Jakarta", 200000)
    bandung.add_ticket("Bandung", "Bali", 300000)
    bandung.add_ticket("Bandung", "Malang", 150000)

    bali = Station("Bali")
    bali.add_ticket("Bali", "Jakarta", 400000)
    bali.add_ticket("Bali", "Bandung", 300000)
    bali.add_ticket("Bali", "Malang", 350000)

    malang = Station("Malang")
    malang.add_ticket("Malang", "Jakarta", 100000)
    malang.add_ticket("Malang", "Bandung", 150000)
    malang.add_ticket("Malang", "Bali", 350000)

    # Simulate user's order
    while True:
        origin = input("Enter your starting point: ").capitalize()
        destination = input("Enter your destination: ").capitalize()

        if origin not in ["Jakarta", "Bandung", "Bali", "Malang"] or destination not in ["Jakarta", "Bandung", "Bali", "Malang"]:
            print("Invalid origin or destination. Please enter a valid city.")
            continue

        # Get available tickets from the station
        station = eval(origin.lower())
        available_tickets = station.get_available_tickets()

        # Check if the ticket exists
        ticket_exists = False
        for ticket in available_tickets:
            if ticket.destination == destination:
                ticket_exists = True
                ticket.price -= 1
                print(f"Ticket successfully booked from {origin} to {destination}.")
                break

        if not ticket_exists:
            print("Ticket not available. Please try again.")

if __name__ == "__main__":
    main()
