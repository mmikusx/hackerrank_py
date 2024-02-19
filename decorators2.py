import operator

def person_lister(f):
    def inner(people):
        age_ascending_list = sorted(people, key=lambda x: int(x[2]))

        for i in range(len(age_ascending_list) - 1):
            if int(age_ascending_list[i][2]) == int(age_ascending_list[i+1][2]) and people.index(age_ascending_list[i]) == people.index(age_ascending_list[i+1]):
                tmp = age_ascending_list[i][2]
                age_ascending_list[i][2] = age_ascending_list[i+1][2]
                age_ascending_list[i+1][2] = tmp

        list = []
        for person in age_ascending_list:
            if person[3] == "M":
                list.append("Mr. " + person[0] + " " + person[1])
            else:
                list.append("Ms. " + person[0] + " " + person[1])

        return list
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')