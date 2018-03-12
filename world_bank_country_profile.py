import requests


def main():
    try:
        country_code = input("Please Enter iso2Code for Country: ").lower()
        # Gets country profile from WorldBank in json format(which is actually a lis of dictionaries
        response = requests.get(
            "http://api.worldbank.org/countries/{}?format=json".format(country_code)
            ).json()
        # return out country profile to console
        return ("""
                Country Name: {0}
                Country's Capital: {1}
                Country's Region: {2}
                Country's Income Level: {3}
                Longitude: {4}
                Latitude: {5}
                Iso2code: {6}
                """.format(
                    response[1][0]['name'],
                    response[1][0]['capitalCity'],
                    response[1][0]['adminregion']['value'],
                    response[1][0]['incomeLevel']['value'],
                    response[1][0]['longitude'],
                    response[1][0]['latitude'],
                    response[1][0]['iso2Code']
                )
        )
    except Exception as e:
        return ('*'*10 + "Please input a valid iso2Code for country" + '*'*10)

if __name__ == "__main__":
    print(main())