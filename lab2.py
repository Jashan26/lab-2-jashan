def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Jashanpreet Kaur", 
        "student_id": 10308695,
        "pizza_toppings": ["CHEESE", "ONIONS", "PEPPRONI"],
        "movies": [
            {"title": "evil dead", "genre": "horror"},
            {"title": "kgf", "genre": "action"}
    
        ]
    }
    # TODO: Step 3 - Add another movie to the data structure
    about_me["movies"].append({"title": "The Godfather", "genre": "horror"})
    
    #adding extra toppings to the data structure
    add_topping = ("olives", "garlic")

    add_pizza_toppings(about_me, add_topping)
    
    print_student_name_and_id(about_me)
    
    print_pizza_toppings(about_me)

    print_movie_titles(about_me)

    print_movie_genres(about_me)
    #print(about_me["movies"])
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = "Jashan"
    Student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me {first_name}.\nMy student ID is {Student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for i in toppings:
        about_me["pizza_toppings"].append(i)
    about_me["pizza_toppings"].sort()
    for topping in about_me["pizza_toppings"]:
        i.lower()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for l in about_me["pizza_toppings"]:
        print(l)  
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = (movie["genre"].title()for movie in about_me["movies"])
    print(f"I like to watch{", ".join(genres)} movies.\n")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    formated_titles = [movies["title"].title() for movies in about_me["movies"]]
    movie_list = ", ".join(formated_titles)
    print("Some of my favourite are", movie_list, "!")

    return
    
if __name__ == '__main__':
    main()