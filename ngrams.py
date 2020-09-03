import random

def find_ngrams(text, order=1, ngrams = {}, lowerCase=False):
  for i in range(len(text) - order + 1):
    gram = text[i:i + order]
    if lowerCase:
      gram = gram.lower()

    try:
      next_letter = text[i + order]
      if lowerCase:
        next_letter = next_letter.lower()
    except:
      next_letter = ''


    if gram in ngrams:
      if next_letter in ngrams[gram]:
        ngrams[gram][next_letter] += 1
      else:
        ngrams[gram][next_letter] = 1
    else:
      ngrams[gram] = {}
      ngrams[gram][next_letter] = 1
      ngrams[gram]['total'] = 0

    ngrams[gram]['total'] += 1
  return ngrams

def pick_random_gram(ngrams):
  grams = list(ngrams.keys())
  index = random.randint(0, len(grams)) # picking a random index
  return grams[index]

def pick_random_letter(gram):
  '''
  Receives a dict containing key letters and frequencies and returns a random letter
  based on their frequencies.
  '''
  num = random.random() * gram['total']
  for letter in gram:
    if letter != 'total':
      num -= gram[letter]
      if num < 0:
        return letter

def generate_phrase(ngrams, seed, end=".", order=1):
  phrase = seed
  letter = pick_random_letter(ngrams[seed[-order:]])
  while letter != end:
    phrase += letter
    letter = pick_random_letter(ngrams[phrase[-order:]])
  phrase += end
  return phrase

def generate_text(ngrams, seed, end=200, order=1):
  phrase = seed
  letter = pick_random_letter(ngrams[seed])
  while len(phrase) < end:
    phrase += letter
    letter = pick_random_letter(ngrams[phrase[-order:]])
  phrase = generate_phrase(ngrams, phrase, order=order)
  return phrase