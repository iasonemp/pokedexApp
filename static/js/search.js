const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const searchResults = document.getElementById("searchResults");

searchButton.addEventListener("click", function () {
  // Get the user's search query
  const query = searchInput.value;

  // Call a function to fetch Pokémon data based on the query
  searchPokemon(query);
});

function searchPokemon(query) {
  // Use the Fetch API to send a request to your Django backend
  fetch(`/api/search/?query=${query}`)
    .then((response) => response.json())
    .then((data) => {
      // Display the results in the searchResults element
      searchResults.innerHTML = JSON.stringify(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
