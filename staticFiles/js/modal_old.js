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
          // --- SPRITES ---
          // STARTER FORM
          modalContent.innerHTML += `
          <span class="inline-images" id="inline-images">
          <img src="${data.starter_sprite}" alt="Pokemon Sprite" class="pokemon-image" />
          <div>${data.starter_id}</div>
          <div>${data.starter_form}</div>
          <!-- <div>${data.starter_type}</div> -->
        `;
          var starterTypesMulti = data.starter_type.split(":");
          for (var i = 0; i < starterTypesMulti.length; i++) {
            modalContent.innerHTML += `
            <div>${starterTypesMulti[i]}</div>
            `;
          }
          // FIRST EVOLUTION(S)
          if (data.t1data.t1sprite) {
            var SpriteLinks = data.t1data.t1sprite.split("delimiter");
            if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
              for (var i = 0; i < SpriteLinks.length; i++) {
                modalContent.innerHTML += `
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
                <img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image" />
                <div>${data.t1data.t1id}</div>
                <div>${data.t1data.t1name}</div>
                <!-- <div>${data.t1data.t1type}</div> -->
              `;
              }
              var t1TypesMulti = data.t1data.t1type.split(":");
              for (var i = 0; i < t1TypesMulti.length; i++) {
                modalContent.innerHTML += `
            <div>${t1TypesMulti[i]}</div>
            `;
              }
            }
          }
          // SECOND EVOLUTION(S)
          if (data.t2data.t2sprite) {
            var SpriteLinks = data.t2data.t2sprite.split("delimiter");
            if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
              for (var i = 0; i < SpriteLinks.length; i++) {
                modalContent.innerHTML += `
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
            <img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image" />
            <div>${data.t2data.t2id}</div>
            <div>${data.t2data.t2name}</div>
            <!-- <div>${data.t2data.t2type}</div> -->
          `;
              }
            }
            var t2TypesMulti = data.t2data.t2type.split(":");
            for (var i = 0; i < t2TypesMulti.length; i++) {
              modalContent.innerHTML += `
            <div>${t2TypesMulti[i]}</div>
            `;
            }
          }
          modalContent.innerHTML += `
           </span><hr>`;

          // --- TYPES ---
          // STARTER FORM
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

  window.addEventListener("keydown", function (event) {
    if (event.key === "Escape" || event.key === "Esc") {
      modal.style.display = "none";
    }
  });
});
