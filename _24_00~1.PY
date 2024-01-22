
import pandas as pd

phonetic_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(phonetic_alphabet)

#converts from csv to dict: (use Pandas, not importing csv)
phonetic_alphabet_dictionary = phonetic_alphabet_data.to_dict()

# TODO: Dictionary Comprehension:
# "select row of letter and row of code, and for the index and rows in the dictionary, iterate through them, assigning the new letter and new code as the new columns header names.
phonetic_alphabet_dictionary = {row["letter"]: row["code"] for (index, row) in phonetic_alphabet_data.iterrows()}    # OR new_key = {row.letter: and new_value = row.code ... (letter: code should be the format of the NEW dict to mimis: "A: Alpha" -  for (index, row) we are going to do something with it. We want to iterate through the rows.
print(f"phonetic_alphabet_dictionary = {phonetic_alphabet_dictionary}")


user_typed_word = input("Type a word (without spaces):\n").upper()
# for each_letter in user_typed_word:  (this code works, BUT it's not List Comprehension)
    # print(each_letter)
    # print(f"The value of key {each_letter} from the dict is: ", phonetic_alphabet_dictionary.get(each_letter))    #gets the value of the letter that was typed by user, matches the row that that value is on, and returns the Value word.

# But use this Format: (for List Comprehension)
# [new_item for item in list (optional: if testpasses])
#each_letter form the for loop a few lines above, it replaced by letter (variable from earlier in the code)

# TODO: List Comprehension code:                                                                                                                                         # answer: new_list = [phonetic_alphabet_dictionary[letter] for letter in user_typed_word]
new_list = [phonetic_alphabet_dictionary[letter] for letter in user_typed_word]
print(new_list)






# new_dictionary = {letter: code for (letter, code) in phonetic_alphabet_dictionary}
# print(new_dictionary)

# new_dictionary = {letter: code for (row.letter, row.code) in phonetic_alphabet.iterrows()}
# print(new_dictionary)

# Original:
# for (letter, code) in phonetic_alphabet.iterrows():
# for (index, row) in phonetic_alphabet.iterrows():
#     print(f"index = {index}\n")
#
#     print(f"row = {row}\n")
#
#
# user_typed_word = input("Type a word:\n")
# for each_letter in user_typed_word:
#     print(each_letter)


    # print(f"row.student = {row.student}\n")  # each of these rows is going to be a Pandas Series object.
    # print(f"row.score = {row.score}\n")

###############


# for (index, row) in student_data_frame.iterrows():
#     print(f"row = {row}\n")
#     print(f"index = {index}\n")
#     print(f"row.student = {row.student}\n")  #each of these rows is going to be a Pandas Series object.
#     print(f"row.score = {row.score}\n")
#     if row.student == "Angela":    #since each of these rows is going to be a Pandas Series object, we can utilize the . functionality with "row.student" and also...
#         print(f"if Angela, row.score = {row.score}\n")