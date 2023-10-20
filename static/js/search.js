var searchInput = document.getElementById("searchInput");
var searchButton = document.getElementById("searchButton");
var searchResults = document.getElementById("searchResults");
var previousQuery = "";

searchButton.addEventListener("click", function () {
  // Get the user's search query
  var query = searchInput.value;
  // Call a function to fetch Pokémon data based on the query
  searchPokemon(query);
});

function searchPokemon(query) {
  var searchResultsContainer = document.getElementById(
    "searchResultsContainer"
  );
  var searchResultsList = document.getElementById("searchResultsList");
  searchResultsList.innerHTML = ""; // Clear any previous results
  if (query !== previousQuery) {
    // Use the Fetch API to send a request to your Django backend
    fetch(`/api/search/?query=${query}`)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        // Display the results in the searchResultsList element
        data.results.forEach((result) => {
          var listItem = document.createElement("li"); // Create a new list item
          listItem.classList.add("list-item"); // Add a CSS class to the list item

          listItem.addEventListener("click", () => {
            // Handle the click event here
            alert(`You clicked on ${result.name}`);
          });

          listItem.textContent = result.name; // Set the text content of the list item
          searchResultsList.appendChild(listItem); // Add the list item to the list
        });

        // Update the visibility of the search results container
        if (data.results.length > 0) {
          searchResultsContainer.style.display = "block";
        } else {
          searchResultsContainer.style.display = "none";
        }

        previousQuery = query; // Update the previousQuery to the current query
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}
