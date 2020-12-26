import json
from difflib import get_close_matches
# imported data
data = json.load(open("data.json"))

# translate is not a good function name
def translate (w): 
# functions convert to a lower string always
    w=w.lower()
# conditionals
    if w in data:
        return data[w]
        # check if input is correct to keys available sequence matcher
    elif len(get_close_matches(w, data.keys())) > 0:
        # user input if wrong program provides suggestions, store in input in variable(yn) to compare
        yn= input("Did you mean %s instead? Enter Y if Yes, N if No" % get_close_matches(w, data.keys())[0])
        if yn =="Y":
            return get_close_matches(w, data.keys())[0]
            # condition if suggested words by program are not what the user intended
        elif yn =="N":
            return "The word does'nt exist"
            # end statemnt if words suggested by program are not what the user wanted
        else:
            return "We did not understand your query"
    else:
        return "The word does not exist"
        # when user enters a word that does not exist

word = input ("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)