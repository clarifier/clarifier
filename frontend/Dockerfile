# Build
FROM oven/bun
WORKDIR /app

# For watching files and because no-root is better
RUN useradd -ms /bin/sh -u 1001 app
COPY --chown=app:app . /app
RUN chown app:app /app

USER app
RUN bun i

EXPOSE 5173

CMD ["bun", "dev", "--host", "0.0.0.0"]
