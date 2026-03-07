import re

COMPARISON_PATTERNS = [
    r'next\s+\$?[A-Z]{1,5}',   
    r'like\s+\$?[A-Z]{1,5}',       
    r'another\s+\$?[A-Z]{1,5}',    
    r'mini\s+\$?[A-Z]{1,5}',
    r'be\s+\$?[A-Z]{1,5}',
]

def is_comparison_mention(text,ticker):
    for pattern in COMPARISON_PATTERNS:
        matches = re.findall(pattern,text.upper())
        for match in matches:
            if ticker in match:
                return True
    return False

