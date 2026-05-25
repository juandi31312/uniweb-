document.getElementById("btn").addEventListener("click", function() {
    fetch('/productos/json/') 
        .then(response => response.json())
        .then(data => {
            const contenedor = document.getElementById("out");
            contenedor.innerHTML = "<strong>Lista de productos:</strong><ul>";
            
            data.forEach(p => {
                // Aquí quitamos .fields, porque en tu vista ya envías el objeto directamente
                contenedor.innerHTML += `<li>${p.nombre} - Precio: $${p.precio}</li>`;
            });
            
            contenedor.innerHTML += "</ul>";
        })
        .catch(error => {
            console.error("Error al traer datos:", error);
            document.getElementById("out").innerText = "Error al cargar productos.";
        });
});

