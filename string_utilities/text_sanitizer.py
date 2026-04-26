# Project: Dynamic Content Filter
# Author: Daniel Kehinde

def clean_text(original_text, blacklist):
    # This loop checks every "bad" word in our list
    for word in blacklist:
        if word in original_text:
            # Automating the mask length based on the word
            mask = "*" * len(word)
            original_text = original_text.replace(word, mask)
    
    return original_text

# --- Running the code below ---

# 1. Get the sentence from the user
user_sentence = input("Enter a sentence to check: ").lower()

# 2. Define the words to hide
forbidden_words = ["ass", "idiot", "badword","fuck","stupid"] 

# 3. Use the function and store the result
cleaned_result = clean_text(user_sentence, forbidden_words)

# 4. Show the final result
print("-" * 20)
print("Sanitized Output:")
print(cleaned_result)

