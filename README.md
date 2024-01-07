# User's Guide

This Django project is a Pokedex application, allowing users to explore and search for information about Pokémon.


[View Live Web App](https://django-pokedexapp.onrender.com/)

|Front Page|
|:-:|
|![front page](screenshots/front-page.webp)|

## Main Technologies

- Python
- Django
- SQLite
- Vanilla JavaScript

## Features

### Shortcuts

&nbsp;&nbsp;&nbsp;&nbsp;[Search Pokemon](#search-pokemon)\
&nbsp;&nbsp;&nbsp;&nbsp;[Login/Register](#loginregister)\
&nbsp;&nbsp;&nbsp;&nbsp;[Pokemon's Page](#pokemon-page)\
&nbsp;&nbsp;&nbsp;&nbsp;[Pokemon's Comments](#pokemon-comments)\
&nbsp;&nbsp;&nbsp;&nbsp;[Pokemon's Evolution Tree](#pokemon-evolution-tree)\
&nbsp;&nbsp;&nbsp;&nbsp;[Favorite Pokemons](#favorite-pokemons)






#### Search Pokemon
&nbsp;&nbsp;&nbsp;&nbsp;Any visitor of the app, authenticated or not, can browse through all the pokemons via a search bar which exists in both the home page and the pokemon page. The search result can be filtered by either the name or the type of a pokemon. By applying no filter, you can browse through all the pokemons. **Pagination** is applied of course:

|||
|:-:|:-:|
|![Pokemon Name Search](screenshots/pokemon-name-search.png)|![Pokemon Type Search](screenshots/pokemon-type-search.png)|

||
|:-:|
|![Pagination](screenshots/pagination.png)|

#### Login/Register
&nbsp;&nbsp;&nbsp;&nbsp;A user can register with **username/password** or **google account**.
