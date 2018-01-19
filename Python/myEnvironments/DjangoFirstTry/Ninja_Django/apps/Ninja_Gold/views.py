from __future__ import unicode_literals
from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

def index(request):
    # clear out session or hard code it
    #request.session.flush() #clears session

    # establish session variables here
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activity'] = [] # what do?

    return render(request, 'Ninja_Gold/index.html')

def reset(request):
    request.session.flush()
    return redirect('/')

def process(request):
    # determine where it came from
    activity = request.POST['activity']

    # reset the result
    result = ''

    # if farm clicked do a thing
    if activity == 'farm':
        # does it work?
        print "we visited the farm, check"

        # generate random gold from farm value
        gold = randint(10, 21)
        print gold

        #send gold to session, then increment session gold
        request.session['gold'] += gold
        print request.session['gold']
    
        # 
        result = {
            'color': 'green',
            'content':'you visited the farm and earned {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
        }
    
    if activity == 'cave':
        # does it work?
        print "we visited the cave, check"

        # generate random gold from cave value
        gold = randint(2, 11)
        print gold

        #send gold to session, then increment session gold
        request.session['gold'] += gold
    
        # 
        result = {
            'color': 'green',
            'content':'you visited the cave and earned {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
        }
    
    if activity == 'house':
        # does it work?
        print "we visited the house, check"

        # generate random gold from house value
        gold = randint(2, 6)
        print gold

        #send gold to session, then increment session gold
        request.session['gold'] += gold
        result = {
            'color': 'green',
            'content':'you visited the house and earned {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
        }
    
    if activity == 'casino':
        # does it work?
        print "we visited the casino, check"

        # generate random gold from casino value
        gold = randint(-50, 51)
        print gold, 'from casino'

        #send gold to session, then increment session gold
        request.session['gold'] += gold
    
        # 
        if gold <= 0:
            result = {
                'color': 'red',
                'content': 'you visited the casino and lost {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
            }   
        else:
            result = {
                'color': 'green',
                'content':'you visited the house and earned {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
            }

    # post to activity log - this lives in session, then append it to the top of items
    request.session['activity'].append(result)

    """
    def gamble(activity, ""):
        #send gold to session, then increment session gold
        request.session['gold'] += gold

        if gold <= 0:
            result = {
                'color': 'red',
                'content': 'you visited the casino and lost {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
            }   
        else:
            result = {
                'color': 'green',
                'content':'you visited the house and earned {} gold at {}'.format(gold, datetime.now().strftime("%Y-%m-%D %H:%M"))
            }

        return result
    """

    return redirect('/')
