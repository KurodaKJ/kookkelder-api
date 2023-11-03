from db_instance import db
from models.user_model import UserModel
from services.user_service.i_user_service import IUserService


class UserService(IUserService):
    def create_user(self, username, password, user_type_id):
        try:
            new_user = UserModel(username=username, password=password, user_type_id=user_type_id)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise e

    def get_user_by_id(self, user_id):
        try:
            user = UserModel.query.get(user_id)
            return user
        except Exception as e:
            raise e

    def get_user_by_username(self, username):
        try:
            user = UserModel.query.filter_by(username=username).first()
            return user
        except Exception as e:
            raise e

    def get_all_users(self):
        try:
            users = UserModel.query.all()
            return users
        except Exception as e:
            raise e

    def update_user(self, user_id, username, password, user_type_id):
        try:
            user = UserModel.query.get(user_id)
            if user:
                user.username = username
                user.password = password
                user.user_type_id = user_type_id
                db.session.commit()
                return user
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_user(self, user_id):
        try:
            user = UserModel.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return user
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e
