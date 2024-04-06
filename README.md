# tsoha-car_collection

Car collection sovelluksen ideana on käyttäjän mahdollistaminen luoda autotalleja, joihin hän voi lisätä autoja ja halutessaan poistaa niitä autotalleista eli kokoelmastaan.
Käyttäjä voi luoda uuden tunnuksen ja kirjautua omaan profiiliin.

Kirjautuneena käyttäjä voi hyödyntää seuraavia toimintoja:

- luoda uuden autotallin
- kirjautua ulos profiilistaan
- poistaa haluamansa autotallin kokoelmastaan (sen sisällä olevat autot myös poistuvat käyttäjältä)
- Avata autotallin, jolloin näkee siinä olevat autot
- Autotallin ollessa auki voi sinne lisätä autoja tai poistaa sieltä autoja


# Käynnistysohjeet
Taustavaatimukset:
- python3 ladattuna
- Pip (Python package manager)
- PostgreSQL ladattuna ja serveri on auki, ohjeita tietokannan käynnistykseen täältä -->  https://github.com/hy-tsoha/local-pg


Kloonaa repositorio omalle koneellesi

`git clone https://github.com/BorisBanchev/tsoha-car_collection.git`

Siirry oikeaan hakemistoon, johon repositorio kloonattiin

`cd tsoha-car_collection`

Luo .env ympäristö tiedosto seuraavilla muuttujilla:

`DATABASE_URL=<tietokannan-paikallinen-osoite>`  
`SECRET_KEY=<salainen-avain>`  

Käynnistä virtuaaliympäristö

`python3 -m venv venv`  
`source venv/bin/activate`

Asenna Flask koneellesi

`pip install flask`

Asenna sovelluksen riippuvuudet

`pip install -r requirements.txt`

Jos PostreSQL-tietokanta asennettuna onnistuneesti koneelle serveri avataan ennen sovelluksen käynnistystä

`start-pg.sh` 

Sovellus käyttää PostgreSQL-tietokantaa. Tietokannan skeema määritellään seuraavalla komennolla

`psql < schema.sql`  

Käynnistä sovellus

`flask run`  
