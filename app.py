import csv
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)


def check_level(value):
    if value >= 2000:
        return "high"
    elif value >= 1000:
        return "medium"
    else:
        return "normal"


def read_co2_file(filename):
    data = {}

    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    if not row["Day"] or not row["CO2"]:
                        continue

                    day = int(row["Day"])
                    co2 = float(row["CO2"])

                    data[day] = {
                        "co2": co2,
                        "status": check_level(co2)
                    }

                except:
                    continue

        print("Loaded records:", len(data))
        return data

    except FileNotFoundError:
        print("CSV file not found")
        return {}

    except Exception as e:
        print("Error:", e)
        return {}


co2_data = read_co2_file("CO2.csv")


def generate_chart(data):

    if not data:
        print("No data for chart")
        return ""

    days = sorted(data.keys())
    values = [data[d]["co2"] for d in days]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(days, values, marker="o")

    ax.set_title("CO2 līmenis pa dienām")
    ax.set_xlabel("Diena")
    ax.set_ylabel("ppm")

    ax.set_ylim(0, max(values) + 100)

    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    img = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return img


def get_day_value(day):
    return co2_data.get(day)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/day", methods=["GET", "POST"])
def day_view():
    result = None
    error = None

    if request.method == "POST":
        try:
            day = int(request.form["day"])
            info = get_day_value(day)

            if info:
                result = info
            else:
                error = "Diena nav atrasta"

        except ValueError:
            error = "Nepareizs ievads"

    return render_template("day.html", result=result, error=error)


@app.route("/chart")
def chart_view():
    chart = generate_chart(co2_data)
    return render_template("chart.html", chart=chart)


if __name__ == "__main__":
    app.run(debug=True)