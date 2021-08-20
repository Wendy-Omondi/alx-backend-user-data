#1/usr/bin/env python3
"""Encrytping password and checking validity"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string."""
    encoded_pwd = password.encode()
    hashed_pwd = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates that the provided password matches the hashed password."""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
