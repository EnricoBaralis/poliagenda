class Event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

    def __str__(self):
        return f"Title: {self.title}, Date: {self.date}, Description: {self.description}"


class Agenda:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, description):
        event = Event(title, date, description)
        self.events.append(event)

    def remove_event(self, title):
        self.events = [event for event in self.events if event.title != title]

    def list_events(self):
        for event in self.events:
            print(event)


if __name__ == "__main__":
    agenda = Agenda()
    print(
        """
     _____      _ _           _                                _       
    |  __ \    | (_)         (_)     /\                       | |      
    | |__) |__ | |_ _ __ ___  _     /  \   __ _  ___ _ __   __| | __ _ 
    |  ___/ _ \| | | '_ ` _ \| |   / /\ \ / _` |/ _ \ '_ \ / _` |/ _` |
    | |  | (_) | | | | | | | | |  / ____ \ (_| |  __/ | | | (_| | (_| |
    |_|   \___/|_|_|_| |_| |_|_| /_/    \_\__, |\___|_| |_|\__,_|\__,_|
                                          __/ |                       
                                         |___/                        
    
    Welcome to the Polimi Agenda Application!
    """
    )
    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. List Events")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the event: ")
            date = input("Enter the date of the event: ")
            description = input("Enter the description of the event: ")
            agenda.add_event(title, date, description)
        elif choice == "2":
            title = input("Enter the title of the event to remove: ")
            agenda.remove_event(title)
        elif choice == "3":
            print("Listing all events:")
            agenda.list_events()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
