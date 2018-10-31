films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
    }

choice = input("What film would you like to watch?: ").strip().title()

if choice in films:
   #  pass  # tells python to just "move on"
    age = int(("How old are you?: ").strip())

    #  check user age
    
    if age >= films[choice][0]:
        print("Enjoy the film!")
        # check enough seats

        num_seats = films[choice][1]
        
        if films[choice][1] > 0:
            films[choice][1] = films[choice][1] - 1
            print("Enjoy the film")
        else:
            print("Sorry, we are sold out!")
        
    else:
        print("you are too young to see this film")
else:
    print("Film not included...")
