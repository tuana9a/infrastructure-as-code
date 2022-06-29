# How to transfer docker images from computers to computers

[https://stackoverflow.com/a/23938978/10459230](https://stackoverflow.com/a/23938978/10459230)

You will need to save the Docker image as a tar file:

```bash
docker save -o <path for generated tar file> <image name>
```

Then copy your image to a new system with regular file transfer tools such as cp, scp or rsync(preferred for big files). After that you will have to load the image into Docker:

```bash
docker load -i <path to image tar file>
```

PS: You may need to sudo all commands.

**EDIT**: You should add filename (not just directory) with -o, for example:

```bash
docker save -o c:/myfile.tar centos:16
```

# **CAUTIONS**

- in production we should separate gitlab and gitlab runner on different machines (virtual machines)

  - and should not share docker engine between them because gitlab runner can shutdown gitlab :yank

- should register gitlab-runner with

```bash
gitlab-runner register
```

- gitlab will use port 22 for `git clone` command so default ssh port should be changed for default cloning behavior

- gitlab require at least **4 GB** of RAM to work
  - if your instance below this value then gitlab will never work
