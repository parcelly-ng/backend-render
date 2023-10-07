from string import Template
from .send_out import send
from session.main import update as update_session, add_order, check_order


messagebox = {
    'greetings': "Hello {},\n\
        \n\
I'm Paul, your personal logistics assistant. 🤖\n\
I'm here to make your shipping experience hassle-free. 📦\n\
\n\
Here's what I can help you with:\n\
\n\
📝 *Order*: Create a new shipment with ease.\n\
🚚 *Track*: Check the status of your existing orders.\n\
💰 *Wallet*: Manage and top up your account balance.\n\
\n\
If you ever need assistance or have questions, don't hesitate to reach out to our dedicated customer care team at +2347036669426. We're here to ensure your shipments go smoothly.\n\
\n\
How can I assist you today?",

    'lost': 'I didnt get your last message',

    'order': "To create a new order, simply type *'Order'* and provide the necessary details like pickup location, delivery address, and any special instructions.",

    'confirm_order': "Great! 🚀 You've just created a new order. Please review the following details and confirm:\n\
\n\
*Order Details:*\n\
{}\n\
\n\
If everything looks good, please type *'Confirm'* to proceed with this order. If you need to make any changes or have questions, simply type *'Edit'* then the correct info",

    'order_confirmed': "Order Confirmed and shared with our riders. \n\
Expect Riders and their Price offers soon"
}


def brain(message, session, number):

    if (('hello' in message.lower()) or ('hi' in message.lower())) and (session == 'A'):
        print('hello')
        greeting(number=number)
    elif ('order' in message.lower()) and (session == 'A'):
        order(number=number)
    elif ('order' in message.lower()) and (session == 'Order'):
        confirm_order(number=number, message=message)
    elif 'confirm' in message.lower() and session == 'Order':
        order_confirmed(number=number)

    else:
        lost(number=number)


def greeting(number, messagebox=messagebox):
    '''
    this is the first stage and hence the only thing happening here is greeting and the first main menu
    depending on their response they are taken to a differnt stage
    '''
    reply = messagebox['greetings'].format(number)

    send(number=number, message=reply)


def lost(number, messagebox=messagebox):
    '''
    this is the fall back message for when the bot doesnt understand what is been said
    '''
    reply = messagebox['lost']
    send(number=number, message=reply)


def order(number, messagebox=messagebox):
    update_session(number=number, session='Order')
    reply = messagebox['order']
    send(number=number, message=reply)


def confirm_order(number, message, messagebox=messagebox):
    add_order(number=number, order=message)
    reply = messagebox['confirm_order'].format(message)
    send(number=number, message=reply)


def order_confirmed(number, messagebox=messagebox):
    order = check_order(number)
    update_session(number=number, session='Confirmed')
    print('order sent')
    print(order)
    reply = messagebox['order_confirmed']
    send(number=number, message=reply)
