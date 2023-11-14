# IT5016D_Assessment 2 - Software Project
## Team Members
- Dylan Dacre

## Project Description
The Helpdesk Ticket System is a command-line Python application designed to streamline the process of submitting, managing, and responding to IT-related issues within an organization. This user-friendly system allows IT staff and users to interact with a menu-driven interface, providing a straightforward way to create, track, and resolve helpdesk tickets.

## Features
1. New Ticket Submission:

    - Users can easily submit new helpdesk tickets by providing essential information, including Staff ID, Ticket Creator Name, Contact Email, and a description of the issue.
    - The system automatically assigns a unique ticket number to each new ticket, and if the issue description includes the words "Password Change," a new password is generated.
2. Ticket Display:

    - Users and IT staff can view a list of all submitted tickets, including details such as ticket number, staff ID, ticket creator name, contact email, description, response (if available), and ticket status.
3. Responding to Tickets:

    - IT staff can respond to open tickets by providing a detailed response. Once a response is added, the ticket is marked as closed, preventing further modifications.
4. Reopening Tickets:

    - Closed tickets can be reopened, allowing for additional responses and updates. This feature enables ongoing communication until the issue is fully resolved.
5. Ticket Statistics:

    - The system provides an overview of ticket statistics, including the total number of submitted tickets, resolved tickets, and open tickets (including reopened).

## Text Formatting
- The application utilizes ANSI escape codes for text formatting, allowing for colored output. Successful actions are displayed in green, while errors and critical messages are shown in red.

## Using the Application
It's recommended to use an application that supports ANSI escape codes othwrwise the text formatting will not be displayed correctly. The application has been tested using Python 3.11.3 in the following applications:
- PyCharm 2023.2.3
- Visual Studio Code 1.84.2

Download the repository, open Pycharm or Visual Studio Code, navigate to the project folder, and open the Software_Project.py file. Run the file to start the application.
