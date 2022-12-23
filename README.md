# JWT Auth w/ FastAPI in Python

## The coolness of JWT

JWT otherwise known as JSON Web Token is a means of "securely transmitting information between parties as a JSON object." JWT's take advantage of key infrastructures through use of digital certificates. Therefore, JWT is a stateless protocol with regards ti authorizing client connections: 

> JWT relieves the web server of having to maintain a client session state

## The coolenss of Pydantic Base Models

> Pydantic data classes allow us to easily implement how req/res should be structured without having to define a bunch of boilerplate code

##My Learning Tid-Bits:

> pip show package_name

Reports information related to the package including the installation site. I was concerned about where my PyJWT packages were ending up in my virutal environment

> from decouple import config

Config from decouple allows us to easily manage application parameters with .env files - for example - JWT algorithm and secret parameters

> secrets.token_hex(16)

Allows us to easily generate a secret for use in our JWT thanks Python's standard library

