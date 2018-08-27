# build image
```bash
docker build -t qniu/sshd:debian_jessie .
```

# build run
```bash
docker run -d -p 10022:22 --name debian_sshd qniu/sshd:debian_jessie
```