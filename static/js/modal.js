document.addEventListener("DOMContentLoaded", function () {
  const pokemonImages = document.querySelectorAll(".pokemon-image");
  const modal = document.getElementById("pokemon-modal");
  const pokemonInfo = document.getElementById("pokemon-info");
  const closeBtn = document.querySelector(".close");

  // Function to open the modal
  function openModal(pokemon_name) {
    // const modal = document.getElementById("pokemon-modal");
    // modal.style.display = "block";
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          const data = JSON.parse(xhr.responseText);
          const modalContent = document.createElement("div");
          modalContent.innerHTML = `
            <h2>${data.starter_form}</h2>
            <p>Tier 1 Evolution: ${data.tier_1_evolution}</p>
            <p>Tier 2 Evolution: ${data.tier_2_evolution}</p>
            <!-- Add more HTML elements as needed -->
        `;

          // Clear existing content and append the new content
          pokemonInfo.innerHTML = "";
          pokemonInfo.appendChild(modalContent);

          modal.style.display = "block";
        } else {
          alert("Error fetching Pokémon data.");
        }
      }
    };
    xhr.open("GET", "/detail/" + pokemon_name);
    xhr.send();
  }

  pokemonImages.forEach(function (image) {
    image.addEventListener("click", function () {
      const pokemon_name = image.getAttribute("data-pokemon-name");
      openModal(pokemon_name);
    });
  });

  closeBtn.addEventListener("click", function () {
    modal.style.display = "none";
  });

  window.addEventListener("click", function (event) {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});
// Fetch additional Pokémon information using AJAX and update the modal content
// You can use Django's URL routing to fetch the data for the selected Pokémon

// Function to close the modal
// function closeModal() {
//   const modal = document.getElementById("pokemon-modal");
//   modal.style.display = "none";
// }

// // Close the modal if the user clicks outside of it
// window.onclick = function (event) {
//   const modal = document.getElementById("pokemon-modal");
//   if (event.target === modal) {
//     modal.style.display = "none";
//   }
// };
// // -------------------------------------------------------------------

// document.addEventListener("DOMContentLoaded", function () {
//   const pokemonImages = document.querySelectorAll('.pokemon-image');
//   const modal = document.getElementById('pokemon-modal');
//   const pokemonInfo = document.getElementById('pokemon-info');
//   const closeBtn = document.querySelector('.close');

//   pokemonImages.forEach(function (image) {
//       image.addEventListener('click', function () {
//           const pokemonId = image.getAttribute('data-pokemon-id');
//           const xhr = new XMLHttpRequest();

//           xhr.onreadystatechange = function () {
//               if (xhr.readyState === 4) {
//                   if (xhr.status === 200) {
//                       const data = JSON.parse(xhr.responseText);
//                       pokemonInfo.innerHTML = 'Name: ' + data.name + '<br>HP: ' + data.hp + '<br>Attack: ' + data.attack;
//                       modal.style.display = 'block';
//                   } else {
//                       alert('Error fetching Pokémon data.');
//                   }
//               }
//           };

//           xhr.open('GET', '/pokemon/' + pokemonId + '/');
//           xhr.send();
//       });
//   });

//   closeBtn.addEventListener('click', function () {
//       modal.style.display = 'none';
//   });
// });
