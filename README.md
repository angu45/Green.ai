# Nova AI Studio — Agentic Workspace Starter

A professional, responsive front-end starter built with HTML, CSS, JavaScript and an optional PyScript/Python helper.

## Features
- ChatGPT-inspired dark workspace UI
- Sidebar tools: chat, writing, ebook outline, image prompt lab and code assistant
- Rule-based prompt router that chooses a workspace by intent
- Local conversation history via browser `localStorage`
- Export conversations and individual outputs as `.txt`
- Attach a local `.txt`, `.md`, `.json` or `.csv` file and include a short excerpt
- Responsive mobile sidebar and accessible live conversation region
- `main.py` demonstrates a Python intent classifier and task planner
- Vercel-ready static project

## Important: what "no API" means
This project intentionally does not pretend to be a full generative AI model. Without a remote model API or downloaded model weights, it uses deterministic templates and routing. It cannot match ChatGPT's general reasoning, generate photorealistic images, or reliably create a complete long ebook from scratch.

For genuine browser-side ML, consider Transformers.js and a compatible small pretrained model. Model weights must be downloaded/cached and may be large; device RAM, GPU/WebGPU support, browser compatibility and licensing matter. Image generation generally needs a compatible image model and substantial compute or a hosted image-generation service.

## Run locally
Because browser module/runtime security varies by browser, use a local static server instead of opening `index.html` as a `file://` URL.

Python installed:
```bash
python -m http.server 8000
```
Open `http://localhost:8000`.

PyScript is loaded from its official CDN; an internet connection is needed for that runtime. The JavaScript UI remains the primary functioning layer if PyScript initialization is unavailable.

## Deploy to Vercel
1. Create a GitHub repository and upload these project files to its root.
2. Sign in to Vercel and import the repository.
3. Use the default static deployment settings; no build command is required.
4. Deploy and test the generated URL on mobile and desktop.
5. Every push to the connected branch can trigger a new deployment.

## Suggested next phase for real model inference
- Text: `@huggingface/transformers` (Transformers.js) with a small compatible text-generation model, after checking model card, license, memory footprint and browser support.
- Python ML: PyScript/Pyodide is suitable for lightweight browser Python utilities, not large GPU training workloads.
- Image generation: integrate an explicitly licensed browser-capable model, or a secure backend/model service. Do not expose private API keys in front-end JavaScript.
- Agent workflow: define tool permissions, step limits, validation, cancellation, error reporting and user confirmation before any external side effects.

## Open-source references
- Transformers.js: https://github.com/huggingface/transformers.js
- PyScript: https://github.com/pyscript/pyscript
- Vercel deployments: https://vercel.com/docs/deployments/overview

## Security and privacy
Conversation history is stored in this browser profile. Clearing site data or using a different browser/device may remove or hide it. Do not store sensitive data in this prototype. Uploaded files are read in-browser; the app does not upload them to a server.
