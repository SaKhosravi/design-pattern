"""
In this example, we have a list of customer tickets from which
we are going to select one with different strategies:
    -FIFO
    -FILO
    -Random
    ...
In this file, we do this without using design patterns.
"""
import random
import string
from typing import List


def generate_id(length=8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: set
    customer: str
    issue: str

    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(issue=issue, customer=customer))

    def process_tickets(self, process_strategy: str = "fifo"):
        if len(self.tickets) == 0:
            print("there are no tickets to process,.")
            return

        if process_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)

        elif process_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)

        elif process_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for i in list_copy:
                self.process_ticket(i)

    def process_ticket(self, ticket: SupportTicket):
        print("----------------")
        print(f"ticket id is :{ticket.id}")
        print(f"user is:{ticket.customer}")
        print(f"issue is:{ticket.issue}")
        print()


app = CustomerSupport()
app.create_ticket("Sara", "computer issue")
app.create_ticket("Tom", "mobile issue")
app.create_ticket("Jennifer", "tablet issue")

app.process_tickets("fifo")
