function generateMatrix(
  rows,
  cols,
  orientation,
  floor,
  spaces = [],
  div,
  eventClick = true
) {
  var table = document.createElement("table");
  table.classList.add("table", "table-bordered", "table-hover", "map-table");

  if (orientation === "HORIZONTAL") {
    for (var i = 0; i < rows; i++) {
      var row = document.createElement("tr");

      // Crear una celda para el número de fila
      var rowHeader = document.createElement("td");
      rowHeader.textContent = `Fila N° ${i + 1}`;
      rowHeader.classList.add("header");
      row.appendChild(rowHeader);

      for (var j = 0; j < cols; j++) {
        var cell = document.createElement("td");
        var name = `${floor}_F${i + 1}-E${j + 1}`;

        if (existRegister(spaces, name))
          cell.classList.add("map-cell", "text-center", "activeField", "pqEst");
        else cell.classList.add("map-cell", "text-center", "pqEst");

        // Agregar evento onclick a la celda
        if (eventClick) {
          cell.onclick = function () {
            toggleCellBackground(this);
          };
          cell.innerHTML = `${name}`;
        } else {
          var br = busyRegister(spaces, name);
          if (br[0]) {
            cell.classList.add("map-cell", "text-center", "busyField", "pqEst");
            cell.innerHTML = `${name} <span class="plate">${br[1]}<span>`;
          } else {
            cell.innerHTML = `${name}`;
          }
        }

        row.appendChild(cell);
      }

      table.appendChild(row);
    }
  } else if (orientation === "VERTICAL") {
    var headerRow = document.createElement("tr");

    for (var j = 0; j < rows; j++) {
      var colHeader = document.createElement("td");
      colHeader.textContent = `Fila N° ${j + 1}`;
      colHeader.classList.add("header");
      headerRow.appendChild(colHeader);
    }
    table.appendChild(headerRow);

    for (var i = 0; i < cols; i++) {
      var row = document.createElement("tr");

      for (var j = 0; j < rows; j++) {
        var cell = document.createElement("td");

        var name = `${floor}_F${j + 1}-E${i + 1}`;
        if (existRegister(spaces, name))
          cell.classList.add("map-cell", "text-center", "activeField", "pqEst");
        else cell.classList.add("map-cell", "text-center", "pqEst");

        // Agregar evento onclick a la celda
        if (eventClick) {
          cell.onclick = function () {
            toggleCellBackground(this);
          };
          cell.textContent = name;
        } else {
          var br = busyRegister(spaces, name);
          if (br[0]) {
            cell.classList.add("map-cell", "text-center", "busyField", "pqEst");
            cell.innerHTML = `${name} <span class="plate">${br[1]}<span>`;
          } else {
            cell.innerHTML = `${name}`;
          }
        }
        row.appendChild(cell);
      }
      table.appendChild(row);
    }
  }

  // Limpiar el contenedor antes de agregar la nueva matriz
  var oldMatrix = document.getElementById(div);
  oldMatrix.innerHTML = "";
  oldMatrix.appendChild(table);
}

function toggleCellBackground(cell) {
  cell.classList.toggle("activeField");
}

function existRegister(spaces, value) {
  var space = spaces.find((space) => space.name === value);
  if (space) {
    return space.status;
  } else return true;
}

function busyRegister(spaces, value) {
  var space = spaces.find((space) => space.name === value);
  if (space) {
    return [space.busy, space.plate];
  } else return [false, ""];
}
