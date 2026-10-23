# CPU Scheduling Visualizer — Mini Project Report

## 1. Introduction
An operating system manages hardware and software resources and controls the execution of processes. CPU scheduling decides which ready process receives CPU time. This project demonstrates three scheduling policies through an interactive web interface.

## 2. Problem Statement
Manual simulation requires repeated calculations of execution order, completion time, turnaround time, and waiting time. This application automates those calculations and displays results in a table and Gantt chart.

## 3. Objectives
1. Understand CPU scheduling.
2. Implement FCFS, non-preemptive SJF, and Round Robin.
3. Accept process information from the user.
4. Calculate CT, TAT, WT, and their averages.
5. Display the CPU execution order through a Gantt chart.
6. Compare the results of scheduling algorithms.

## 4. Hardware and Software Requirements
### Hardware
- Dual-core processor or equivalent
- 4 GB RAM recommended
- 500 MB free storage
- Keyboard, mouse, and display

### Software
- Windows, Linux, or macOS
- Python 3.9+
- Flask
- HTML5 and CSS3
- Modern web browser
- VS Code or another code editor

## 5. Algorithms
### FCFS
1. Sort processes by arrival time.
2. If the CPU is idle, advance to the next arrival time.
3. Execute each process to completion in arrival order.
4. Calculate CT, TAT, and WT.

### Non-preemptive SJF
1. Find processes that have arrived and are ready.
2. Select the ready process with the shortest burst time.
3. Run it to completion.
4. Repeat until all processes finish.

### Round Robin
1. Add arrived processes to the ready queue.
2. Run the first ready process for at most the time quantum.
3. Add newly arrived processes to the queue.
4. Re-queue an unfinished process; otherwise mark it complete.
5. Repeat until all processes finish.

## 6. Formulas
- Completion Time (CT): time at which a process finishes.
- Turnaround Time (TAT) = CT − Arrival Time (AT)
- Waiting Time (WT) = TAT − Burst Time (BT)
- Average WT = sum of WT / number of processes
- Average TAT = sum of TAT / number of processes

## 7. Modules
- Input and validation module
- Scheduling algorithm module
- Metrics calculation module
- Gantt chart visualization module
- Results presentation module

## 8. Expected Output
The user enters process details and selects an algorithm. The application displays the Gantt chart, per-process CT/TAT/WT values, and average waiting and turnaround times.

## 9. Result
The application illustrates that execution order and waiting times vary according to the selected algorithm and input dataset. SJF may reduce average waiting time for some datasets, while Round Robin provides time-sharing behaviour.

## 10. Future Scope
- Add SRTF and priority scheduling.
- Export results to PDF or CSV.
- Save previous simulations.
- Add animated Gantt charts and ready-queue steps.
- Add additional performance statistics.

## 11. Conclusion
The CPU Scheduling Visualizer demonstrates the practical implementation of FCFS, non-preemptive SJF, and Round Robin. It automatically calculates scheduling metrics and presents the CPU timeline, helping learners compare scheduling policies.
