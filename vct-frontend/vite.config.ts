import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      "/converse": {
        target: 'http://0.0.0.0:8000',
        changeOrigin: true,
        secure: false,      
        ws: true
      }
    }
  }
})