from dataclasses import dataclass


@dataclass
class Urls:
    BASE: str = "https://test.deribit.com/api/v2/"
    GET_INDEX_PRICE: str = BASE + "public/get_index_price?index_name={}"
