# Arquitectura de Sistemas 1

## Nombre
Ana Valeria Vicente Axpuac

## Carné
202408029

## Curso
Arquitectura de Sistemas

## Semestre
6to semestre

## Carrera
Ingeniería en sistemas, informática y ciencias de la comunicación


# API Django - HW 03

API REST desarrollada utilizando Django y Django REST Framework.

La API implementa un sistema modular compuesto por cinco aplicaciones principales: clientes, productos, ventas, inventario y proveedores.

El proyecto cuenta con 15 modelos relacionados entre sí mediante relaciones entre entidades. Cada modelo utiliza UUID como identificador principal, eliminación lógica mediante soft delete y campos automáticos para controlar la fecha de creación y modificación de los registros.

Además, se implementó el sistema de migraciones de Django para administrar la creación y modificación de la estructura de datos.


# Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Git


# Requisitos

Para ejecutar el proyecto es necesario tener instalado:

- Python 3.x
- pip


# Instalación

Después de descargar o clonar el repositorio, abrir una terminal dentro de la carpeta del proyecto.


## Crear entorno virtual

```bash
python -m venv .venv
```


## Activar entorno virtual

En Windows PowerShell:

```powershell
.venv\Scripts\activate
```

En Linux/Mac:

```bash
source .venv/bin/activate
```


## Instalar dependencias

Ejecutar:

```bash
pip install -r requirements.txt
```


# Configuración de la base de datos

El proyecto utiliza SQLite como base de datos local.

Para crear las tablas mediante las migraciones de Django ejecutar:

```bash
python manage.py migrate
```


Para generar nuevas migraciones después de modificar modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```


# Ejecución

Ejecutar la API con:

```bash
python manage.py runserver
```

Cuando el servidor se inicie correctamente aparecerá un mensaje similar a:

```text
Starting development server at http://127.0.0.1:8000/
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```


# Estructura del proyecto

El proyecto está dividido en cinco aplicaciones principales:

```text
clientes
productos
ventas
inventario
proveedores
```

Cada aplicación contiene sus respectivos modelos, serializers, vistas y rutas para exponer los recursos mediante una API REST.


# Aplicaciones desarrolladas


## Clientes

Permite administrar la información relacionada con los clientes del sistema.

Modelos:

- Cliente
- Direccion
- Contacto

Endpoints:

```text
/api/clientes/
/api/direcciones/
/api/contactos/
```


## Productos

Gestiona la información relacionada con productos, categorías y marcas.

Modelos:

- Categoria
- Marca
- Producto

Endpoints:

```text
/api/categorias/
/api/marcas/
/api/productos/
```


## Ventas

Administra órdenes de compra, detalles de órdenes y facturación.

Modelos:

- OrdenCompra
- DetalleOrden
- Factura

Endpoints:

```text
/api/ordenes/
/api/detalles/
/api/facturas/
```


## Inventario

Controla la información relacionada con almacenamiento y movimientos de productos.

Modelos:

- Bodega
- MovimientoInventario
- InventarioProducto

Endpoints:

```text
/api/bodegas/
/api/movimientos/
/api/inventario/
```


## Proveedores

Administra proveedores, servicios disponibles y contratos establecidos.

Modelos:

- Proveedor
- ServicioProveedor
- ContratoProveedor

Endpoints:

```text
/api/proveedores/
/api/servicios/
/api/contratos/
```


# Características de los modelos

Todos los modelos implementados cuentan con:

- Identificador UUID como llave primaria.
- Campo de eliminación lógica mediante soft delete.
- Fecha de creación automática.
- Fecha de modificación automática.


Además, se utilizaron diferentes tipos de datos:

- CharField
- TextField
- IntegerField
- PositiveIntegerField
- FloatField
- DecimalField
- BooleanField
- DateField
- DateTimeField
- EmailField
- ForeignKey
- OneToOneField


# Ejemplos de uso


## Obtener productos

```http
GET http://127.0.0.1:8000/api/productos/
```


## Obtener producto por ID

```http
GET http://127.0.0.1:8000/api/productos/{id}/
```


## Crear producto

```http
POST http://127.0.0.1:8000/api/productos/
```

Ejemplo de cuerpo JSON:

```json
{
    "categoria": "uuid_categoria",
    "marca": "uuid_marca",
    "nombre": "Laptop Lenovo",
    "descripcion_corta": "Laptop para trabajo y estudio",
    "precio": 6500.00,
    "cantidad": 10,
    "disponible": true
}
```


## Actualizar producto

```http
PUT http://127.0.0.1:8000/api/productos/{id}/
```


Ejemplo de cuerpo JSON:

```json
{
    "nombre": "Laptop Lenovo ThinkPad",
    "precio": 7200.00
}
```


## Eliminar producto

```http
DELETE http://127.0.0.1:8000/api/productos/{id}/
```


# Códigos de respuesta

`200 OK`  
La consulta, actualización o eliminación se realizó correctamente.

`201 Created`  
El registro fue creado correctamente.

`400 Bad Request`  
Los datos enviados son incorrectos o están incompletos.

`404 Not Found`  
El recurso solicitado no existe.


# Migraciones

El proyecto utiliza el sistema de migraciones de Django para administrar los cambios en la estructura de datos.

Se realizaron:

- Migraciones iniciales para la creación de modelos.
- Migraciones posteriores para modificar campos existentes y demostrar el flujo de actualización de estructura.


Comandos utilizados:

```bash
python manage.py makemigrations

python manage.py migrate
```


# Pruebas

La API puede probarse utilizando herramientas como:

- Postman
- Insomnia
- Navegador mediante Django REST Framework


Para solicitudes POST y PUT se debe enviar la información en formato JSON.


