from word_list import words
import csv


def export_to_csv(data, filename):
  """
  """
  with open('%s.csv' % filename, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["word", "count"])                                               
    writer.writeheader()
    writer.writerows(data)

  print('[export_to_csv] done writing to csv')



def main():

    print("Counting number of letters in %d words" % len(words))
    alphabet_count = {}
    for word in words:
        for letter in word:
            if letter not in alphabet_count.keys():
                alphabet_count[letter] = 1
            alphabet_count[letter] = alphabet_count[letter] + 1


    print("Calculator word score based on letter frequencies")
    words_letter_score = {}
    for word in words:
        score = 0
        unique_letters = set(word)
        for letter in unique_letters:
            score = score + alphabet_count[letter]
        words_letter_score[word] = score

    words_letter_score_sorted = dict(sorted(words_letter_score.items(), key = lambda item: item[1]))
    words_score_csv = []
    for word in words_letter_score_sorted:
        words_score_csv.append({ 'word': word, 'count': words_letter_score_sorted[word] })

    export_to_csv(words_score_csv, "word_score")

if __name__ == "__main__":
    main()