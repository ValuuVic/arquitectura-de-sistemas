### Arquitectura de Sistemas 1
#### Nombre
Ana Valeria Vicente Axpuac
#### Carné
202408029
#### Curso
Arquitectura de Sistemas 
#### Semestre
6to semestre
#### Carrera
Ingeniería en sistemas, informatica y ciencias de la comunicación

### API de productos - HW 01

API REST sencilla desarrollada con Node.js, Express y TypeScript.
La API permite consultar, agregar, actualizar y eliminar productos utilizando los métodos HTTP GET, POST, PUT y DELETE.
La información se almacena temporalmente en un arreglo, por lo que no se utiliza una base de datos.

#### Tecnologías utilizadas

- Node.js
- Express
- TypeScript
- npm

#### Requisitos

Para ejecutar el proyecto es necesario tener instalado:
- Node.js
- npm

#### Instalación

Después de descargar o clonar el repositorio, abrir una terminal dentro de la carpeta del proyecto.
Instalar las dependencias con:

```bash
npm install
```

En Windows PowerShell también se puede utilizar:

```powershell
npm.cmd install
```

#### Ejecución

Ejecutar la API con:
```bash
npm run dev
```
En Windows PowerShell:
```powershell
npm.cmd run dev
```
Cuando el servidor se inicie, aparecerá un mensaje similar a:

```text
API ejecutándose en http://localhost:3000
```
La API estará disponible en:

```text
http://localhost:3000
```
#### Ejemplos de uso

##### Obtener todos los productos

```http
GET http://localhost:3000/productos
```

##### Obtener un producto por ID

```http
GET http://localhost:3000/productos/1
```

##### Agregar un producto

```http
POST http://localhost:3000/productos
```

Cuerpo de la solicitud en formato JSON:

```json
{
  "nombre": "Delineador NYX",
  "precio": 75
}
```

##### Actualizar un producto

```http
PUT http://localhost:3000/productos/1
```

Cuerpo de la solicitud en formato JSON:

```json
{
  "nombre": "Labial Avon Mate",
  "precio": 55
}
```

##### Eliminar un producto

```http
DELETE http://localhost:3000/productos/2
```

#### Códigos de respuesta

`200 OK` La consulta, actualización o eliminación se realizó correctamente 
`201 Created` El producto fue creado correctamente 
`400 Bad Request` Los datos enviados son incorrectos o están incompletos 
`404 Not Found` El producto solicitado no existe 

#### Pruebas
Puede probarse utilizando Insomnia. 
Para las solicitudes POST y PUT se debe seleccionar el cuerpo de tipo JSON y enviar los campos `nombre` y `precio`.

#### Almacenamiento

Los productos se almacenan temporalmente en un arreglo dentro de la aplicación.
Los productos agregados, modificados o eliminados regresarán a su estado original cuando el servidor se reinicie, ya que la API no utiliza una base de datos. 
