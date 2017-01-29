def tempreature_birthdate():
    """        Author: Mohammed Salman
        Metropolia university of Applied Sciences
        Assignment 7: Internet
        29.01.2017
        How was the weather when you were born"""
    import requests
    req = requests.get('http://api.wunderground.com/api/aaf4fff332ac5aa0/history_19980806/q/CA/Kattakurgan.json')
    request_json = req.json()
    result = {}
    result['date'] = request_json['history']['date']['pretty']
    result['tempi'] = request_json['history']['observations'][0]['tempi']
    result['tempm'] = request_json['history']['observations'][0]['tempm']
    print("On {date} the high tempreture was {tempi} and the low tempreture was {tempm}.".format(**result))
tempreature_birthdate()
