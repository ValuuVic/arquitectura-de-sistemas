import express from "express";
import {
  formatearTarea,
  obtenerEstado
} from "@monorepo/shared";

const app = express();
const PORT = 3000;

app.use(express.json());

const tareas = [
  { id: 1, nombre: "Estudiar Turborepo", completada: true },
  { id: 2, nombre: "Crear el backend", completada: true },
  { id: 3, nombre: "Conectar librería compartida", completada: false }
];

app.get("/", (req, res) => {
  res.json({
    mensaje: "API del Gestor de Tareas funcionando",
    aplicacion: "Backend Express",
    libreria: "@monorepo/shared"
  });
});

app.get("/api/tareas", (req, res) => {
  const resultado = tareas.map((tarea) => ({
    id: tarea.id,
    nombre: tarea.nombre,
    nombreFormateado: formatearTarea(tarea.nombre),
    estado: obtenerEstado(tarea.completada),
    completada: tarea.completada
  }));

  res.json({
    mensaje: "Lista de tareas",
    total: resultado.length,
    tareas: resultado
  });
});

app.listen(PORT, () => {
  console.log(`Servidor funcionando en http://localhost:${PORT}`);
});
