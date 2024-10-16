const container = document.querySelector(".container");

const btnSignIn = document.getElementById("btn-sign-in")
const btnSignUp = document.getElementById("btn-sign-up")

btnSignIn.addEventListener("click",()=> {
    container.classList.remove("toggle");
})

btnSignUp.addEventListener("click",()=> {
    container.classList.add("toggle");
})

// Función para el botón "Volver"
document.querySelector('.volver').addEventListener('click', function() {
    window.open('index.html',);
});

// Función para el botón "Inicio"
document.querySelector('.inicio').addEventListener('click', function() {
    window.open('index.html'); 
});
