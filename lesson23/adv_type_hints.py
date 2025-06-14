from typing import Optional, Any
from typing import List
from typing import Union

'''Optional Example'''
def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"
print(get_name())

'''Union Example'''
def process_value(value: Union[int, str]) ->str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"
print(process_value("1"))

'''Any Example'''
def process_anything(value: Any):
    return f"Processed: {value}"
print(process_anything("Hello"))