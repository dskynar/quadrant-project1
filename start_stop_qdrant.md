# Qdrant Database Lifecycle Management Guide

This guide outlines the standard operational commands to start, stop, inspect, and restart your Qdrant vector database container on your EC2 instance.

---

## 1. Starting Qdrant
To spin up a new Qdrant instance, navigate to your project directory (e.g., `~/quadrant-project1`) where your local `qdrant_storage` folder lives, and run the following command. 

*Note: This command includes the `-d` (detached) flag to run the container as a background service, freeing up your terminal.*

```bash
docker run -d --name qdrant \
    -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant

```

### Breakdown of Flags used:

* **`-d`**: Detached mode (runs the container in the background).
* **`--name qdrant`**: Assigns a friendly name so you don't have to look up a random container ID to stop it.
* **`-p 6333:6333 -p 6334:6334`**: Maps the HTTP and gRPC ports from inside the container to your EC2 instance.
* **`-v ...`**: Mounts your local storage folder to keep data persistent even if the container is destroyed.

---

## 2. Checking Status

To verify that the container started successfully and is listening on the mapped ports, list all active Docker containers:

```bash
docker ps

```

Look for `qdrant` under the **NAMES** column and ensure the status reads `Up (X time)`.

---

## 3. Stopping Qdrant

When you need to pause your database (e.g., to perform system maintenance or reduce CPU overhead), cleanly shut down the container using its assigned name:

```bash
docker stop qdrant

```

*This safely stops the engine processes inside the container without deleting any of your vectors or collection layouts stored on disk.*

---

## 4. Restarting an Existing Container

If you have already stopped the container using the command above, **do not run `docker run` again** (doing so will throw a name conflict error). Instead, simply wake up the existing configuration:

```bash
docker start qdrant

```

---

## 5. Completely Removing the Container

If you ever want to update the underlying Qdrant image version or change the network ports, you must destroy the old container envelope before running a new `docker run` command:

```bash
# Stop it first
docker stop qdrant

# Remove the container envelope
docker rm qdrant

```

> 🔒 **Data Safety Note:** Running `docker rm` will **not** delete your vector databases or schemas. Because you used a volume mount (`-v`), all actual collection data remains completely safe inside your local `~/quadrant-project1/qdrant_storage` directory!

```

```
