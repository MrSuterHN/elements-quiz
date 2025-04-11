import streamlit as st
import random

st.title("🎈 My new app")



elements = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminum",
    "Si": "Silicon",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "Ar": "Argon",
    "K": "Potassium",
    "Ca": "Calcium",
    "Sc": "Scandium",
    "Ti": "Titanium",
    "V": "Vanadium",
    "Cr": "Chromium",
    "Mn": "Manganese",
    "Fe": "Iron",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsenic",
    "Se": "Selenium",
    "Br": "Bromine",
    "Kr": "Krypton",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirconium",
    "Nb": "Niobium",
    "Mo": "Molybdenum",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silver",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Tin",
    "Sb": "Antimony",
    "Te": "Tellurium",
    "I": "Iodine",
    "Xe": "Xenon",
    "Cs": "Cesium",
    "Ba": "Barium",
    "La": "Lanthanum",
    "Ce": "Cerium",
    "Pr": "Praseodymium",
    "Nd": "Neodymium",
    "Pm": "Promethium",
    "Sm": "Samarium",
    "Eu": "Europium",
    "Gd": "Gadolinium",
    "Tb": "Terbium",
    "Dy": "Dysprosium",
    "Ho": "Holmium",
    "Er": "Erbium",
    "Tm": "Thulium",
    "Yb": "Ytterbium",
    "Lu": "Lutetium",
    "Hf": "Hafnium",
    "Ta": "Tantalum",
    "W": "Tungsten",
    "Re": "Rhenium",
    "Os": "Osmium",
    "Ir": "Iridium",
    "Pt": "Platinum",
    "Au": "Gold",
    "Hg": "Mercury",
    "Tl": "Thallium",
    "Pb": "Lead",
    "Bi": "Bismuth",
    "Po": "Polonium",
    "At": "Astatine",
    "Rn": "Radon"
}

#first_n_elements = 0
#elements_in_quiz = 0

def get_random_elements(elements_dict, count, quiz_size):
    sub_elements = dict(list(elements_dict.items())[:count])
    return dict(random.sample(sub_elements.items(), quiz_size))

def export_quiz_to_file(elements_dict, count, quiz_size, filename="element_quiz.txt"):
    selected = get_random_elements(elements_dict, count, quiz_size)
    lines = []

    # Shuffle the selected items to randomize the order of questions
    selected_items = list(selected.items())
    random.shuffle(selected_items)

    lines.append("2nd Elements Quiz".center(50) + "\n")
    print("2nd Elements Quiz".center(50) + "\n")
    lines.append("Write the correct name or symbol for each item below.\n\n")
    print("Write the correct name or symbol for each item below.\n\n")

    # Split into two groups: 5 asking for symbols and 5 asking for names
    first_half = quiz_size // 2
    symbol_questions = selected_items[:first_half]  # First half will ask for symbol
    name_questions = selected_items[quiz_size - first_half:]    # Last half will ask for name

    # Find the name with the most number of characters
    longest_name_length = max(len(name) for name in elements.values())

    # Add symbol questions (give name, ask for symbol)
    for i, (symbol, name) in enumerate(symbol_questions, start=1):
        lines.append(f"{i:>2}. {'_' * 4} → {name:<{longest_name_length}}\n")
        print(f"{i:>2}. {'_' * 4} → {name:<{longest_name_length}}\n")
    # Add name questions (ask for name, give symbol)
    for i, (symbol, name) in enumerate(name_questions, start=quiz_size - first_half+1):
        lines.append(f"{i:>2}. {symbol:<2} → {'_' * 15}\n")
        print(f"{i:>2}. {symbol:<2} → {'_' * 15}\n")
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)

    print(f"Quiz exported to {filename}")


def main():
    while True:
        print("=" * 35)
        print("  Element Quiz Maker and Study Tool")
        print("=" * 35)
        print("Please choose an option:\n")
        print("1. Make a Quiz")
        print("2. Study the Elements")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            make_quiz()

        elif choice == '2':
            study_elements()
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

        #export_quiz_to_file(elements, first_n_elements)

def make_quiz():
    print("\n[Make a Quiz selected]")
    while True:
        try:
            first_n_elements = int(input("How many of the first elements would you like to be quizzed on? "))
            if first_n_elements <= 0:
                print("Please enter a positive number.")
            else:
                while True:
                    try:
                        elements_in_quiz = int(input('How many of the n elements do you want in your quiz? '))
                        if elements_in_quiz <= 0:
                            print('Please enter a positive number.')
                        elif elements_in_quiz > first_n_elements:
                            print(f"You can't quiz on more than {first_n_elements} elements.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid integer.")

                print(f"\nGenerating quiz for the first {first_n_elements} elements...\n")
                export_quiz_to_file(elements, first_n_elements, elements_in_quiz)
                input("Press Enter to continue...")
                break
        except ValueError:
            print("Please enter a valid integer.")
    #return n

def study_elements():
    print("\n[Study the Elements selected]")

    element_list = list(elements.items())

    while True:
        # Get range from user
        while True:
            try:
                start = int(input("Enter the starting element number (e.g., 1 for Hydrogen): "))
                end = int(input("Enter the ending element number (e.g., 10 for Neon): "))
                if start < 1 or end > len(element_list) or start > end:
                    print(f"Please choose numbers between 1 and {len(element_list)}, with start ≤ end.")
                else:
                    break
            except ValueError:
                print("Please enter valid integers.")

        selected_elements = element_list[start - 1:end]
        print(f"\nStudying elements {start} to {end}...\n")

        # Pass 1: Symbol → Name
        print("🔁 Symbol → Name Practice:\n")
        for symbol, name in selected_elements:
            answer = input(f"What is the name: '{symbol}'? ").strip()
            if answer.lower() == name.lower():
                print(' ' *35 + " ✅ Correct!\n")
            else:
                print(' ' *35 + f"❌ Oops! The correct answer is: {name}\n")

        # Pass 2: Name → Symbol
        print("🔁 Name → Symbol Practice:\n")
        for symbol, name in selected_elements:
            answer = input(f"What is the symbol '{name}'? ").strip()
            if answer.lower() == symbol.lower():
                print(' ' *35 + "✅ Correct!\n")
            else:
                print(' ' *35 + f"❌ Oops! The correct answer is: {symbol}\n")

        cont = input("Would you like to study another set of elements? (y/n): ").strip().lower()
        if cont != 'y':
            break


if __name__ == "__main__":
    main()


