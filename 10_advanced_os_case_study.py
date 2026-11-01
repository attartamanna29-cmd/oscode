# Experiment 10: Case Study on Advanced Operating Systems
# A short menu-based study aid; this experiment is generally theory/case-study based.

topics = {
    "1": ("Multiprocessing", "Uses two or more CPUs/cores to execute tasks."),
    "2": ("Distributed OS", "Coordinates multiple networked computers as one system."),
    "3": ("Real-Time OS", "Gives responses within strict time limits."),
    "4": ("Virtualization", "Runs virtual machines on one physical computer."),
    "5": ("Cloud Computing", "Provides computing resources over the internet."),
    "6": ("Mobile OS", "Manages mobile-device hardware, apps and power.")
}

while True:
    print("\nAdvanced OS Case Study")
    for key, value in topics.items():
        print(key + ".", value[0])
    print("0. Exit")
    choice = input("Choose a topic: ")

    if choice == "0":
        break
    elif choice in topics:
        name, detail = topics[choice]
        print(name + ":", detail)
    else:
        print("Invalid choice.")
