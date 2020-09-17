import random

def check_number_validity(message):
  while True:
    try:
      number = int(input(message))
      if type(number) == int:
        return number
    except ValueError:
      print("Veuillez entrer un nombre valide! 😣")


def greet():
  print("\nBienvenue dans le jeu de la fourchette ! 😁🍴\n")
  print("Vous devez deviner un nombre entre un minimum et un maximum ...")
  print("... c'est parti !\n")

  minimum = check_number_validity(message='Entrez un nombre minimum: ')
  maximum = check_number_validity(message="Et un nombre maximum: ")
  number_tries = 0

  if minimum > maximum:
    bad_min = minimum
    bad_max = maximum
    minimum = bad_max
    maximum = bad_min

  number_to_guess = random.randint(minimum, maximum)


  config = [
    minimum,
    maximum,
    number_tries,
    number_to_guess,
  ]

  return config


def play():
  minimum, maximum, number_tries, number_to_guess = greet()

  print(f"\nOk on y va !\n")

  while True:
    print(f"Le nombre à trouver se situe entre {minimum} et {maximum}")
    guess = check_number_validity('\n>>> Entrez un nombre: ')

    result = check_guess([minimum, maximum, number_tries, number_to_guess], guess)
    if not result:
      return
    else:
      minimum, maximum, number_tries, number_to_guess = result


def replay():
  replay = False
  while not replay:
    answer = input("On recommence ? O(ui)/N(on) 😏😉 \n")
    if answer.lower() == "N".lower() or answer.lower() == "Non".lower():
      return False
    elif answer.lower() == "O".lower() or answer.lower() == "Oui".lower():
      return True
    else:
      print("Je n'ai pas compris")


def check_guess(game_params, guess):
  minimum, maximum, number_tries, number_to_guess = game_params

  if guess < minimum or guess > maximum:
    print("/!\\ Oula ! C'est en dehors des limites ça ! On ne va pas compter cet essai 😁\n")
    return [
      minimum,
      maximum,
      number_tries,
      number_to_guess,
    ]

  number_tries += 1

  if guess == number_to_guess:
    print(f"\nBravo vous avez gagné en {number_tries} essais!\n")

    want_to_replay = replay()
    if (want_to_replay):
      minimum = int(input("Veuillez entrer un nombre minimum: "))
      maximum = int(input("Et un nombre maximum: "))
      number_tries = 0

      number_to_guess = random.randint(minimum, maximum)
    else:
      print("Merci d'avoir joué et à bientot ! 😁😁😁😁")
      return False

  elif guess > minimum and guess < number_to_guess:
    print("[+] C'est plus!\n")
    minimum = guess

  elif guess < maximum and guess > number_to_guess:
    print("[-] C'est moins!\n")
    maximum = guess

  return [
    minimum,
    maximum,
    number_tries,
    number_to_guess,
  ]


play()