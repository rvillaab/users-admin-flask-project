from models import User

def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    return user