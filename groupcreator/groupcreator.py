from person import Person
from group import Group
my_list = []
NUM_GROUPS = 3
groups = []


with open("people.txt", "r") as f:
    for x in f:
        info = x.split(";")
        name_like_info = info[0].strip().split(" ")
        name = name_like_info[0]
        likes = name_like_info[1::]
        if len(info) > 1:
            dislikes = info[1].strip().split(" ")
        else:
            dislikes = []
        my_list.append(Person(name, likes, dislikes))
#Generates preliminary groups
num_people = len(my_list)
person_index = 0
offset = num_people % NUM_GROUPS
for x in range(NUM_GROUPS):
    current_group = []
    if offset == 0:
        for y in range(len(my_list)//NUM_GROUPS):
            current_group.append(my_list[person_index])
            person_index+=1
    else:
        for y in range((len(my_list)//NUM_GROUPS) + 1):
            current_group.append(my_list[person_index])
            person_index+=1
        offset -= 1
    groups.append(Group(current_group))
def swap(groups, good):
    continue_swapping = False
    for group in groups:
        for other_group in groups:
            if group != other_group:
                for person in group.my_people:
                    for other_person in other_group.my_people:
                        before_hatred = group.get_hatred() + other_group.get_hatred()
                        person.swap(other_person)
                        after_hatred = group.get_hatred() + other_group.get_hatred()
                        if good:
                            swap_bool = (after_hatred >= before_hatred)
                        else:
                            swap_bool = (before_hatred >= after_hatred)
                        if  swap_bool:
                            person.swap(other_person)
                        else:
                            continue_swapping = True
    if continue_swapping:
        swap(groups, good)


swap(groups, True)
for group in groups:
    for person in group.my_people:
        print(person.me)
    print("\n")

current_hatred = 0
possible_hatred = 0
for group in groups:
    current_hatred += group.get_hatred()
swap(groups, False)
for group in groups:
    possible_hatred += group.get_hatred()
print("\nHatred Meter: " + str(current_hatred / possible_hatred))
