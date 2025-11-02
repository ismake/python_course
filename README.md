# Python Course — Proyecto: Calculadora de Propinas

Este repositorio contiene los ejercicios iniciales del curso **De Cero a Experto en Python**.
El objetivo de este mini-proyecto es practicar la estructura de proyecto, entornos virtuales,
tests con `pytest`, el flujo de trabajo profesional (Git + GitHub) y la depuración con VS Code.

---
## 📂 Estructura del proyecto

```
python_course/
 ├─ src/
 │   └─ propinas.py
 ├─ tests/
 │   └─ test_propinas.py
 ├─ .venv/
 ├─ .vscode/
 ├─ pytest.ini
 └─ README.md
```

---
## ⚙️ Requisitos

- **Python 3.14+** (o cualquier versión 3.x)
- **pip** (gestor de paquetes)
- **pytest** (instalar dentro del entorno virtual)
- **Visual Studio Code** (recomendado) con extensiones **Python** y **Pylance**

---
## 🚀 Instalación / Primera configuración

1. Abrir la terminal en la carpeta del proyecto:
   ```bash
   cd ~/Documents/Python/Projects/python_course
   ```

2. Crear y activar entorno virtual (si no existe):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar dependencias de desarrollo:
   ```bash
   pip install --upgrade pip
   pip install pytest black flake8 ipython
   ```

---
## ▶️ Ejecutar el script de ejemplo

```bash
python src/propinas.py
```

---
## 🧪 Ejecutar tests

```bash
pytest -q
```

Si quieres ejecutar un test específico:
```bash
pytest tests/test_propinas.py -k "nombre_del_test"
```

---
## 🪄 Conectar tu proyecto con GitHub

1. **Inicializa Git en tu proyecto (si no lo has hecho):**
   ```bash
   git init
   ```

2. **Crea un repositorio remoto en GitHub:**
   - Entra a [https://github.com/new](https://github.com/new)
   - Asigna el nombre: `python_course`
   - Marca la opción *“Add a README later”* (ya lo tienes creado localmente)

3. **Conecta el repo local con el remoto:**
   ```bash
   git remote add origin https://github.com/TU_USUARIO/python_course.git
   ```

4. **Haz tu primer commit y push:**
   ```bash
   git add .
   git commit -m "Proyecto base: Calculadora de propinas"
   git branch -M main
   git push -u origin main
   ```

5. **Verifica en GitHub** que el proyecto se subió correctamente.

---
## 🐞 Depurar con breakpoints en VS Code

1. Abre **VS Code** y entra al archivo `src/propinas.py`.
2. Haz clic a la izquierda de la línea donde quieras detener la ejecución (aparecerá un punto rojo: el breakpoint).
3. Abre la pestaña **Run and Debug (▷)** en la barra lateral.
4. Si no existe, crea `.vscode/launch.json` con el siguiente contenido:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Depurar propinas.py",
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}/src/propinas.py",
               "console": "integratedTerminal"
           }
       ]
   }
   ```

5. Presiona **F5** o el botón verde ▶️ para ejecutar en modo depuración.
6. Usa la barra superior de control para avanzar paso a paso o inspeccionar variables.

---
## 💡 Buenas prácticas

- Usa entornos virtuales (`.venv/`) y agrégalo a `.gitignore`.
- Escribe tests pequeños, claros y frecuentes.
- Usa `black` y `flake8` para mantener el código limpio.
- Haz commits atómicos y descriptivos.

---
## 📜 Licencia

Este repositorio es para fines educativos. Puedes agregar aquí la licencia que prefieras (por ejemplo, MIT o GPL).

