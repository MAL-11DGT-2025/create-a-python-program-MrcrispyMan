Bible = input("What is the first book of the Bible? ").strip()  # This asks the user and strips extra spaces.

# Corrected list of books.
Bible_list = ["Genesis", "Exodus", "Numbers", "Leviticus"]  

# Corrected print statement to show the options.
print("Genesis, Exodus, Numbers, Leviticus")  

# Check if the input matches the correct answer.
if Bible.capitalize() == "Genesis":  # We capitalize the input to account for cases where the user might type "genesis" or "GENESIS".
    print("You're right!")
else:
    print("That is not a Bible thing. ")
# test