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

### Week 5 — Insight Engine Extension (Analytics Layer)
**Goal:** Add real analytics capability to the multi-city API dashboard by computing statistics and generating human-readable insights.

#### 📊 New Features Added
- Implemented an **analytics module** with:
  - `compute_basic_stats(df)` — calculates:
    - mean  
    - variance  
    - min / max  
    - weekly temperature change  
  - `generate_insights(city, stats)` — produces natural-language insights such as:
    - “Tokyo warmed by 3.2°C over the last week.”
    - “London shows high variance in temperature (unstable weather).”
- Added `save_insights()` to export each city’s insights into:
    data/projects/api_plotter/insights/<city>_insights.txt
- Integrated insights into the main CLI dashboard (`api_plotter.py`):
- After fetching & saving CSVs
- After generating plots
- Dashboard now auto-computes:
  - analytics  
  - insights  
  - insight text files  
- Example CLI:
    ```bash
    cd src
    python -m projects.api_plotter.api_plotter \
    --cities Tokyo London Boston \
    --vars temperature_2m
    ```

### Week 6 — Weekly Insight Engine + Portfolio Polish
**Goal:** Turn the multi-city API dashboard into a recruiter-ready analytics project by adding automated weekly insights, structured outputs, and clean documentation.

#### 📊 New Features Added
- Upgraded analytics pipeline to compute **weekly statistics** from hourly time-series data:
  - mean  
  - variance  
  - min / max  
  - weekly change (last value − first value)  
  - percent change  
- Implemented **auto-detected variable handling**:
  - Supports temperature and non-temperature variables (e.g., wind speed)
  - Insight language adapts automatically (e.g., “warmed/cooled” vs “increased/decreased”)

#### 🧠 Insight Generation Logic
- Built a rule-based insight engine that converts statistics into natural-language summaries:
  - “London warmed by 3.1°C over the past week.”
  - “Wind speed showed high variability this week.”
  - “Temperatures ranged from −2.0°C to 8.5°C.”
- Insights are generated **automatically per city**, not hard-coded.

#### 📁 Output Structure Improvements
- Added professional output organization:
  - Human-readable insight reports (TXT)
  - Machine-readable structured outputs (JSON)

#### 📈 Dashboard Integration
- Integrated insight generation directly into the CLI workflow:
- Data fetch → CSV save → plot generation → analytics → insights
- Single command now produces:
- CSV files
- Single-city plots
- Multi-city comparison plots
- Weekly insight reports

#### 🧪 Example CLI
```bash
cd src
python -m projects.api_plotter.api_plotter \
--cities Tokyo London Boston \
--vars temperature_2m \
--insights
```

### Week 7 — Estimation + Control (Kalman Filter Integration)
**Goal:** Transition from pure data pipelines to robotics-relevant estimation and control concepts, bridging software engineering with robotics fundamentals.
- Focused on state estimation and control theory as a core robotics skill.
- Studied how estimation (Kalman Filter) and control (PID) complement each other in real systems.
- Connected prior PID control work with filtering concepts:
    - Control decides what input to apply
    - Estimation decides what the true system state actually is
- Built intuition around the Estimation → Control → Estimation loop used in:
    - Autonomous vehicles
    - Drones
    - Mobile robots
- Clarified how Kalman Filters act as the “sensor fusion & smoothing layer” feeding reliable state into controllers.

**Key Learning Outcome:**
Modern robotics systems are not control-only or estimation-only — they are tightly coupled pipelines where estimation stabilizes control, and control assumptions inform prediction.

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

### Week 6 - Continue learning about Kalman Filter
- Watched intuition videos on Kalman Filters (no-math versions).
- Wrote a 5-sentence conceptual explanation (estimation, noise handling, prediction/correction loop).
    1. The Kalman filter estimates the true state of a system by combining a mathematical prediction with noisy sensor measurements.
    2. Simple PID control struggles under noise because sensors never report perfect values, causing unstable or jittery behavior.
    3. The prediction step uses a physics model and the previous state to estimate where the robot should be after an input (e.g., throttle or motor command).
    4. The correction/update step adjusts that prediction based on the difference between the predicted value and the actual noisy sensor reading.
    5. Robots rely on Kalman filters because they provide a smooth, reliable estimate of position, speed, or orientation — essential for drones, cars, and manipulators operating in noisy real-world environments.
- Drew a continuous prediction → correction diagram to visualize the loop.

### Week 7 — Kalman Filter + Estimation–Control Pipeline
- Deepened understanding of Kalman Filter beyond intuition videos:
    - Prediction step (motion / system model)
    - Update step (sensor measurement correction)
    - Role of uncertainty (process noise vs measurement noise)
- Explicitly studied estimation vs control responsibilities:
    - Estimation answers: “Where am I really?”
    - Control answers: “What should I do next?”
- Mapped real-world examples:
    - Cruise control (speed estimation + throttle control)
    - Robot localization (position estimate + movement commands)
- Reinforced why Kalman Filters are foundational for:
    - Sensor fusion (IMU + GPS + encoders)
    - Stability under noisy measurements
    - Reliable feedback for controllers
- Conceptual Milestone:
    - Can now clearly explain why Kalman Filters exist, where they sit in the pipeline, and how they interact with controllers — without relying on math-heavy derivations.

### Week 8 — Sensor Fusion & Bias-Aware Estimation (Project #2)
**Primary Focus:** Robotics estimation project (IMU + GPS sensor fusion)

- Designed and implemented a **2D bias-aware Kalman Filter** for IMU + GPS fusion
- Modeled accelerometer bias as a latent state and estimated it via innovation
- Demonstrated how GPS update rate affects:
  - bias observability
  - estimator stability
  - correction magnitude
- Integrated estimation with closed-loop control to show:
  - estimation errors directly affect control performance
  - robust control requires robust state estimation
- Produced comparative simulations for:
  - Fast GPS (0.5s)
  - Slow GPS (2.5s)
  - Very slow GPS (5.0s)
- Saved plots and documented results in a dedicated project README

**Note:** Algorithm practice was deprioritized this week to complete a resume-critical robotics project.

## 💡 LeetCode / Algorithms
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

### Week 5 - Binary Trees
- Watched videos to understand the fundamental.
    - BST Insert and Remove
    - Depth first search
    - Breadth-first search
    - BST sets and maps
    - Iterative DFS

- Learned and practiced: 
    - Invert Binary Tree
    - Maximum Depth of Binary Tree
    - Diameter of binary tree
    - Balanced binary tree

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

### Week 7 — Binary Trees (Medium-Level Confidence)
- Solved / Confident With:
    - Lowest Common Ancestor of a BST
    - Binary Tree Level Order Traversal
    - Binary Tree Right Side View
    - Count Good Nodes in Binary Tree
    - Validate Binary Search Tree
    - Kth Smallest Element in a BST

### Week 8 - Backtracking
- Watched videos to understand the fundamental.
    - Subsets
    - Combination Sum

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