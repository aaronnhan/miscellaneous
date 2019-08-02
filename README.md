# miscellaneous

Greedy imperfect team selector based on people's preferences

Input data in people.txt. Format is:

Person liked_person1 ... liked_personx; disliked_person1 ... disliked_personx
Person2 ...                             ...
...

Change number of teams you want to make in NUM_GROUPS constant in groupcreator.py
Change the default value someone is given in NO_PICK_VAL in person.py (higher value means more disliked)
Change how much ranking is important by SQUARED_VAL_OFFSET in person.py (higher value means ranking is more important!)
