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
          // COMMENTS
          var comment_list = data.comment_list;
          for (var i = 0; i < comment_list.length; i++) {
            modalContent.innerHTML += `
            <div>${comment_list[i].user}</div>
            <div>${comment_list[i].body}</div>
              `;
          }
          // STARTER FORM
          modalContent.innerHTML += `
            <button id="writeCommentButton">Write Comment</button>            
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
          // EVOLUTION(S) : Sprites, Names, IDs, Types
          if (data.evo_data.evo_sprite) {
            var SpriteLinks = data.evo_data.evo_sprite.split("delimiter");
            var TypeSplit = data.evo_data.evo_type.split("delimiter");
            var NameSplit = data.evo_data.evo_name.split("delimiter");
            var IdSplit = data.evo_data.evo_id.split("delimiter");

            if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
              for (var i = 0; i < SpriteLinks.length; i++) {
                modalContent.innerHTML += `
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
                <img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image" />
                <div>${TypeSplit[i]}</div>
                <div>${NameSplit[i]}</div>
                <div>${IdSplit[i]}</div>
              `;
              }
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
          const writeCommentButton =
            document.getElementById("writeCommentButton");
          if (writeCommentButton) {
            writeCommentButton.addEventListener("click", () => {
              console.log("working");
            });
          }

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
