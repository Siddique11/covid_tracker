from django.shortcuts import render


# Create your views here.


def home(request):
    import json
    import requests

    api_request = requests.get("https://coronavirus-19-api.herokuapp.com/all")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, "home.html", {"api": api})


def bd(request):
    import json
    import requests

    api_request = requests.get(
        "https://coronavirus-19-api.herokuapp.com/countries/Bangladesh")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, "bd.html", {"api": api})


def countries(request):
    import json
    import requests
    # api_request = requests.get(
    #     "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F13B331E-B5CB-4945-9EB3-A7E3ECCF6A95")

    api_request = requests.get(
        "https://coronavirus-19-api.herokuapp.com/countries")

    load_api = []

    try:
        api = json.loads(api_request.content)
        for i in range(len(api)):
            load_api.append(api[i])

    except Exception as e:
        api = "Error..."
    #

    return render(request, "countries.html", {'load_api': load_api, 'api': api})


def about(request):
    return render(request, "about.html")
