document.addEventListener("DOMContentLoaded", function () {
  const evolutionButton = document.getElementById("evolutionButton");
  const modal = document.getElementById("pokemon-modal");
  const pokemonInfo = document.getElementById("pokemon-info");
  const closeBtn = document.querySelector(".close");

  // Function to open the modal
  function openModal(pokemon_name) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          const data = JSON.parse(xhr.responseText);
          // CREATE THE DIV THAT WILL CONTAIN THE HTML CODE
          let modalContent = document.createElement("div");

          // IF EVOLUTIONS, THEN EVOLUTION TREE
          if (data.evo_data.evo_sprite) {
            // STARTER sprite, name, id
            modalContent.innerHTML += `
            <span class="inline-images" id="inline-images">
            <a href="http://127.0.0.1:8000/pokemon/${data.evo_data.starter_name}"><img src="${data.evo_data.starter_sprite}" alt="Pokemon Sprite" class="pokemon-image" /></a>
            <div>${data.evo_data.starter_name}</div>
            <div>${data.evo_data.starter_id}</div>
          `;
            // STARTER type split in case of multiple types
            var starterTypesMulti = data.evo_data.starter_type.split(":");
            for (var i = 0; i < starterTypesMulti.length; i++) {
              modalContent.innerHTML += `
              <div>${starterTypesMulti[i]}</div>
              `;
            }
            // EVOLUTION(S) : Sprites, Names, IDs, Types

            var SpriteLinks = data.evo_data.evo_sprite.split("delimiter");
            var TypeSplit = data.evo_data.evo_type.split("delimiter");
            var NameSplit = data.evo_data.evo_name.split("delimiter");
            var IdSplit = data.evo_data.evo_id.split("delimiter");

            if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
              for (var i = 0; i < SpriteLinks.length; i++) {
                modalContent.innerHTML += `
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
                <a href="http://127.0.0.1:8000/pokemon/${NameSplit[i]}"><img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image evolution-image" data-evolution-name="${NameSplit[i]}" /></a>
                <div>${NameSplit[i]}</div>
                <div>${IdSplit[i]}</div>
              `;
                // EVOLUTION type split in case of multiple types
                var evoTypesMulti = TypeSplit[i].split(":");
                for (var j = 0; j < evoTypesMulti.length; j++) {
                  modalContent.innerHTML += `
                <div>${evoTypesMulti[j]}</div>
                `;
                }
              }
            }
          } else {
            // Handle case when there are no evolutions
            modalContent.innerHTML += `<hr>
            <div>This Pokémon doesn't have any evolutions.</div>`;
          }
          modalContent.innerHTML += `
             </span>`;

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
  // ****************************************************************

  // const evolutionImages = document.querySelectorAll(".evolution-image");

  // evolutionImages.forEach(function (evolutionImage) {
  //   evolutionImage.addEventListener("click", function () {
  //     const evolutionName = evolutionImage.getAttribute("data-evolution-name");
  //     openModal(evolutionName);
  //     console.log("hi");
  //   });
  // });
  // *********************************************
  evolutionButton.addEventListener("click", function () {
    const pokemon_name = evolutionButton.getAttribute("data-pokemon-name");
    openModal(pokemon_name);
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
