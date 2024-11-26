
# py-sql-executor

Este proyecto es una herramienta diseñada para gestionar y manipular scripts SQL de manera eficiente.

## Guía de instalación

### 1. Crear un entorno virtual

Para crear un entorno virtual, ejecuta el siguiente comando en tu terminal:

```bash
python -m venv venv
```
Si o esta instaldo venv realizar los siguiente:

```bash
pip install venv
```

### 2. Instalar los requisitos

Asegúrate de estar en el directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias requeridas:

```bash
pip install -r requirements.txt
```

### 3. Activar el entorno virtual

Para activar el entorno virtual, utiliza uno de los siguientes comandos según tu sistema operativo:

- En **Windows**:
```bash
venv\Scripts\activate
```

- En **Linux o macOS**:
```bash
source venv/bin/activate
```

### 4. Ejecutar el script principal

Finalmente, para ejecutar el script principal del proyecto, usa el siguiente comando:

```bash
python main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.


## Configuración de Ruff Fix en IntelliJ IDEA

Para configurar Ruff Fix como una herramienta externa en IntelliJ IDEA:

1. Abre IntelliJ IDEA
2. Ve a `File` > `Settings` (en Windows/Linux) o `IntelliJ IDEA` > `Preferences` (en macOS)
3. Navega a `Tools` > `External Tools`
4. Haz clic en el botón `+` (más) para añadir una nueva herramienta
5. Configura la herramienta con los siguientes detalles:
   - **Name**: `Ruff Fix`
   - **Program**: `ruff` (o la ruta completa al ejecutable de ruff)
   - **Arguments**: `check --fix`
   - **Working directory**: `$ProjectFileDir$`

### Uso de la herramienta
- Puedes encontrar la herramienta en `Tools` > `External Tools` > `Ruff Fix`
- También puedes configurar un atajo de teclado personalizado para ejecutarla rápidamente

### Requisitos
- Asegúrate de tener Ruff instalado en tu entorno de Python
- Puedes instalarlo con: `pip install ruff`