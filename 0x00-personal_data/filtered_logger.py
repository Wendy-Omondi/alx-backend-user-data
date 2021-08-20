#!/usr/bin/env python3
"""Regex-ing, Log formatter, Create logger, Connect to secure database,
    Read and filter data, Encrypting passwords, Check valid password
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated"""
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message
