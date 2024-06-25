#!/usr/bin/env python
# coding: utf-8

# In[73]:


'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

social_graph = {
        "@bongolpoc":{"first_name":"Joselito",
                      "last_name":"Olpoc",
                      "following":[
                      ]
        },
        "@joaquin":  {"first_name":"Joaquin",
                      "last_name":"Gonzales",
                      "following":[
                              "@chums","@jobenilagan"
                      ]
        },
        "@chums" : {"first_name":"Matthew",
                    "last_name":"Uy",
                    "following":[
                            "@bongolpoc","@miketan","@rudyang","@joeilagan"
                    ]
        },
        "@jobenilagan":{"first_name":"Joben",
                       "last_name":"Ilagan",
                       "following":[
                            "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
        },
        "@joeilagan":{"first_name":"Joe",
                      "last_name":"Ilagan",
                      "following":[
                            "@eeebeee","@jobenilagan","@chums"
                  ]
        },
        "@eeebeee":  {"first_name":"Elizabeth",
                      "last_name":"Ilagan",
                      "following":[
                            "@jobenilagan","@joeilagan"
                  ]
        },
    }

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #follower if to_member is in from_member's following
    follows = to_member in social_graph[from_member]["following"]

    #followed by if from_member is in to_member's following
    isfollowed = from_member in social_graph[to_member]["following"]

    if follows and isfollowed:
        return "friends"
        
    elif follows:
        return "follower"

    elif isfollowed:
        return "followed by"

    else:
        return "no relationship"
    
relationship_status("@chums", "@joaquin", social_graph)


# In[75]:


board1 = [
['O','X','X','O'],
['O','X','O','X'],
['','','O','X'],
['O','X','O','X']
]

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    size = len(board)

    # checks row
    for row in board:
        if all(symbol == row[0] and symbol for symbol in row):
            return row[0]

    # checks column
    # uses col index
    for col in range(size):
        if all(board[row][col] == board[0][col] and board[row][col] for row in range(size)):
            return board[0][col]

    # checks diagonal from top left
    # i is index
    if all(board[i][i] == board[0][0] and board[i][i] for i in range(size)):
        return board[0][0]

    # checks diagonal from top right
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[i][size - 1 - i] for i in range(size)):
        return board[0][size - 1]

    return "NO WINNER"

tic_tac_toe(board1)


# In[77]:


route_map = {
         ("upd","admu") : {"travel_time_mins" : 10},
         ("admu","dlsu") : {"travel_time_mins" : 35},
         ("dlsu","ust") : {"travel_time_mins": 55},
         ("ust","upd") : {"travel_time_mins" : 40}
    }
    
def eta(first_stop, second_stop, route_map):
    '''ETA.
    
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # list of stops
    stops = [key[0] for key in route_map.keys()]  
    stops.append(stops[0])
    # to complete the circular route

    current_stop = first_stop
    total_travel_time = 0

    while current_stop != second_stop:
        index = stops.index(current_stop)
        next_stop = stops[(index + 1) % len(stops)]

        if (current_stop, next_stop) in route_map:
            time = route_map[(current_stop, next_stop)]["travel_time_mins"]
            total_travel_time += time

        else:
            return "route not found"

        current_stop = next_stop

    return total_travel_time
    
eta("admu", "ust", route_map)


# In[ ]:




