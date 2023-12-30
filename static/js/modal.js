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
          modalContent.classList.add('modal-evolutions-wrapper')

          // IF EVOLUTIONS, THEN EVOLUTION TREE
          if (data.evo_data.evo_sprite) {
            // Create the evolution chain wrapper
            var evolutionChainWrapper = document.createElement('div');
            evolutionChainWrapper.classList.add('pokemonInEvolutionChainWrapper');
            evolutionChainWrapper.classList.add('firstPokemonInEvolutionChain');            
          
            // Add content to the evolution chain wrapper
            evolutionChainWrapper.innerHTML = `
              <a href="http://127.0.0.1:8000/pokemon/${data.evo_data.starter_name}">
                <img src="${data.evo_data.starter_sprite}" alt="Pokemon Sprite" class="pokemon-image" />
              </a>
              <div>${data.evo_data.starter_name}</div>
              <div>${data.evo_data.starter_id}</div>
            `;
          
            // Append the evolution chain wrapper to modalContent
            modalContent.appendChild(evolutionChainWrapper);
          
            // Create a typeWrapper for the starter Pokemon
            var starterTypeWrapper = document.createElement('div');
            starterTypeWrapper.classList.add('pokemonTypeWrapper');
          
            // STARTER type split in case of multiple types
            var starterTypesMulti = data.evo_data.starter_type.split(":");
            for (var i = 0; i < starterTypesMulti.length; i++) {
              // Add types to the type wrapper
              var typeDiv = document.createElement('div');
              typeDiv.classList.add('pokeType')
              typeDiv.classList.add( `${starterTypesMulti[i]}Type`)
              //We create the <p> element inside the typeDiv and add it
              var typeName = document.createElement('p');
              typeName.textContent = starterTypesMulti[i];
              typeDiv.appendChild(typeName);

              starterTypeWrapper.appendChild(typeDiv);
            }
          
            // Append the type wrapper to the current evolution chain wrapper
            evolutionChainWrapper.appendChild(starterTypeWrapper);
          
            // EVOLUTION(S) : Sprites, Names, IDs, Types

            var SpriteLinks = data.evo_data.evo_sprite.split("delimiter");
            var TypeSplit = data.evo_data.evo_type.split("delimiter");
            var NameSplit = data.evo_data.evo_name.split("delimiter");
            var IdSplit = data.evo_data.evo_id.split("delimiter");

            if (SpriteLinks.length > 0 && SpriteLinks[0] !== "") {
              for (var i = 0; i < SpriteLinks.length; i++) {
                // Create the evolution chain wrapper
                var evolutionChainWrapper = document.createElement('div');
                evolutionChainWrapper.classList.add('pokemonInEvolutionChainWrapper');

                //modalContent.innerHTML += `<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />`
                // Add content to the evolution chain wrapper
                let htmlContentString = `
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Arrow_right_font_awesome.svg/1200px-Arrow_right_font_awesome.svg.png" class="right-arrow" />
                    <div class="evolutionPokemonDataWrapper">
                      <a href="http://127.0.0.1:8000/pokemon/${NameSplit[i]}">
                        <img src="${SpriteLinks[i]}" alt="Pokemon Sprite" class="pokemon-image evolution-image" data-evolution-name="${NameSplit[i]}" />
                      </a>
                      <div>${NameSplit[i]}</div>
                      <div>${IdSplit[i]}</div>
                      <div class="pokemonTypeWrapper">                  
                `;

                var evoTypesMulti = TypeSplit[i].split(":");

                for (var j = 0; j <evoTypesMulti.length; j++) {
                  htmlContentString += `<div class="pokeType ${evoTypesMulti[j]}Type">
                                          <p>${evoTypesMulti[j]}</p>
                                        </div>`;
                }

                htmlContentString += `  </div>
                                      </div>`;

                evolutionChainWrapper.innerHTML = htmlContentString;
                // Append the evolution chain wrapper to modalContent
                modalContent.appendChild(evolutionChainWrapper);
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

          modal.style.display = "flex";
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
