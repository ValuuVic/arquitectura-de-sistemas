import test from "node:test";
import assert from "node:assert/strict";

import {
  formatearTarea,
  obtenerEstado
} from "./index.js";

test("Debe formatear el nombre de una tarea", () => {
  const resultado = formatearTarea("Estudiar");

  assert.equal(resultado, "📌 Estudiar");
});

test("Debe devolver Completada cuando la tarea terminó", () => {
  const resultado = obtenerEstado(true);

  assert.equal(resultado, "Completada");
});

test("Debe devolver Pendiente cuando la tarea no terminó", () => {
  const resultado = obtenerEstado(false);

  assert.equal(resultado, "Pendiente");
});
