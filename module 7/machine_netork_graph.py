
"""
Exercise 1: Create the Machine Network Graph
Write a class called MachineNetwork that:
1.​ Stores the graph in a dictionary called self.machine_links
2.​ Has a method add_machine(machine) to add a machine
3.​ Has a method add_link(m1, m2) to connect two machines (both directions)
4.​ Has a method print_network() to print all machines and their connections
5.​ Has a method print_connected_machines(machine) to print all machines
directly connected to a given machine
Then create the following links:
●​ Machine_A ↔ Machine_B​
●​ Machine_A ↔ Machine_C​
●​ Machine_B ↔ Machine_D​
●​ Machine_C ↔ Machine_D​
●​ Machine_C ↔ Machine_E​
When you print the network, it should show each machine and its neighbor list.
"""


class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        self.add_machine(m1)
        self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        for machine in self.machine_links:
            print(f"{machine} -> {self.machine_links[machine]}")

    def print_connected_machines(self, machine):
        if machine not in self.machine_links:
            print("Machine not found.")
            return
        
        print(f"{machine} -> {self.machine_links[machine]}")


# Test Exercise 1
network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

print("Network:")
network.print_network()

print("\nConnections of Machine_C:")
network.print_connected_machines("Machine_C")
