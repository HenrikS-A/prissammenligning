import requests

# Valgfrie argumenter (optional arguments) som har startverdien None
def hent_data(soek=None, sidetall=None, merke=None, sortering=None):
    url = "https://kassal.app/api/v1/products"

    parametere = {
        "search": soek,
        "page": sidetall,
        "size": 2,
        "brand": merke,
        "price_min": 15, # for at produktene skal ha data, flesteparten av produktene under 15kr har ikke data...
        "sort": sortering
    }

    authToken = "kl5WOZbtvjPcPpLLnKYABpyQ22DnWav7ORT4ARat"
    headers = {
            "Authorization": "Bearer " + authToken,
            "Content-Type": "application/json"
        }
  
    respons = requests.get(url, parametere, headers=headers)

    print(respons.status_code)
    data = respons.json()

    return data


def hent_data_ean(ean):

    url = f"https://kassal.app/api/v1/products/ean/{ean}" # Annen måte å legge inn parametere

    authToken = "kl5WOZbtvjPcPpLLnKYABpyQ22DnWav7ORT4ARat"
    headers = {
            "Authorization": "Bearer " + authToken,
            "Content-Type": "application/json"
        }
  
    respons = requests.get(url, headers=headers)

    print(respons.status_code)
    data = respons.json()

    return data


def hent_butikker(lat, lng, km=None):

    url = "https://kassal.app/api/v1/physical-stores"

    parametere = {
        "size": 10,
        "lat": lat,
        "lng": lng,
        "km": km
    }

    authToken = "kl5WOZbtvjPcPpLLnKYABpyQ22DnWav7ORT4ARat"
    headers = {
            "Authorization": "Bearer " + authToken,
            "Content-Type": "application/json"
        }
  
    respons = requests.get(url, parametere, headers=headers)

    print(respons.status_code)
    data = respons.json()

    return data







# Bruk dette for å lettere kunne lese printet data i json format:


## a = hent_api("Appelsin", sortering="price_desc")

## import json
## print(json.dumps(a, indent=4))
