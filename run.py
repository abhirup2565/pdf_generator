from app import create_app
from app.extension import db 
from app.Models import User


app = create_app()

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)