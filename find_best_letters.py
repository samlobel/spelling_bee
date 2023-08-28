

def get_word_set():
    # Also filter out words that use more than 7 unique letters.
    with open('good_word_list.txt', 'r') as f:
    # with open('long_english_words.txt', 'r') as f:
        words = f.readlines()
    words = [word.strip() for word in words]
    words = [w for w in words if len(set(w)) <= 7]
    words = [w for w in words if w.isalpha()]
    words = [w.lower() for w in words]
    return set(words)

WORDS = get_word_set()
# print(WORDS)
    

def validate_word(word, letters, center_letter):
    # Only letters, more than 4 letters, only letters in letters, and has center letter.
    if not word.isalpha():
        return False
    if len(word) < 4:
        return False

    word_set = set(word)
    if center_letter not in word_set:
        return False
    if not word_set.issubset(letters):
        return False
        
    return True

def score_valid_word(word):
    # https://www.nytimes.com/2021/07/26/crosswords/spelling-bee-forum-introduction.html#:~:text=Four%2Dletter%20words%20are%20worth,every%20letter%20at%20least%20once.
    # If 4 letters, 1. If more, 1 point per letter. If all (7) letters, 7 point bonus
    if len(word) == 4:
        return 1
    score = len(word)
    if len(set(word)) == 7:
        score += 7
    return score

def get_valid_words(letters, center_letter, all_words=WORDS):
    valid_words = [w for w in all_words if validate_word(w, letters, center_letter)]
    return valid_words

def get_total_score(letters, center_letter, all_words=WORDS):
    valid_words = get_valid_words(letters, center_letter, all_words)
    return sum(score_valid_word(w) for w in valid_words)


def print_words_and_total_score(letters, center_letter, all_words=WORDS):
    valid_words = get_valid_words(letters, center_letter, all_words)
    valid_words_with_score = [(score_valid_word(w), w) for w in valid_words]
    for vw in reversed(sorted(valid_words_with_score)):
        print(vw[1])
    print(get_total_score(letters, center_letter))



def get_best_center_letter_and_score(letters):
    letters = list(letters)
    letters_and_scores = [(get_total_score(letters, l), l) for l in letters]
    return max(letters_and_scores) # Returns (score, letter)


def get_best_set_of_seven_letters():
    letters = "abcdefghijklmnopqrstuvwxyz"
    while len(letters) > 7:
        best_score_so_far = -1
        letter_to_remove = None
        for l in letters:
            print('test out removing letter:', l)
            letters_without_l = letters.replace(l, "")
            score, best_center_letter = get_best_center_letter_and_score(letters_without_l)
            if score > best_score_so_far:
                best_score_so_far = score
                letter_to_remove = l
        print("Removing letter:", letter_to_remove)
        letters = letters.replace(letter_to_remove, "")
        best_center_letter = get_best_center_letter_and_score(letters)[1]
        print("Left with letters:", letters, "and center letter:", best_center_letter)
        print("Score of this one is ", best_score_so_far)
    
    print("Best set of 7 letters:", letters)
    print("Best center letter:", best_center_letter)











if __name__ == '__main__':
    # print_words_and_total_score("aeinrst", "e")
    get_best_set_of_seven_letters()