# Frontend (Untitled UI + Vite)

Este frontend vive en `./frontend` y está basado en el **starter kit de Untitled UI para Vite**.

## Requisitos

- Node.js (LTS recomendado)
- npm


### 2) Descargar el starter kit (Vite)

- Descarga el starter kit desde:
  - https://www.untitledui.com/react/integrations/vite 

  npx untitledui@latest init untitled-ui --vite 

### 3) Asegurar que el proyecto quede al nivel correcto

A veces al descomprimir queda una carpeta anidada, por ejemplo:

- `frontend/untitled-ui/package.json`

El objetivo es que los archivos del proyecto queden directamente en `frontend/`:

- `frontend/package.json`
- `frontend/index.html`
- `frontend/src/`
- `frontend/vite.config.ts`

Si estaba anidado, mueve el contenido “hacia arriba” y elimina la carpeta extra.

### 4) Instalar dependencias

Desde `./frontend`:

```bash
npm install
```

Esto descargará todas las dependencias en `node_modules/` usando `package.json` / `package-lock.json`.

### 5) Ejecutar el servidor de desarrollo

```bash
npm run dev
```

Abre:

- http://localhost:5173/

## Notas rápidas

- `npm install` es necesario cuando:
  - Descargas/clonas un proyecto nuevo
  - Cambia `package.json` o `package-lock.json`
  - Borras `node_modules/`
- Las rutas principales se definen en:
  - `src/main.tsx`
- La pantalla inicial del starter kit está en:
  - `src/pages/home-screen.tsx`

## Recursos

- Untitled UI React: https://www.untitledui.com/react
- Docs: https://www.untitledui.com/react/docs/introduction
