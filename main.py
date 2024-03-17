
path_to_file = 'books/frankenstein.txt'

def main():
  print(f"--- Begin report of {path_to_file} ---")
  text = get_book_text(path_to_file)
  num_words = get_num_words(text)
  print(f"{num_words} words found in the document\n")
  
  chars_dict = get_chars_dict(text)
  sorted = get_alpha_and_sort(chars_dict)
  for dict in sorted:
    print(f"The '{dict['letter']}' character was found {dict['count']} times")
  
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_chars_dict(text):
  letter_count = {}

  for letter in text:
    char = letter.lower()
    if (char in letter_count):
      letter_count[char] += 1
    else:
      letter_count[char] = 1

  return letter_count

def get_alpha_and_sort(dict):
  def by_count_and_decending(d):
    return d["count"] * -1
  
  unsorted = []
  for key in dict:
    if (key.isalpha()):
      unsorted.append({'letter': key, 'count': dict[key]})
  
  unsorted.sort(key=by_count_and_decending)
  return unsorted

main()