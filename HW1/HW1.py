# Paragon National Group Winter 2023
# Computer Science Track
# HW1

# Assigned: Jan 8, 2022
# Due: Jan 15, 2022 11:59pm

# This is the first programming assignment of the computer science track.
# The questions will cover the topics learned in the first lecture, which entailed
# variables, basic operations, arrays, and dictionaries.

# This function prints out a sentence saying "Welcome to the start of the PNG CS
# track"
def print_welcome_message():
    #TODO
    return

# This function takes the number of cents as an argument and prints the best 
# combination of quarters, dimes, nickels, and pennies in descending order of
# importance (i.e. 25 cents can be split into 25 pennies, but quarters is more
# important, thus it would be split into 1 quarter). Assume that the argument given
# is non-negative.
# Ex) split_change(1) -> 0 quarters, 0 dimes, 0 nickels, 1 penny
#     split_change(20) -> 0 quarters, 2 dimes, 0 nickels, 0 pennies
#     split_change(67) -> 2 quarters, 1 dime, 1 nickel, 2 pennies 
def split_change(cents):
    #TODO
    return

# This function takes an array of strings of finite length (the strings can only 
# either be 'H', 'h', 'T' or 't') as arguments and returns the number of heads 
# as an integer. Assume that no other strings can be inputted other than those 
# four types.
# Ex) number_of_heads(['H', 'h', 'H', 'H', 'h', 'h', 'H']) -> 7
#     number_of_heads(['H', 'T', 'H', 't']) -> 2
#     number_of_heads([]) -> 0
def number_of_heads(coin_array):
    #TODO
    return

# This function takes two dictionaries and returns a single merged dictionary.
# If there is a repeated key in both dictionaries, then set the value of that
# key in the merged dictionary as the value for that key in dict1
# Ex) merge_dictionaries({}, {})
#       -> {}
#     merge_dictionaries({'PNG': 'Winter'}, {'CS': 'Winter'})
#       -> {'PNG': 'Winter', 'CS': 'Winter'}
#     merge_dictionaries({'PNG': 'Winter'}, {'PNG': 'Fall'})
#       -> {'PNG': 'Winter'}
#     merge_dictionaries({'PNG': 'Winter', 'CS': 'Fall'}, {'Quant': 'Spring'})
#       -> {'PNG': 'Winter', 'CS': 'Fall', 'Quant': 'Spring'}
def merge_dictionaries(dict1, dict2):
    #TODO
    return