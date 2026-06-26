fetch("/tablero")
  .then(response => response.json())
  .then(data => {
    // Procesar los datos del tablero
  });
  document.getElementById("history").innerHTML = "Bienvenido a tu primer caso de murdoku. Resuelve el misterio completando el tablero."=data.history;
  let tablero=document.getElementById("tablero");