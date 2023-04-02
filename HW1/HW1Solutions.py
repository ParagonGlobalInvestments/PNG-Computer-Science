def print_welcome_message():
    print("Welcome to the start of the PNG CS track")

def split_change(cents):
    quarters = cents // 25
    cents -= quarters * 25
    dimes = cents // 10
    cents -= dimes * 10
    nickels = cents // 5
    cents -= nickels * 5
    pennies = cents

    print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")

def number_of_heads(coin_array):
    count = 0
    for coin in coin_array:
        if coin == 'H' or coin == 'h':
            count += 1
    return count

def merge_dictionaries(dict1, dict2):
    for key, value in dict2.items():
        if key not in dict1:
            dict1[key] = value
    return dict1