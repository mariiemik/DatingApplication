import pydantic as pd

class BaseSchema(pd.BaseModel):
    id : int
    token: str

class Token(pd.BaseModel):
    token: str

    class Config:
        from_attributes = True

class User(pd.BaseModel):
    # id: int
    email : str
    password: str
    # password_hash : str

    class Config:
        from_attributes = True

class Profile(BaseSchema):
    name: str
    surname: str
    country_name: str
    city_name: str
    gender: bool
    age: int
    active: bool
    about_me: str
    nickname_tg: str

    class Config:
        from_attributes = True

class Photo(BaseSchema):
    # profile_id: int
    photo_url: str

    class Config:
        from_attributes = True

class Like(BaseSchema):
    # user_from_id: int
    user_id_to: int

    class Config:
        from_attributes = True