from flask import Blueprint, request, render_template

working_route = Blueprint("working", __name__, url_prefix="/working")


working = [
    {
        "name": "Anton",
        "Номер": 380991234567,
        "Компанія": "Home",
        "photo": "/static/завантаження.jpg"
    },
    {
        "name": "Max",
        "Номер": 380681234567,
        "Компанія": "Hilti",
        "photo": "/static/завантаження (1).jpg"
    }
]


@working_route.route("/<data_working>")
def data(data_working):
    data_working = int(data_working)
    if data_working >= len(working):
        return "<h1>такого працівника немає у списку</h1>", 404
    data = working[data_working]
    return render_template("worker.html", data=data)


@working_route.route("/form/create/", methods=['GET'])
def create_data():
    return """
<form  method="post" enctype="/static">
    <label>Працівник</label>
    <input name="name" type="text">
    <label>Номер</label>
    <input name="Номер" type="text">
    <label>Компанія</label>
    <input name="Компанія" type="text">
    <label>Фото</label>
    <input name="photo" type="text">
    <input type="submit" value="Загрузить">>
</form>    
"""

@working_route.route("/form/create/", methods=['POST'])
def create_new_working():
    data_working = request.form.to_dict()
    working.append(data_working)
    return "Нового працівника додано. Всього у базі: " + str(len(working))

