import { formatearTarea, obtenerEstado } from "@monorepo/shared";
import "./style.css";

const app = document.querySelector("#app");

app.innerHTML = `
  <main class="contenedor">
    <h1>Gestor de Tareas</h1>
    <p>Frontend con Vite + Backend con Express</p>

    <h2>Mis tareas</h2>
    <div id="lista-tareas">
      <p>Cargando tareas...</p>
    </div>
  </main>
`;

async function cargarTareas() {
  const contenedor = document.querySelector("#lista-tareas");

  try {
    const respuesta = await fetch("/api/tareas");

    if (!respuesta.ok) {
      throw new Error("No se pudieron obtener las tareas");
    }

    const datos = await respuesta.json();

    contenedor.replaceChildren();

    datos.tareas.forEach((tarea) => {
      const tarjeta = document.createElement("div");
      tarjeta.className = "tarea";

      const nombre = document.createElement("strong");
      nombre.textContent = formatearTarea(tarea.nombre);

      const estado = document.createElement("span");
      estado.className = tarea.completada
        ? "completada"
        : "pendiente";
      estado.textContent = obtenerEstado(tarea.completada);

      tarjeta.append(nombre, estado);
      contenedor.appendChild(tarjeta);
    });

  } catch (error) {
    console.error(error);
    contenedor.textContent =
      "Error al conectar con el backend. Verifica que la API esté funcionando.";
  }
}

cargarTareas();
