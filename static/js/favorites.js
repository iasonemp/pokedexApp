document.addEventListener("DOMContentLoaded", function () {
  const addToFavoritesButton = document.getElementById("addToFavoritesButton");
  const removeFavoriteButton = document.getElementById("removeFavoriteButton");

  if (addToFavoritesButton) {
    addToFavoritesButton.addEventListener("click", function () {
      const pokemon_name =
        addToFavoritesButton.getAttribute("data-pokemon-name");
      addToFavorites(pokemon_name);
    });
  }

  if (removeFavoriteButton) {
    removeFavoriteButton.addEventListener("click", function () {
      const pokemon_name =
        removeFavoriteButton.getAttribute("data-pokemon-name");
      removeFromFavorites(pokemon_name);
    });
  }

  function addToFavorites(pokemon_name) {
    fetch(`/add_favorite/${pokemon_name}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert("Pokémon added to favorites!");
        } else {
          alert("Failed to add Pokémon to favorites. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  function removeFromFavorites(pokemon_name) {
    fetch(`/remove_favorite/${pokemon_name}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert("Pokémon removed from favorites.");
        } else {
          alert("Failed to remove Pokémon from favorites. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  // Function to get CSRF token from cookie
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
