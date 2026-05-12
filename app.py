"""
XKCD Comic Viewer - Updated Code
"""
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

XKCD_BASE_URL = "https://xkcd.com"


def get_latest_comic():
    try:
        response = requests.get(f"{XKCD_BASE_URL}/info.0.json", timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


def get_comic_by_number(comic_num):
    try:
        response = requests.get(f"{XKCD_BASE_URL}/{comic_num}/info.0.json", timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


@app.route("/")
def index():
    error = request.args.get("error")
    comic = get_latest_comic()

    if comic:
        latest_num = comic["num"]
        return render_template(
            "index.html",
            comic=comic,
            error=error,
            latest_num=latest_num
        )

    return render_template(
        "index.html",
        comic=None,
        error="Sorry, we couldn't fetch the comic right now. Please try again later.",
        latest_num=None
    )


@app.route("/comic/<int:comic_num>")
def show_comic(comic_num):
    latest = get_latest_comic()

    if latest is None:
        return render_template(
            "index.html",
            comic=None,
            error="Sorry, we couldn't fetch the latest comic right now.",
            latest_num=None
        )

    latest_num = latest["num"]

    if comic_num < 1:
        return redirect(url_for("index", error="Comic numbers start at 1. There is no comic #0."))

    if comic_num > latest_num:
        return redirect(url_for("index", error="That comic number is higher than the latest XKCD comic."))

    comic = get_comic_by_number(comic_num)

    if comic:
        return render_template(
            "index.html",
            comic=comic,
            error=None,
            latest_num=latest_num
        )

    return render_template(
        "index.html",
        comic=None,
        error=f"Comic #{comic_num} could not be found. It may not exist.",
        latest_num=latest_num
    )


@app.route("/search", methods=["POST"])
def search():
    comic_input = request.form.get("comic_num", "").strip()

    if comic_input == "":
        return redirect(url_for("index", error="Please enter a comic number."))

    try:
        comic_num = int(comic_input)
    except ValueError:
        return redirect(url_for("index", error="Please enter a valid number."))

    if comic_num < 1:
        return redirect(url_for("index", error="Comic numbers start at 1. There is no comic #0."))

    return redirect(url_for("show_comic", comic_num=comic_num))


if __name__ == "__main__":
    app.run(debug=True, port=5000)