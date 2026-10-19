export function formatearTarea(nombre) {
  return `${nombre}`;
}

export function obtenerEstado(completada) {
  return completada ? "Completada" : "Pendiente";
}
