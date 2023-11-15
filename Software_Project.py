# Main menu for the IT5014 Helpdesk Ticket System
def display_menu():
    print("\nIT5014 Helpdesk Ticket System:")
    print("------------------------------------------------------------------")
    print("Select from the following choices:")
    print("0: Exit")
    print("1: New Ticket")
    print("2: Show all Tickets")
    print("3: Respond to Ticket")
    print("4: Re-open Ticket")
    print("5: Ticket Statistics")
    print("------------------------------------------------------------------")


# Class to represent text colors
class TextColours:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# Function to get the user's choice from the menu
def get_user_choice():
    while True:
        try:
            user_input = int(
                input(f"{TextColours.HEADER}Enter menu selection 0 - 5: {TextColours.ENDC}"))
            if 0 <= user_input <= 5:
                return user_input
            else:
                print(
                    f"{TextColours.FAIL}Invalid input. Please enter a number between 0 and 5.{TextColours.ENDC}")
        except ValueError:
            print(
                f"{TextColours.FAIL}Invalid input. Please enter a valid number between 0 and 5.{TextColours.ENDC}")


# Class to represent a ticket
class Ticket:
    ticket_counter = 1  # Static field to keep track of the ticket number
    tickets = []  # List to store ticket information

    # Class method to generate a new ticket number
    @classmethod
    def generate_ticket_number(cls):
        ticket_number = cls.ticket_counter + 2000
        cls.ticket_counter += 1
        return ticket_number

    # Class method to get ticket statistics
    @classmethod
    def get_ticket_statistics(cls):
        total_submitted_tickets = len(cls.tickets)
        total_resolved_tickets = sum(
            1 for ticket in cls.tickets if ticket["Ticket Status"] == "Closed")
        total_open_tickets = sum(
            1 for ticket in cls.tickets if ticket["Ticket Status"] in ["Open", "Reopened"])
        return total_submitted_tickets, total_resolved_tickets, total_open_tickets


# Function to submit a new ticket
def submit_new_ticket():
    while True:
        staff_id = input("\nEnter your four digit staff ID: ")
        # Check if the staff ID is a four-digit number
        while not staff_id.isdigit() or len(staff_id) != 4:
            print(
                f"{TextColours.FAIL}Invalid Staff ID. Please enter your four-digit staff ID.{TextColours.ENDC}")
            staff_id = input("Enter your four digit staff ID: ")

        ticket_creator_name = input("Enter your name: ")
        # Check if the name is blank
        while not ticket_creator_name:
            print(
                f"{TextColours.FAIL}Name cannot be blank. Please enter a valid name.{TextColours.ENDC}")
            ticket_creator_name = input("Enter your name: ")

        contact_email = input("Enter contact email: ")
        # Check if the contact email is blank
        while not contact_email:
            print(
                f"{TextColours.FAIL}Email cannot be blank. Please enter a valid email.{TextColours.ENDC}")
            contact_email = input("Enter contact email: ")

        print("If you require a new password type: Password change")
        description = input("Enter description of the problem: ")
        # Check if the description is blank
        while not description:
            print(
                f"{TextColours.FAIL}Description cannot be blank. Please enter a valid description.{TextColours.ENDC}")
            description = input("Enter description of the problem: ")

        # Check if the description contains the words "Password change"
        if any(keyword in description.lower() for keyword in ["password change", "passwordchange"]):
            new_password = staff_id[:2] + ticket_creator_name[:3]
            print(
                f"\nNew Password: {TextColours.OKGREEN}{new_password}{TextColours.ENDC}")
            response = f"User password was set to: {new_password}"
            ticket_status = "Closed"
        # Mark ticket as 'Open' and set default response if the description does not contain the words "Password change"
        else:
            response = "Not yet provided"
            ticket_status = "Open"

        # Generate a new ticket number
        ticket_number = Ticket.generate_ticket_number()

        # Save the ticket information to the list
        Ticket.tickets.append({
            "Ticket Number": ticket_number,
            "Staff ID": staff_id,
            "Ticket Creator Name": ticket_creator_name,
            "Contact Email": contact_email,
            "Description": description,
            "Response": response,
            "Ticket Status": ticket_status
        })

        # Print the ticket information
        # Set the ticket status colour
        ticket_status_colour = TextColours.OKGREEN if ticket_status == "Open" else TextColours.FAIL
        print(
            f"{TextColours.OKGREEN}\nTicket submitted successfully!{TextColours.ENDC}")
        print(f"Ticket Number: {ticket_number}")
        print(f"Staff ID: {staff_id}")
        print(f"Ticket Creator Name: {ticket_creator_name}")
        print(f"Contact Email: {contact_email}")
        print(f"Description: {description}")
        print(f"Response: {response}")
        print(
            f"Ticket Status: [{ticket_status_colour}{ticket_status}{TextColours.ENDC}]")

        # Ask the user if they want to submit another ticket
        another_problem = input(
            f"{TextColours.HEADER}\nDo you have another problem to submit? (Y/N): {TextColours.ENDC}").lower()
        if another_problem != 'y':
            break


