import re

def __CPF_is_valid(document: str) -> bool:
    CPF_pattern = "^(?:\\d{3}\\.?){2}\\d{3}-?\\d{2}$"
    return re.match(CPF_pattern, document) is not None

def __RG_is_valid(document: str) -> bool:
    RG_pattern = "^\\d{2}(?:\\.?\\d{3}){2}-?\\d$"
    return re.match(RG_pattern, document) is not None

def remove_document_special_characters(document: str) -> str:
    return document \
        .replace(".", "") \
        .replace("-", "")

def document_is_valid(document: str) -> bool:
    return __CPF_is_valid(document)
