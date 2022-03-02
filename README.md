<p align='center'> <img src="https://i.ibb.co/Nt69GbB/chappy.png" alt="chappy" height="80" border="0"> </p>

## 💼 The project

#### 📝 Description :

chappy is a Django multiapp who allow user to shop christmas themed product and chat with connected users.

#### 💡 Features :

- Shop (listing & incrementing)
- Authentifiation
- Online Chat
- Connected & disconnected status
- Group chat

#### 👩🏾‍💻 Built With :

This project was carried out with the use of the following languages :

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Socket.io](https://img.shields.io/badge/Socket.io-010101?&style=for-the-badge&logo=Socket.io&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)


for the database: 

![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


## 📺 Getting Started

#### 🔐 Prerequisites: 


- [ ] Python 3 `https://nodejs.org/en/download/ ` 

- [ ] Docker desktop `https://nodejs.org/en/download/ ` 

- [ ] DB Browser for SQLite
  
- [ ] Pillow

```sh
   pip3 install Pillow
   ```

- [ ] Channels_redis 3.3.1

```sh
  pip3 install channels_redis==3.3.1
   ```


#### 💾 Installation :

- [ ] Clone the repo :

  ```sh
     git clone https://github.com/fifi-dev/Django-initalization.git
     ```

- [ ] Open Docker desktop

- [ ] Run the Redis Container

   ```sh
   docker run -p 6379:6379 -d redis:5
   ```

- [ ] run the project

  ```sh
     python3 manage.py runserver
     ```
   

### Folder Structure

    .
    ├── chat                    # Test files (alternatively `spec` or `tests`)
    │   ├── migrations          # Load and stress tests
    │   ├── static                    # Test files (alternatively `spec` or `tests`)
    │   ├── templates                    # Test files (alternatively `spec` or `tests`)  
    │   ├── admin.py   
    │   ├── apps.py
    │   ├── consumers.py
    │   ├── models.py
    │   ├── routing.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    ├── course                    # Test files (alternatively `spec` or `tests`)
    │   ├── asgi.py          # Load and stress tests
    │   ├── settings.py         # End-to-end, integration tests (alternatively `e2e`)
    │   └── urls.py                # Unit tests
    │   └── wsgi.py                # Unit tests
    ├── firstApp                    # Test files (alternatively `spec` or `tests`)
    │   ├── migrations          # Load and stress tests
    │   ├── static                    # Test files (alternatively `spec` or `tests`)
    │   ├── templates                    # Test files (alternatively `spec` or `tests`)  
    │   ├── admin.py   
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py 
    ├── santaHood                    # Test files (alternatively `spec` or `tests`)
    │   ├── migrations          # Load and stress tests
    │   ├── static                    # Test files (alternatively `spec` or `tests`)
    │   ├── templates                    # Test files (alternatively `spec` or `tests`)  
    │   ├── admin.py   
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py 
    ├── db.sqlite3
    ├── db.sqlite3-journal
    ├── manage.py
    └── README.md

### Admin

- id

```sh
   superuser
   ```

- password

```sh
   12345678
   ```

#### 🤝 Contributing :

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

- Fork the Project
- Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
- Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the Branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request



## 🏆 Credits :


- BAZANA NTOMO Fideline `https://github.com/fifi-dev`


## 📜 Licence
 <a align="center"  rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>

