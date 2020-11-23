from flask import Flask

app = Flask(__name__)

@app.route("/")
def coding_challenge_api():
    users = ["John A.", "Jane A.", "Alex A.", "Ryan A.", "Adrian A.", "Ryan A.", "Judy A.", "Hector A.", "Terry A.", "Moses A.",
    "John B.", "Jane B.", "Alex B.", "Ryan B.", "Adrian B.", "Ryan B.", "Judy B.", "Hector B.", "Terry B.", "Moses B.",
    "John C.", "Jane C.", "Alex C.", "Ryan C.", "Adrian C.", "Ryan C.", "Judy C.", "Hector C.", "Terry C.", "Moses C.",
    "John D.", "Jane D.", "Alex D.", "Ryan D.", "Adrian D.", "Ryan D.", "Judy D.", "Hector D.", "Terry D.", "Moses D.",
    "John E.", "Jane E.", "Alex E.", "Ryan E.", "Adrian E.", "Ryan E.", "Judy E.", "Hector E.", "Terry E.", "Moses E.",
    "John F.", "Jane F.", "Alex F.", "Ryan F.", "Adrian F.", "Ryan F.", "Judy F.", "Hector F.", "Terry F.", "Moses F.",
    "John G.", "Jane G.", "Alex G.", "Ryan G.", "Adrian G.", "Ryan G.", "Judy G.", "Hector G.", "Terry G.", "Moses G.",
    "John H.", "Jane H.", "Alex H.", "Ryan H.", "Adrian H.", "Ryan H.", "Judy H.", "Hector H.", "Terry H.", "Moses H.",
    "John I.", "Jane I.", "Alex I.", "Ryan I.", "Adrian I.", "Ryan I.", "Judy I.", "Hector I.", "Terry I.", "Moses I.",
    "John J.", "Jane J.", "Alex J.", "Ryan J.", "Adrian J.", "Ryan J.", "Judy J.", "Hector J.", "Terry J.", "Moses J."]
    return users

if (__name__) == "__main__":
    app.run()