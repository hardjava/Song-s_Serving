# 🧾 Song’s Serving
- A lightweight robot assistant that delivers small items (e.g., water, tissues, spoons) to restaurant tables upon request, helping reduce staff workload in busy environments.

## 🛠 Skills
![Java](https://img.shields.io/badge/Java-%23ED8B00.svg?style=flat&logo=java&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-%236DB33F.svg?style=flat&logo=springboot&logoColor=white)
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-%23000000.svg?style=flat&logo=flask&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-%2300979D.svg?style=flat&logo=arduino&logoColor=white)

## 📌 Overview
- While dining at a crowded restaurant, I noticed that staff were overwhelmed with serving main dishes, while customers were constantly requesting minor items like water or tissues.
These small requests often caused delays.
- I developed Song’s Serving to solve this — a simple robot system that autonomously delivers basic items to the correct table.

## ⚙️ Main Functions
- Customers place requests through a web form (select table + items).

- A Flask server receives the request and queues it via a Tkinter-based desktop UI.

- Staff can confirm or cancel the request.

- Upon confirmation, an Arduino robot navigates to the selected table using line-tracing with IR sensors and intersection count.

- Communication between Flask and Arduino is handled via HC-06 Bluetooth.
