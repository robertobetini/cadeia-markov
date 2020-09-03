import ngrams as ng

def add_text(ngrams, path, order=1, lowerCase=False):
  file = open(path, encoding='utf-8')
  text = file.read()
  file.close()
  ngrams = ng.find_ngrams(text, order=order, ngrams=ngrams, lowerCase=lowerCase)

ngrams = {}
order = 6
add_text(ngrams, 'medicina.txt', order, False)
# add_text(ngrams, 'lei.txt', order, False)

print()
print('*************************************************************************************')
print('*************************************************************************************')
seed = ng.pick_random_gram(ngrams)
print(ng.generate_text(ngrams, seed, order=order, end=500))
print('*************************************************************************************')
print('*************************************************************************************')
print()

while True:
  answer = input('Digite pressione ENTER para gerar uma nova frase ou digite SAIR para fechar o programa. ')
  if answer.lower() == "sair":
    break

  print()
  print('*************************************************************************************')
  print('*************************************************************************************')
  seed = ng.pick_random_gram(ngrams)
  print(ng.generate_text(ngrams, seed, order=order, end=500))
  print('*************************************************************************************')
  print('*************************************************************************************')
  print()
