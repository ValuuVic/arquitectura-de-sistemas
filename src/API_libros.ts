import express from "express";
import type { Request, Response } from "express";

const api = express();
const PORT = 3000;

// Permite a la API recibir información en formato JSON
api.use(express.json());

// Estructura de un libro
interface Libro {
  id: number;
  titulo: string;
  autor: string;
  prestado: boolean;
}

// Datos temporales
const libros: Libro[] = [
  {
    id: 1,
    titulo: "Los juegos del hambre",
    autor: "Suzanne Collins",
    prestado: false,
  },
  {
    id: 2,
    titulo: "Los diarios de la boticaria",
    autor: "Natsu Hyūga",
    prestado: true,
  },
  {
    id: 3,
    titulo: "Cadaver exquisito",
    autor: "Agustina Bazterrica",
    prestado: false,
  },
];

// Ruta principal
api.get("/", (_req: Request, res: Response) => {
  res.status(200).json({
    mensaje: "API de Biblioteca Digital funcionando correctamente",
  });
});

// GET 
// Lista todos los libros
api.get("/books", (_req: Request, res: Response) => {
  res.status(200).json(libros);
});

// GET 
// Busca un libro por ID
api.get("/books/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id) || id <= 0) {
    res.status(400).json({
      mensaje: "El ID debe ser un número entero positivo",
    });
    return;
  }

  const libroEncontrado = libros.find(
    (libro) => libro.id === id
  );

  if (!libroEncontrado) {
    res.status(404).json({
      mensaje: "Libro no encontrado",
    });
    return;
  }

  res.status(200).json(libroEncontrado);
});

// POST 
// Agrega un nuevo libro
api.post("/books", (req: Request, res: Response) => {
  // Validar que el contenido enviado sea JSON
  if (!req.is("application/json")) {
    res.status(415).json({
      mensaje: "El cuerpo de la solicitud debe enviarse en formato JSON",
    });
    return;
  }

  const { titulo, autor, prestado } = req.body ?? {};

  // Valida los datos recibidos
  if (
    typeof titulo !== "string" ||
    titulo.trim() === "" ||
    typeof autor !== "string" ||
    autor.trim() === "" ||
    typeof prestado !== "boolean"
  ) {
    res.status(400).json({
      mensaje:
        "Debe enviar titulo, autor y prestado. El campo prestado debe ser booleano.",
    });
    return;
  }

  const nuevoId =
    libros.length === 0
      ? 1
      : Math.max(...libros.map((libro) => libro.id)) + 1;

  const nuevoLibro: Libro = {
    id: nuevoId,
    titulo: titulo.trim(),
    autor: autor.trim(),
    prestado: prestado,
  };

  libros.push(nuevoLibro);

  res.status(201).json({
    mensaje: "Libro agregado correctamente",
    libro: nuevoLibro,
  });
});

// PUT
// Actualiza un libro
api.put("/books/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id) || id <= 0) {
    res.status(400).json({
      mensaje: "El ID debe ser un número entero positivo",
    });
    return;
  }

  const libroEncontrado = libros.find(
    (libro) => libro.id === id
  );

  if (!libroEncontrado) {
    res.status(404).json({
      mensaje: "Libro no encontrado",
    });
    return;
  }

  if (!req.is("application/json")) {
    res.status(415).json({
      mensaje: "El cuerpo de la solicitud debe enviarse en formato JSON",
    });
    return;
  }

  const { titulo, autor, prestado } = req.body ?? {};

  if (
    typeof titulo !== "string" ||
    titulo.trim() === "" ||
    typeof autor !== "string" ||
    autor.trim() === "" ||
    typeof prestado !== "boolean"
  ) {
    res.status(400).json({
      mensaje:
        "Debe enviar titulo, autor y prestado. El campo prestado debe ser booleano.",
    });
    return;
  }

  libroEncontrado.titulo = titulo.trim();
  libroEncontrado.autor = autor.trim();
  libroEncontrado.prestado = prestado;

  res.status(200).json({
    mensaje: "Libro actualizado correctamente",
    libro: libroEncontrado,
  });
});

// DELETE 
// Elimina un libro
api.delete("/books/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id) || id <= 0) {
    res.status(400).json({
      mensaje: "El ID debe ser un número entero positivo",
    });
    return;
  }

  const posicion = libros.findIndex(
    (libro) => libro.id === id
  );

  if (posicion === -1) {
    res.status(404).json({
      mensaje: "Libro no encontrado",
    });
    return;
  }

  const libroEliminado = libros.splice(posicion, 1)[0];

  res.status(200).json({
    mensaje: "Libro eliminado correctamente",
    libro: libroEliminado,
  });
});

// GET
// Función para ver la Aptitud arquitectonica
api.get("/health/fitness", (_req: Request, res: Response) => {
  const totalLibros = libros.length;

  const librosPrestados = libros.filter(
    (libro) => libro.prestado
  ).length;

  // Evita división entre cero
  const ratioPrestados =
    totalLibros === 0
      ? 0
      : librosPrestados / totalLibros;

  const porcentajePrestados =
    Number((ratioPrestados * 100).toFixed(2));

  // No pueden existir más de 100 libros
  const capacidadValida = totalLibros <= 100;

  // Menos del 80% de los libros deben estar prestados
  const ratioValido = ratioPrestados < 0.8;

  // Si ambas se cumplen
  if (capacidadValida && ratioValido) {
    res.status(200).json({
      estado: "Healthy",
      mensaje: "La arquitectura cumple las restricciones de calidad",
      metricas: {
        librosTotales: totalLibros,
        librosPrestados: librosPrestados,
        porcentajePrestados: porcentajePrestados,
        capacidadMaxima: 100,
        porcentajeMaximoPrestados: 80,
      },
    });

    return;
  }

  // Si alguna falla
  res.status(503).json({
    estado: "Degradacion de Calidad",
    mensaje:
      "La arquitectura no cumple una o más restricciones de calidad",
    metricas: {
      librosTotales: totalLibros,
      librosPrestados: librosPrestados,
      porcentajePrestados: porcentajePrestados,
      capacidadMaxima: 100,
      porcentajeMaximoPrestados: 80,
    },
    restricciones: {
      capacidad: capacidadValida
        ? "Cumple"
        : "No cumple",
      ratioPrestados: ratioValido
        ? "Cumple"
        : "No cumple",
    },
  });
});

// Inicia el servidor
api.listen(PORT, () => {
  console.log(`API ejecutándose en http://localhost:${PORT}`);
});