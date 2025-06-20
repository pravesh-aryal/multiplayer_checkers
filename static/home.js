

btnGuest = document.getElementById("btn-guest")

btnGuest.addEventListener("click", (event) => {
    console.log("Play as a guest clicked.")
    window.location.href = "/gamescreen"
})