from flask import Flask, render_template, request
from scheduler import schedule_processes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    form_data = {
        "algorithm": "FCFS",
        "quantum": "2",
        "processes": "P1,0,5\nP2,1,3\nP3,2,1"
    }

    if request.method == "POST":
        form_data["algorithm"] = request.form.get("algorithm", "FCFS")
        form_data["quantum"] = request.form.get("quantum", "2")
        form_data["processes"] = request.form.get("processes", "")

        try:
            processes = []
            for line_number, line in enumerate(form_data["processes"].splitlines(), start=1):
                line = line.strip()
                if not line:
                    continue
                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 3:
                    raise ValueError(
                        f"Line {line_number}: enter values in Process ID, Arrival Time, Burst Time format."
                    )
                pid = parts[0]
                arrival = int(parts[1])
                burst = int(parts[2])
                if not pid:
                    raise ValueError(f"Line {line_number}: Process ID cannot be empty.")
                if arrival < 0:
                    raise ValueError(f"Line {line_number}: Arrival Time cannot be negative.")
                if burst <= 0:
                    raise ValueError(f"Line {line_number}: Burst Time must be greater than zero.")
                processes.append({"pid": pid, "arrival": arrival, "burst": burst})

            if not processes:
                raise ValueError("Enter at least one process.")
            if len({p["pid"] for p in processes}) != len(processes):
                raise ValueError("Each Process ID must be unique.")

            quantum = int(form_data["quantum"])
            if form_data["algorithm"] == "RR" and quantum <= 0:
                raise ValueError("Time quantum must be greater than zero.")

            result = schedule_processes(processes, form_data["algorithm"], quantum)
        except ValueError as exc:
            error = str(exc)
        except Exception:
            error = "Something went wrong. Check your inputs and try again."

    return render_template("index.html", result=result, error=error, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)
