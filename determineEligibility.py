def determineEligibilty_toGraduate(name,credits,gpa,satScore):
    if credits >= 24 and gpa >= 2.5 and satScore >= 800:
        print(f"{name} is eligible to graduate")
    else:
        print(f"{name} is not eligible to graduate")

def listOfMovies(name, price, genre):
    print(f"{name} is a {genre} movie and costs ${price}")
    if genre == "comedy":
        print("You will laugh a lot")
    elif genre == "horror":
        print("you will be scared")
    else:
        print("You will be entertained")