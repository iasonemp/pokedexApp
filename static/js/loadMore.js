document
  .getElementById("loadMoreButton")
  .addEventListener("click", function () {
    loadPokemon();
    loadMoreButton.style.display = "none";
  });

// // Event listener for scrolling
// window.addEventListener("scroll", function () {
//   // Check if the user has scrolled to the bottom
//   if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
//     loadPokemon();
//   }
// });
// // });

function loadPokemon() {
  // Get the container for the existing Pokémon list
  const pokemonList = document.querySelector(".pokemon-container");

  // Get all the Pokémon elements currently on the page
  const existingPokemonElements = document.querySelectorAll(".pokemon");
  console.log(existingPokemonElements);
  // Check if there are more Pokémon to load
  const remainingPokemon = existingPokemonElements.length % 3;
  console.log(remainingPokemon);

  // Clone the last 12 Pokémon elements
  const clonedPokemonElements = Array.from(existingPokemonElements)
    .slice(-remainingPokemon)
    .map((pokemonElement) => pokemonElement.cloneNode(true));

  // Append the cloned Pokémon elements to the list
  clonedPokemonElements.forEach((pokemonElement) => {
    pokemonList.appendChild(pokemonElement);
  });
}
