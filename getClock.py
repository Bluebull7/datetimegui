# GET CLOCK FOR GUi

from world-time-api import services as serv

myclient = serv.client('timezone')
requests = {"area":"America","location":"New York"}
