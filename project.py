import dotenv
import pydantic_settings
from typing import Literal


class Config(pydantic_settings.BaseSettings):
    context: Literal['local', 'selenoid'] = 'local'

    base_url: str = 'https://www.regard.ru/'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 3.0
    headless: bool = False


dotenv.load_dotenv()
config = Config(dotenv.find_dotenv(f'.env.{Config().context}'))
