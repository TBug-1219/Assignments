def main():
    people = ["Alice", "Bob", "Charlie", "Diana",
              "Eve", "Frank", "Grace"]
    phoneNumbers = ["123-456-7890", "234-567-8901",
                    "345-678-9012", "456-789-0123",
                    "567-890-1234", "678-901-2345",
                    "789-012-3456"]
    
    searchName = input("Enter the name (or part of the name) to "\
                       "search for: ").lower()

    found = False
    for i in range(len(people)):
        if searchName in people[i].lower():
            print(f"Found: {people[i]} - Phone Number: "\
                  "{phoneNumbers[i]}")
            found = True

    if not found:
        print(f"No match found for: {searchName}")


if __name__ == "__main__":
    main()
