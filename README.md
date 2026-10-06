# ORBITRA'26 WebGL 3D Website

Interactive 3D WebGL experience built on the PlayCanvas engine.

---

## 🚀 How to Run Locally

Because WebGL applications load binary assets (`.glb` 3D models, `.wasm` modules, `.basis` compressed textures, and JSON configuration files), they must be served through an HTTP server rather than opened directly via `file://`.

### Option 1: One-Click Launch (Windows)
Double-click [start.bat](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/start.bat). It will automatically start the server and open your default browser.

### Option 2: Using Node.js
```bash
node serve.js
```
Then visit [http://localhost:3000](http://localhost:3000).

### Option 3: Using Python
```bash
python server.py
```
Then visit [http://localhost:3000](http://localhost:3000).

---

## 📁 Project Architecture

- [index.html](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/index.html) - Application entry point.
- [styles.css](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/styles.css) - Responsive viewport, aspect-ratio reflow, and full-bleed WebGL canvas styling.
- [playcanvas-stable.min.js](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/playcanvas-stable.min.js) - PlayCanvas WebGL/WebGPU 3D rendering engine.
- [__settings__.js](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/__settings__.js) - Context options (WebGL2/WebGL1), script registry, and Basis transcoder configuration.
- [__start__.js](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/__start__.js) - Canvas initialization, graphics device creation, and scene loading pipeline.
- [__loading__.js](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/__loading__.js) - Preloader UI with typography and GSAP transitions.
- [config.json](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/config.json) - Complete PlayCanvas asset registry mapping all materials, textures, shaders, audio, models, and scripts.
- [2509662.json](file:///c:/Users/Navlesh%20Singh/Desktop/New%20folder/New%20folder/2509662.json) - Main 3D scene definition (entities, lights, cameras, and components).
- `files/assets/` - Local repository of all 3D assets:
  - GLB 3D models (compute trays, pods, satellite, architecture)
  - Basis Universal compressed texture assets
  - WebAssembly Basis transcoders (`basis.wasm.js`, `basis.wasm.wasm`)
  - Audio effects & ambiances
  - Custom game and interaction scripts
