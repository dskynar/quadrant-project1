# Qdrant Database Logging & Monitoring Guide

Because your Qdrant instance is running inside an isolated Docker container, its operational logs are managed directly by the Docker daemon rather than the standard Ubuntu system logs (such as `/var/log/syslog`). 

Use the following commands on your **EC2 instance** to inspect, track, and debug incoming API traffic from your local development environment.

---

## Method 1: The Quick Log Dump
To review a historical snapshot of all activities, errors, and system initialization steps since the container was first launched, run:

```bash
docker logs qdrant

```

---

## Method 2: Live Stream Monitoring (Highly Recommended)

To actively monitor inbound vector queries, collection management tasks, or vector embedding uploads from your laptop's Python client script in real-time, attach the follow (`-f`) flag:

```bash
docker logs -f qdrant

```

### Deciphering the Log Stream

When executing Python operations locally, look for structured HTTP logs flashing across your screen. They will resemble the following layouts:

* **Collection Modifications (e.g., creating indices):**
```text
INFO  actix_web::middleware::logger: 12.34.56.78 "POST /collections/my_collection HTTP/1.1" 200 ...

```


* **Payload Embeddings / Vector Vector Searches:**
```text
INFO  actix_web::middleware::logger: 12.34.56.78 "POST /collections/my_collection/points/search HTTP/1.1" 200 ...

```



> 💡 **Tip:** The source IP address captured at the beginning of each entry (e.g., `12.34.56.78`) corresponds directly to your laptop's external network IP.
> 🛑 **To stop the live stream:** Press **`Ctrl + C`** on your keyboard to terminate the view and safely return to your command prompt.

---

## Method 3: View Recent Events (Tail Logs)

If the container remains active for extended periods, the log history can become quite long. To limit your output buffer strictly to the most recent operations, target the last few lines using `--tail`:

```bash
# Display only the 20 most recent API interactions
docker logs --tail 20 qdrant

```

```

```
