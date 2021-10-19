market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
 
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    return stoplight
stoplight = switchLights(market_2nd)
switchLights(market_2nd)
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
print ('It worked! One light is red! ' + str(stoplight))