# tsoha-car_collection

Car collection sovelluksen ideana on käyttäjän mahdollistaminen luoda autotalleja, joihin hän voi lisätä autoja ja halutessaan poistaa niitä autotalleista eli kokoelmastaan.
Käyttäjä voi luoda uuden tunnuksen ja kirjautua omaan profiiliin.

Kirjautuneena käyttäjä voi hyödyntää seuraavia toimintoja:

- luoda uuden autotallin
- kirjautua ulos profiilistaan
- poistaa haluamansa autotallin kokoelmastaan (sen sisällä olevat autot myös poistuvat käyttäjältä)
- Avata autotallin, jolloin näkee siinä olevat autot
- Autotallin ollessa auki voi sinne lisätä autoja tai poistaa sieltä autoja

# Sovelluksen nykyinen tilanne

- Käyttäjä voi luoda tunnuksen ja kirjautua sisään sovellukseen
- Sovellus ilmoittaa käyttäjälle virheellisistä syötteistä
- Käyttäjä voi luoda autotallin ja poistaa autotallin kokoelmastaan
- Käyttäjä voi lisätä auton valitsemaansa autotalliin
- Autoja voi myös poistaa autotallista sen ollessa auki

# Testaa sovellusta pilvessä

Klikkaa avataksesi sovelluksen --> https://car-collection-app.fly.dev

# Käynnistysohjeet (lokaalisesti)

Taustavaatimukset:

- python3 ladattuna
- Pip (Python package manager)
- PostgreSQL ladattuna ja serveri on auki, ohjeita tietokannan käynnistykseen täältä --> https://github.com/hy-tsoha/local-pg

Kloonaa repositorio omalle koneellesi

`git clone https://github.com/BorisBanchev/tsoha-car_collection.git`

Siirry oikeaan hakemistoon, johon repositorio kloonattiin

`cd tsoha-car_collection`

Luo .env ympäristö tiedosto seuraavilla muuttujilla:

`DATABASE_URL=<tietokannan-paikallinen-osoite>`  
`SECRET_KEY=<salainen-avain>`  
`FLY_DEPLOYMENT=False`

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
