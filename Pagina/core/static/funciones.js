function boton() {
    marti = document.querySelector(".marti");
    marti.onclick = function () {
        navBar = document.querySelector(".nav_bar");
        navBar.classList.toggle("active");
    }
}

function mostrarSeccion(idSeccion) {
    var secciones = document.getElementsByClassName('seccion');
    for (var i = 0; i < secciones.length; i++) {
        secciones[i].classList.remove("mostrar");
        secciones[i].classList.add("ocultar");
    }

    var seccion = document.getElementById(idSeccion);
    seccion.classList.remove("ocultar");
    seccion.classList.add("mostrar");
}



function toggleButtons() {
    var button1 = document.getElementById("button1");
    var button2 = document.getElementById("button2");

    if (button1.style.display === "none") {
        button1.style.display = "block";
        button2.style.display = "none";
        var suscripcion = document.getElementById("suscripcion");
        confirm("Estas seguro de desuscribirte?")
        suscripcion.innerHTML = "No subscrito";
    }
    else {
        button1.style.display = "none";
        button2.style.display = "block";
        var suscripcion = document.getElementById("suscripcion");
        confirm("Estas seguro de suscribirte?")
        suscripcion.innerHTML = "Subscrito";
    }
}

function aumentar() {
    var contador = document.getElementById("contador");
    contador.value = parseInt(contador.value) + 1;
}

function disminuir() {
    var contador = document.getElementById("contador");
    var valor = parseInt(contador.value);
    if (valor > 1) {
        contador.value = valor - 1;
    } else {
        contador.value = 1;
    }
}

// Obtén todos los enlaces con el atributo href que comienza con "#"
const enlaces = document.querySelectorAll('a[href^="#"]');

// Recorre cada enlace y agrega un evento de clic
enlaces.forEach(enlace => {
  enlace.addEventListener('click', function (e) {
    // Evita el comportamiento predeterminado del enlace
    e.preventDefault();

    // Obtiene el destino del enlace (el identificador del elemento de destino)
    const destino = this.getAttribute('href');

    // Utiliza el método scrollIntoView para desplazarse suavemente hacia el destino
    document.querySelector(destino).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

window.addEventListener('DOMContentLoaded', function() {
    var boton = document.querySelector('.boton');
  
    boton.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  });