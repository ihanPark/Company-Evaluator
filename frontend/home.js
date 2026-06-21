const newAnalysisButton =
  document.getElementById("newAnalysisButton");

const archiveButton =
  document.getElementById("archiveButton");

const dcfRimButton =
  document.getElementById("dcfRimButton");


newAnalysisButton.addEventListener("click", function () {
  window.location.href = "model-selection.html";
});

dcfRimButton.addEventListener("click", function () {
  window.location.href = "dcf_rim_selection.html";
});

archiveButton.addEventListener("click", function () {
  console.log("Archive page is not available yet.");
});
