# django4_quickstart_template
## docker-compose version

### This is a "prod config" by default, however will show both ways to launch the containers as dev and as prod

#### remember you have to be on the "root" folder (where the app, database, nginx and pgadmin folders are) to run the docker-compose
---

### For both configs follow steps 1 to 6

1. django-admin startproject dbz-proj --template https://github.com/devadalberto/django4_quickstart_template/archive/refs/heads/devdocker.zip
2. cd dbz-proj
3. rename the .env and .devenv sample files

```bash
mv .env.sample .env
or
mv .env.dev.sample .env
```

4. update the PROJECT_NAME on the file (.env and/or .devenv)
5. make sure your entrypoint.\*.sh files have exec permissions (sudo chmod a+x entrypoint.*)

```bash
chmod a+x app/entrypoint.*
```

6. depending on the environment comment/uncomment the lines 8 or 9 from file app/manage.py
   
   By default the config is using the "prod" config


#### PROD Configuration 

```bash
docker-compose up -d --build
```

This config runs on port 8844 (with an nginx as a reverse proxy) and django runs using gunicorn

---

### DEV configuration

```bash
docker-compose -f docker-compose.dev.yml up --build
```

This Dev config runs on port 9000 and django uses it's build in webserver
---

### ToDo

- [X] Doc for PROD deployment
- [X] Modify deployments so they use 2 files: .env & .devenv files
- [X] Finish documentation for DEV deployment
- [ ] Fix code to uncomment the flake8 on the app/Dockerfile
- [ ] Optimize image size
- [ ] Check for Security
- [ ] Automate deployment

### Credits

#### Lot of the code in this project was "proudly borrowed" from other projects, if I miss to list yours here please let me know

1. https://github.com/cookiecutter/cookiecutter-django
2. https://github.com/veryacademy/django-ecommerce-project-v2
