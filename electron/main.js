const { app, BrowserWindow } = require('electron');
const path = require('path');
const express = require('express');
const { spawn } = require('child_process');

let win;
let backendProcess = null;

function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: { nodeIntegration: true }
  });
  win.loadURL('http://localhost:3000');
//  win.webContents.openDevTools();
}

function startBackendServer() {
const backendExe = path.resolve(__dirname, 'backend/server'); // Or wherever the exe is
backendProcess = spawn(backendExe, [], { stdio: 'inherit' });

}
app.on('ready', () => {
  // Start the backend server first
  startBackendServer();

  // Start the local HTTP server for React build
  const server = express();
  const buildPath = path.join(__dirname, 'build');
  server.use(express.static(buildPath));
  server.get('/', (req, res) => {
    res.sendFile(path.join(buildPath, 'index.html'));
  });
  server.listen(3000, () => {
    console.log('Serving React app at http://localhost:3000');
    createWindow();
  });
});

app.on('window-all-closed', () => {
  if (backendProcess) backendProcess.kill(); // Stop backend on app close
  if (process.platform !== 'darwin') app.quit();
});

app.on('activate', () => {
  if (win === null) createWindow();
});
