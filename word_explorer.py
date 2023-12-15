import random

# Dictionary of words and their definitions
grade2_words = {
    'apple': 'A red or green fruit that is round and crunchy.',
    'bread': 'Food made from flour and water, often sliced for eating.',
    'chair': 'A piece of furniture to sit on with a back and four legs.',
    'dream': 'A story in your mind while you are sleeping.',
    'earth': 'The planet we live on, the third from the sun.',
    'fairy': 'A tiny, magical, make-believe being with wings.',
    'grape': 'A small, juicy fruit used to make juice or wine.',
    'house': 'A place where people live, often with a family.',
    'igloo': 'A round house made of ice and snow, built by Inuit people.',
    'jelly': 'A sweet, wobbly food made from sugar and fruit juice.',
    'kite': 'A toy that flies in the air, tied to a string.',
    'lemon': 'A sour, yellow fruit used in food and drinks.',
    'mango': 'A sweet, juicy, tropical fruit with a pit.',
    'night': 'The time when it is dark, and most people sleep.',
    'ocean': 'A very large area of salt water, bigger than a sea.',
    'piano': 'A large musical instrument with black and white keys.',
    'queen': 'The female ruler of a country, or in a deck of cards.',
    'river': 'A long, flowing body of water that goes to the sea.',
    'sheep': 'A farm animal with wool, that gives us meat and milk.',
    'train': 'A series of connected cars that run on tracks.',
    'umbra': 'The darkest part of a shadow during an eclipse.',
    'viola': 'A musical instrument like a small violin.',
    'whale': 'A very big sea animal that breathes air through a hole.',
    'x-ray': 'A picture of the bones inside your body.',
    'zebra': 'An African wild animal like a horse with black and white stripes.'
}


def get_random_word_and_clue(word_dict):
    """Randomly select a word and its clue from the dictionary."""
    word, clue = random.choice(list(word_dict.items()))
    return word, clue

def main():
    while True:
        word, clue = get_random_word_and_clue(grade2_words)

        print("\nNew Word! Can you guess it?")
        print(f"Clue: {clue}")

        attempts = 3
        while attempts > 0:
            guess = input(f"Guess the word ({attempts} attempts left): ").lower()
            if guess == word:
                print("Correct! You guessed the word.")
                break
            else:
                print("Incorrect, try again.")
                attempts -= 1

        if attempts == 0:
            print(f"Sorry, the correct word was '{word}'.")

        # Ask if the player wants to continue playing
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
