# Function to read telephone numbers from a file and store them in a list
def read_phone_numbers(file_name):
    """
    Reads telephone numbers from a file and returns them as a list.
    :param file_name: Name of the file containing phone numbers.
    :return: List of phone numbers.
    """
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to translate alphabetic characters in a phone number to their numeric equivalents
def translate_phone_number(phone_number):
    """
    Translates a phone number with alphabetic characters to its numeric equivalent.
    :param phone_number: The original phone number (e.g., "555-GET-FOOD").
    :return: Translated phone number (e.g., "555-438-3663").
    """
    # Mapping of alphabetic characters to their numeric equivalents
    char_to_digit = {
        **dict.fromkeys("ABC", '2'),
        **dict.fromkeys("DEF", '3'),
        **dict.fromkeys("GHI", '4'),
        **dict.fromkeys("JKL", '5'),
        **dict.fromkeys("MNO", '6'),
        **dict.fromkeys("PQRS", '7'),
        **dict.fromkeys("TUV", '8'),
        **dict.fromkeys("WXYZ", '9'),
    }

    # Convert each character in the phone number
    translated = []
    for char in phone_number:
        if char.isalpha():  # Convert alphabetic characters
            translated.append(char_to_digit[char.upper()])
        else:  # Keep numeric and special characters as is
            translated.append(char)

    return ''.join(translated)

# Function to process the phone numbers and display the results
def process_and_display_numbers(file_name):
    """
    Processes the phone numbers by translating alphabetic characters and displaying the results.
    :param file_name: Name of the file containing phone numbers.
    """
    original_numbers = read_phone_numbers(file_name)
    translated_numbers = [translate_phone_number(number) for number in original_numbers]

    print(f"{'Original Number':<20} {'Converted Number':<20}")
    print("-" * 40)
    for original, translated in zip(original_numbers, translated_numbers):
        print(f"{original:<20} {translated:<20}")

# Main function
def main():
    """
    Main function to orchestrate the reading, processing, and displaying of phone numbers.
    """
    file_name = "wordNumbers.txt"  # Predefined file name
    try:
        process_and_display_numbers(file_name)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Program entry point
if __name__ == "__main__":
    main()
