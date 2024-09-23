
from datetime import datetime
#Write class and imports here!




if __name__ == "__main__":
    #Don't modify the main program!
    messages=[]
    dateFormat='%d.%m.%Y'
    timeFormat='%d.%m.%Y %H:%M:%S'
    messages.append(SMSMessage('+35844123123', '+35840632123', datetime.strptime('02.11.2021 11:38:15', timeFormat), 'Kotiin ja heti'))
    messages.append(SMSMessage('+35844126783', '+358406334523', datetime.strptime('12.01.2021 23:45:34', timeFormat), 'Osta makkaraa'))
    messages.append(SMSMessage('+35845678533', '+3584007243', datetime.strptime('12.01.2021 22:33:44', timeFormat), 'I Love You!!'))
    messages.append(SMSMessage('+35844126783', '+358406334523', datetime.strptime('13.01.2021 00:55:01', timeFormat), 'Muistitko makkaran?!?!'))

    print('All messages:')
    for v in messages:
        print(v)

    print()
    dt=datetime.strptime('12.01.2021', dateFormat)
    todays_messages=SMSUtils.find_messages_dt(messages, dt)
    print(datetime.strftime(dt, '%d.%m.%Y'),'messages:')
    for v in todays_messages:
        print(v)
    
    print()
    sender='+35844126783'
    print('Sender', sender, 'messages:')
    SMSUtils.find_messages_sender(messages, sender)