# Function to show all tickets
def show_all_tickets():
    # Check if there are any tickets
    if not Ticket.tickets:
        print(f"{TextColours.FAIL}\nNo tickets have been submitted.{TextColours.ENDC}")
    else:
        print("\nAll Tickets:")
        # Print all the tickets
        for ticket in Ticket.tickets:
            # Set the ticket status colour
            ticket_status_colour = TextColours.OKGREEN if ticket[
                "Ticket Status"] == "Open" else TextColours.FAIL
            print("------------------------------------------------------------------")
            print("Ticket Number:", ticket["Ticket Number"])
            print("Staff ID:", ticket["Staff ID"])
            print("Ticket Creator Name:", ticket["Ticket Creator Name"])
            print("Contact Email:", ticket["Contact Email"])
            print("Description:", ticket["Description"])
            print("Response:", ticket["Response"])
            print(
                f"Ticket Status: [{ticket_status_colour}{ticket['Ticket Status']}{TextColours.ENDC}]")
            print("------------------------------------------------------------------")


# Function to respond to a ticket
def respond_to_ticket():
    # Check if there are any tickets
    if not Ticket.tickets:
        print(f"{TextColours.FAIL}\nNo tickets have been submitted.{TextColours.ENDC}")
        return

    while True:
        # Check if there are any open tickets
        if not any(ticket["Ticket Status"] == "Open" for ticket in Ticket.tickets):
            print(f"{TextColours.FAIL}\nNo open tickets found.{TextColours.ENDC}")
            return

        # Print all the open ticket numbers
        print("\nOpen Tickets:")
        open_ticket_numbers = [str(ticket["Ticket Number"])
                               for ticket in Ticket.tickets if ticket["Ticket Status"] == "Open"]
        open_tickets_str = ", ".join(open_ticket_numbers)
        print(open_tickets_str)

        ticket_number = input(
            f"{TextColours.HEADER}\nEnter the four-digit ticket number: {TextColours.ENDC}")

        # Find the ticket with the given ticket number
        found_ticket = None
        for ticket in Ticket.tickets:
            if str(ticket["Ticket Number"]) == ticket_number:
                found_ticket = ticket
                break

        # Check if the ticket was found
        if found_ticket is None:
            print(
                f"{TextColours.FAIL}\nInvalid ticket number. Ticket not found.{TextColours.ENDC}")
        # Check if the ticket is already closed
        else:
            if found_ticket["Ticket Status"] == "Closed":
                print(
                    f"{TextColours.FAIL}\nThis ticket is already closed. Cannot respond.{TextColours.ENDC}")
            # Add a response to the ticket if it is open
            else:
                print(
                    f"\nResponding to ticket: {TextColours.OKGREEN}{ticket_number}{TextColours.ENDC}")
                response = input(
                    f"{TextColours.HEADER}Response: {TextColours.ENDC}")
                found_ticket["Response"] = response
                found_ticket["Ticket Status"] = "Closed"
                print(
                    f"{TextColours.OKGREEN}\nResponse added successfully. Ticket marked as closed.{TextColours.ENDC}")

        # Ask the user if they want to submit another response
        another_response = input(
            f"{TextColours.HEADER}\nDo you have another response to submit? (Y/N): {TextColours.ENDC}").lower()
        if another_response != 'y':
            break


