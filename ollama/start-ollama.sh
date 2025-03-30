#!/bin/sh

echo "🚀 Starting Ollama..."
ollama serve &

# Wait for API to be ready (optional but clean)
until curl -s http://localhost:11434/api/tags > /dev/null; do
  echo "⏳ Waiting for Ollama to be ready..."
  sleep 2
done

echo "✅ Ollama is ready with model loaded!"
tail -f /dev/null
