# JC's Day-Trip Generator
# every 'y' and 'n' have a path, have fun!

import random

destinations = ['Leisure World', 'Emerald City', 'Crayola Factory', 'Atlantis', 'Arrakis', 'Isla Nublar', 'Sunnydale, CA', 'Castle Rock', 'Whoville', 'Hell', 'Mt. Olympus', 'Sanctuary Hills', 'Elysium', 'Asphodel', 'Hollow Bastion', 'Traverse Town', 'Windhelm', 'Skyhold', 'Tevinter Imperium', 'Emprise du Lion']
restaurants = ['Pizza Planet', 'JJs Diner', 'The Double R Diner', 'Good Burger', 'The Pie Hole', 'Cheers', 'Bluths Original Frozen Banana Stand', 'The Frosty Palace', 'Cake Baby', 'The Winking Skeever', 'Tritons Tri-Tip', 'McDonalds', 'Krusty Burger', 'Lard Lad', 'Paunch Burger', 'Central Perk', 'The Frosty Place', 'Pollo Tropicale', 'Yum Mi', 'Barnacle Billys']
vehicles = ['catbus', 'magic schoolbus', 'hoverboard', 'broomstick', 'magic carpet', 'submarine', 'the Polar Express', 'the back of a dragon', 'the Millennium Falcon', 'Thomas the Tank Engine', 'Howls Moving Castle', 'high-speed monorail', 'tricycle', 'rollerblades', 'heelys', 'horseback', 'carraige', 'go-kart', 'rocket boots', 'interdimensional vessel']
activities = ['knitting class', 'basket weaving class', 'renaissance fair', 'puppet show', 'Von Trapp musical number', 'mani/pedi', 'Build-A-Bear workshop', 'stand-up comedy special', 'hot dog eating contest', 'ping pong tournement', 'trapeze show', 'puppy petting zoo', 'Museum of Single-Use Plastics', 'dumpster diving contest', 'drag show', 'drink and draw party', 'antique festival', 'wine tasting', 'hip-hop dance class', 'hot yoga session']
adjectives = ['breathtaking', 'tantalizing', 'mind-blowing', 'riveting', 'fascinating', 'enchanting', 'lively', 'fabulous', 'gorgeous', 'brown-cow stunning', 'sensational', 'showstopping', 'one-of-a-kind']
verbs = ['this time of year', 'these days', 'in the spring', 'when the cherry blossoms bloom', 'all year round', 'and very remote', 'with free wifi', 'and totally instagrammable']

#

def run_trip_gen():
    print("""
Thank you for choosing Miss Frizzle's Travel Service: 
Where the road ends, adventure begins!""")
    start_op = input('Are you ready for the trip of a lifetime? y/n : ')
    if start_op == 'y':
        get_dest()
    elif start_op == 'n':
        deny_trip()

def deny_trip():
    last_chance = input('Are you sure? y/n : ')
    if last_chance == 'y':
        print('Then get out of my office!')
    elif last_chance == 'n':
        tempt = input('Can I temp you with a trip to Atlantis? y/n : ')
        if tempt == 'y':
            get_dest.destination = destinations[3]
            get_rest()
        elif tempt == 'n':
            print("I'm calling the police!")

def adj_rand():
    adjective = random.choice(adjectives)
    return adjective

def verb_rand():
    verb = random.choice(verbs)
    return verb

def dest_rand():
    dest_rand_result = random.choice(destinations)
    return dest_rand_result

def food_rand():
    restaurant = random.choice(restaurants)
    return restaurant

def vehicle_rand():
    vehicle = random.choice(vehicles)
    return vehicle

def activity_rand():
    activity = random.choice(activities)
    return activity

def get_dest():
    get_dest.destination = dest_rand()
    dest_answer = input(f"{get_dest.destination} is truly a {adj_rand()} location {verb_rand()}. Does this interest you? y/n : ")
    if dest_answer == 'y':
        print(f"I've heard wonderful things about {get_dest.destination}! You have fine taste.")
        get_rest()
    elif dest_answer == 'n':
        print("Not a problem! Let's try something else.")
        get_dest()

def get_rest():
    get_rest.restaurant = food_rand()
    rest_choice = input(f"A fan favorite restaurant in {get_dest.destination} is {get_rest.restaurant}. Shall I get you a reservation? y/n : ")
    if rest_choice == 'y':
        print("You're gonna LOVE this place! Let's continue - ")
        get_vehicle()
    elif rest_choice == 'n':
        print("They only have 3 stars on yelp anyway...")
        get_rest()

