import pickle

def save_data(data, filename):
    with open (filename, "wb") as file:
        pickle.dump(data, file)

def load_data(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

def main():
    user_input = input("Zadej číslice odděleně mezerou:")
    int_list = [int(item) for item in user_input.split()]

    filename = "data.pkl"

    save_data(int_list, filename)

    loaded_list = load_data(filename)

    print("Načtena data ze souboru:", loaded_list)

if __name__ == "__main__":
    main()