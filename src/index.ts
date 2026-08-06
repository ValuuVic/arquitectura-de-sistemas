import express, { Request, Response } from "express";
import { apiReference } from "@scalar/express-api-reference";
import { openApiDocument } from "./documentacion";

const api = express();
const PORT = 3000;

//permite a la API recibir información en formato JSON
api.use(express.json());
//Devuelve la especificación OpenAPI en formato JSON
api.get("/openapi.json", (_req: Request, res: Response) => {res.status(200).json(openApiDocument);});
// Muestra la documentación de la API con Scalar.
api.use("/docs",
  apiReference({content: openApiDocument, theme: "default",})
);

//estructura de un producto.
interface Producto {
  id: number;
  nombre: string;
  precio: number;
}

//datos temporales que al reiniciar la API vuelven a su estado original
const productos: Producto[] = [
  {
    id: 1,
    nombre: "Labial Avon",
    precio: 40,
  },
  {
    id: 2,
    nombre: "Rubor Bissu",
    precio: 50,
  },
  {
    id: 3,
    nombre: "Gloss Dior",
    precio: 300,
  },
];

//ruta principal para comprobar si la API es funcional
api.get("/", (_req: Request, res: Response) => {
  res.status(200).json({
    mensaje: "API funcionando correctamente",
  });
});

//GET - obtener todos los productos
api.get("/productos", (_req: Request, res: Response) => {
  res.status(200).json(productos);
});

//GET - obtener un producto por medio de su ID
api.get("/productos/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id) || id <= 0) {
    res.status(400).json({
      mensaje: "El ID debe ser un número entero positivo",
    });
    return;
  }

  const productoEncontrado = productos.find(
    (producto) => producto.id === id
  );

  if (!productoEncontrado) {
    res.status(404).json({
      mensaje: "Producto no encontrado",
    });
    return;
  }

  res.status(200).json(productoEncontrado);
});

//POST - agregar un producto
api.post("/productos", (req: Request, res: Response) => {
  const { nombre, precio } = req.body ?? {};

  if (
    typeof nombre !== "string" ||
    nombre.trim() === "" ||
    typeof precio !== "number" ||
    precio <= 0
  ) {
    res.status(400).json({
      mensaje: "Debe enviar un nombre y un precio mayor que 0",
    });
    return;
  }

  const nuevoId =
    productos.length === 0
      ? 1
      : Math.max(...productos.map((producto) => producto.id)) + 1;

  const nuevoProducto: Producto = {
    id: nuevoId,
    nombre: nombre.trim(),
    precio: precio,
  };

  productos.push(nuevoProducto);

  res.status(201).json({
    mensaje: "Producto agregado",
    producto: nuevoProducto,
  });
});

//PUT - actualizar un producto
api.put("/productos/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id) || id <= 0) {
    res.status(400).json({
      mensaje: "El ID debe ser un número entero positivo",
    });
    return;
  }

  const productoEncontrado = productos.find(
    (producto) => producto.id === id
  );

  if (!productoEncontrado) {
    res.status(404).json({
      mensaje: "Producto no encontrado",
    });
    return;
  }

  const { nombre, precio } = req.body ?? {};

  if (
    typeof nombre !== "string" ||
    nombre.trim() === "" ||
    typeof precio !== "number" ||
    precio <= 0
  ) {
    res.status(400).json({
      mensaje: "Debe enviar un nombre y un precio mayor que 0",
    });
    return;
  }

  productoEncontrado.nombre = nombre.trim();
  productoEncontrado.precio = precio;

  res.status(200).json({
    mensaje: "Producto actualizado",
    producto: productoEncontrado,
  });
});

//DELETE - eliminar un producto
api.delete("/productos/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);

  if (!Number.isInteger(id) || id <= 0) {
    res.status(400).json({
      mensaje: "El ID debe ser un número entero positivo",
    });
    return;
  }

  const posicion = productos.findIndex(
    (producto) => producto.id === id
  );

  if (posicion === -1) {
    res.status(404).json({
      mensaje: "Producto no encontrado",
    });
    return;
  }

  const productoEliminado = productos.splice(posicion, 1)[0];

  res.status(200).json({
    mensaje: "Producto eliminado",
    producto: productoEliminado,
  });
});

//inicia el servidor
api.listen(PORT, () => {
  console.log(`API ejecutándose en http://localhost:${PORT}`);
});