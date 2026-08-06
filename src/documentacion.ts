export const openApiDocument = {
  openapi: "3.0.3",
  info: {
    title: "API básica de productos",
    version: "1.0.0",
    description:
      "API desarrollada con Express y TypeScript para consultar, agregar, actualizar y eliminar productos.",
  },

  servers: [
    {
      url: "http://localhost:3000",
      description: "Servidor local",
    },
  ],

  paths: {
    "/productos": {
      get: {
        summary: "Obtener todos los productos",
        description: "Devuelve la lista completa de productos registrados.",
        responses: {
          "200": {
            description: "Lista de productos obtenida correctamente",
          },
        },
      },

      post: {
        summary: "Agregar un producto",
        description: "Permite registrar un nuevo producto.",
        requestBody: {
          required: true,
          description: "Datos del producto que se desea agregar",
          content: {
            "application/json": {
              schema: {
                type: "object",
                required: ["nombre", "precio"],
                properties: {
                  nombre: {
                    type: "string",
                    description: "Nombre del producto",
                    example: "Delineador NYX",
                  },
                  precio: {
                    type: "number",
                    description: "Precio del producto",
                    example: 75,
                  },
                },
              },
            },
          },
        },
        responses: {
          "201": {
            description: "Producto agregado correctamente",
          },
          "400": {
            description: "Los datos enviados son incorrectos o incompletos",
          },
        },
      },
    },

    "/productos/{id}": {
      get: {
        summary: "Obtener un producto por ID",
        description:
          "Busca un producto utilizando su identificador numérico.",
        parameters: [
          {
            name: "id",
            in: "path",
            required: true,
            description: "Identificador del producto",
            schema: {
              type: "integer",
              example: 1,
            },
          },
        ],
        responses: {
          "200": {
            description: "Producto encontrado correctamente",
          },
          "400": {
            description: "El ID enviado no es válido",
          },
          "404": {
            description: "Producto no encontrado",
          },
        },
      },

      put: {
        summary: "Actualizar un producto",
        description:
          "Permite modificar el nombre y el precio de un producto existente.",
        parameters: [
          {
            name: "id",
            in: "path",
            required: true,
            description: "Identificador del producto que se desea actualizar",
            schema: {
              type: "integer",
              example: 1,
            },
          },
        ],
        requestBody: {
          required: true,
          description: "Nuevos datos del producto",
          content: {
            "application/json": {
              schema: {
                type: "object",
                required: ["nombre", "precio"],
                properties: {
                  nombre: {
                    type: "string",
                    description: "Nuevo nombre del producto",
                    example: "Labial Avon Mate",
                  },
                  precio: {
                    type: "number",
                    description: "Nuevo precio del producto",
                    example: 55,
                  },
                },
              },
            },
          },
        },
        responses: {
          "200": {
            description: "Producto actualizado correctamente",
          },
          "400": {
            description: "Los datos enviados son incorrectos o incompletos",
          },
          "404": {
            description: "Producto no encontrado",
          },
        },
      },

      delete: {
        summary: "Eliminar un producto",
        description:
          "Elimina un producto utilizando su identificador.",
        parameters: [
          {
            name: "id",
            in: "path",
            required: true,
            description: "Identificador del producto que se desea eliminar",
            schema: {
              type: "integer",
              example: 2,
            },
          },
        ],
        responses: {
          "200": {
            description: "Producto eliminado correctamente",
          },
          "400": {
            description: "El ID enviado no es válido",
          },
          "404": {
            description: "Producto no encontrado",
          },
        },
      },
    },
  },
};