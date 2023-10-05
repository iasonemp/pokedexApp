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
          // CREATE THE DIV
          let modalContent = document.createElement("div");
          // STARTER FORM
          modalContent.innerHTML += `
          <span class="inline-images" id="inline-images">
          <img src="${data.starter_sprite}" alt="Pokemon Sprite" class="pokemon-image" />
        `;
          // FIRST EVOLUTION(S)
          var SpriteLinks = data.t1sprite.split("delimiter");
          if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
            for (var i = 0; i < SpriteLinks.length; i++) {
              modalContent.innerHTML += `
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
                <img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image" />
              `;
            }
          }
          // SECOND EVOLUTION(S)
          var SpriteLinks = data.t2sprite.split("delimiter");
          if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
            for (var i = 0; i < SpriteLinks.length; i++) {
              modalContent.innerHTML += `
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
            <img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image" />
          `;
            }
          }
          modalContent.innerHTML += `
           </span><hr>`;
          // STARTER TYPES
          var StarterTypeSplit = data.types.split(":");
          console.log(StarterTypeSplit);
          modalContent.innerHTML += `
          <span class="inline-types" id="inline-types">`;
          for (var i = 0; i < StarterTypeSplit.length; i++) {
            modalContent.innerHTML += `<div>${StarterTypeSplit[i]}</div>`;
          }
          modalContent.innerHTML += `
           </span>`;

          // STATS
          modalContent.innerHTML += `
            <p>Height: ${data.height}</p>
            <p>Weight: ${data.weight}</p>
            <li>HP: ${data.hp}</li>
            <li>Attack: ${data.attack}</li>
            <li>Defense: ${data.defense}</li>
            <li>Special Attack: ${data.special_attack}</li>
            <li>Special Defense: ${data.special_defense}</li>
            <li>Speed: ${data.speed}</li>
        `;
          document.addEventListener("DOMContentLoaded", function () {
            var inlineImagesSpan = document.getElementById("inline-images");
            var divElement = document.createElement("div");
            divElement.innerHTML = SpriteLinksHtml;
            inlineImagesSpan.appendChild(divElement);
          });
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
