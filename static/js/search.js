var searchInput = document.getElementById("searchInput");
var searchButton = document.getElementById("searchButton");
var searchResults = document.getElementById("searchResults");
var previousQuery = "";

searchInput.addEventListener("input", function () {
  var query = searchInput.value; // Get the current input value
  query = query.replace(/[^a-zA-Z]/g, "");
  searchPokemon(query);
});

searchButton.addEventListener("click", function () {
  // Get the user's search query
  var query = searchInput.value;
  query = query.replace(/[^a-zA-Z]/g, "");
  // Call a function to fetch Pokémon data based on the query
  window.location.href = `/search/?q=${query}`;
});

function searchPokemon(query) {
  var searchResultsContainer = document.getElementById(
    "searchResultsContainer"
  );

  var searchResultsList = document.getElementById("searchResultsList");
  searchResultsList.innerHTML = ""; // Clear any previous results
  // if (query !== previousQuery) {
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
          // alert(`You clicked on ${result.name}`);
          const pokemonUrl = `http://127.0.0.1:8000/pokemon/${result.name}`;
          window.location.href = pokemonUrl;
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
  // }
}
document.addEventListener("click", function (event) {
  const searchResultsContainer = document.getElementById(
    "searchResultsContainer"
  );
  const searchInput = document.getElementById("searchInput");

  // Check if the click event target is not within the search results container or search input
  if (event.target !== searchResultsContainer && event.target !== searchInput) {
    // Hide the search results container

    searchResultsContainer.style.display = "none";
  }
});

document.addEventListener("keydown", function (event) {
  const searchResultsContainer = document.getElementById(
    "searchResultsContainer"
  );

  if (event.key === "Escape" || event.key === "Esc") {
    searchResultsContainer.style.display = "none";
  }

  if ((event.ctrlKey || event.metaKey) && event.key === "f") {
    // Prevent the browser's built-in Find feature
    event.preventDefault();

    // Focus on the search input field
    searchInput.focus();
  }
});

searchInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    // Trigger a click on the search button
    searchButton.click();
  }
});
