

btnGuest = document.getElementById("btn-guest")
btnSignup = document.getElementById("btn-signup")
btnLogin = document.getElementById("btn-login")

btnGuest.addEventListener("click", (event) => {
    console.log("Play as a guest clicked.")
    window.location.href = "/gamescreen"
})

btnSignup.addEventListener("click", (event) => 
{
    console.log("Signup button clicked.")
    window.location.href = "/signup"
}
)

btnLogin.addEventListener("click", (event)=>
{
    console.log("Login button clicked.")
    window.location.href = "/login"
})