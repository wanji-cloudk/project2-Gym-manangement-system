class Gym:
    def __init__(self):
        self.capacity = 80
        self.members = []
        self.waitlist = []
        self.classes = {
            "spin": [],
            "yoga": [],
            "boxing": [],
            "regular_workout": []
            }
        self.class_capacity = 20


    def prompt_member(self):
        name = input("Greetings,kindly enter your name: ").strip().capitalize()
        class_name = input("Which class would you like to book(spin, yoga, boxing, regular workout)?").strip().lower()
        self.book_class(name, class_name)

    def book_class(self, member_name, class_name):
        if len(self.members) > self.capacity:
            self.waitlist.append(member_name)
            print(f"Greetings!:{member_name}, apologize for inconvenience gym is currently full, you have been added to waitlist, thank you for your patience.")
            return
        if class_name in self.classes:
            if len(self.classes[class_name]) < self.class_capacity:
                self.classes[class_name].append(member_name)
                self.members.append(member_name)
                print(f"Congratulations! {member_name}, you have booked for {class_name} class.")
            else:
                print(f"Sorry, {member_name}, the {class_name} class is fully booked, Would you like to book another class?")
        else:
            print(f"Sorry: The {class_name} classs does not exist, please choose from the listed classes.")

    def show_classes(self):
        print("\nCurrent Class Booking:")
        for class_name, attendants in self.classes.items():
            status = "Available" if len(attendants) < self.class_capacity else "Full"
            print(f"{class_name.capitalize()}: {len(attendants)}/{self.class_capacity} - {status}")
        print(f"\nTotal Members Checked In: {len(self.members)}/{self.capacity}")
        if self.waitlist:
            print(f"Waitlist: {len(self.waitlist)} members currently on waitlist.")

def main():
    gym = Gym()
    while True:
        gym.prompt_member()
        gym.show_classes()

if __name__ == "__main__":
    main()
