const dcfButton = document.getElementById("dcfButton");
const rimButton = document.getElementById("rimButton");
const archiveButton = document.getElementById("archiveButton");
const backButton = document.getElementById("backButton");

dcfButton.addEventListener("click", function () {
  window.location.href = "dcf-analysis.html";
});

rimButton.addEventListener("click", function () {
  window.location.href = "rim-analysis.html";
});

archiveButton.addEventListener("click", function () {
  console.log("Archive page is not available yet.");
});

backButton.addEventListener("click", function () {
  window.location.href = "index.html";
});
