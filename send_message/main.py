from string import Template
from send_out import send


messagebox = {
    'greetings': "Hello {}, \n\
    My  name  is Paul the Bot  and  im here to help. \n\
    Here are the  following keywords to help you navigate and use me. \n\
    *Order* (this is to create a new order) \n\
    *Track* (this is to track old orders) \n\
    *Wallet* (this is to manage and topup your wallet) \n\
    If  you feel lost or have any questions pls reach out to our customercare @ 2347036669426 ",
    'lost':'I didnt get your last message'
}





def brain(message,session,number):
    if 'hello'or 'hi' in message.lower():
        greeting(number=number)
    elif session == 'A':
        greeting(number=number)
    else:
        pass
    


def greeting(number,messagebox=messagebox):
    '''
    this is the first stage and hence the only thing happening here is greeting and the first main menu
    depending on their response they are taken to a differnt stage
    '''
    reply=messagebox['greetings'].format(number)

    send(number=number, message=reply)


def lost(number,messagebox=messagebox):
    '''
    this is the fall back message for when the bot doesnt understand what is been said
    '''
    reply=messagebox['lost']
    send(number=number, message=reply)