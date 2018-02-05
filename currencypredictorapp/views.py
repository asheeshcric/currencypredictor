from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
import datetime, requests, json
from decouple import config

def home(request):
    return render(request, 'index.html')

def layout(request):
    return render(request, 'layout.html')

def about(request):
    return render(request, 'about.html')

# Getting the Historical Data of a Currency

def getPrice(id):
    url = "https://min-api.cryptocompare.com/data/histoday"
    if id == 2:
        currency = 'ETH'
    elif id == 3:
        currency = 'LTC'
    elif id == 4:
        currency = 'DASH'
    else:
        currency = 'BTC'
    params = {
        'fsym': currency,
        'tsym': 'USD',
        'limit': '60',
        'aggregate': '3',
        'e': 'CCCAGG',
    }
    response = requests.get(url=url, params=params)
    # print(response.json())
    return response.json()

# View to return the data for plotting
class BitcoinPrices(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id):
        price_history = getPrice(id)
        price_data = price_history['Data']
        data = []
        labels = []
        for value in price_data:
            # print(value['y'])
            data.append(value['close'])
            labels.append(datetime.datetime.fromtimestamp(int(value['time'])).strftime('%Y-%m-%d %H:%M:%S'))
        context = {
            'labels': labels,
            'data': data,
        }
        # print(context)
        return Response(context)

class FutureBitcoinPrices(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id):
        price_history = getPrice(id)
        price_data = price_history['Data']

        # Making the data suitable for an API request to predict the prices:
        data = []
        for value in price_data:
            data.append(value['close'])
        data = data[-30:]
        data = str([data, len(data), 3])
        print("data = ", data)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': config('API_TOKEN'),
        }
        url = 'https://api.algorithmia.com/v1/algo/TimeSeries/Forecast/0.2.0'
        future_response = requests.post(url=url, headers=headers, data=data)
        print("future_response = ",future_response.text)

        fdata = []
        for value in future_response.json()['result']:
            fdata.append(value)
        print("fdata = ", fdata)
        today = datetime.datetime.today()
        flabels = [today + datetime.timedelta(days=x+3) for x in range(0, len(fdata))]
        print("flabels = ", flabels)
        context = {
            'labels': flabels,
            'data': fdata,
        }
        return Response(context)





