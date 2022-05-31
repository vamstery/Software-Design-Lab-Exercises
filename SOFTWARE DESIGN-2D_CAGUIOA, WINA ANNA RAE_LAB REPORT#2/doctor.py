
#This code is from the book Lambert, K. A. (2018). Fundamentals of Python: First Programs (2nd ed.). Cengage Learning and
#has been upgraded by the condition in the project with the help of the internet.



import random

history = []

hedges = ("Please tell me more.",
"Many of my patients tell me the same thing.",
"Please coninue.")

qualifiers = ("Why do you say that ",
"You seem to think that ",
"Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your",
"we":"you", "us":"you", "mine":"yours",
"you":"I", "your":"my", "yours":"mine"}

 

class Doctor:
    def __init__(self):
        pass
        
    def greeting(self):
        return "Good morning, I hope you are well today.\nWhat can I do for you?"
        
    def farewell(self):
        return "Have a nice day!"

    def reply(self,sentence):
       
        probability = random.randint(1, 5)
        if probability in (1, 2):
           
            answer = random.choice(hedges)
        elif probability == 3 and len(history) > 3:
            
            answer = "Earlier you said that " + \
            changePerson(random.choice(history))
        else:
        
            answer = random.choice(qualifiers) + changePerson(sentence)
     
        history.append(sentence)
        return answer

 

def changePerson(sentence):
  
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():

    doctor=Doctor()
    print(doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        print(doctor.reply(sentence))


if __name__ == "__main__":
    main()