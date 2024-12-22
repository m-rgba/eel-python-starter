# Use Python 3 image
FROM python:3

# Set working directory
WORKDIR /app

# Copy and setup entrypoint
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh && \
    sed -i 's/\r$//' /app/entrypoint.sh

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create directory for mounted volume and set permissions
RUN mkdir -p /src/web/templates && \
    chmod -R 777 /src

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]