from pydantic import BaseModel

from typing import Optional


class User(BaseModel):
    id: str
    name: str
    secret_santa: Optional["User"] = None
    wishlist: str = ""

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "secret_santa": (
                {"id": self.secret_santa.id, "name": self.secret_santa.name}
                if self.secret_santa
                else None
            ),
            "wishlist": self.wishlist,
        }

    @staticmethod
    def get_dummy_user():
        return User(id="", name="Guest", secret_santa=None, wishlist="")


class Room(BaseModel):
    id: str
    users: list[User]
    admin: User

    def dict(self):
        return {
            "id": self.id,
            "users": [user.dict() for user in self.users],
            "admin": self.admin.dict(),
        }
