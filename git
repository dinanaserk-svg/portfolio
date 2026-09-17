
import os
import datetime

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from clothing_item_and_user import ClothingItem
from outfit import ColorMatcher
from wardrobe import Wardrobe
from Weather import Weather
from user_profile import User


# تحديد template_folder و static_folder ليعمل من المجلد الرئيسي مباشرة
app = Flask(__name__, static_folder="static", template_folder=".")

UPLOAD_FOLDER = os.path.join("static", "uploads")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# =========================
# Objects
# =========================

my_wardrobe = Wardrobe()
matcher = ColorMatcher()
my_weather = Weather()
current_user = User()


# =========================
# Helper Functions
# =========================

def item_to_dict(item):
    """
    تحويل قطعة الملابس إلى Dictionary لضمان عدم حدوث خطأ أثناء تحويل JSON
    """
    if isinstance(item, dict):
        return item

    if hasattr(item, "__dict__"):
        return item.__dict__

    return {
        "name": getattr(item, "name", ""),
        "category": getattr(item, "category", ""),
        "color": getattr(item, "color", ""),
        "season": getattr(item, "season", ""),
        "occasion": getattr(item, "occasion", ""),
        "image": getattr(item, "image", "default.jpg")
    }


# =========================
# Home Page
# =========================

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# =========================
# CSS File
# =========================

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")


# =========================
# Uploaded Images
# =========================

@app.route("/static/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


# =========================
# Wardrobe - Get Items
# =========================

@app.route("/api/wardrobe", methods=["GET"])
def get_wardrobe():
    return jsonify(
        my_wardrobe.clothes_list
    )


# =========================
# Wardrobe - Add Item
# =========================

@app.route("/api/wardrobe", methods=["POST"])
def add_item():

    name = request.form.get("name", "").strip()
    category = request.form.get("category", "").strip()
    color = request.form.get("color", "").strip()
    season = request.form.get("season", "").strip()
    occasion = request.form.get("occasion", "casual").strip()

    if not name or not category or not color or not season:
        return jsonify({
            "message": "Please fill in all required fields."
        }), 400

    image_filename = "default.jpg"

    if "image" in request.files:
        file = request.files["image"]

        if file and file.filename != "":
            filename = secure_filename(file.filename)

            file.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            image_filename = filename

    item = ClothingItem(
        name,
        category,
        color,
        season,
        occasion
    )

    cloth_data = {
        "name": item.name,
        "category": item.category,
        "color": item.color,
        "season": item.season,
        "occasion": item.occasion,
        "image": image_filename
    }

    my_wardrobe.clothes_list.append(cloth_data)
    my_wardrobe.save()

    return jsonify({
        "message": "Item added successfully!"
    })


# =========================
# Wardrobe - Delete Item
# =========================

@app.route("/api/wardrobe/<path:name>", methods=["DELETE"])
def remove_item(name):

    for item in my_wardrobe.clothes_list:

        item_name = (
            item.get("name")
            if isinstance(item, dict)
            else getattr(item, "name", None)
        )

        if item_name == name:

            my_wardrobe.clothes_list.remove(item)
            my_wardrobe.save()

            return jsonify({
                "message": "Item removed successfully!"
            })

    return jsonify({
        "message": "Item not found!"
    }), 404


# =========================
# Weather
# =========================

@app.route("/api/weather", methods=["GET"])
def get_weather():

    # الحصول على التاريخ والوقت الحاليين
    now = datetime.datetime.now()

    return jsonify({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%I:%M:%S %p"),
        "temperature": my_weather.temperature(),
        "season": my_weather.season()
    })


# =========================
# Color Matcher
# =========================

@app.route("/api/match", methods=["POST"])
def match_colors():

    data = request.get_json()

    if not data:
        return jsonify({
            "match": False
        })

    color1 = data.get("color1", "")
    color2 = data.get("color2", "")

    if not color1 or not color2:
        return jsonify({
            "match": False
        })

    result = matcher.is_match(
        color1,
        color2
    )

    return jsonify({
        "match": result
    })


# =========================
# Outfit Suggestion
# =========================

@app.route("/api/outfit", methods=["GET"])
def suggest_outfit():

    current_season = my_weather.season()

    outfit = matcher.suggest_outfit(
        my_wardrobe.clothes_list,
        current_season
    )

    if outfit is None:
        return jsonify(None)

    return jsonify({
        "top": item_to_dict(outfit.top),
        "bottom": item_to_dict(outfit.bottom),
        "shoes": item_to_dict(outfit.shoes)
    })


# =========================
# Profile
# =========================

@app.route("/api/profile", methods=["GET"])
def get_profile():

    current_user.load_user()

    return jsonify({
        "name": getattr(
            current_user,
            "name",
            None
        ) or "StyleDoulabi User",

        "email": getattr(
            current_user,
            "email",
            None
        ) or "user@style.com",

        "age": getattr(
            current_user,
            "age",
            None
        ) or "",

        "fav_color": getattr(
            current_user,
            "fav_color",
            None
        ) or "N/A",

        "fav_season": getattr(
            current_user,
            "fav_season",
            None
        ) or "N/A"
    })


# =========================
# Run App
# =========================

if __name__ == "__main__":
    app.run(
        debug=True
    )
