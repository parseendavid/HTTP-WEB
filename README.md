### World Bank Country Profile Extractor.
* This console app helps get a simple profile of a country from The World Bank
### Requirements
* Python 3
* requests==2.18.4

### Features

* Take an iso2code of a country and returns a profile containing the following information.
    for the code `ke`
    ```shell
        Country Name: Kenya
        Country's Capital: Nairobi
        Country's Region: Sub-Saharan Africa (excluding high income)
        Country's Income Level: Lower middle income
        Longitude: 36.8126
        Latitude: -1.27975
        Iso2code: KE
    ```


### Local Installation

1. Clone this repository

	` git clone https://github.com/parseendavid/HTTP-WEB.git`

2. cd into the repo
    
    `cd <repo_name>`
3. Create a virtual environment if you want one
	
	`virtualenv <name_for_your_environment>`
4. Install requirements either to a virtual environment or to python
    	
	`pip install -r requirements.txt`
###  Usage
1. In console:
    * Start your virtual environment if you have one
    * Run `Python3 world_bank_country_profile.py`