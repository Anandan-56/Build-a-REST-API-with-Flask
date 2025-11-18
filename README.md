REST API with Flask – User Management

This project is part of **Task 4**: Build a REST API using Flask.
The API allows you to **Create, Read, Update, Delete (CRUD)** user data using in-memory storage.

---

📘 Objective

Build a RESTful API that manages user information such as name and email using Python and Flask.

---

 🛠 Tools & Technologies

Python
Flask
Postman (API testing)
In-memory dictionary** for data storage

 📂 **Project Structure**

```
project-folder/
│── app.py
│── README.md
```

---

🚀 How to Run the Project

### 1️⃣ Install Flask

Open terminal and run:

```bash
pip install flask
```

2️⃣ Run the Flask Server

Run the app:

```bash
python app.py
```

If successful, you will see:

```
 * Running on http://127.0.0.1:5000
```

Keep this terminal window open

---

# 📡 **API Endpoints**

 ✔ 1. Create User (POST)
 <img width="1920" height="1080" alt="Screenshot (504)" src="https://github.com/user-attachments/assets/ca282ad0-6c7a-43f3-a2da-f6ba9a6303a1" />




✔ 2. Get All Users (GET)

**URL:**

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ea1a4177-b234-44ed-92a6-26ab534806ec" />


## ✔ **3. Get User by ID (GET)**

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/30f3872a-26b1-473a-afb5-cae3b8ca1216" />


✔ 4. Update User (PUT)



<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3eefa77b-89ae-4a1b-86a2-ade06549e6ef" />


5. Delete User (DELETE)**

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1374197f-0960-40a4-84ef-3e9234eb7518" />


# 📝 **In-Memory Data Storage**

Users are stored in a Python dictionary:

```python
users = {
  1: {"id": 1, "name": "John", "email": "john@example.com"}
}
```

This resets every time the server restarts.

---

🧪 Testing

You can test using:

👉 Postman

* Create New Request → Choose method (POST/GET/PUT/DELETE)
* Enter URL
* Set Body → raw → JSON for POST/PUT

 👉 cURL 

Example POST request:

```bash
curl -X POST http://127.0.0.1:5000/users ^
     -H "Content-Type: application/json" ^
     -d "{\"name\":\"John\", \"email\":\"john@example.com\"}"
```

---


