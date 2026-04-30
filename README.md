# README

Here, I will build a simple ETL (Extract, Transform, Load) workflow using Docker Compose including two services 1) PostgreSQL to store data and 2) Python to load and process the data. This setup mirrors how real-world data pipelines are often prototyped and tested because Compose gives you a reliable, repeatable way to build and share these workflows

Key steps are highlithed here:
1. Build and run custom Docker images
2. Define multi-service environments with a Compose file
3. Pass environment variables and connect services
4. Use volumes for persistent storage
5. Run, inspect, and reuse your full stack with one command
6. Added a health check to make sure services only start when they’re truly ready.
7. Rewrote your Dockerfile using a multi-stage build, slimming down your image and separating build concerns from runtime needs.
8. Hardened your container by running it as a non-root user and moved configuration into a .env file to make it safer and more shareable.
