# nameless personal diary (NPD)
# actually simple personal diary, but i dont wanna name it.
# licensed under my own personal license, which is basically "do whatever you want with it, but don't blame me if it breaks".

def user_input():
    # loops until user inputs a valid command
    while True:
        try:
            command = input("enter a command (write, read, exit): ").strip().lower()
            if command in ["write", "read", "exit"]:
                return command
            else:
                print("Invalid command. Please try again.")
        except KeyboardInterrupt:
            print("keyboard interrupt, killing program...")
            exit()

def write_entry(entries):
    # write a diary entry
    try:
        entry = input("enter your diary entry: ").strip()
    except KeyboardInterrupt:
        print("keyboard interrupt, killing program...")
    entries.append(entry)
    with open("diary.txt", "a") as f:
        f.write(entry + "\n")

def read_entries(entries):
    # read all diary entries
    if entries:
        print("diary entries:")
        for entry in entries:
            print(f"- {entry}")
    else:
        print("No diary entries found.")

def main():
    # main function to run the program
    try:
        with open("diary.txt", "r") as f:
            entries = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        entries = []

    while True:
        command = user_input()
        if command == "write":
            write_entry(entries)
        elif command == "read":
            read_entries(entries)
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
