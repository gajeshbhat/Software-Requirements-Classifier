# Use the official Ollama base
FROM ollama/ollama:latest

# Pre-pull the desired model (IMPORTANT: must be done AFTER ollama serve is up)
RUN mkdir -p /models

# Start server temporarily to allow pulling
RUN bash -c "ollama serve & sleep 5 && ollama pull codellama:instruct"

# Copy your startup script
COPY start-ollama.sh /start-ollama.sh
RUN chmod +x /start-ollama.sh

# Start Ollama server on boot
ENTRYPOINT ["/bin/sh", "/start-ollama.sh"]
