// Function to open the modal
function openModal(pokemonName) {
  const modal = document.getElementById("myModal");
  modal.style.display = "block";
  // Fetch additional Pokémon information using AJAX and update the modal content
  // You can use Django's URL routing to fetch the data for the selected Pokémon
}

// Function to close the modal
function closeModal() {
  const modal = document.getElementById("myModal");
  modal.style.display = "none";
}

// Close the modal if the user clicks outside of it
window.onclick = function (event) {
  const modal = document.getElementById("myModal");
  if (event.target === modal) {
    modal.style.display = "none";
  }
};
