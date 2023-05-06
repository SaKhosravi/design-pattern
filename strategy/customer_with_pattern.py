"""
In this file, we want to solve the Customer problem with the strategy pattern.
Problem:
    in the previous code, if we want to add more strategies we need to modify
    the "process_ticket" method. So, "process_ticket" has a low Cohesion.Because "process_ticket"
     is responsible for both ticket process and strategy.

Strategy Design Patterns solve these kinds of problems.

First:
     We define an Interface class with abstract method "create_ordering".
Second:
    for each strategy, we define a class that inherits from the TicketOrderStrategy class,
    and override the "create_ordering" function.
"""
import random
import string
from typing import List
from abc import ABC,abstractmethod

def generate_id(length=8):
    return "".join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
    id: set
    customer: str
    issue: str
    def __init__(self,customer,issue) -> None:
        self.id = generate_id()
        self.customer= customer
        self.issue = issue


class TicketOrderStrategy(ABC):
    @abstractmethod
    def create_ordering(self,list:List[SupportTicket]) ->List[SupportTicket]:
        pass


class FIFOStrategy(TicketOrderStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class FILOStrategy(TicketOrderStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        return reversed(list_copy)


class RandomStrategy(TicketOrderStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(issue=issue, customer=customer))

    def process_tickets(self, process_strategy: TicketOrderStrategy):

        # create the oreder list
        ticket_list = process_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("there are no tickets to process,.")
            return
        for ticket in ticket_list:
            self.process_ticket(ticket=ticket)

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

app.process_tickets(RandomStrategy())