# Function to reopen a ticket
def reopen_ticket():
    # Check if there are any tickets
    if not Ticket.tickets:
        print(f"{TextColours.FAIL}\nNo tickets have been submitted.{TextColours.ENDC}")
        return

    while True:
        # Check if there are any closed tickets
        if not any(ticket["Ticket Status"] == "Closed" for ticket in Ticket.tickets):
            print(f"{TextColours.FAIL}\nNo closed tickets found.{TextColours.ENDC}")
            return

        # Print all the closed ticket numbers
        print("\nClosed Tickets:")
        closed_ticket_numbers = [str(ticket["Ticket Number"])
                                 for ticket in Ticket.tickets if ticket["Ticket Status"] == "Closed"]
        closed_tickets_str = ", ".join(closed_ticket_numbers)
        print(closed_tickets_str)

        ticket_number = input(
            f"{TextColours.HEADER}\nEnter the four-digit ticket number to reopen: {TextColours.ENDC}")

        # Find the ticket with the given ticket number
        found_ticket = None
        for ticket in Ticket.tickets:
            if str(ticket["Ticket Number"]) == ticket_number:
                found_ticket = ticket
                break

        # Check if the ticket was found
        if found_ticket is None:
            print(
                f"{TextColours.FAIL}\nInvalid ticket number. Ticket not found.{TextColours.ENDC}")
        # Check if the ticket is already open
        else:
            if found_ticket["Ticket Status"] == "Open":
                print(
                    f"{TextColours.FAIL}\nThis ticket is already open. Cannot reopen.{TextColours.ENDC}")
            # Reopen the ticket if it is closed
            else:
                found_ticket["Ticket Status"] = "Reopened"
                print(
                    f"{TextColours.OKGREEN}\nTicket {ticket_number} has been reopened. You can now submit new responses.{TextColours.ENDC}")

        # Ask the user if they want to reopen another ticket
        another_reopen = input(
            f"{TextColours.HEADER}\nDo you want to reopen another ticket? (Y/N): {TextColours.ENDC}").lower()
        if another_reopen != 'y':
            break


# Function to show ticket statistics
def ticket_statistics():
    total_submitted, total_resolved, total_open = Ticket.get_ticket_statistics()
    print(f"{TextColours.HEADER}\nTicket Statistics:{TextColours.ENDC}")
    print(
        f"Submitted Tickets: {TextColours.OKGREEN}{total_submitted}{TextColours.ENDC}")
    print(
        f"Resolved Tickets: {TextColours.OKGREEN}{total_resolved}{TextColours.ENDC}")
    print(f"Open Tickets: {TextColours.OKGREEN}{total_open}{TextColours.ENDC}")


# Main program
if __name__ == "__main__":
    while True:
        display_menu()
        user_choice = get_user_choice()

        # Check the user's choice and call the appropriate function
        if user_choice == 0:
            print(
                f"{TextColours.OKGREEN}\nExiting the program. Goodbye!{TextColours.ENDC}")
            break
        elif user_choice == 1:
            submit_new_ticket()
        elif user_choice == 2:
            show_all_tickets()
        elif user_choice == 3:
            respond_to_ticket()
        elif user_choice == 4:
            reopen_ticket()
        elif user_choice == 5:
            ticket_statistics()