def get_vehicle():
    get_vehicle.vehicle = vehicle_rand()
    vehicle_choice = input(f"The best way to {get_dest.destination} is by {get_vehicle.vehicle}. Does that work for you? y/n : ")
    if vehicle_choice == 'y':
        print("You'll be riding in style, that's for sure.")
        get_activity()
    elif vehicle_choice == 'n':
        print("No worries! I hear they're dangerous!")
        get_vehicle()

def get_activity():
    get_activity.activity = activity_rand()
    activity_choice = input(f"Let's plan something fun while you're there - how about a {get_activity.activity}? You interested? y/n : ")
    if activity_choice == 'y':
        print("How exciting, take pictures!")
        get_summary()
    elif activity_choice == 'n':
        print("It probably wouldn't have been that fun anyway, right?")
        get_activity()

def edit_itenerary():
    print("Which part would you like to change?")
    change_response = input("""
    Please enter one of the following options; 
    a) Destination
    b) Restaurant
    c) Transportation
    d) Activity.
    
    """)
    if change_response == 'a':
        edit_dest()
    elif change_response == 'b':
        edit_rest()
    elif change_response == 'c':
        edit_vehicle()
    elif change_response == 'd':
        edit_activity()
    else:
        get_summary()

def edit_dest():
    get_dest.destination = dest_rand()
    new_dest_response = input(f"You could visit {get_dest.destination} instead? y/n : ")
    if new_dest_response == 'y':
        print("Fantastic!")
        get_summary()
    elif new_dest_response == 'n':
        edit_dest()

def edit_rest():
    get_rest.restaurant = food_rand()
    new_rest_response = input(f"Would you rather eat at {get_rest.restaurant}? y/n : ")
    if new_rest_response == 'y':
        print("Stupendous!")
        get_summary()
    elif new_rest_response == 'n':
        edit_vehicle()

def edit_vehicle():
    get_vehicle.vehicle = vehicle_rand()
    new_vehicle_response = input(f"I hear {get_vehicle.vehicle} is great? y/n : ")
    if new_vehicle_response == 'y':
        print("Amazing!")
        get_summary()
    elif new_vehicle_response == 'n':
        edit_vehicle()

def edit_activity():
    get_activity.activity = activity_rand()
    new_activity_response = input(f"How about {get_activity.activity} instead? y/n : ")
    if new_activity_response == 'y':
        print("Glorious!")
        get_summary()
    elif new_activity_response == 'n':
        edit_dest()

def get_summary():
    print(f"""Let's review your itenerary:
    Destination: {get_dest.destination}
    Restaurant: {get_rest.restaurant}
    Transportation: {get_vehicle.vehicle}
    Activity: {get_activity.activity}""")
    final_answer = input("Are you excited about this trip? y/n : ")
    if final_answer == 'y':
        print(f"You are all set to go, my friend! Enjoy your trip, see you next time!")
    elif final_answer == 'n':
        edit_itenerary()
        
                

run_trip_gen()

# The generator above doesn't utilize paramaters as it should
# Below I tried using paramater more thoroughly to better understand, but still didn't quite get it - looking forward to seeing the solution!

#def get_rand_destination():
#    var1 = random.choice(destinations)
#    dest_result = get_dest_answer(var1) 
#    if dest_result == False:
#        get_rand_destination()
#        return dest_result
#    else:
#        return dest_result

#def get_dest_answer(var1):
#    answer_value = get_1st_input(var1)
#    if answer_value == False:
#        return answer_value
#    else:
#        return answer_value

#def get_1st_input(var1):
#    initial_dest_answer = input(f"Want to go to {var1}? y/n : ")
#    if initial_dest_answer == 'y':
#        return var1
#    elif initial_dest_answer == 'n':
#        rejection = False
#        return rejection


#def present_itenerary(var1): 
#    print(var1)
#    destination_select = confirm_iten()
#    if destination_select != var1:
#        present_itenerary(destination_select)
#    else:
#        return
    

#def confirm_iten():
#    iten_confirm = input("Would you like to confirm this reservation? y/n ")
#    if iten_confirm == 'y':
#        print("hooray!")
#    elif iten_confirm == 'n':
#        change_answer = input("Which item would you like to change? a/b/c/d : ")
#        if change_answer == 'a':
#            new_dest_value = get_rand_destination()
#        return new_dest_value

#def generator():
#   destination_select = get_rand_destination()
#   present_itenerary(destination_select)
   

#generator()