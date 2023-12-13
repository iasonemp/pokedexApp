document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete_comment");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const commentId = this.getAttribute("data-comment-id");
      if (confirm("Are you sure you want to delete this comment?")) {
        // Send an AJAX request to the server for comment deletion
        fetch(`/delete_comment/${commentId}/`, {
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.status === "success") {
              const commentElement = document.getElementById(
                `comment-${data.comment_id}`
              );
              if (commentElement) {
                commentElement.remove();
                // Optionally, you can update the UI to remove the deleted comment
                // Update the UI as needed
                alert("Comment deleted successfully!");
              }
            } else {
              alert("Failed to delete comment. Please try again.");
            }
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      }
    });
  });

  // Function to get CSRF token from cookie
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
