# User's Guide

This Django project is a Pokedex application, allowing users to explore and search for information about Pokémon.


[View Live Web App](https://django-pokedexapp.onrender.com/)

|Front Page|
|:-:|
|![front page](screenshots/front-page.png)|

## Main Technologies

- Python
- Django
- SQLite
- Vanilla JavaScript

## Features

### Shortcuts

&nbsp;&nbsp;&nbsp;&nbsp;[Search Pokemon](#search-pokemon)\
&nbsp;&nbsp;&nbsp;&nbsp;[Login/Register](#loginregister)\
&nbsp;&nbsp;&nbsp;&nbsp;[Pokemon Page](#pokemon-page)\
&nbsp;&nbsp;&nbsp;&nbsp;[Evolution Tree](#evolution-tree)\
&nbsp;&nbsp;&nbsp;&nbsp;[Favorite Pokemons](#favorite-pokemons)






#### Search Pokemon
&nbsp;&nbsp;&nbsp;&nbsp;Any visitor of the app, authenticated or not, can browse through all the pokemons via a search bar which exists in both the home page and the pokemon page. The search result can be filtered by either the name or the type of a pokemon. Clicking on a type beneath a Pokemon's name will trigger the search filter. By applying no filter, you can browse through all the pokemons. **Pagination** is applied of course:

|||
|:-:|:-:|
|![Pokemon Name Search](screenshots/pokemon-name-search.png)|![Pokemon Type Search](screenshots/pokemon-type-search.png)|

||
|:-:|
|![Pagination](screenshots/pagination.png)|

#### Login/Register
&nbsp;&nbsp;&nbsp;&nbsp;A user can register with **username/password** or **google account**.

||
|:-:|
|![Login Screen](screenshots/login.png)|

#### Pokemon Page

&nbsp;&nbsp;&nbsp;&nbsp;Each Pokemon has its own page with additional details like stats, comments, and, if one exists, an evolution tree. If you are logged in, you can comment and add this Pokémon to your favorites.

||
|:-:|
|![Pokemon Page](screenshots/pokemon-page.png)|

#### Evolution Tree

&nbsp;&nbsp;&nbsp;&nbsp;On the Pokémon page, if a Pokémon has future or prior evolutions, you'll find the "Evolutions" button. Clicking on it will reveal the evolution tree of the Pokémon.

||
|:-:|
|![Evolution Tree](screenshots/evolution-tree.png)|

#### Favorite Pokemons

&nbsp;&nbsp;&nbsp;&nbsp;On the Pokémon page, if you are logged in you have the ability to add a pokemon to your favorites to make sure it appears first the next time you visit the front page or use the search.

||
|:-:|
|![Favorite Pokemons](screenshots/favorite-pokemon-front-page.png)|
