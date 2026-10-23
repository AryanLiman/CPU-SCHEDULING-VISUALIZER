"""CPU scheduling algorithms: FCFS, non-preemptive SJF, and Round Robin."""

def _metrics(processes, segments):
    completion = {}
    for segment in segments:
        if segment["pid"] != "IDLE":
            completion[segment["pid"]] = segment["end"]

    rows = []
    for p in processes:
        ct = completion[p["pid"]]
        tat = ct - p["arrival"]
        wt = tat - p["burst"]
        rows.append({
            "pid": p["pid"], "arrival": p["arrival"], "burst": p["burst"],
            "completion": ct, "turnaround": tat, "waiting": wt
        })
    rows.sort(key=lambda row: next(i for i, p in enumerate(processes) if p["pid"] == row["pid"]))
    avg_wt = sum(row["waiting"] for row in rows) / len(rows)
    avg_tat = sum(row["turnaround"] for row in rows) / len(rows)
    return rows, round(avg_wt, 2), round(avg_tat, 2)


def _add_segment(segments, pid, start, end):
    if end <= start:
        return
    if segments and segments[-1]["pid"] == pid and segments[-1]["end"] == start:
        segments[-1]["end"] = end
    else:
        segments.append({"pid": pid, "start": start, "end": end})


def fcfs(processes):
    ordered = sorted(processes, key=lambda p: (p["arrival"], p["input_order"]))
    time = 0
    segments = []
    for p in ordered:
        if time < p["arrival"]:
            _add_segment(segments, "IDLE", time, p["arrival"])
            time = p["arrival"]
        start = time
        time += p["burst"]
        _add_segment(segments, p["pid"], start, time)
    return segments


def sjf_non_preemptive(processes):
    remaining = list(processes)
    time = 0
    segments = []
    while remaining:
        available = [p for p in remaining if p["arrival"] <= time]
        if not available:
            next_arrival = min(p["arrival"] for p in remaining)
            _add_segment(segments, "IDLE", time, next_arrival)
            time = next_arrival
            available = [p for p in remaining if p["arrival"] <= time]
        chosen = min(available, key=lambda p: (p["burst"], p["arrival"], p["input_order"]))
        start = time
        time += chosen["burst"]
        _add_segment(segments, chosen["pid"], start, time)
        remaining.remove(chosen)
    return segments


def round_robin(processes, quantum):
    ordered = sorted(processes, key=lambda p: (p["arrival"], p["input_order"]))
    remaining = {p["pid"]: p["burst"] for p in ordered}
    arrivals = {p["pid"]: p["arrival"] for p in ordered}
    by_pid = {p["pid"]: p for p in ordered}
    queue = []
    segments = []
    time = 0
    next_index = 0
    finished = 0

    while finished < len(ordered):
        while next_index < len(ordered) and ordered[next_index]["arrival"] <= time:
            queue.append(ordered[next_index]["pid"])
            next_index += 1

        if not queue:
            next_arrival = ordered[next_index]["arrival"]
            _add_segment(segments, "IDLE", time, next_arrival)
            time = next_arrival
            continue

        pid = queue.pop(0)
        run_for = min(quantum, remaining[pid])
        start = time
        time += run_for
        remaining[pid] -= run_for
        _add_segment(segments, pid, start, time)

        while next_index < len(ordered) and ordered[next_index]["arrival"] <= time:
            queue.append(ordered[next_index]["pid"])
            next_index += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            finished += 1

    return segments


def schedule_processes(processes, algorithm, quantum=2):
    # Preserve the user's entry order for table output and tie-breaking.
    normalized = []
    for i, p in enumerate(processes):
        normalized.append({
            "pid": p["pid"], "arrival": p["arrival"], "burst": p["burst"],
            "input_order": i
        })

    if algorithm == "FCFS":
        segments = fcfs(normalized)
        title = "First Come, First Served (FCFS)"
    elif algorithm == "SJF":
        segments = sjf_non_preemptive(normalized)
        title = "Shortest Job First — Non-preemptive (SJF)"
    elif algorithm == "RR":
        segments = round_robin(normalized, quantum)
        title = f"Round Robin (time quantum = {quantum})"
    else:
        raise ValueError("Select a valid scheduling algorithm.")

    rows, avg_wt, avg_tat = _metrics(normalized, segments)
    return {
        "algorithm_title": title,
        "rows": rows,
        "segments": segments,
        "average_waiting": avg_wt,
        "average_turnaround": avg_tat
    }
