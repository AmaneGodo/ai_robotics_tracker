# 🧠 AI & Robotics Learning Tracker

This repository documents my weekly progress toward becoming a Robotics + AI Software Engineer, with the goal of securing an internship in Summer 2026.

## 🚧 Project Deliverables
### Week 1 — Environment Setup
- Created GitHub repository: ai_robotics_tracker
- Initialized project structure and README
- Installed core libraries: requests, pandas, matplotlib, openpyxl

### Week 2 — API + JSON Plotter
- Built a Python pipeline that fetches weather JSON data (Open-Meteo)
- Converted JSON → Pandas DataFrame → plotted time-series graph
- Practiced:
    - requests for API calls
    - pandas for data processing
    - matplotlib for visualization

### Week 3 - API Plotter -> Dashboard Extension
- Refactored Week 2 project into clean, modular components:
    - `data_handler.py` — builds API URLs, fetches JSON, converts to DataFrame
    - `plot_util.py` — handles plotting logic (single-variable & multi-variable)
    - `api_plotter.py` — main CLI orchestrator that uses the two modules
- Added CLI arguments (e.g., `--vars temperature_2m`) for flexible data selection
- Saved outputs into structured folders:
    - `data/projects/api_plotter/csv/`
    - `data/projects/api_plotter/plots/`
- Successfully ran the project through Python module execution:
    ```terminal
    cd src
    python -m projects.api_plotter.api_plotter --vars temperature_2m
    ```
- Produced hourly temperature plots and CSV outputs for different variables
- Learned the purpose of __init__.py:
    - Marks a folder as a Python package
    - Allows relative imports like:
        ```python
        from .data_handler import build_url
        ```
    - Enables the structure to scale like a real software project
- Improved modularity, readability, and structure

### Week 4 - API Potter -> Multi-City Dashboard Extension
- Added multi-city support (Tokyo, London, Boston)
- Updated CLI to accept ist of cities:
    `--cities Tokyo Boston London`
- Created city -> coordinate mapping 
    - Just the three mentioned aboved for now, simple dictionary for locations
- Implemented multi-series plotting with `plot_multi`.
- Stored outputs in structured folders:
    - data/projects/api_plotter/csv/
    - data/projects/api_plotter/plots/
- Verified CSV outputs + single-city PNGs + combined comparison PNG.
- This project now resembles an internship-ready data pipeline with:
    * CLI interface  
    * Modular code  
    * DataFrame handling  
    * Multi-series visualization  

## 🤖 Robotics / AI Practice
### Week 1 — Foundation & Setup
- Installed robotics-related libraries: numpy, pandas, matplotlib, requests, opencv-python
- Verified Python environment (python --version, pip list)
- Explored how JSON and arrays represent real-world sensor streams
- Watched “ROS2 Explained in 15 Minutes” for conceptual overview

### Week 2 — Numerical Foundations
- Strengthened vector/matrix intuition using NumPy
- Implemented dot and cross products by hand and with NumPy
- Visualized 2D motion with Matplotlib
- Key concept learned: “Robotics is math in motion.”

### Week 3 — PID Control Simulation
- Watched “PID Control Explained: Ultimate Guide”
- Simulated P, PI, and PID controllers in Python
- Observed overshoot, settling behavior, and steady-state error
- Produced visual comparison of P vs PI vs PID
- Code: src/robotics/pid_control_demo.py
- Plot: data/robotics/pid_tuning_ccomparison.png

### Week 4 - PID Control With Seonsor Noise
- Added measurement noise to PID simulation to mimic real robotic sensors
    ```python
    measured = true_position + np.random.normal(0, 0.3)
    ```
- Observed how noise affecs control stability (especially the derivative term)
- Implemented PID ccorrection using measured (noisy) sensor data
- Tuned parameters to reduce oscillations while eliminating steady-state error:
    - Lowering K_derivative prevents noise from explodinng derivative.
    - Increasinng k_integral removes steady-state error.
    - Increasing k_proportional leads to faster response but could cause overshoot when too much.
- Plotted:
    - True Position
    - Noisy Sensor Measurement
    - PID Corrected Output
- Learned why robots needs filatering (noise -> instability) and how PID reactes.

### Week 5 – Why Robots Need Filters (Kalman Filter Foundations)
- Watched “Kalman Filter Explained Simply” to understand filter intuition.
- Learned why robots cannot rely on raw sensor readings due to noise, drift, and imperfect measurements.
- Studied how PID controllers struggle with noisy signals, especially the derivative term, which amplifies randomness and causes unstable corrections.
- Understood the purpose of the Kalman Filter:
    - Predict the next state using a motion model
    - Compare it with the noisy sensor reading
    - Combine them into the best estimate using uncertainty weights
- Wrote a clean 5-sentence explanation summarizing:
    - Why robots need filters
    - Why PID alone fails
    - How the Kalman Filter improves state estimation
- Drew and documented the classic Predict → Update → Repeat loop diagram.

## 💡 NeetCode / Algorithms
### Week 1 — Sliding Window Patterns
- Practiced:
    - Best Time to Buy & Sell Stock
    - Longest Substring Without Repeating Characters
    - Longest Repeating Character Replacement
    - Permutation in String
    - Minimum Window Substring
    - Sliding Window Maximum

### Week 2 — Linked List Patterns
- Practiced:
    - Reverse Linked List
    - Merge Two Sorted Lists
    - Reorder List
    - Remove Nth Node From End of List
    - Copy List With Random Pointer

### Week 4 – Linked Lists II (Implementation Confidence)
- This week's main focus was to not just to learn but also to be comfortable to solve on my own. 
    - Reverse Linked List
    - Merge Two Sorted Lists
    - Reorder List
    - Remove Nth Node From End of List
    - Copy List With Random Pointer


**Completed:**
- Reversed Linked List (self-coded)  
- Merge Two Sorted Lists (self-coded)  
- Reorder List (self-coded)  
- Remove Nth Node (self-coded)  
- Copy List With Random Pointer (self-coded)  
- Add Two Numbers (retry independently; understanding improved)  

**Notes / Growth:**
- Core pointer manipulation patterns becoming more intuitive.  
- Able to write solutions from memory after guided practice.  
- Still improving “problem → code” translation speed.  

## 🌐 Networking Progress
### Week 1 — Profile Setup
- Updated LinkedIn profile
- Added Merrimack MSCS (AI) information
- Posted an intro about starting graduate studies
- Followed 10 companies in AI/Robotics

### Week 2 — Connect & Observe
- Sent 10+ connection requests to Merrimack classmates
- Joined 3 LinkedIn communities on AI/Robotics
- Followed two open-source robotics repositories:
    - ros2/ros2
    - cyberbotics/webots

### Week 3 - Continue connecting
- Updated my about page on LinkedIn 
- Added my ai robotics project detail in experience. 
- Liked two posts for sllight engagement
    - Google Deepmind
    - NVIDIA
- followed Jensen Huang and connected with NCSU alumni

### Week 4 – Continued Visibility 
- Updated Featured section on LinkedIn:
  - Added GitHub repo link for API Dashboard + Robotics simulations.
  - Added multi-city plot image as visual project proof.
- Maintain weekly micro-engagement (2–3 robotics posts).
- Connect with 2 more engineers in robotics / SWE.