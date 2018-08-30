# TTL255.com - PyTips
#
# PyTips 2 - Use itertools.product to replace nested loops

import itertools
from pprint import pprint

#
# Example 1
#

#
# Setup
#


def get_pfxs(region, role):
    prefixes = {
        'as': {
            'data': ['10.1.2.0/25', '10.1.3.0/25'],
            'voice': ['10.1.2.128/25', '10.1.3.128/25'],
        },
        'eu': {
            'data': ['10.2.6.0/25', '10.2.7.0/25'],
            'voice': ['10.2.6.128/25', '10.2.7.128/25'],
        },
        'na': {
            'data': ['10.3.11.0/25', '10.3.11.0/25'],
            'voice': ['10.3.12.128/25', '10.3.12.128/25'],
        }
    }
    return prefixes[region][role]


regions = ['as', 'eu', 'na']
pfx_roles = ['data', 'voice']

#
# Function call inside of nested loop
#
print('{:->35}'.format(''))
print('Function call inside of nested loop')
print('{:->35}\n'.format(''))
pfx_list = []
for region in regions:
    for role in pfx_roles:
        pfx_list.extend(get_pfxs(region=region, role=role))
pprint(pfx_list)

#
# Function call with loop and itertools.product
#
print('\n{:->45}'.format(''))
print('Function call with loop and itertools.product')
print('{:->45}\n'.format(''))
pfx_list = []
for region, role in itertools.product(regions, pfx_roles):
    pfx_list.extend(get_pfxs(region=region, role=role))
pprint(pfx_list)


#
# Example 2
#

#
# Setup
#
iata_cc = ['bai', 'mex', 'tyo', ]
dev_types = ['switch', 'router']
dev_roles = ['core', 'edge']

#
# Device name generation with nested loops
#
print('\n{:->40}'.format(''))
print('Device name generation with nested loops')
print('{:->40}\n'.format(''))
for cc in iata_cc:
    for dev_t in dev_types:
        for dev_r in dev_roles:
            for dev_id in range(1, 3):
                print('{cc}-{dev_t}-{dev_r}-{dev_id}'.
                      format(cc=cc, dev_t=dev_t, dev_r=dev_r, dev_id=dev_id))

#
# Device name generation with itertools.product
#
print('\n{:->45}'.format(''))
print('Device name generation with itertools.product')
print('{:->45}\n'.format(''))
for cc, dev_t, dev_r, dev_id in itertools.product(iata_cc, dev_types, dev_roles, range(1, 3)):
    print('{cc}-{dev_t}-{dev_r}-{dev_id}'.
          format(cc=cc, dev_t=dev_t, dev_r=dev_r, dev_id=dev_id))
