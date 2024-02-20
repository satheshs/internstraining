#question 1
#letter count
def letter_count(sentence):
    count = {}
    for i in sentence.upper():
        if i != ' ':
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    return count
question1 = letter_count("heLlo world")
print("QUESTION 1")
for i, count in question1.items():
    print(f"{i} - {count}")
print('\n')


#question 2
#remove dupicates
def rem_dupe(sentence):
    words = sentence.split()
    unique_word = []
    for word in words:
        if word not in unique_word:
            unique_word.append(word)
        else:
            continue
    return " ".join(unique_word)
print("QUESTION 2")
print(rem_dupe("ONE TWO ONE THREE TWO FOUR THREE"))
print('\n')


#question 3
#upper and lower case //python = PyThOn
def alter_case(word):
    result = ""
    for i, char in enumerate(word):
        if i%2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result
# return " ".join([char.upper() if i%2 == 0 else char.lower() for i, char in enumerate(word)]
print("QUESTION 3")
print(alter_case("hello world"))
print('\n')


#question 4
#No of capital letters
def capital_count(word):
    count = 0
    for i in word:
        if i.isupper():
            count +=1
    return count
print("QUESTION 4")
print(capital_count("PyThON"))
print('\n')


#question 5
#reverse each word in a sentence
def reverse_word(sentence):
    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence
reversed_sent = reverse_word("Once in a blue moon")
print("QUESTION 5")
print(reversed_sent)
print('\n')