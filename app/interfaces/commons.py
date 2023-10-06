from pydantic import BaseModel


class HeathCheckOutputSuccess(BaseModel):
    title: str = "Heathcheck Success!"
    message: str = "OK"


class HeathCheckOutputInternalError(BaseModel):
    title: str = "Heathcheck Error!"
    message: str = "Internal Server Error"


class HeathCheckOutputBadGateway(BaseModel):
    title: str = "Heathcheck Gateway"
    message: str = "Server Bad Gateway"


class HeathCheckOutputTimeOut(BaseModel):
    title: str = "Heathcheck Timeout"
    message: str = "Request server timeout"
