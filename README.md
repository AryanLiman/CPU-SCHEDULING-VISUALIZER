# CPU Scheduling Visualizer

An educational Operating System mini-project that simulates **FCFS**, **non-preemptive SJF**, and **Round Robin** scheduling in a Flask web application.

## Features

- Enter process ID, arrival time, and burst time.
- Select FCFS, non-preemptive SJF, or Round Robin.
- Set the Round Robin time quantum.
- Calculate Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT).
- Show average waiting and turnaround times.
- Visualize CPU execution with a Gantt chart, including idle time.
- Validate input values and show helpful error messages.
- Responsive interface for desktop and mobile screens.

## Requirements

- Python 3.9 or newer
- pip
- A modern web browser

## Run locally

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. (Recommended) Create and activate a virtual environment.

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the application:
   ```bash
   python app.py
   ```
6. Open the local address printed in the terminal (normally `http://127.0.0.1:5000`).

Press `Ctrl+C` in the terminal to stop the server.

## Input format

Enter one process per line:

```text
ProcessID, ArrivalTime, BurstTime
```

Example:

```text
P1,0,5
P2,1,3
P3,2,1
```

Arrival time must be a non-negative integer. Burst time and Round Robin time quantum must be positive integers. Process IDs must be unique.

## Scheduling and formulas

- **FCFS:** executes processes in arrival order.
- **SJF:** non-preemptive; selects the shortest burst among processes that have arrived and are ready.
- **Round Robin:** runs each ready process for at most the selected time quantum before placing unfinished processes at the back of the ready queue.
- `TAT = CT - AT`
- `WT = TAT - BT`
- Average WT = total WT / number of processes
- Average TAT = total TAT / number of processes

## Project structure

```text
CPU_Scheduling_Visualizer_GitHub/
├── app.py
├── scheduler.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Upload to GitHub

1. Sign in to GitHub and choose **New repository**.
2. Name it `cpu-scheduling-visualizer`.
3. Keep it public or private as required by your course.
4. Upload the extracted project files (not the ZIP itself if you want GitHub to display the source files directly), or use Git:

   ```bash
   git init
   git add .
   git commit -m "Add CPU Scheduling Visualizer"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/cpu-scheduling-visualizer.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to authenticate, follow GitHub's current sign-in instructions.

## Academic details

- **Project title:** CPU Scheduling Visualizer
- **Subject:** Operating System
- **Student name in supplied report:** Aryan Liman
- **Roll number in supplied report:** 44

## Limitations / future scope

This version implements FCFS, non-preemptive SJF, and Round Robin. Future extensions could include SRTF, priority scheduling, downloadable reports, saved simulations, and step-by-step ready-queue animation.

## License

For educational use. Add a license file if you want to specify reuse terms.
