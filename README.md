# Module to Control Water Quality in Aquaponics
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## International Academic Collaboration
This research project was developed as a collaborative international effort between the **Universidad Politécnica de Juventino Rosas (UPJR)**, Mexico, and the **Faculty of Agronomic Sciences of the Universidad de Chile**. 

The module was created in **2018** within the framework of the **SICES (Second Meeting of Innovation and Creativity for Internationalization at Home)** call, a program dedicated to fostering global academic cooperation and innovation between Mexico and Chile.

---

## Project Overview
The system is a modular and intelligent solution designed for the real-time monitoring of critical environmental and chemical variables in aquaponic environments. By integrating IoT hardware and cloud computing, it ensures a balanced ecosystem for both aquatic life and hydroponic crops.

### Development Methodology
The project was executed in three strategic phases:
*   **Phase 1: Instrumentation** 
    Setting up a hybrid hardware architecture using **Raspberry Pi** and **Arduino** to measure water temperature, ambient humidity, air temperature, and water levels.
*   **Phase 2: Processing & Communication** 
    Developing control logic using **Java** and the **Pi4J library** to manage GPIO pins and interpret raw sensor data for remote visualization.
*   **Phase 3: Cloud & Big Data** 
    Data migration to a cloud infrastructure for mass storage and future implementation of **Artificial Intelligence (AI)** for predictive analysis.

---

## Tech Stack & Hardware

### **Hardware Components**
*   **Main Controllers:** Raspberry Pi (Central Processing) & Arduino (Analog Sensor Interface).
*   **Sensors:** 
    *   **DHT11:** Ambient temperature and humidity.
    *   **DS18B20:** High-precision submersible water temperature.
    *   **YF-S201:** Water flow rate monitoring.
    *   **Ultrasonic Sensor:** Water level measurement.
    *   **PIR Sensor:** Motion detection for system security.

### **Software Stack**
*   **Embedded:** C/C++ (Arduino), Java (Raspberry Pi/Pi4J).
*   **Backend:** Python 3 + Flask (Cloud API).
*   **Frontend:** HTML5, CSS3, and JavaScript (Real-time Dashboard).
*   **Cloud Hosting:** Heroku / Local Server.

---

## Repository Structure

```text
├── arduino/           # .ino firmware for sensor acquisition
├── raspberry/         # Python scripts (bridge between Serial and Cloud)
├── backend/           # Flask API logic and requirements.txt
├── dashboard/         # HTML/JS files for the monitoring interface
└── README.md          # Project documentation

## Citation
If you use this software in your research, please cite it as follows:
```bibtex
@software{Arellano_Module_Control_Water_Quality_Aquaponics},
  author = {Arellano, Maria, et al.},
  title = {Module to Control Water Quality in Aquaponics},
  year = {2018},
  publisher = {Zenodo}
}
