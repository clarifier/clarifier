# Build
FROM oven/bun
WORKDIR /app
COPY . /app
RUN bun i
EXPOSE 5173
CMD ["bun", "dev", "--host", "0.0.0.0"]
