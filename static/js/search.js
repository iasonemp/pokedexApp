var searchInput = document.getElementById("searchInput");
var searchButton = document.getElementById("searchButton");
var searchResults = document.getElementById("searchResults");
var previousQuery = "";
var nameSearchRadio = document.getElementById("nameSearch");
var typeSearchRadio = document.getElementById("typeSearch");

// Retrieve the last selected radio button state from localStorage
var lastSelectedRadio = localStorage.getItem("lastSelectedRadio");
if (lastSelectedRadio) {
  if (lastSelectedRadio === "name") {
    nameSearchRadio.checked = true;
  } else if (lastSelectedRadio === "type") {
    typeSearchRadio.checked = true;
  }
}
searchInput.addEventListener("input", function () {
  // get user's query and clean it
  var query = searchInput.value;
  query = query.replace(/[^a-zA-Z]/g, "");

  if (nameSearchRadio.checked) {
    nameSearchPokemon(query);
  } else if (typeSearchRadio.checked) {
    typeSearchPokemon(query);
  }
});

nameSearchRadio.addEventListener("change", function () {
  // Save the selected radio button state to localStorage
  localStorage.setItem("lastSelectedRadio", "name");
  // change search input placeholder
  searchInput.placeholder = "Search Pokémon Name";
});

typeSearchRadio.addEventListener("change", function () {
  // Save the selected radio button state to localStorage
  localStorage.setItem("lastSelectedRadio", "type");
  // change search input placeholder
  searchInput.placeholder = "Search Pokémon Type";
});

searchButton.addEventListener("click", function () {
  // get user's query and clean it
  var query = searchInput.value;
  query = query.replace(/[^a-zA-Z]/g, "");

  // change url based on button checked
  if (nameSearchRadio.checked) {
    window.location.href = `/?name=${query}`;
  } else if (typeSearchRadio.checked) {
    window.location.href = `/?type=${query}`;
  }
});

function typeSearchPokemon(query) {
  var searchResultsContainer = document.getElementById(
    "searchResultsContainer"
  );
  var searchResultsList = document.getElementById("searchResultsList");
  searchResultsList.innerHTML = ""; // Clear any previous results
  // if (query !== previousQuery) {
  // Use the Fetch API to send a request to your Django backend
  fetch(`/api/type_search/?query=${query}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"), // Make sure to include the CSRF token
    },
    body: JSON.stringify({ pokemonType: query }),
  })
    .then((response) => {
      // Check if the response status is OK (200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      let data = response.json();
      // Parse the JSON from the response
      return data;
    })
    .then((data) => {
      // Display the results in the searchResultsList element

      data.results.forEach((result) => {
        var listItem = document.createElement("li"); // Create a new list item
        listItem.classList.add("list-item"); // Add a CSS class to the list item

        listItem.addEventListener("click", () => {
          searchInput.value = result;
        });

        listItem.textContent = result; // Set the text content of the list item
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
function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}

function nameSearchPokemon(query) {
  var searchResultsContainer = document.getElementById(
    "searchResultsContainer"
  );

  var searchResultsList = document.getElementById("searchResultsList");
  searchResultsList.innerHTML = ""; // Clear any previous results
  // if (query !== previousQuery) {
  // Use the Fetch API to send a request to your Django backend
  fetch(`/api/name_search/?query=${query}`)
    .then((response) => {
      let data = response.json();
      return data;
    })
    .then((data) => {
      // Display the results in the searchResultsList element
      data.results.forEach((result) => {
        var listItem = document.createElement("li"); // Create a new list item
        listItem.classList.add("list-item"); // Add a CSS class to the list item

        listItem.addEventListener("click", () => {
          searchInput.value = result.name;
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
