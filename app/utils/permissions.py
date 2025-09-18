from typing import Literal

Operation = Literal[
    "READ", "CREATE", "READ-ALL", "UPDATE", "DELETE", "ADD-USER", "REMOVE-USER"
]

ApplicationRole = Literal["admin", "user", "driver"]