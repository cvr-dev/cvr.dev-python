#!/usr/bin/env python

import cvr

client = cvr.Client(api_key='your api key')
client.test_api_key()

for virksomhed in client.cvr.virksomheder(cvr_numre=[10103940]):
    print('Found virksomhed', virksomhed.cvr_nummer)

for penhed in client.cvr.produktionsenheder(p_numre=[1003388394]):
    print('Found penhed', penhed.p_nummer)
