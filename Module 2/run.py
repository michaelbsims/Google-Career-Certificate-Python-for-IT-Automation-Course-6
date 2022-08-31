#! /usr/bin/env python3
#module 2, html

import os
import requests

feedbackdir = '/data/feedback'
for file in os.listdir(feedbackdir):
    format = ['title', 'name', 'date', 'feedback']
    feedbackcontent = {}
    with open('{}/{}'.format(feedbackdir, file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace('\n', '')
            counter[format[counter]] = line.strip('\n')
            counter += 1
    response = requests.post("http://###/feedback/",json = content)
    if response.status_code != 201
        raise exception("Post failed | Satus code: {} | File: {}"".format(response.status_code, file))
    print("Feedback successfully posted")
