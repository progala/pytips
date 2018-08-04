# TTL255.com - PyTips
#
# PyTips 1 - Get loop counter with enumerate()

#
# Setup
#
my_ip = '10.16.32.113'

my_ip_octets = my_ip.split('.')

#
# Looping over collection with helper variable.
#
ip_to_dec = 0
for i in range(len(my_ip_octets)):
    ip_to_dec += int(my_ip_octets[i]) * 256**i

print('{:<20}{:<20}'.format('Dotted-decimal', 'Decimal'))
print('{:<20}{:<20}'.format(my_ip, ip_to_dec))

#
# Looping over collection with helper variable.
#
ip_to_dec = 0
for i, octet in enumerate(my_ip_octets):
    ip_to_dec += int(octet) * 256**i

print('{:<20}{:<20}'.format('Dotted-decimal', 'Decimal'))
print('{:<20}{:<20}'.format(my_ip, ip_to_dec))

#
# Enumerate with counter starting from 1.
#
todo_list = [
    'Snooze alarm',
    'Reluctantly get up',
    'Check email',
    'Check Twitter',
    'Check Facebook',
    'Have coffee',
]

print('My TODO for today:')
for i, elem in enumerate(todo_list, start=1):
    print('{:>3}: {}'.format(i, elem))
