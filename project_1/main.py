# I wanted to play around and create a smarter chatbot response system. I used inspiration from a couple of 
# youtube videos for functions (message probability) and came up with a couple response outcomes

import re #import regex
import long_input as long_input #import responses file

# takes in input message, makes probability calculations based on words seen while iterating
def interp_message(input_message, familiar_words, single_response=False, required_words=[])
    message_expect = 0
    includes_required_words = True

    #loops through and checks if user input words are in list of familiar words, if yes then we
    # will increment message_expect value
    for word in input_message:
        if word in familiar_words:
            message_expect +=1

    #check for required words
    for word in required_words:
        if word not in user_message:
            includes_required_words = False;
            break;

    #calculates percentage of words that are familiar then converts it to a whole number
    if includes_required_words or single_response:
        return int(float(message_expect)/float(len(famiar_words))*100)
    else:
        return 0; #no match

    def iterate_messages(message):
        highest_prob_list = {}
        #adds items to dictionary
        def response(chattybot_response, word_list, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            #create a key at the index of the bot response
            highest_prob_list[chattybot_response] = message_expect(message, word_list, required_words)
        #
        #response key!  (response, [expected user input])
        response('Hello there!'['hello', 'hi', 'whats good','hey'], single_response=True) #not sure how efficient this is
        response('This is ARTG5000! Welcome'['what','class','is','this'], required_words=['what','class'] #required words to make sure they are asking about what class
        
        
        match = max(highest_prob_list, key=highest_prob_list.get)

        #utilize long_input function that returns response everytime there is unknown user input
        return long_input.unknown() if highest_prob_list[match] < 1 else match



# gets user response, splits input into an array so we can analyze each word 
# seperately and output the most appropriate response
def get_response(user_input):
    #ignores extra symbols found in text
    decode_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower)
    response = iterate_messages(decode_message)
    return response

while True:
    print('ChattyBot' + get_response(input("You: ")))