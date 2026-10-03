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


---

# Entrega HW-03: ejecución completa y autenticación JWT

Esta sección complementa el contenido anterior y contiene el procedimiento completo
para ejecutar la API con autenticación. Los ejemplos de recursos anteriores requieren
ahora el encabezado `Authorization: Bearer <access>`. Para actualizaciones parciales
usa `PATCH`; `PUT` requiere todos los campos obligatorios. DELETE devuelve `204 No Content`.

## Repositorio y rama de entrega

- Repositorio para las entregas: [ValuuVic/arquitectura-de-sistemas](https://github.com/ValuuVic/arquitectura-de-sistemas).
- Rama de esta tarea: [hw-03](https://github.com/ValuuVic/arquitectura-de-sistemas/tree/hw-03).
- README de la entrega: [README.md en hw-03](https://github.com/ValuuVic/arquitectura-de-sistemas/blob/hw-03/README.md).

La rama `hw-03` ya existe y contiene el historial de `main`. Para trabajar en ella:

```bash
git clone https://github.com/ValuuVic/arquitectura-de-sistemas.git
cd arquitectura-de-sistemas
git switch hw-03
```

Si la rama todavía no existiera en otro repositorio, se crea desde `main` con
`git switch main`, `git pull --ff-only` y `git switch -c hw-03`.
No recrees ni sobrescribas la rama de entrega existente.

## Instalación desde cero

Se verificó con Python 3.14, Django 6.1.1 y Django REST Framework 3.18.1.
`requirements.txt` incluye también Simple JWT, PyJWT y python-dotenv.

Desde la raíz del repositorio, donde está `manage.py`, en Windows PowerShell:

```powershell
python -m venv .venv
# Los comandos usan directamente el entorno virtual, sin necesidad de activarlo.
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
# Ejecuta la siguiente copia solo si aún no tienes .env:
Copy-Item .env.example .env
```

En Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
# Solo si todavía no existe .env:
cp .env.example .env
```

## Variables de entorno

Antes de iniciar, edita `.env` y sustituye los dos valores de ejemplo por claves
aleatorias independientes. Genera una clave por ejecución, dos veces:

```powershell
.\.venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(64))"
```

En Linux/macOS usa `python -c "import secrets; print(secrets.token_urlsafe(64))"`.
Guarda una clave en `DJANGO_SECRET_KEY` y la otra en `JWT_SIGNING_KEY`.
No compartas ni subas `.env`; está excluido por `.gitignore`.

| Variable | Descripción | Valor predeterminado |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Secreto de Django, obligatorio | Sin valor |
| `JWT_SIGNING_KEY` | Secreto independiente para firma HS256, mínimo 32 bytes | Sin valor |
| `DJANGO_DEBUG` | Depuración local | `False`; plantilla local: `True` |
| `DJANGO_ALLOWED_HOSTS` | Hosts separados por comas | `localhost,127.0.0.1` |
| `JWT_ACCESS_TOKEN_MINUTES` | Duración del access; entero positivo | `15` |
| `JWT_REFRESH_TOKEN_DAYS` | Duración del refresh; entero positivo | `1` |

Las variables del sistema prevalecen sobre `.env`. En producción utiliza HTTPS,
`DJANGO_DEBUG=False`, hosts específicos y claves propias.

## Crear la base de datos, usuario y servidor

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

En Linux/macOS, con el entorno activado, sustituye
`.\.venv\Scripts\python.exe` por `python`.

La API se ejecuta en `http://127.0.0.1:8000/`. El administrador está en
`http://127.0.0.1:8000/admin/` y conserva la autenticación por sesión de Django.
Las cuentas de autenticación son usuarios activos de Django; un registro de
`Cliente` no equivale a un usuario para login.

## Configuración compatible con los archivos originales

Para conservar los archivos existentes, `config/jwt_settings.py` extiende
`config/settings.py` y `config/jwt_urls.py` incorpora las rutas originales.
El nuevo `manage.py` utiliza `config.jwt_settings` por defecto. Si previamente
definiste `DJANGO_SETTINGS_MODULE`, debe tener el valor `config.jwt_settings`.
No ejecutes la entrega con `--settings=config.settings`, pues ese módulo conserva
la configuración original sin JWT.

Para un servidor WSGI usa `config.jwt_wsgi:application`; para ASGI usa
`config.jwt_asgi:application`, con `DJANGO_SETTINGS_MODULE=config.jwt_settings`.

## Endpoints de autenticación

Todos usan POST y cuerpos JSON con `Content-Type: application/json`:

| Ruta | Cuerpo | Respuesta correcta |
| --- | --- | --- |
| `/api/auth/login/` | `{"username":"tu_usuario","password":"tu_clave"}` | `200`, con `access` y `refresh` |
| `/api/auth/refresh/` | `{"refresh":"<refresh>"}` | `200`, con un nuevo `access` |
| `/api/auth/verify/` | `{"token":"<access>"}` | `200`, con `{}` |

Login valida las credenciales del usuario de Django. `access` se envía en las
solicitudes de recursos; `refresh` solamente se utiliza para renovar el acceso.
Las rutas de autenticación no requieren un token previo.

La validación de recursos utiliza `JWTAuthentication` y `IsAuthenticated` de DRF,
comprobando firma, vencimiento, tipo de token y usuario activo. Los 15 recursos
documentados arriba están protegidos en lectura y escritura, tanto las colecciones
como sus detalles `/api/<recurso>/<uuid>/`. Cualquier usuario activo autenticado
puede realizar las operaciones existentes; no se agregaron roles.

`verify` comprueba firma y vencimiento, pero no que el usuario continúe activo.
La solicitud al recurso protegido y la renovación sí comprueban el usuario.
El refresh mantiene su vencimiento original, sin rotación ni revocación individual.
Al cerrar sesión, el cliente elimina ambos tokens; los tokens emitidos pueden seguir
válidos hasta vencer. Cambiar `JWT_SIGNING_KEY` invalida todos los tokens anteriores.

## Probar desde PowerShell

Con el servidor abierto, ejecuta en otra terminal:

```powershell
$base = 'http://127.0.0.1:8000'
$credentials = Get-Credential -Message 'Usuario y contraseña de Django'
$body = @{
    username = $credentials.UserName
    password = $credentials.GetNetworkCredential().Password
} | ConvertTo-Json

$tokens = Invoke-RestMethod -Method Post -Uri "$base/api/auth/login/" -ContentType 'application/json' -Body $body
$headers = @{ Authorization = "Bearer $($tokens.access)" }
Invoke-RestMethod -Uri "$base/api/productos/" -Headers $headers

$renewed = Invoke-RestMethod -Method Post -Uri "$base/api/auth/refresh/" -ContentType 'application/json' -Body (@{ refresh = $tokens.refresh } | ConvertTo-Json)
Invoke-RestMethod -Method Post -Uri "$base/api/auth/verify/" -ContentType 'application/json' -Body (@{ token = $renewed.access } | ConvertTo-Json)

# Esta solicitud debe fallar con HTTP 401 porque no envía token:
Invoke-RestMethod -Uri "$base/api/productos/"
```

En Postman o Insomnia realiza el login, copia el `access` y configura
Authorization → Bearer Token para consultar o modificar recursos.
Usa la barra final en las rutas. Un access inválido, vencido o manipulado,
o un refresh usado como access, produce `401 Unauthorized`.

## Comprobaciones automáticas

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test config.tests --verbosity 2
.\.venv\Scripts\python.exe -m pip check
```

Las ocho pruebas verifican login, acceso autenticado a los 15 recursos, rechazo
de lecturas y escrituras anónimas, renovación, verificación, tokens inválidos,
vencidos y manipulados, usuarios inactivos y CRUD autenticado de categorías.
Utilizan una base temporal sin modificar los datos de la base local.

## Archivos agregados para completar la entrega

- `manage.py`: comandos de Django con configuración JWT por defecto.
- `requirements.txt`: dependencias para instalar el proyecto.
- `.env.example`: plantilla sin secretos reales.
- `.gitignore`: exclusión de secretos, entorno virtual y archivos locales.
- `config/jwt_settings.py` y `config/jwt_urls.py`: configuración y rutas JWT complementarias.
- `config/jwt_wsgi.py` y `config/jwt_asgi.py`: puntos de entrada con JWT.
- `config/tests.py`: pruebas de autenticación y regresión.
- `ventas/__init__.py`, `ventas/views.py` y `ventas/urls.py`: archivos faltantes de la aplicación de ventas.

Los archivos originales se conservan. El único archivo existente modificado
para esta actualización es `README.md`, al que se añadió esta sección.


