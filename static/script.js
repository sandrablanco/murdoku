fetch("/tablero")
  .then(response => response.json())
  .then(data => {
    // Procesar los datos del tablero
  document.getElementById("history").innerHTML = "Bienvenido a tu primer caso de murdoku. Resuelve el misterio completando el tablero." + data.history;
  let tablero=document.getElementById("tablero");
  
  for (let i = 0; i < data.casillas.length; i++) {
    let c = data.casillas[i];
    let div = document.createElement("div");
    div.className = "casilla";
    let texto =
        "F: " + c.fila +
        " C: " + c.columna +
        "\n" +
        c.contenido;
    div.innerText = texto;
    if (c.fila <= 3 && c.columna <= 3) {
        div.classList.add("sala");
    }
    else if (c.fila <= 3 && c.columna >= 4) {
        div.classList.add("dormitorio");
    }
    else if (c.fila >= 4 && c.columna <= 3) {
        div.classList.add("salon");
    }
    else {
        div.classList.add("comedor");
    }
    tablero.appendChild(div);
}
});

